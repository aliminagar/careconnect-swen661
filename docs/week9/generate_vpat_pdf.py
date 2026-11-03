"""Render the VPAT Markdown as a paginated PDF with headless Chrome."""

from __future__ import annotations

import html
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "CARECONNECT_DESKTOP_VPAT.md"
OUTPUT = HERE / "CARECONNECT_DESKTOP_VPAT.pdf"
CHROME_PATHS = (
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
)


def inline(value: str) -> str:
    value = value.translate(str.maketrans({
        "\u2013": "-", "\u2014": "-", "\u2011": "-",
        "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
    }))
    value = html.escape(value, quote=False)
    value = re.sub(r"\[([^\]]+)\]\((https?://[^ )]+)\)", r'<a href="\2">\1</a>', value)
    value = re.sub(r"\[([^\]]+)\]\(([^ )]+)\)", r"\1", value)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    value = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"\*(.+?)\*", r"<em>\1</em>", value)
    return value


def parse_table(lines: list[str]) -> str:
    rows = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append(cells)
    if not rows:
        return ""
    header = "".join(f"<th>{inline(cell)}</th>" for cell in rows[0])
    body = []
    for cells in rows[1:]:
        cells += [""] * (len(rows[0]) - len(cells))
        body.append("<tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in cells) + "</tr>")
    return f"<table><thead><tr>{header}</tr></thead><tbody>{''.join(body)}</tbody></table>"


def render_markdown(text: str) -> str:
    lines = text.splitlines()
    output: list[str] = []
    index = 0
    while index < len(lines):
        current = lines[index].strip()
        if not current:
            index += 1
            continue
        if current.startswith("|"):
            table_lines = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index].strip())
                index += 1
            output.append(parse_table(table_lines))
            continue
        heading = re.match(r"^(#{1,3})\s+(.*)", current)
        if heading:
            level = len(heading.group(1))
            output.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
        elif current.startswith("- "):
            items = []
            while index < len(lines) and lines[index].strip().startswith("- "):
                items.append(f"<li>{inline(lines[index].strip()[2:])}</li>")
                index += 1
            output.append("<ul>" + "".join(items) + "</ul>")
            continue
        elif current.startswith("```"):
            index += 1
            code_lines = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code_lines.append(html.escape(lines[index]))
                index += 1
            output.append("<pre><code>" + "\n".join(code_lines) + "</code></pre>")
        else:
            output.append(f"<p>{inline(current)}</p>")
        index += 1
    return "\n".join(output)


def find_chrome() -> Path:
    for candidate in CHROME_PATHS:
        if candidate.is_file():
            return candidate
    for name in ("chrome", "msedge"):
        found = shutil.which(name)
        if found:
            return Path(found)
    raise SystemExit("Google Chrome or Microsoft Edge is required to render the VPAT PDF.")


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    if not re.search(r"\|\s*\*\*1\.1\.1\b", source):
        raise SystemExit("WCAG criterion matrix not found in VPAT source.")

    content = render_markdown(source)
    document = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>CareConnect Desktop Accessibility Conformance Report</title>
<style>
@page {{ size: Letter landscape; margin: 0.55in 0.48in; }}
* {{ box-sizing: border-box; }}
body {{ font: 9pt/1.35 Aptos, Calibri, Arial, sans-serif; color: #202b33; }}
h1 {{ color: #17324d; font-size: 22pt; margin: 0 0 10pt; }}
h2 {{ color: #17324d; font-size: 15pt; margin: 20pt 0 7pt; break-after: avoid; }}
h3 {{ color: #28536f; font-size: 11pt; margin: 13pt 0 5pt; break-after: avoid; }}
p {{ margin: 0 0 7pt; }}
ul {{ margin: 2pt 0 8pt 18pt; padding: 0; }}
li {{ margin: 0 0 4pt; }}
a {{ color: #155e7a; text-decoration: underline; }}
code {{ font: 8pt Consolas, monospace; }}
pre {{ white-space: pre-wrap; border: 1px solid #d1d9de; padding: 7pt; }}
table {{ width: 100%; border-collapse: collapse; table-layout: fixed; margin: 6pt 0 12pt; }}
thead {{ display: table-header-group; }}
tr {{ break-inside: avoid; page-break-inside: avoid; }}
th, td {{ border: 0.5pt solid #aab8c2; padding: 4pt 5pt; text-align: left; vertical-align: top; overflow-wrap: anywhere; }}
th {{ background: #dce8ef; color: #17324d; font-weight: 700; }}
td {{ font-size: 7.4pt; line-height: 1.23; }}
th {{ font-size: 8pt; }}
table:has(thead th:nth-child(3)) th:first-child,
table:has(thead th:nth-child(3)) td:first-child {{ width: 16%; }}
table:has(thead th:nth-child(3)) th:nth-child(2),
table:has(thead th:nth-child(3)) td:nth-child(2) {{ width: 37%; }}
table:has(thead th:nth-child(3)) th:nth-child(3),
table:has(thead th:nth-child(3)) td:nth-child(3) {{ width: 47%; }}
</style></head><body>{content}</body></html>"""

    chrome = find_chrome()
    with tempfile.TemporaryDirectory(prefix="careconnect-vpat-") as temp:
        temp_path = Path(temp)
        html_path = temp_path / "vpat.html"
        profile_path = temp_path / "chrome-profile"
        html_path.write_text(document, encoding="utf-8")
        command = [
            str(chrome),
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--user-data-dir={profile_path}",
            f"--print-to-pdf={OUTPUT}",
            html_path.resolve().as_uri(),
        ]
        completed = subprocess.run(command, capture_output=True, text=True, timeout=90)
        if completed.returncode:
            raise SystemExit(
                f"Chrome PDF export failed ({completed.returncode}).\n"
                f"{completed.stderr[-3000:]}"
            )

    if not OUTPUT.is_file() or OUTPUT.stat().st_size < 1000:
        raise SystemExit("PDF export failed or produced an unexpectedly small file.")
    pdf_bytes = OUTPUT.read_bytes()
    if not pdf_bytes.startswith(b"%PDF-") or b"%%EOF" not in pdf_bytes[-2048:]:
        raise SystemExit("Generated output does not have a valid PDF signature and end marker.")
    page_objects = re.findall(rb"/Type\s*/Page\b", pdf_bytes)
    if not page_objects:
        raise SystemExit("Generated PDF contains no page objects.")
    print(f"Generated and validated {OUTPUT.name} ({OUTPUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
