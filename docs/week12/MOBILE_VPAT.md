# CareConnect Mobile — WCAG 2.1 Level A and AA Conformance Report

**Product:** CareConnect Mobile (Flutter and React Native / Expo)
**Project:** SWEN 661 Team 1
**Report scope:** all 50 WCAG 2.1 Level A and AA success criteria for the user interface of both mobile implementations.

## Product and evaluation information

| Field | Information |
|---|---|
| Product | CareConnect mobile demonstration app |
| Versions | Flutter and React Native source in this repository; a single final release version is not identified |
| Platforms | Android and iOS code targets; the located manual accessibility evidence is Android-only |
| Report date | 2026-11-02 |
| Evaluation basis | Current source/READMEs plus the committed Week 6 automated and manual evidence records |
| Evaluator | Team project evidence; this is not an independent certification |

CareConnect mobile uses native controls and sample data to demonstrate daily schedule, medication, appointment, activity, and message workflows. Flutter uses Provider/`AppState`; React Native uses Context/`useReducer`. Both have accessibility-oriented labels/states, text sizing, and one-handed controls. The app is an educational prototype, not a medical device or secure clinical record.

## Conformance terminology and limitations

Status terms: **Supports**, **Partially Supports**, **Does Not Support**, and **Not Applicable**. “Partially Supports” is used where code or targeted test evidence exists but the criterion has not been established across both apps and supported assistive technologies. It does not claim a known failure unless the notes say so. No criterion is assigned “Does Not Support” because the evidence reviewed does not establish a definitive failure; gaps remain **unverified**, not silently passed.

The Week 6 report records an Android TalkBack walkthrough for both apps, six passing Maestro flows, Flutter accessibility-guideline tests, and React Native component/workflow tests. It does not record iOS VoiceOver testing or a complete criterion-by-criterion evaluation of both final mobile builds. Current app code may have changed since that evidence. Contrast ratios and text-spacing overrides were not comprehensively measured. See [Week 6 evidence](../week6/ACCESSIBILITY_TEST_REPORT.md), [Maestro run record](../week6/MAESTRO_EVIDENCE.md), and [platform READMEs](../../mobile-flutter/README.md), [Flutter](../../mobile-rn/README.md) [React Native](../../mobile-rn/README.md).

## WCAG 2.1 Level A and AA criteria

| Criterion | Level | Status | Implementation, evidence, and limitation |
|---|---|---|---|
| **1.1.1 Non-text Content** | A | **Partially Supports.** | Icon controls and tappable rows use semantic labels/roles; automated widget/component tests cover representative labels. Android TalkBack was recorded; full image/decorative-content review and iOS VoiceOver are pending. |
| **1.2.1 Audio-only and Video-only (Prerecorded)** | A | **Not Applicable.** | No prerecorded audio-only or video-only content is documented in either app. |
| **1.2.2 Captions (Prerecorded)** | A | **Not Applicable.** | No prerecorded synchronized audio/video is documented. |
| **1.2.3 Audio Description or Media Alternative (Prerecorded)** | A | **Not Applicable.** | No prerecorded video content is documented. |
| **1.2.4 Captions (Live)** | AA | **Not Applicable.** | No live synchronized audio/video is documented. |
| **1.2.5 Audio Description (Prerecorded)** | AA | **Not Applicable.** | No prerecorded video content is documented. |
| **1.3.1 Info and Relationships** | A | **Partially Supports.** | Flutter widgets and React Native controls expose labels, roles, and states; tests exercise semantics. Complete screen-by-screen TalkBack/VoiceOver tree review on current builds remains pending. |
| **1.3.2 Meaningful Sequence** | A | **Partially Supports.** | Named-route navigation (Flutter) and typed React Navigation preserve screen/flow order. Reading order has not been re-audited with screen readers on both final builds. |
| **1.3.3 Sensory Characteristics** | A | **Partially Supports.** | Actions have text labels and visible controls; no sensory-only instruction is documented. Validate every user instruction and status with both platforms' AT. |
| **1.3.4 Orientation** | AA | **Partially Supports.** | Flutter has phone/tablet responsive layouts; React Native `app.json` sets portrait orientation. Landscape behavior is not established for both apps. Use portrait orientation as a workaround; verify landscape support before claiming full conformance. |
| **1.3.5 Identify Input Purpose** | AA | **Partially Supports.** | Form fields have visible labels and semantic names. A complete audit of platform autofill/input-purpose metadata is not recorded. |
| **1.4.1 Use of Color** | A | **Partially Supports.** | Status text/icons and selected states supplement color in shared controls. A full status-by-status color-independence review on both apps is pending. |
| **1.4.2 Audio Control** | A | **Not Applicable.** | The apps do not document automatically playing audio. |
| **1.4.3 Contrast (Minimum)** | AA | **Partially Supports.** | Design tokens and light/dark themes are implemented. The located mobile evidence does not include comprehensive rendered contrast measurements for every screen/state. Use system/in-app theme choices; record measured contrast before claiming full support. |
| **1.4.4 Resize Text** | AA | **Partially Supports.** | Flutter and React Native include a 200% in-app text-size option and scalable controls. Current-build testing of every screen at 200% plus system text scaling is pending. |
| **1.4.5 Images of Text** | AA | **Partially Supports.** | Primary interface copy is rendered as text; no image-of-text audit covering all assets is recorded. |
| **1.4.10 Reflow** | AA | **Partially Supports.** | Phone/tablet layouts and scrollable screens are implemented. No complete viewport/text-size test record establishes no two-dimensional scrolling or content loss for both builds. |
| **1.4.11 Non-text Contrast** | AA | **Partially Supports.** | Focus rings, control borders, and theme tokens are implemented. Numeric 3:1 measurements for every control boundary, state, and focus indicator are not recorded. |
| **1.4.12 Text Spacing** | AA | **Partially Supports.** | Scalable layouts exist, but WCAG line-height, paragraph, letter, and word-spacing overrides were not tested. Increase app/system text size while a full spacing test remains pending. |
| **1.4.13 Content on Hover or Focus** | AA | **Partially Supports.** | Mobile interfaces are touch-first and expose labels/tooltips where implemented. Verify any hover/focus-triggered content with external keyboard and AT; no complete behavior record is available. |
| **2.1.1 Keyboard** | A | **Partially Supports.** | Native touch controls and keyboard-focus styling are implemented; external-keyboard operation on Android/iOS was not recorded. Touch remains the documented primary interaction. |
| **2.1.2 No Keyboard Trap** | A | **Partially Supports.** | Navigation and dialog controls provide close/cancel routes; no comprehensive hardware-keyboard trap test is recorded on both platforms. |
| **2.1.4 Character Key Shortcuts** | A | **Not Applicable.** | No single-character keyboard shortcuts are documented in the mobile apps. |
| **2.2.1 Timing Adjustable** | A | **Partially Supports.** | No user task deadline or session timeout is documented. Verify that every transient confirmation/undo affordance remains available long enough for users who need more time. |
| **2.2.2 Pause, Stop, Hide** | A | **Not Applicable.** | No automatically moving, blinking, scrolling, or periodically updating media/content requiring pause controls is documented. |
| **2.3.1 Three Flashes or Below Threshold** | A | **Not Applicable.** | No flashing content is documented. |
| **2.4.1 Bypass Blocks** | A | **Partially Supports.** | Native navigation and screen-reader control navigation are present. A dedicated skip-to-content control is not documented in mobile screens; validate long screens with TalkBack/VoiceOver. |
| **2.4.2 Page Titled** | A | **Partially Supports.** | App and route names are set in navigation, but platform window/screen title announcements were not comprehensively checked on current builds. |
| **2.4.3 Focus Order** | A | **Partially Supports.** | React Navigation and Flutter named routes provide ordered flows; tap targets and focus states have targeted tests. Complete screen-reader/external-keyboard order testing is pending. |
| **2.4.4 Link Purpose (In Context)** | A | **Partially Supports.** | Controls use action-oriented accessible labels; a full audit of all linked text/action names is not recorded. |
| **2.4.5 Multiple Ways** | AA | **Partially Supports.** | Main destinations have persistent tab navigation and some dashboard/detail shortcuts. There is no full route-by-route demonstration of multiple ways to locate every screen. |
| **2.4.6 Headings and Labels** | AA | **Partially Supports.** | Forms and controls have names; screen and section heading hierarchy has not been audited across both final apps with AT. |
| **2.4.7 Focus Visible** | AA | **Partially Supports.** | Shared `TapButton` implements a visible focus ring and tests cover it; a complete external-keyboard visual check on Android/iOS is pending. |
| **2.5.1 Pointer Gestures** | A | **Partially Supports.** | Dashboard reordering has Move Up/Move Down controls as alternatives to optional drag. Verify all gesture-based actions have equivalent single-pointer controls on each platform. |
| **2.5.2 Pointer Cancellation** | A | **Partially Supports.** | Native buttons/pressables are used; a dedicated down/up/cancel interaction audit is not recorded. |
| **2.5.3 Label in Name** | A | **Partially Supports.** | Visible labels and accessibility labels are used on representative controls. Full comparison of visible label text against programmatic names is pending. |
| **2.5.4 Motion Actuation** | A | **Not Applicable.** | No device motion or user movement is used to activate features. |
| **3.1.1 Language of Page** | A | **Partially Supports.** | UI copy is English; platform locale/language announcement was not independently verified with both TalkBack and VoiceOver. |
| **3.1.2 Language of Parts** | AA | **Not Applicable.** | The documented user-interface content is English only; no foreign-language passage is identified. |
| **3.2.1 On Focus** | A | **Partially Supports.** | Focusing native controls is not documented as a navigation trigger. Verify with external keyboard and screen reader on the final builds. |
| **3.2.2 On Input** | A | **Partially Supports.** | Forms use explicit actions and validation; no full test records show that changing every input does not unexpectedly change context. |
| **3.2.3 Consistent Navigation** | AA | **Partially Supports.** | Both apps use a consistent five-destination navigation shell. A complete screen-by-screen consistency review is pending. |
| **3.2.4 Consistent Identification** | AA | **Partially Supports.** | Shared controls and design tokens are used; test evidence covers component behavior but not every repeated action label. |
| **3.3.1 Error Identification** | A | **Partially Supports.** | Form validation and accessible feedback are implemented/tested in both codebases. Current-build TalkBack/VoiceOver review of all error states remains pending. |
| **3.3.2 Labels or Instructions** | A | **Partially Supports.** | Visible labels, hints, and required states are implemented; component tests cover representative forms. Verify every field on current builds. |
| **3.3.3 Error Suggestion** | AA | **Partially Supports.** | Form errors provide guidance where implemented; no full error-message audit across all forms is recorded. |
| **3.3.4 Error Prevention (Legal, Financial, Data)** | AA | **Partially Supports.** | Destructive actions use confirmation dialogs and some state can be reversed. Review all data-changing flows and ensure submitted values can be checked/corrected. |
| **4.1.1 Parsing** | A | **Not Applicable.** | These are native mobile interfaces; no browser markup-language content is evaluated under this criterion. |
| **4.1.2 Name, Role, Value** | A | **Partially Supports.** | Native semantic roles, labels, and selected/pressed states are implemented and covered by tests. Android TalkBack evidence is recorded; iOS VoiceOver and full final-build control-state coverage are pending. |
| **4.1.3 Status Messages** | AA | **Partially Supports.** | Flutter/RN expose polite validation/status feedback in documented flows. Verify all status announcements with TalkBack and VoiceOver; iOS behavior is unknown. |

## Known limitations and workarounds

- **No iOS VoiceOver evidence:** use Android builds with TalkBack for the recorded accessibility workflow; do not claim iOS conformance until both iOS builds are tested with VoiceOver.
- **Contrast and text-spacing measurements are incomplete:** use the available light/dark theme and text-size controls; do not interpret those options as proof of WCAG contrast or text-spacing conformance.
- **Mobile screenshots are not included in this repository's current user-guide evidence:** capture current device screens from Flutter and React Native builds before final submission.
- **Sample data and local state only:** do not use the prototype to manage real medications, emergency events, or protected health information.

## Evidence references

- [Week 6 accessibility report](../week6/ACCESSIBILITY_TEST_REPORT.md)
- [Week 6 TalkBack and Maestro run evidence](../week6/MAESTRO_EVIDENCE.md)
- [Flutter accessibility guideline test](../../mobile-flutter/test/accessibility/accessibility_guidelines_test.dart)
- [Flutter README](../../mobile-flutter/README.md)
- [React Native README](../../mobile-rn/README.md)
