# CareConnect — User Guide

CareConnect is an educational care-coordination prototype for care recipients and caregivers. It helps people view a daily routine, medication schedule, appointments, activity, and messages. The user interface is designed to reduce memory load through clear labels, predictable navigation, large controls, and visible status feedback.

> **Important:** CareConnect is not a medical device or clinical service. It uses demonstration/sample data and does not provide medical advice, verify medication instructions, contact emergency services, or securely manage real patient records. Do not enter real health information or rely on it for care decisions.

## Access and installation

| Platform | How to access it | Availability and caveats |
|---|---|---|
| Web (React) | Open [CareConnect on GitHub Pages](https://laowai-fi.github.io/careconnect-swen661-T1/). The web app can also be started locally using the developer guide. | This is the only public hosted app link recorded for this project. A browser may offer an install option for the PWA; availability depends on browser/OS. |
| Android / iOS (Flutter) | For a development preview, follow [mobile-flutter/README.md](../../mobile-flutter/README.md). Historical Android APKs were shared separately for Week 6; they are not checked into this repository. | No current Play Store or App Store release is documented. iOS requires a Mac/Xcode build environment. |
| Android / iOS (React Native) | For a development preview, follow [mobile-rn/README.md](../../mobile-rn/README.md) and start Expo. | No current Play Store or App Store release is documented. The repository does not include a configured EAS release profile. |
| macOS / Windows / Linux (Electron) | Follow the install and build notes in [desktop-electron/README.md](../../desktop-electron/README.md). Installers are produced by the Desktop Electron GitHub Actions workflow. | Installers are CI artifacts, not a signed public release. macOS Gatekeeper and Windows SmartScreen may warn because the builds are unsigned. The macOS build has been manually checked; Windows and Linux assistive-technology behavior has not. |

## First use

1. Launch the web or desktop app, or open the mobile preview.
2. Choose **Sign in** or **Sign up**. Authentication is a demo flow, not a real account service. Use non-sensitive sample information only.
3. Use the app navigation to open Dashboard, Medications, Appointments, Activity, or Messages.
4. Explore Settings for theme, text-size, high-contrast, or hand-mode options available on that platform.
5. Use the in-app confirmation dialogs before destructive actions. Verify the displayed data before changing it.

Data behavior differs by platform. The desktop app saves a sample care plan locally and offers import/export. The web app stores demo state in the browser. The mobile apps are standalone demonstrations and do not synchronize care plans between platforms. Do not treat any saved state as a secure health record or backup.

## Key features

### Daily overview and navigation

- Dashboard shows the sample care plan's status, alerts, upcoming items, and unread messages.
- Use the persistent tab/navigation controls to move between the main areas.
- Mobile provides phone and tablet navigation layouts; Electron also offers native menus and keyboard shortcuts.

### Medications and appointments

- View the sample list and mark a medication as taken/not taken.
- Add, edit, or delete demonstration items where the platform supports management controls.
- Review date, time, location, dose, or assignment text carefully. These values are sample content, not a prescription or verified appointment.
- Destructive actions use confirmation dialogs in the documented implementations.

### Activity and messages

- Activity displays a sample history of care-plan actions.
- Messages supports read/unread state and common composition/archive actions, with exact controls varying by platform.
- Messages and activity are local demo interactions; they do not contact clinicians or caregivers.

### Left-Hand / one-handed mode

Open Settings (or the platform's View menu) and choose the hand mode. The interface moves frequently used navigation/actions toward the selected hand where implemented. If controls do not move as expected, turn the setting off and use the standard navigation layout.

### Emergency action

On the mobile and desktop prototypes, the SOS action presents a confirmation before opening the device dialer through a `tel:` link. The app itself cannot place or verify a call. Always use the device's normal emergency calling workflow.

## Accessibility features

- **Screen readers:** Web and Electron use labeled controls and semantic structure. Android TalkBack walkthroughs are recorded for the mobile apps. iOS VoiceOver testing for mobile is not recorded.
- **Keyboard:** Web has a skip link, visible focus, and keyboard-operated dialogs/navigation. Electron adds native menus and shortcuts; see [desktop keyboard shortcuts](../../desktop-electron/README.md#keyboard-shortcuts). Mobile is primarily touch-oriented; an external-keyboard evaluation is still needed.
- **Text size and zoom:** Use the in-app text-size setting where available. Desktop also supports operating-system/browser zoom. Layout and text-size behavior can vary by platform.
- **Contrast and themes:** Light/dark themes are available on mobile; in-app high contrast is available in documented web/desktop builds. The desktop app was checked with macOS Increase Contrast; Windows Contrast Themes were not tested. No theme toggle replaces a criterion-specific contrast evaluation.
- **Focus and dialogs:** Web/Desktop keyboard tests document visible focus, Escape dismissal, and focus restoration for dialogs. Mobile screen-reader behavior must be verified on each final native build.
- **Motion and gestures:** Key actions have labeled buttons; dashboard reorder has tap-based Move Up/Move Down alternatives in the mobile implementations.

For criterion-by-criterion status and the exact evidence scope, see the [Mobile VPAT](MOBILE_VPAT.md), [Desktop VPAT](../week9/CARECONNECT_DESKTOP_VPAT.md), and [Web VPAT](WEB_VPAT.md).

## Screenshots

The following screenshots are existing project evidence, not newly captured screenshots of the final release.

### Web

![CareConnect web landing page](../../web/docs/screenshots/01-landing.png)

![CareConnect web patient Today page](../../web/docs/screenshots/06-patient-today.png)

![CareConnect web caregiver dashboard](../../web/docs/screenshots/10-caregiver-dashboard.png)

More web screenshots are in [`web/docs/screenshots/`](../../web/docs/screenshots/).

### Desktop

![CareConnect Electron landing page](../week8/evidence/01-landing.png)

![CareConnect Electron dashboard](../week8/evidence/02-dashboard.png)

![CareConnect Electron settings dialog](../week8/evidence/04-settings-dialog.png)

More desktop screenshots are in [`docs/week8/evidence/`](../week8/evidence/).

### Mobile screenshot status

No current Flutter or React Native UI screenshots are checked into this repository. The Week 6 Android TalkBack and Maestro evidence is described in [ACCESSIBILITY_TEST_REPORT.md](../week6/ACCESSIBILITY_TEST_REPORT.md) and [MAESTRO_EVIDENCE.md](../week6/MAESTRO_EVIDENCE.md); those records do not provide a current, embedded mobile user-guide screenshot set. Add screenshots from the final Android/iOS builds before submission rather than reusing web images as mobile evidence.

## FAQ and troubleshooting

**Is this a real medication or medical service?**
No. It is an educational prototype with sample data. Ask a clinician or pharmacist about health and medication decisions.

**Can I sign up for a real account or reset a password?**
No production identity service is documented. Sign-in/sign-up are demonstration interactions; there is no real account recovery.

**Will my data synchronize between phone, desktop, and web?**
No. Cross-platform synchronization is not implemented. Desktop local storage/export and browser local storage are separate.

**Why does the assistant give only basic answers?**
It is restricted to explaining CareConnect and onboarding. It must not be used for medical advice. If the optional hosted assistant is unavailable, the web app may use its scripted fallback.

**Why did the SOS button not call emergency services?**
The prototype asks for confirmation and opens the device dialer. It cannot place, monitor, or verify a call.

**The app warns me when I install it. Is that expected?**
Yes for current unsigned desktop builds. See the platform-specific installation instructions in the desktop README. Only install artifacts obtained from the team's trusted course/repository location.

**A screen-reader announcement is missing. What should I do?**
On web, VoiceOver with Safari did not speak the appointment-deletion confirmation even though a visible status message and polite status region are present. This is a known limitation; visually confirm the result. For mobile, the repository does not establish iOS VoiceOver behavior.

**Where are the project tests and full accessibility details?**
Use [the developer guide](DEVELOPER_GUIDE.md), the platform READMEs, and the linked accessibility reports in the [Week 12 index](README.md).
