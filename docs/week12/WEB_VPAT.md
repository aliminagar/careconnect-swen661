# CareConnect Web — WCAG 2.1 Level A and AA Conformance Report

**Product:** CareConnect Web (React/Vite)
**Project:** SWEN 661 Team 1
**Report scope:** all 50 WCAG 2.1 Level A and AA success criteria for the responsive web application.

## Product and evaluation information

| Field | Information |
|---|---|
| Product | CareConnect responsive web app / installable web experience |
| Version baseline | Week 12 Part 1 accessibility fix branch; PR #19 was reported merged to `main` on 2026-10-30 |
| Public URL | https://laowai-fi.github.io/careconnect-swen661-T1/ |
| Report date | 2026-11-02 |
| Evaluation basis | Team-supplied Week 12 Part 1 results, current implementation documentation, and the single live homepage Lighthouse report in `docs/week11/evidence/` |
| Evaluator | Team project evidence; this is not an independent certification |

The product uses React and browser-local demonstration data with mock sign-in. A scoped onboarding assistant may use a Supabase Edge Function. It is not a medical-advice or production clinical service.

## Conformance terminology and evidence limits

Status terms: **Supports**, **Partially Supports**, **Does Not Support**, and **Not Applicable**. The report's audit claims are limited to recorded evidence. WAVE and axe DevTools were run against the **local production build of the fix branch** on 12 routes; they were not post-merge scans of the public URL. The submitted Part 1 document retains a placeholder for a live re-audit. The separate November 1 Lighthouse run is a single live homepage lab audit, not a whole-site accessibility test.

The team report records WAVE with 0 errors/contrast errors and axe DevTools with 0 issues on 12 routes, 24 route/mode Lighthouse accessibility scores of 100 on the local production build, 455 Playwright passes / 0 failures / 23 documented WebKit skips, 135 Jest/RTL passes, keyboard-only testing, and a VoiceOver/Safari session. One known limitation remains: VoiceOver did not speak the appointment-deletion status message, though it was visible and exposed as a polite status region. This is reported as partial support for 4.1.3 rather than a pass.

## WCAG 2.1 Level A and AA criteria

| Criterion | Level | Status | Implementation, evidence, and limitation |
|---|---|---|---|
| **1.1.1 Non-text Content** | A | **Supports.** | Week 12 route and overlay axe scans reported no violations; icon controls have accessible names and decorative icons are hidden. Evidence is the local fix-branch production build. |
| **1.2.1 Audio-only and Video-only (Prerecorded)** | A | **Not Applicable.** | No prerecorded audio-only or video-only media is documented in the app. |
| **1.2.2 Captions (Prerecorded)** | A | **Not Applicable.** | No prerecorded synchronized audio/video is documented. |
| **1.2.3 Audio Description or Media Alternative (Prerecorded)** | A | **Not Applicable.** | No prerecorded video is documented. |
| **1.2.4 Captions (Live)** | AA | **Not Applicable.** | No live synchronized audio/video is documented. |
| **1.2.5 Audio Description (Prerecorded)** | AA | **Not Applicable.** | No prerecorded video is documented. |
| **1.3.1 Info and Relationships** | A | **Supports.** | Semantic landmarks, headings, labels, and dialog relationships are tested across 12 routes, themes, and overlays; VoiceOver/Safari landmark and heading checks are recorded. |
| **1.3.2 Meaningful Sequence** | A | **Supports.** | The Part 1 report records logical keyboard order and screen-reader heading/navigation behavior; automated route tests check headings and controls. |
| **1.3.3 Sensory Characteristics** | A | **Partially Supports.** | Controls use text labels, but no dedicated audit of every instruction for sensory-only references is recorded. Review each route's instructions and help text. |
| **1.3.4 Orientation** | AA | **Partially Supports.** | Responsive web layouts were exercised at mobile and desktop widths and no orientation lock is documented. Separate portrait/landscape verification for all routes is not recorded. |
| **1.3.5 Identify Input Purpose** | AA | **Partially Supports.** | Forms have labels and validation. A field-by-field audit of autocomplete/input-purpose tokens is not included in the submitted evidence. |
| **1.4.1 Use of Color** | A | **Supports.** | Statuses include text/icons and are not represented by color alone; route and theme accessibility checks are recorded. |
| **1.4.2 Audio Control** | A | **Not Applicable.** | The app does not document automatically playing audio. |
| **1.4.3 Contrast (Minimum)** | AA | **Supports.** | The Week 12 fix-branch report records contrast corrections and WAVE 0 contrast errors on 12 local production routes. The report also includes the VoiceOver status limitation, unrelated to text contrast. |
| **1.4.4 Resize Text** | AA | **Supports.** | Text scaling/zoom behavior and responsive screens are documented; the team manually tested larger text and browser layouts. |
| **1.4.5 Images of Text** | AA | **Partially Supports.** | Main interface content is live text; a comprehensive audit of every image asset for essential embedded text is not recorded. |
| **1.4.10 Reflow** | AA | **Supports.** | Team evidence reports narrow and wide viewport tests, including 320px–1440px coverage in existing web accessibility documentation, without horizontal scrolling. |
| **1.4.11 Non-text Contrast** | AA | **Partially Supports.** | Focus rings and non-text controls were retested; there is no complete numeric 3:1 inventory for all graphical objects and states. |
| **1.4.12 Text Spacing** | AA | **Partially Supports.** | Text resizing is tested, but the specified WCAG line, paragraph, letter, and word-spacing override combination is not documented. |
| **1.4.13 Content on Hover or Focus** | AA | **Partially Supports.** | Keyboard focus behavior is tested; no inventory verifies dismissibility, hoverability, and persistence for every hover/focus-triggered tooltip or popover. |
| **2.1.1 Keyboard** | A | **Supports.** | The team reports a manual keyboard-only pass and Playwright coverage of every route, visible focus, and keyboard-operable assistant/dialog flows. |
| **2.1.2 No Keyboard Trap** | A | **Supports.** | Automated and manual evidence records dialogs/drawers closing with Escape and focus restoration; no keyboard traps were found. |
| **2.1.4 Character Key Shortcuts** | A | **Not Applicable.** | No single-character keyboard shortcuts are documented; Enter in the assistant field is a conventional form action, not a single-character command shortcut. |
| **2.2.1 Timing Adjustable** | A | **Supports.** | No user task deadline or session timeout is reported. The assistant's response delay is not a task time limit. |
| **2.2.2 Pause, Stop, Hide** | A | **Partially Supports.** | No moving or flashing content is documented, but a header time/date indicator may update automatically. Confirm whether updates are exposed continuously and whether users can pause/hide them before making a full claim. |
| **2.3.1 Three Flashes or Below Threshold** | A | **Not Applicable.** | No flashing content is documented. |
| **2.4.1 Bypass Blocks** | A | **Supports.** | A skip link is first in keyboard order and targets main content; automated tests and manual keyboard evidence are recorded. |
| **2.4.2 Page Titled** | A | **Supports.** | Per-route document titles and headings are exercised in route semantics tests; screen-reader navigation reports new page headings on navigation. |
| **2.4.3 Focus Order** | A | **Supports.** | Keyboard tests cover all 12 routes, focus visibility/order, overlays, route heading focus, validation focus, and modal restoration. |
| **2.4.4 Link Purpose (In Context)** | A | **Supports.** | Route and form tests plus the manual keyboard/screen-reader evidence cover labeled links and controls. |
| **2.4.5 Multiple Ways** | AA | **Partially Supports.** | Persistent navigation and dashboard links provide multiple paths to some screens; evidence does not show two ways to locate every page in the site. |
| **2.4.6 Headings and Labels** | AA | **Supports.** | Team tests check one h1, heading order, semantic labels, and named controls across routes; VoiceOver heading navigation is documented. |
| **2.4.7 Focus Visible** | AA | **Supports.** | A scripted test checks a visible computed focus outline on all route tab stops, and manual keyboard testing reports a clear focus ring. |
| **2.5.1 Pointer Gestures** | A | **Supports.** | Common actions use single-pointer controls; dashboard rearrangement has tap/keyboard Move Up/Down alternatives rather than a drag-only requirement. |
| **2.5.2 Pointer Cancellation** | A | **Partially Supports.** | Standard buttons are used; the evidence does not include a dedicated pointer-down/up/cancel test for all custom controls. |
| **2.5.3 Label in Name** | A | **Supports.** | The Week 12 report records correction of the assistant input's competing accessible names to one visible/programmatic label and tests icon controls. |
| **2.5.4 Motion Actuation** | A | **Not Applicable.** | No feature is documented as being activated by device motion or user movement. |
| **3.1.1 Language of Page** | A | **Supports.** | The web document declares English and route-level semantics tests check document language. |
| **3.1.2 Language of Parts** | AA | **Not Applicable.** | The documented interface content is English only; no foreign-language passages are identified. |
| **3.2.1 On Focus** | A | **Supports.** | Focusing a control does not trigger a documented context change; keyboard/manual workflow tests cover the principal screens. |
| **3.2.2 On Input** | A | **Supports.** | Forms require explicit submission; the team records successful manual/automated validation flows without unexpected input-triggered navigation. |
| **3.2.3 Consistent Navigation** | AA | **Supports.** | The same main navigation is used across the app routes; route coverage and cross-browser checks are recorded. |
| **3.2.4 Consistent Identification** | AA | **Supports.** | Shared form, button, navigation, and status patterns are used; route and component tests cover repeated controls. |
| **3.3.1 Error Identification** | A | **Supports.** | The report records inline and summary errors, invalid states, associated descriptions, and focus movement to the first invalid field. |
| **3.3.2 Labels or Instructions** | A | **Supports.** | Visible labels, required states, and form instructions are used; axe and screen-reader tests cover forms across routes. |
| **3.3.3 Error Suggestion** | AA | **Supports.** | Reported form errors provide corrective guidance for invalid/missing values; Jest/RTL and VoiceOver validation evidence is documented. |
| **3.3.4 Error Prevention (Legal, Financial, Data)** | AA | **Partially Supports.** | Destructive appointment actions use confirmation dialogs and forms provide review/error correction; no complete audit of every data-change flow is recorded. |
| **4.1.1 Parsing** | A | **Supports.** | axe and HTML_CodeSniffer runs over the 12-route local production build reported no WCAG markup errors in the stated scope; this does not cover every future state or OS surface. |
| **4.1.2 Name, Role, Value** | A | **Supports.** | axe scans and VoiceOver checks cover roles, names, selected/current states, dialogs, and forms; the assistant's competing input names were corrected. |
| **4.1.3 Status Messages** | AA | **Partially Supports.** | Status regions are implemented and automated tests pass, but VoiceOver with Safari did not speak the appointment deletion confirmation on manual retest. The confirmation remains visually available; confirm by checking the page after deletion. |

## Known limitations and workarounds

- **Appointment deletion status:** the visible “deleted” message is exposed as a polite status region but was not spoken by VoiceOver/Safari. Visually confirm the result; do not rely on speech for this specific confirmation.
- **Live-site tool scans:** the reported WAVE/axe DevTools runs used the local production build of the fix branch. Run fresh WAVE/axe scans on the deployed version and replace the placeholder in the supplied Week 12 Word report before claiming they passed live.
- **Partial manual retest scope:** keyboard and VoiceOver tests are valuable evidence but do not establish exhaustive conformance for every state, browser, or assistive technology.
- **Local demo data/auth:** the web app is not a production health-data service. Avoid real PHI.

## Evidence references

- [Submitted Week 12 Part 1 results](README.md) (details are also in the supplied `Team1_Week12_Submission_Items.docx`)
- [Web accessibility implementation notes](../../web/ACCESSIBILITY.md)
- [Part 4 live Lighthouse evidence](../week11/evidence/)
- [Current web application README](../../web/README.md)
