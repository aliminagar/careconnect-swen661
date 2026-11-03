# CareConnect Desktop: Week 9 Accessibility Testing (Part 1)

Target: WCAG 2.1 Level AA. Branch: `feat/electron-accessibility-wk9`. Builds tested: the installed macOS build (0.8.0, Intel Mac, macOS 26.6.2) for keyboard testing, the app run with `npm start` for VoiceOver testing, and the renderer served by `npm run dev` for the automated scan.

Part 2 (fixes) and Part 3 (VPAT) use the findings in section 4 as their work list.

The Part 3 desktop accessibility conformance report is available in editable [Markdown](CARECONNECT_DESKTOP_VPAT.md), generated [Word](CARECONNECT_DESKTOP_VPAT_Week9_With_Results.docx), and [PDF](CARECONNECT_DESKTOP_VPAT.pdf) formats. It covers every WCAG 2.1 Level A and AA success criterion, distinguishes tested conformance from pending verification, and records limitations and workarounds.

## 1. Automated testing (axe)

The renderer was scanned with axe-core (the engine used by axe DevTools) at 1440 x 900 in light and dark themes, using the `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`, `wcag22aa` and `best-practice` rule sets.

Screens: landing, sign up, sign in, dashboard, medications, appointments, activity, messages.
Dialogs: add medication, add appointment, compose message, settings (also with High contrast on), keyboard shortcuts, emergency.

To repeat: run `cd desktop-electron && npm ci && npm run dev`, open `http://127.0.0.1:5173/` in Chrome, sign in with any email and password, and run the axe DevTools extension on each screen and dialog.

Result before fixes: sign up, sign in and the dashboard have no issues. The findings are in section 4 (items 1 to 6). The Part 2 code fixes and test results are documented in `PART2_FIXES.md`. The post-fix Chrome axe DevTools screenshots and their exact scope are recorded below; Jest axe checks do not replace the required DevTools evidence or rendered color-contrast scan.

### Post-fix Chrome axe DevTools evidence

Run on 2026-10-11 in Chrome against `http://127.0.0.1:5173/`, using axe DevTools 4.13.0 Page Scan. WCAG 2.1 AA was selected and Best Practices was off. With DevTools docked, the CareConnect viewport was approximately 431 × 730 CSS px. Every scan below completed and showed **Total Issues: 0**. The dark-theme pass covered all seven primary screens; light-theme scans specifically rechecked the dashboard, appointment-assignee contrast, message count badges, and emergency description contrast. This records the actual scan scope; it does not claim every screen/dialog was scanned in both themes.

| Rendered screen/state | Theme | Result | Evidence |
|---|---|---|---|
| Landing | Dark | 0 issues | [`axe-landing-dark-zero-violations.jpg`](evidence/axe-landing-dark-zero-violations.jpg) |
| Sign in | Dark | 0 issues | [`axe-signin-dark-zero-violations.jpg`](evidence/axe-signin-dark-zero-violations.jpg) |
| Dashboard | Dark | 0 issues | [`axe-dashboard-dark-zero-violations.jpg`](evidence/axe-dashboard-dark-zero-violations.jpg) |
| Medications | Dark | 0 issues | [`axe-medications-dark-zero-violations.jpg`](evidence/axe-medications-dark-zero-violations.jpg) |
| Appointments, including assigned-care banner | Dark | 0 issues | [`axe-appointments-dark-zero-violations.jpg`](evidence/axe-appointments-dark-zero-violations.jpg) |
| Activity | Dark | 0 issues | [`axe-activity-dark-zero-violations.jpg`](evidence/axe-activity-dark-zero-violations.jpg) |
| Messages | Dark | 0 issues | [`axe-messages-dark-zero-violations.jpg`](evidence/axe-messages-dark-zero-violations.jpg) |
| Dashboard | Light | 0 issues | [`axe-dashboard-light-zero-violations.jpg`](evidence/axe-dashboard-light-zero-violations.jpg) |
| Appointments, including assigned-care banner | Light | 0 issues | [`axe-appointments-light-zero-violations.jpg`](evidence/axe-appointments-light-zero-violations.jpg) |
| Messages, including inbox/archive counts | Light | 0 issues | [`axe-messages-light-zero-violations.jpg`](evidence/axe-messages-light-zero-violations.jpg) |
| Emergency dialog (SOS not activated) | Light | 0 issues | [`axe-emergency-dialog-light-zero-violations.jpg`](evidence/axe-emergency-dialog-light-zero-violations.jpg) |

## 2. Keyboard-only testing (macOS)

Run with the mouse not used for the test steps. Full Keyboard Access was on. Ctrl is replaced by Cmd on macOS.

| # | Area | Result | Notes |
|---|---|---|---|
| K1 | Landing | Pass | Tab order is Sign in, Create an account, Help. Focus ring is clear. |
| K2 | Sign in | Pass | Email, password, Sign in, Sign up link. Retested after the Part 2 fixes: an empty submit shows an error under each field and focus moves to the first invalid field (Email). Before the fixes, focus stayed on the Sign in button (item 7). |
| K3 | Sign up | Pass | All fields reachable in order. |
| K4 | Skip link | Pass | First Tab shows "Skip to main content". |
| K5 | Dashboard | Pass | Customize, cards, alert dismiss buttons and View all are reachable. Customize dialog traps focus and returns it. The Check-in card records a check-in with Return. |
| K6 | Main navigation | Pass | Sidebar buttons show a focus ring and the current page. |
| K7 | Cmd+1 to Cmd+5 | Pass | Each opens the right page. |
| K8 | Medications | Pass | Mark taken (Space), Add, Edit and Delete confirmation work. The installed 0.8.0 build showed an empty schedule time in the Edit form; the current build (`npm start`) shows the saved time. |
| K9 | Appointments | Pass | Add, Edit and Delete confirmation work. Fields, Cancel and Save are reachable, Escape closes and focus returns to the button that opened it. |
| K10 | Activity | Pass | Refresh and filter chips work with Enter. Retested after the Part 2 fixes: Refresh no longer records a check-in entry. Before the fixes it added a "Checked in via dashboard" entry (item 9). |
| K11 | Messages | Pass | List, open message, mark read or unread, Reply, Archive, Delete (with confirmation, Escape cancels) and the whole compose form work by keyboard. Send and Reply send. Archive moves the message to the Archive tab and focus is kept. After Send, focus lands on the CareConnect web content group. |
| K12 | Dialogs | Pass | Settings, Keyboard shortcuts, Emergency, Customize, add and edit forms and delete confirmations trap focus, close with Escape and return focus to the opener. |
| K13 | Cmd+, and F1 | Pass | Settings and Keyboard shortcuts open. |
| K14 | Cmd+N and Cmd+F | Pass | Find works. Retested after the Part 2 fixes: Cmd+N opens the new message compose form. Before the fixes it opened Messages only (item 8). |
| K15 | Cmd+S, E, O, P | Pass | Save, Export, Import and Print run. |
| K16 | Cmd+= and Cmd+0 | Pass | Zoom in and reset. |
| K17 | Cmd+Shift+L and H | Pass | Left-hand mode and High contrast toggle. |
| K18 | In-app menus | N/A | macOS uses the native menu bar. |
| K19 | Native menu bar | Pass | Ctrl+F2, then Right and Down arrows open File, Edit, View and Help and move through their items. Items run, and F1 from Help opens Keyboard shortcuts. |
| K20 | Arrow keys | Pass | Arrow keys work in the native menus. Space and Enter work on toggles and chips. |
| K21 | Keyboard traps | Pass | None found. |
| K22 | Focus visible | Pass | A clear ring in light, dark and High contrast. |
| K23 | Tab order | Pass | Skip link, account menu, toolbar, patient picker, sidebar, then page content. |

## 3. Screen reader testing (VoiceOver on macOS)

Tested 10/10/2026 on macOS with VoiceOver and Full Keyboard Access on. Cmd+F5 turns VoiceOver on. The VO key is Ctrl+Option.

| # | Step | Expected | Result | Notes |
|---|---|---|---|---|
| S1 | Launch app, landing page | Window title, a heading, Sign in and Sign up buttons | Pass | Buttons are announced when reached with the keyboard. To read page content, click the page and use VO+Down (interact), then VO+Right to move through items. |
| S2 | Sign in form | Labels, required, error text | Pass | Field names and "required" are announced. Submitting an empty form announces that the password is required. |
| S3 | Dashboard | Main navigation and main landmarks, headings, widget names, status line | Pass | "Main" is announced and page headings (Overview, Medications and so on) are announced and selectable. The Overview sidebar item reads only as selectable text. |
| S4 | Rotor (VO+U) | Headings and landmarks list is sensible, one h1 per page | Pass with note | Headings (dashboard): Dashboard, Margaret's status today, Alerts, Today's medications, Next appointment, Unread messages. Landmarks: CareConnect navigation (complementary), main navigation, main, and regions for status overview, alerts, today's medications, next appointment and unread messages, plus footer. No banner or toolbar landmark: the title bar and toolbar are reachable with VO+Right but are not in the landmarks list (item 6). The sidebar landmark is named "CareConnect navigation" but is a complementary landmark, which is confusing next to the real navigation landmark. Retested after the Part 2 fixes: the sidebar landmark now reads "Care plan controls", and the landing page has a Help region. |
| S5 | Medications, mark taken | State change and a status message without moving focus | Pass | Dashboard: marking and unmarking a medication announces its name and new status. Medications page, retested after the Part 2 fixes: the control announces the medication name and its selected state, and says it can be activated again to toggle it off. Before the fixes it announced only "Selected" (item 10). |
| S6 | Add medication dialog | Dialog name, field labels, focus stays inside, closing returns focus | Pass | Dialog and field labels are announced. Closing or saving returns to the Medications page. |
| S7 | Appointments | Cards read with date, time and status | Pass | Cards are read with VO+Right once Full Keyboard Access is on. |
| S8 | Messages, compose and attach | Dialog or page name, field labels, Attach button | Pass | All fields and the Attach file button are announced. Attaching a file announces the prompt with correct details. No extra hidden element was read. Retested after the Part 2 fixes: Attach still works by keyboard. |
| S9 | Settings | Switches announce on or off | Pass | Items announce as selected or unselected, and choosing another option announces that it was selected. |
| S10 | Emergency dialog | Alert dialog name and description | Pass | The dialog is announced when the Emergency button opens it. SOS was not pressed. |
| S11 | Menu bar (VO+M) | Menus and items with shortcuts | Pass | All menus and items are read aloud. |
| S12 | Live updates | Check-in and save results announced | Pass | The check-in status message is announced. |

The screen reader recording (3 to 5 minutes) is submitted as a separate file.

## 4. Findings

WCAG failures:

1. **1.4.3 Contrast (Minimum).** Appointments page, the "is assigned" text in the green banner (`AppointmentsPage.tsx`, the `opacity-80` span): 4.26:1, needs 4.5:1.
2. **1.4.3 Contrast (Minimum).** Emergency dialog description (`AppShell.tsx`, `emergency-body`): 4.47:1, needs 4.5:1.
3. **2.1.1 Keyboard (axe: scrollable-region-focusable).** The hidden attachment file input in the compose form (`MessagesPage.tsx`, `input type="file"` with `sr-only` and `tabindex="-1"`) is flagged as a scrollable region with no focusable content.
4. **1.4.3 Contrast (Minimum).** Messages page, the inbox and archive count badges (`MessagesPage.tsx`, the `opacity-80` spans): 4.42:1 and 3.89:1 in the light theme, needs 4.5:1.

Best-practice findings:

5. **page-has-heading-one.** The landing page has no h1.
6. **region.** The window title bar, menu bar, toolbar and account area are outside any landmark. The landing footer text is outside a footer landmark.


Usability findings from keyboard testing:

7. **Sign in.** After a failed submit, focus stays on the Sign in button instead of moving to the first invalid field.
8. **Cmd+N.** The menu item is labeled "Messages Menu" and does not open the compose form.
9. **Activity Refresh.** Refresh adds a "Checked in via dashboard" entry although no check-in was recorded and the dashboard still says the check-in is not done.

Screen reader finding:

10. **Medications toggle.** On the Medications page the mark-taken control announces only "Selected" and does not say the medication name or the new state, unlike the dashboard. Add an accessible name and state (for example `aria-pressed` with a label naming the medication) and a status message.

Status after Part 2 fixes (retest on `npm start`, macOS 26.6.2, VoiceOver): findings 7 (K2), 8 (K14), 9 (K10), 10 (S5) were retested by hand and pass. The sidebar landmark rename (item 6, S4) and the compose Attach button (S8) were confirmed in VoiceOver. Findings 1 to 5 were rechecked with axe-core and the contrast scan on the merged code and report no issues. With axe Best Practices on, the only remaining item is a `region` note on the emergency dialog backdrop (see `PART2_FIXES.md`).

Contrast check of rendered text: every visible text item on each screen and dialog was measured in light and dark themes (colors composited over their backgrounds, 4.5:1 for normal text and 3:1 for large text). Only the items in findings 1, 2 and 4 fail. The "Signing in..." and "Send" buttons measured 2.3:1 but are disabled controls, which WCAG 1.4.3 exempts.
