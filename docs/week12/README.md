# Week 12 Part 3 — Complete Documentation

**Project:** CareConnect — SWEN 661 Team 1
**Repository:** [LaoWai-Fi/careconnect-swen661-T1](https://github.com/LaoWai-Fi/careconnect-swen661-T1)
**Scope:** user documentation, developer documentation, and WCAG 2.1 Level A/AA conformance reports for web, desktop, and both mobile implementations.

## Submission files

| Deliverable | Editable source / evidence |
|---|---|
| User guide | [USER_GUIDE.md](USER_GUIDE.md) |
| Developer guide | [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) |
| Mobile VPAT — Flutter and React Native | [Markdown source](MOBILE_VPAT.md) · [Word document](CareConnect_Mobile_WCAG21_AA_VPAT.docx) |
| Desktop VPAT — Electron | [Markdown source](../week9/CARECONNECT_DESKTOP_VPAT.md) · [Word document](../week9/CARECONNECT_DESKTOP_VPAT_Week9_With_Results.docx) · [PDF](../week9/CARECONNECT_DESKTOP_VPAT.pdf) |
| Web VPAT — React | [Markdown source](WEB_VPAT.md) · [Word document](CareConnect_Web_WCAG21_AA_VPAT.docx) |

The desktop report is the existing Week 9 evaluation reused for this assignment. It covers all 50 WCAG 2.1 Level A and AA criteria and documents its evidence baseline and known gaps; it is not represented as a new Week 12 retest.

## Evidence and scope notes

- The supplied `Team1_Week12_Submission_Items.docx` contains the team's web accessibility testing and fix evidence. Its WAVE and axe DevTools runs were on the local production build of the fix branch, not a post-merge scan of the live site. The Word submission still contains a placeholder asking for the post-merge live-site result; replace that text before submitting the full Week 12 package.
- The team's web report records 455 Playwright passes, 23 documented WebKit skips, 135 Jest/RTL passes, keyboard-only testing, and VoiceOver/Safari testing. The known limitation is that VoiceOver did not speak the appointment-deletion status message.
- Mobile evidence in this repository records TalkBack testing on an Android emulator and six successful Maestro workflows. It does not record iOS VoiceOver testing or a current final-build test on iOS.
- The mobile user-guide section uses no fabricated screenshots. The repository currently has web and desktop screenshots, but no current Flutter/React Native screen captures. Capture and insert those before treating the mobile screenshot portion as complete.
- A live Lighthouse report in `docs/week11/evidence/` is one homepage lab run; it is not full-site WCAG evidence and does not replace a manual assistive-technology evaluation.

## Final human verification checklist

- [ ] Replace the stale post-merge placeholder in the supplied Week 12 Word submission. If claiming live WAVE/axe results, run those tools on the deployed version and save the actual reports/screenshots.
- [ ] Capture current Flutter and React Native screenshots on a device/emulator and add them to the user guide or the final submission package.
- [ ] If iOS is in the submission scope, build both apps and complete VoiceOver checks; the current evidence only establishes Android TalkBack testing.
- [ ] Re-run the mobile and desktop manual checks against the exact final builds. Windows/NVDA and Windows contrast themes remain untested for desktop.
- [ ] Confirm the instructor accepts Markdown plus linked Word VPATs as editable documentation; if a single combined Word submission is required, export the user and developer guides and combine them with the three VPATs.

## Related documentation

- [Desktop Week 8 submission index](../week8/README.md)
- [Web accessibility implementation notes](../../web/ACCESSIBILITY.md)
- [Week 9 desktop accessibility tests and fixes](../week9/ACCESSIBILITY_TESTING.md)
- [Week 6 mobile accessibility evidence](../week6/ACCESSIBILITY_TEST_REPORT.md)
