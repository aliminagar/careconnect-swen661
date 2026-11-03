# University of Maryland Global Campus

**SWEN 661 - User Interface Implementation**
**Assignment 9: Desktop Accessibility and VPAT**
**Project:** CareConnect - Left-Handed User Focused UI

| Team | Members | Date |
| --- | --- | --- |
| Team 1 | Dom Puller, Wiliss Tako, Rehman Uddin | 10/13/2026 |
| Repository | LaoWai-Fi/careconnect-swen661-T1 | Working branch: `89uddinrt-week-9-desktop-vpat` |

## Accessibility and UI Testing Conformance Summary

This Assignment 9 conformance report covers the CareConnect Electron desktop application against all 50 WCAG 2.1 Level A and AA success criteria, with desktop implementation notes, conformance status, and evidence or known gaps for each. Evidence is drawn from the desktop Week 8 and Week 9 implementation and testing records. Mobile-app evidence is outside this report's scope.

| Platform | Accessibility implementation | Evidence |
| --- | --- | --- |
| Electron desktop (React/TypeScript renderer) | Semantic HTML/ARIA, labeled forms, keyboard navigation and native shortcuts, focus-managed dialogs, status announcements, light/dark/high-contrast settings, text scaling/zoom, and Left-Hand Mode. | Week 9 axe DevTools screenshots and jest-axe tests; recorded macOS keyboard and VoiceOver checks; automated test and coverage records. Scope and gaps are detailed below. |

## WCAG 2.1 Level A and AA Criteria

Status terms follow VPAT conformance levels: **Supports**, **Partially Supports**, **Does Not Support**, and **Not Applicable**. Each criterion includes the desktop implementation and the evidence or limitation behind its status. A pending verification item is not a pass. No manual assistive-technology testing beyond the documented macOS VoiceOver checks is claimed.

| Criterion | CareConnect Desktop implementation | Status and verification |
| --- | --- | --- |
| **1.1.1 Non-text Content (Level A)** | Informative imagery and controls have text alternatives or accessible names; decorative artwork is hidden from assistive technology. | **Supports.** Informative controls use text or accessible names; decorative icons and emoji are hidden from assistive technology. Automated axe checks exercise the recorded pages and dialogs. See Week 9 accessibility tests and the VoiceOver checks. |
| **1.2.1 Audio-only and Video-only (Prerecorded) (Level A)** | The desktop application does not provide prerecorded audio-only or video-only media. | **Not Applicable.** The application does not provide prerecorded audio-only or video-only media. |
| **1.2.2 Captions (Prerecorded) (Level A)** | No prerecorded synchronized audio/video is provided. | **Not Applicable.** The application contains no prerecorded synchronized audio/video. |
| **1.2.3 Audio Description or Media Alternative (Prerecorded) (Level A)** | No prerecorded video with an audio track is provided. | **Not Applicable.** The application contains no prerecorded video with an audio track. |
| **1.2.4 Captions (Live) (Level AA)** | No live synchronized audio/video is provided. | **Not Applicable.** The application provides no live synchronized audio/video. |
| **1.2.5 Audio Description (Prerecorded) (Level AA)** | No prerecorded video with audio description needs is provided. | **Not Applicable.** The application provides no prerecorded video with an audio track. |
| **1.3.1 Info and Relationships (Level A)** | Semantic headings, landmarks, form labels, named regions, and dialog relationships structure the renderer. | **Supports.** The interface uses headings, landmarks, labeled regions, form labels, and dialog relationships. Week 9 added shell landmarks and a landing-page heading; axe scans and VoiceOver rotor checks are documented. An axe Best Practices scan still notes the emergency alert-dialog backdrop region; the report records this as a best-practice note, not an identified WCAG 2.1 A/AA failure. |
| **1.3.2 Meaningful Sequence (Level A)** | The renderer DOM and keyboard navigation preserve a meaningful sequence through shell, pages, and dialogs. | **Supports.** The content follows a meaningful DOM and reading order. Mac keyboard tab order and VoiceOver page/heading navigation were manually exercised; automated renderer tests cover primary pages. |
| **1.3.3 Sensory Characteristics (Level A)** | Instructions and action labels use text and programmatic names, not sensory characteristics alone. | **Supports.** Directions and controls are identified with text, labels, and programmatic names rather than relying solely on shape, color, location, or sound. Relevant axe and VoiceOver evidence is documented; no audio-only instruction is present. |
| **1.3.4 Orientation (Level AA)** | The resizable Electron window and responsive renderer styles support portrait/landscape viewport changes. | **Supports.** The renderer has responsive orientation/viewport styles and does not lock screen orientation. The app is resizable. Landscape/narrow viewport styling is present in `src/index.css`; exhaustive orientation/device testing remains advisable. |
| **1.3.5 Identify Input Purpose (Level AA)** | Account name, email, and password inputs use autocomplete purposes and associated field labels. | **Supports.** Account name, email, and password controls expose autocomplete purposes (`name`, `email`, `new-password`, `current-password`). Forms use associated labels. See `SignInPage.tsx`, `SignUpPage.tsx`, and `FormField.tsx`. |
| **1.4.1 Use of Color (Level A)** | State is conveyed with text, icons, labels, and programmatic state as well as color. | **Supports.** Color is supplemented by text, icons, labels, or state semantics for status and controls. Axe and manual VoiceOver checks cover documented states; high-contrast modes are also available. |
| **1.4.2 Audio Control (Level A)** | The app does not play audio automatically. | **Not Applicable.** The application does not play audio automatically. |
| **1.4.3 Contrast (Minimum) (Level AA)** | Text color tokens are designed for contrast; rendered text was measured in light and dark themes, with reported fixes rechecked. | **Supports.** Week 9 records rendered text contrast measurement in both themes and post-fix zero-issue contrast checks for the previously failing appointment, emergency-dialog, and message-count text. Full criterion-specific evidence and scan scope are in `ACCESSIBILITY_TESTING.md` and `PART2_FIXES.md`; jsdom axe checks do not measure contrast. |
| **1.4.4 Resize Text (Level AA)** | In-app text size and native zoom shortcuts provide resizing up to 200%; macOS testing recorded no clipping or loss of function. | **Supports.** Manual testing on macOS reports successful 200% zoom and larger app text without clipping or loss of function. The application provides text-size settings and zoom shortcuts (up to 200%). This evidence does not establish WCAG 1.4.10 reflow at 400%. |
| **1.4.5 Images of Text (Level AA)** | Primary interface content is live text; no essential text is embedded in images. | **Supports.** Primary interface content is rendered as text, not images of text. No essential image-of-text content was identified in the recorded screens. |
| **1.4.10 Reflow (Level AA)** | Responsive layouts and zoom are implemented; reflow at 320 CSS px/400% has not yet been verified. | **Partially Supports.** The app has responsive layouts; manual macOS testing at 200% zoom passed, and recorded axe scans used a roughly 431 CSS-pixel-wide renderer viewport. A 320 CSS-pixel viewport or equivalent 400% zoom reflow test is not recorded. **Pending:** verify all app pages and dialogs at 320 CSS px wide with no two-dimensional scrolling except permitted content, and check at 400% zoom. Until then, use the app's zoom/text-size controls and resize/maximize the window; this is not a substitute for that verification. |
| **1.4.11 Non-text Contrast (Level AA)** | Controls define borders and visible focus indicators; high-contrast modes are available. | **Partially Supports.** Focus indicators were manually observed as visible in light, dark, and in-app high-contrast modes; macOS Increase Contrast was also checked. Numeric 3:1 contrast measurement of component boundaries, states, and focus indicators, including Windows forced-colors/Contrast Themes, is not documented. **Pending:** measure relevant graphical objects and states, and verify Windows Contrast Themes. |
| **1.4.12 Text Spacing (Level AA)** | Text uses scalable layout, but WCAG-defined text-spacing overrides have not yet been tested. | **Partially Supports.** Normal text sizing and larger app text were exercised, but the WCAG text-spacing overrides (line height, paragraph spacing, letter spacing, and word spacing) were not tested. No conformance claim is made for content under those overrides. **Pending:** apply the criterion's spacing values across pages and dialogs and verify no content/functionality loss. Users can increase app text size or zoom while that test remains pending. |
| **1.4.13 Content on Hover or Focus (Level AA)** | Some controls include native title tooltip text; behavior and persistence on hover/focus have not been verified. | **Partially Supports.** Some controls set native `title` tooltip text (for example, delete and navigation controls). Equivalent labels/actions exist, but whether the host tooltip is dismissible, hoverable, and persistent was not verified. **Pending:** test title tooltips with pointer and keyboard focus on supported operating systems; ensure essential information is available without relying on the native tooltip. |
| **2.1.1 Keyboard (Level A)** | Renderer controls, app navigation, Electron menus, and documented keyboard shortcuts provide keyboard operation. | **Supports.** Mac keyboard-only testing covered the documented workflows, dialogs, menu items, and shortcuts; automated tests cover keyboard navigation, dialog traps, dismissal, and menu commands. Week 9 retested corrected sign-in focus, New Message, and medication controls. Windows and Linux native menu/tray keyboard use still need platform testing. |
| **2.1.2 No Keyboard Trap (Level A)** | Dialogs trap focus while open and close by Escape/controls, returning focus to their opener. | **Supports.** Manual macOS testing reports no keyboard traps; dialog tests verify Escape dismissal and focus return, and focus-trap tests verify contained Tab/Shift+Tab behavior while dialogs are open. |
| **2.1.4 Character Key Shortcuts (Level A)** | Documented accelerators use Command/Ctrl modifiers or function keys; no single-character shortcut is documented. | **Supports.** App shortcuts use Command/Ctrl modifiers or function keys (for example F1); no single-character shortcut is documented. See `desktop-electron/README.md` keyboard shortcut table. |
| **2.2.1 Timing Adjustable (Level A)** | User actions have no time limit or session timeout; the demo sign-in delay is not a task deadline. | **Not Applicable.** No user-facing time limit or timed session expiration is implemented. Demo sign-in delay is a short response animation, not a limit on task completion. |
| **2.2.2 Pause, Stop, Hide (Level A)** | No continuously moving, blinking, scrolling, or periodically updating content requiring pause controls was identified. | **Not Applicable.** No automatically moving, blinking, scrolling, or periodically updating content requiring a pause/stop/hide control was identified. Status announcements follow user actions. |
| **2.3.1 Three Flashes or Below Threshold (Level A)** | No flashing content was identified in the evaluated application. | **Not Applicable.** No flashing content was identified in the evaluated application. |
| **2.4.1 Bypass Blocks (Level A)** | A keyboard-accessible skip-to-main-content link bypasses repeated shell navigation. | **Supports.** The renderer provides a keyboard-accessible “Skip to main content” link. The macOS manual keyboard record confirms it appears on the first Tab; the Week 9 landmark changes were covered by axe checks. |
| **2.4.2 Page Titled (Level A)** | The document and app window identify CareConnect Desktop; rendered pages have headings. | **Supports.** The document title is “CareConnect Desktop”; the product window is identified as CareConnect. VoiceOver launch testing recorded the window title and page heading. |
| **2.4.3 Focus Order (Level A)** | The shell has a logical keyboard order; invalid sign-in moves focus to the first invalid field; dialogs return focus. | **Supports.** Mac keyboard testing records a logical order through the shell and page content; sign-in errors move focus to the first invalid field. Dialogs trap focus while open and return it to the opener. |
| **2.4.4 Link Purpose (In Context) (Level A)** | Links and action controls have descriptive labels or accessible names in context. | **Supports.** Links and action controls use descriptive labels or accessible names in their context. Axe checks and VoiceOver/keyboard checks cover documented primary flows. |
| **2.4.5 Multiple Ways (Level AA)** | Primary pages are reachable through persistent app navigation and native menus/keyboard shortcuts. | **Supports.** Primary pages can be reached through the app navigation and documented keyboard shortcuts/native menus. The Help and search functions provide additional access paths for applicable content. |
| **2.4.6 Headings and Labels (Level AA)** | Pages and dialogs use descriptive headings and controls use labels. | **Supports.** Pages and dialogs have descriptive headings and controls have labels. Week 9 corrected the landing-page h1; axe checks and VoiceOver heading-rotor testing are recorded. |
| **2.4.7 Focus Visible (Level AA)** | Visible focus styling is defined for controls and was manually observed on macOS in light, dark, and high-contrast modes. | **Supports.** Manual macOS keyboard checks report visible focus rings in light, dark, and in-app high-contrast modes. Automated styles define focus-visible outlines. Windows/Linux appearance has not been manually verified. |
| **2.5.1 Pointer Gestures (Level A)** | Primary actions use standard single-pointer controls; no multipoint or path gesture is required. | **Not Applicable.** No multipoint or path-based gesture is required to operate the application; actions use standard controls. |
| **2.5.2 Pointer Cancellation (Level A)** | Standard controls activate on normal press/release; keyboard alternatives are available for app tasks. | **Supports.** Standard button and control activation is used rather than custom pointer-down-only actions. Keyboard operation provides an equivalent input method. This criterion was not separately tested with a pointer-cancellation test protocol. |
| **2.5.3 Label in Name (Level A)** | Visible labels are reflected in accessible names for tested controls; icon-only controls receive names. | **Supports.** Visible button/control labels are reflected in programmatic names where tested, with additional accessible names for icon-only controls. Axe checks and VoiceOver manual checks cover representative pages and dialogs. |
| **2.5.4 Motion Actuation (Level A)** | No device-motion or user-movement actuation is used. | **Not Applicable.** The application does not use device motion or user movement to trigger functionality. |
| **3.1.1 Language of Page (Level A)** | The renderer document declares English (`lang="en"`). | **Supports.** The document root declares `lang="en"`. See `desktop-electron/index.html`. |
| **3.1.2 Language of Parts (Level AA)** | The evaluated user interface is English and has no identified passages in another language. | **Not Applicable.** The evaluated interface contains English content only; no passages in another language requiring a language-of-part declaration were identified. |
| **3.2.1 On Focus (Level A)** | Focusing a control does not itself trigger navigation, submission, or another context change. | **Supports.** Focusing a control does not itself trigger a context change. This is consistent with the native form/control patterns and keyboard test records. |
| **3.2.2 On Input (Level A)** | Entering form values does not submit or change context without explicit user activation. | **Supports.** Changing a form value does not automatically submit or change context. Actions require an explicit button/menu activation; form and workflow tests cover common input flows. |
| **3.2.3 Consistent Navigation (Level AA)** | The signed-in shell retains consistent navigation labels and order across its primary pages. | **Supports.** The signed-in shell presents consistent navigation across the five primary pages. The macOS keyboard and navigation tests exercise those page transitions. |
| **3.2.4 Consistent Identification (Level AA)** | Repeated controls and actions use consistent labels and identification patterns across the shell. | **Supports.** Repeated controls and navigation items use consistent labels and icon/text patterns across the shell. Automated and manual records cover the repeated navigation and common actions. |
| **3.3.1 Error Identification (Level A)** | Validation errors identify missing/invalid values, expose invalid state, and focus the first invalid sign-in field. | **Supports.** Invalid fields expose an error message and invalid state; sign-in errors are associated with fields and focus moves to the first invalid field. Week 9 Part 2 tests these changes; VoiceOver sign-in validation is documented. |
| **3.3.2 Labels or Instructions (Level A)** | Form fields have programmatic labels, required status, hints, and associated validation messages. | **Supports.** Form fields have programmatic labels; required status, hints, and errors are programmatically associated. FormField and screen-reader test records provide evidence. |
| **3.3.3 Error Suggestion (Level AA)** | Validation feedback supplies correction guidance where applicable, including password length and matching confirmation. | **Supports.** Where a correction can be suggested, errors and hints provide it (for example, the password's minimum length and mismatched confirmation). Automated sign-in validation tests and manual VoiceOver sign-in checks are recorded. |
| **3.3.4 Error Prevention (Legal, Financial, Data) (Level AA)** | User-controllable care-plan records are entered through forms with explicit Add/Save actions; destructive delete actions use an alert confirmation dialog, and medication taken status can be toggled back. | **Supports.** The app stores user-controllable care-plan data locally, so this criterion is applicable even though the product is a demo and has no production service. The user reviews form contents before choosing Add/Save; delete operations require a confirmation dialog with Cancel/Delete; reversible status actions can be toggled back. Week 8 keyboard testing records medication/appointment/message add/edit/delete workflows and delete confirmation; automated page/workflow tests cover the forms and dialogs. This evidence applies to the documented demo workflows; it is not a claim about a production account or server. |
| **4.1.1 Parsing (Level A)** | The product is a web-rendered Electron application; the renderer uses semantic HTML and React output. | **Supports.** The React renderer is built and type-checked, and axe checks report no WCAG 2.1 A/AA markup violations in their stated scope. As this criterion concerns programmatically determinable markup, automated checks are relevant evidence but do not cover every OS-rendered surface. |
| **4.1.2 Name, Role, Value (Level A)** | Interactive controls expose programmatic names, roles, values, and state; medication toggles include medication-specific state. | **Supports.** Native controls and ARIA names, roles, states, and values are used; Week 9 fixed the medication toggle name/state and attachment input exposure. Axe checks, control-specific tests, and VoiceOver checks are documented. |
| **4.1.3 Status Messages (Level AA)** | Status and live regions announce save, refresh, check-in, and medication updates without moving focus. | **Supports.** Status and live regions announce save, refresh, check-in, and medication state updates without moving focus. Week 9 tests and VoiceOver manual checks are recorded. |

## Automated and rendered test evidence

| Test | Result and scope |
| --- | --- |
| jest-axe | Week 8/9 renderer tests exercise the landing/sign-in experience, five primary signed-in pages, settings, shortcuts, emergency dialogs, and medication/appointment forms. jsdom disables axe color-contrast because rendered colors are not computed there. |
| Chrome axe DevTools 4.13.0 | Week 9 records seven primary pages in dark theme and selected light theme pages/dialogs at approximately 431 x 730 CSS px, with zero reported issues for those scans. This is not exhaustive coverage of all dialogs, themes, states, packaged builds, or operating systems. Evidence screenshots and precise scope are in `docs/week9/ACCESSIBILITY_TESTING.md`. |
| Rendered text contrast | Week 9 records measurement in light/dark themes (4.5:1 normal text, 3:1 large text); previously reported contrast defects were fixed and rechecked. This does not establish non-text contrast. |
| Historical automated tests | Week 8 report records 224 Jest tests and 5 Electron end-to-end tests passing. Week 9 Part 2 records typecheck, lint, and 224 Jest tests passing at that time. These are historical records, not a current CI result. |
| Current CI status (GitHub Actions run on `dbbfc338`) | `npm ci`, typecheck, lint, and Jest coverage passed. The `xvfb-run -a npm run test:e2e` step failed; the packaging job was skipped. This is the latest main-branch run checked for this report. No claim that the E2E suite or overall workflow passes is made. See the [Desktop Electron run](https://github.com/LaoWai-Fi/careconnect-swen661-T1/actions/runs/38266297078). |

## Screen reader testing (VoiceOver)

The desktop Week 9 record states that VoiceOver was tested on macOS 26.6.2 with Full Keyboard Access on, with post-fix checks recorded October 10, 2026. Only the documented test cases below are claimed. NVDA/Windows and Linux screen readers have not been manually tested.

| Check | Recorded result | Evidence/notes |
| --- | --- | --- |
| Launch and sign-in | Pass | VoiceOver announced window/title, labels, required fields, and validation feedback. |
| Navigation and rotor | Pass with note | Main landmark, page headings, and regions were navigable. Sidebar label was retested after its Part 2 update. |
| Medication state and dialogs | Pass | Medication name/state and status change announcements were retested; dialog labels and focus behavior were checked. |
| Messages and attachments | Pass | Compose fields and Attach action were reachable/announced; keyboard operation also recorded. |
| Settings, emergency dialog, menus, live updates | Pass | Switch states, alert-dialog name/description, native menu items, and check-in/save announcements were checked. The SOS action was not activated in the axe dialog evidence. |

## Findings and known limitations

| Check / limitation | Result | Workaround / follow-up |
| --- | --- | --- |
| WCAG 1.4.10 Reflow | 200% zoom was recorded as passing on macOS. Reflow at 320 CSS pixels / 400% zoom has not been tested. | **Pending:** verify all screens and dialogs at the criterion's reflow dimensions. Meanwhile, use app zoom/text-size settings and resize or maximize the window; scrolling may be needed. |
| WCAG 1.4.11 Non-text Contrast | Focus visibility was manually observed in light, dark, and in-app high-contrast modes; macOS Increase Contrast was checked. Numeric 3:1 contrast for components/focus and Windows Contrast Themes are unverified. | **Pending:** measure applicable graphical objects and states, and test Windows Contrast Themes. |
| WCAG 1.4.12 Text Spacing | WCAG text-spacing override values were not tested. | **Pending:** apply the line-height, paragraph-spacing, letter-spacing, and word-spacing thresholds across pages and dialogs; verify no content or functionality is lost. App text-size and zoom settings remain available. |
| WCAG 1.4.13 Hover or Focus | Some controls provide native `title` text. Whether tooltips are dismissible, hoverable, and persistent has not been verified. | **Pending:** test tooltip behavior on supported platforms and ensure essential information is available without relying on tooltips. |
| Windows/NVDA and Linux AT | No manual Windows/NVDA, Windows Contrast Themes, or Linux screen-reader test is recorded. macOS VoiceOver evidence does not establish results on these platforms. | **Pending:** test sign-in, landmarks, forms, dialogs, live updates, menus/tray, focus, and keyboard-only workflows with the target OS and assistive technology. |
| Axe scan coverage | Recorded dark-theme scans cover seven primary pages; light-theme scans cover selected pages and the emergency dialog. Other page/dialog/theme combinations and the final packaged build are not covered. | **Pending:** scan all pages and dialogs in both themes and the final packaged build. Do not treat unscanned combinations as passing. |
| Unsigned macOS build notifications | Native notifications are implemented but do not display in the unsigned macOS build, according to the Week 8 report. | Use visible in-app status and activity feedback instead. |
| Demo-only features | Sign-in and data are sample/demo only; Emergency does not contact emergency services. | Do not rely on this application for real care coordination or emergency response. |
| Scope of standards | This report assesses WCAG 2.1 A/AA only. Section 508-specific provisions and EN 301 549 were not evaluated. | No conformance claim is made for Section 508-specific requirements or EN 301 549. |

## Findings and fixes recorded for Week 9

The Week 9 Part 1 issues were addressed in the merged Part 2 work: appointment/emergency/message text contrast fixes; hidden attachment input accessibility; landing heading and shell/help landmarks; sign-in error focus; Cmd+N compose behavior; activity refresh behavior; and medication toggle accessible name/state/status message. Part 2 describes regression evidence and the remaining emergency-dialog axe Best Practices `region` note, which is not reported there as a WCAG 2.1 A/AA failure. See [`PART2_FIXES.md`](PART2_FIXES.md).

## Week 9 submission evidence

| Assignment item | Repository evidence/status |
| --- | --- |
| Accessibility testing report and completed testing checklist | [`ACCESSIBILITY_TESTING.md`](ACCESSIBILITY_TESTING.md), including the recorded axe scan scope, keyboard checks K1-K23, and VoiceOver checks S1-S12. |
| Accessibility fixes and regression evidence | [`PART2_FIXES.md`](PART2_FIXES.md), including fixes, WCAG mapping, tests, and coverage results. |
| axe DevTools results | Screenshots under [`evidence/`](evidence/), with zero-issue results for the specific screens/themes listed in the testing report. Scans do not cover every possible page/dialog/theme combination. |
| Screen-reader demonstration | The Week 9 testing report states that the VoiceOver recording is submitted separately. This report does not claim an NVDA/Windows test. |
| Updated coverage | Week 9 Part 2 records line coverage of 98.44% in its documented test run, above the assignment's 60% minimum. The latest merged-main CI Jest coverage step passed, but the overall workflow failed at E2E. |
| GitHub build/test status | Latest checked main run is linked in the evaluation evidence above; E2E failed and packaging was skipped. |

## Use of AI

AI assistance was used to organize the conformance report, map repository-documented desktop findings to WCAG criteria, and format the document. The manual keyboard and VoiceOver results in this report are attributed only to the team's recorded Week 9 testing; AI did not perform those tests or independently verify assistive-technology behavior.

## Report scope and provenance

Product baseline: CareConnect Desktop 0.8.0 with Week 9 Part 2 fixes on `main` merge `dbbfc33` (PR #13). This report was compiled from repository implementation and test records; manual tests were not repeated for this report. It uses VPAT conformance terminology and a criterion/implementation/status-and-evidence matrix for the requested WCAG 2.1 A/AA scope. It is not the official unmodified VPAT template, a certification, or an independent evaluation.

Editable source: `docs/week9/CARECONNECT_DESKTOP_VPAT.md`. The current exports are [`CARECONNECT_DESKTOP_VPAT_Week9_With_Results.docx`](CARECONNECT_DESKTOP_VPAT_Week9_With_Results.docx) and [`CARECONNECT_DESKTOP_VPAT.pdf`](CARECONNECT_DESKTOP_VPAT.pdf). The Word report uses the Week 6 submission's heading-and-table layout with Week 9 desktop content. Regenerate both from the repository root:

```powershell
python docs/week9/generate_vpat_docx.py
python docs/week9/generate_vpat_pdf.py
```

```powershell
python docs/week9/generate_vpat_docx.py
python docs/week9/generate_vpat_pdf.py
```
