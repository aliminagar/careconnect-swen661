"""Generate the editable Word VPAT-style report from its Markdown source."""

from __future__ import annotations

import html
import argparse
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "CARECONNECT_DESKTOP_VPAT.md"
OUTPUT = HERE / "CARECONNECT_DESKTOP_VPAT_Week9_With_Results.docx"
CRITERIA = [
    "1.1.1", "1.2.1", "1.2.2", "1.2.3", "1.2.4", "1.2.5",
    "1.3.1", "1.3.2", "1.3.3", "1.3.4", "1.3.5",
    "1.4.1", "1.4.2", "1.4.3", "1.4.4", "1.4.5", "1.4.10",
    "1.4.11", "1.4.12", "1.4.13",
    "2.1.1", "2.1.2", "2.1.4", "2.2.1", "2.2.2", "2.3.1",
    "2.4.1", "2.4.2", "2.4.3", "2.4.4", "2.4.5", "2.4.6", "2.4.7",
    "2.5.1", "2.5.2", "2.5.3", "2.5.4",
    "3.1.1", "3.1.2", "3.2.1", "3.2.2", "3.2.3", "3.2.4",
    "3.3.1", "3.3.2", "3.3.3", "3.3.4",
    "4.1.1", "4.1.2", "4.1.3",
]


def xml_text(value: str) -> str:
    return html.escape(value, quote=False)


def plain_text(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", value)
    return value.replace("**", "").replace("`", "").replace("*", "")


def run(value: str, *, bold: bool = False, size: int | None = None, color: str | None = None) -> str:
    properties = []
    if bold:
        properties.append("<w:b/>")
    if size:
        properties.append(f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>')
    if color:
        properties.append(f'<w:color w:val="{color}"/>')
    rpr = f"<w:rPr>{''.join(properties)}</w:rPr>" if properties else ""
    return f"<w:r>{rpr}<w:t xml:space=\"preserve\">{xml_text(plain_text(value))}</w:t></w:r>"


def paragraph(value: str = "", *, style: str | None = None, bold: bool = False, size: int | None = None,
              color: str | None = None, before: int = 0, after: int = 100) -> str:
    ppr_parts = [f'<w:spacing w:before="{before}" w:after="{after}" w:line="240" w:lineRule="auto"/>']
    if style:
        ppr_parts.append(f'<w:pStyle w:val="{style}"/>')
    ppr = f"<w:pPr>{''.join(ppr_parts)}</w:pPr>"
    return f"<w:p>{ppr}{run(value, bold=bold, size=size, color=color)}</w:p>"


def table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    columns = len(rows[0])
    widths = {
        2: [3300, 11388],
        3: [2700, 5700, 6288] if rows[0][0] == "Check / limitation"
        else [3000, 5200, 6488],
        4: [2050, 1700, 4900, 6038],
    }.get(columns, [14688 // columns] * columns)
    border = (
        '<w:tblBorders><w:top w:val="single" w:sz="4" w:color="AAB8C2"/>'
        '<w:left w:val="single" w:sz="4" w:color="AAB8C2"/>'
        '<w:bottom w:val="single" w:sz="4" w:color="AAB8C2"/>'
        '<w:right w:val="single" w:sz="4" w:color="AAB8C2"/>'
        '<w:insideH w:val="single" w:sz="4" w:color="D1D9DE"/>'
        '<w:insideV w:val="single" w:sz="4" w:color="D1D9DE"/></w:tblBorders>'
    )
    props = (
        '<w:tblPr><w:tblW w:w="14688" w:type="dxa"/>'
        '<w:tblLayout w:type="fixed"/>' + border +
        '<w:tblCellMar><w:top w:w="70" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
        '<w:bottom w:w="70" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar></w:tblPr>'
    )
    grid = "<w:tblGrid>" + "".join(f'<w:gridCol w:w="{width}"/>' for width in widths) + "</w:tblGrid>"
    body_rows = []
    for row_index, cells in enumerate(rows):
        cells += [""] * (columns - len(cells))
        header = '<w:trPr><w:tblHeader w:val="true"/></w:trPr>' if row_index == 0 else ""
        cell_xml = []
        for col_index, text in enumerate(cells):
            fill = '<w:shd w:fill="DCE8EF"/>' if row_index == 0 else ""
            text_color = "17324D" if row_index == 0 else None
            cell_paragraph = (
                '<w:p><w:pPr><w:spacing w:after="0" w:line="215" w:lineRule="auto"/>'
                '<w:rPr><w:sz w:val="17"/><w:szCs w:val="17"/></w:rPr></w:pPr>'
                + run(text, bold=row_index == 0 or (columns == 3 and col_index == 2),
                      size=17, color=text_color)
                + "</w:p>"
            )
            cell_xml.append(
                f'<w:tc><w:tcPr><w:tcW w:w="{widths[col_index]}" w:type="dxa"/>{fill}</w:tcPr>'
                f"{cell_paragraph}</w:tc>"
            )
        body_rows.append(f"<w:tr>{header}{''.join(cell_xml)}</w:tr>")
    return f"<w:tbl>{props}{grid}{''.join(body_rows)}</w:tbl>"


def parse_markdown(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    content: list[str] = []
    criteria_rows = 0
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
            rows = [
                [part.strip() for part in line.strip("|").split("|")]
                for line in table_lines
            ]
            rows = [row for row in rows if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in row)]
            if rows and rows[0][0] == "Criterion":
                criteria_rows = len(rows) - 1
                allowed = {"Supports", "Partially Supports", "Does Not Support", "Not Applicable"}
                invalid = []
                for row in rows[1:]:
                    status = row[2] if len(row) > 2 else ""
                    if len(row) < 3 or not any(status.startswith(f"**{level}.") for level in allowed):
                        invalid.append((row[0], status))
                if invalid:
                    raise SystemExit(f"Invalid VPAT conformance level(s): {invalid}")
            content.append(table(rows))
            continue
        heading = re.match(r"^(#{1,3})\s+(.*)", current)
        if heading:
            level = len(heading.group(1))
            style = {1: "Title", 2: "Heading1", 3: "Heading2"}[level]
            content.append(paragraph(heading.group(2), style=style,
                                     size=32 if level == 1 else (26 if level == 2 else 22),
                                     color="17324D", bold=True,
                                     before=220 if level == 1 else 160, after=100))
        elif current.startswith("- "):
            content.append(paragraph("• " + current[2:], size=19, after=50))
        elif current.startswith("> "):
            content.append(paragraph(current[2:], size=19, color="405869", after=100))
        elif current.startswith("```"):
            index += 1
            code_lines = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code_lines.append(lines[index])
                index += 1
            for code_line in code_lines:
                content.append(paragraph(code_line, size=17, color="405869", after=15))
        else:
            content.append(paragraph(current, size=19, after=100))
        index += 1
    return "".join(content), criteria_rows


def make_document(body: str) -> bytes:
    document = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:body>{body}
<w:sectPr><w:pgSz w:w="15840" w:h="12240" w:orient="landscape"/>
<w:pgMar w:top="600" w:right="576" w:bottom="600" w:left="576" w:header="300" w:footer="300" w:gutter="0"/>
</w:sectPr></w:body></w:document>'''
    styles = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Aptos" w:hAnsi="Aptos"/>
<w:sz w:val="19"/><w:szCs w:val="19"/></w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="100" w:line="260" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/>
<w:rPr><w:b/><w:color w:val="17324D"/><w:sz w:val="32"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/>
<w:next w:val="Normal"/><w:rPr><w:b/><w:color w:val="17324D"/><w:sz w:val="26"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/>
<w:next w:val="Normal"/><w:rPr><w:b/><w:color w:val="17324D"/><w:sz w:val="22"/></w:rPr></w:style>
</w:styles>'''
    root = "http://schemas.openxmlformats.org/package/2006/relationships"
    rels = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="{root}">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''
    doc_rels = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="{root}"></Relationships>'''
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>'''
    from io import BytesIO
    stream = BytesIO()
    with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED) as package:
        package.writestr("[Content_Types].xml", content_types)
        package.writestr("_rels/.rels", rels)
        package.writestr("word/document.xml", document)
        package.writestr("word/styles.xml", styles)
        package.writestr("word/_rels/document.xml.rels", doc_rels)
    return stream.getvalue()


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the editable CareConnect desktop VPAT DOCX.")
    parser.add_argument("--source", type=Path, default=SOURCE, help="Markdown source path")
    parser.add_argument("--output", type=Path, default=OUTPUT, help="Output DOCX path")
    args = parser.parse_args()
    output = args.output
    source_text = args.source.read_text(encoding="utf-8")
    for criterion in CRITERIA:
        if not re.search(rf"(?<![\d.]){re.escape(criterion)}(?![\d.])", source_text):
            raise SystemExit(f"Missing WCAG criterion in Markdown source: {criterion}")
    body, criteria_rows = parse_markdown(source_text)
    if criteria_rows != len(CRITERIA):
        raise SystemExit(f"Expected {len(CRITERIA)} criterion rows, found {criteria_rows}")
    output.write_bytes(make_document(body))
    with zipfile.ZipFile(output) as package:
        bad_member = package.testzip()
        if bad_member:
            raise SystemExit(f"Invalid DOCX archive member: {bad_member}")
        xml = package.read("word/document.xml")
        ET.fromstring(xml)
        doc_text = xml.decode("utf-8")
        for criterion in CRITERIA:
            if criterion not in doc_text:
                raise SystemExit(f"Generated DOCX is missing criterion {criterion}")
    print(f"Generated and validated {output.name}: {len(CRITERIA)} WCAG 2.1 A/AA criteria")


if __name__ == "__main__":
    main()
