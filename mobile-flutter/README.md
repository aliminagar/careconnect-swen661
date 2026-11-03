# CareConnect - Flutter (Mobile)

CareConnect is a medical companion app for care recipients (patients) living with short-term memory loss and their caregivers: it lowers the daily cognitive load of remembering medications and appointments for the patient, while giving caregivers clear visibility into schedules and adherence. This folder is the Android + iOS build, implementing the team's Figma design system with a **Left-Hand Mode** accessibility focus. Covers **LO1: Design and build a mobile user interface**.

## What's implemented (Week 4)

- **12 functional screens**: Landing (with assistant chat), Sign In, Sign Up, Dashboard, Medications, Appointments, Activity, Messages, a Message detail screen, a Medication detail screen, an Appointment detail screen, and an Archived messages screen.
- **Real navigation** via the Flutter `Navigator` and named routes (`MaterialApp(initialRoute:, onGenerateRoute:)` in `lib/main.dart`), not a hand-rolled page switch:
  - The bottom nav bar / tablet sidebar use `pushReplacementNamed` between the five main tabs, so the back stack does not grow on every tab tap (matching standard bottom-nav behavior).
  - Selecting a message in the Messages list or in the Dashboard's unread widget does a real `pushNamed('/messages/detail', arguments: message)`, handing that specific `Message` object to the detail screen and giving it a genuine back stack: opening a message and tapping Back returns to the list, not to the previous tab.
  - Tapping a medication or appointment card (outside its Edit/Delete buttons) does the same: `pushNamed('/medications/detail', ...)` / `pushNamed('/appointments/detail', ...)`, opening a detail screen for that specific item with its own Edit and Delete actions, backed by the same form sheet and (for medications) delete-confirmation dialog the list card uses.
  - The Messages screen's header has an Archived-messages button (a plain archive icon, deliberately without a count badge -- unlike an unread count, an archived count can't be cleared by the user, so a persistent number there would just be a permanent, meaningless notification) that does `pushNamed('/messages/archived')`, opening a list of just the messages that have been archived -- they're hidden from the main inbox, not deleted, and this is the one place they're still visible.
  - Sign in / sign up / sign out use `pushNamedAndRemoveUntil` so the auth screens and the authenticated app never end up on the same back stack.
- **State management**: a single `AppState` (`ChangeNotifier`) holds all app data (medications, appointments, activity log, messages, and settings). It is created once in `main.dart` and published through a `ChangeNotifierProvider` (the `provider` package); the app's root widget reads it with `context.watch<AppState>()`, and that rebuild is what propagates a change through every currently-active screen. Screens still receive `AppState` through their own constructors (a plain, ordinary Provider usage pattern - only the root needed to reach for `context.watch`directly), and call its methods directly rather than duplicating data in local `setState`. Local, screen-only UI state (a form's in-progress text, whether a sheet is open) stays in each screen's own `State` with `setState`, per the assignment's guidance that `setState` is fine for small local state but not for state shared across the app. Navigation state itself is not stored on `AppState` at all, it is owned entirely by the `Navigator`.
- **Messages**: read/unread state with its own tap target (a toggle button, not a swipe gesture, per the team's "No Drag-Only Actions" constraint, WCAG 2.5.7), an unread-count badge on the Messages nav item that stays in sync with the Dashboard's "Unread messages" widget, and compose/reply, archive, and delete flows. Archiving a message hides it from the main inbox without deleting it; the Archived messages screen lists just those, and its detail view offers Unarchive in place of Archive to bring one back.
- **One-Handed Mode** (Settings, One-Handed Mode): Left mode anchors the bottom navigation (or the sidebar, on tablets) to the left edge and moves the SOS button to the bottom-left corner, keeping frequent actions in the left thumb zone.
- **Tablet layouts**: sidebar navigation replaces the bottom bar at &gt;=768dp; content grids switch from single-column to multi-column.
- **WCAG 2.2 AA behaviors**:
  - Tap targets &gt;=48dp everywhere (WCAG 2.5.8 baseline used for this assignment); primary buttons 52-60dp.
  - Dashboard reordering works with Move Up / Move Down buttons, no drag required (2.5.7); long-press drag is offered only as an optional extra.
  - Visible focus states on all interactive elements (2.4.7): TapButton draws a 3px focus ring offset 2px (in `--ring`, or `--destructive` for the destructive variant), per the design system's component library.
  - Semantic labels on icon-only buttons and on custom tappable rows (the message list's read/unread toggle, the dashboard's medication and message tiles, the nav items) for TalkBack/VoiceOver.
- **Full TapButton interaction states** (per the Assignment 3 component library, §6.3.1): every variant has hover (`--*-hover`) and press (`--*-active`) background tokens wired in, a disabled state at 40% opacity, and the keyboard focus ring above -- previously the button rendered identically in every state.
- **SOS dialog opens a real** `tel:` **link** (`url_launcher`), matching the design system's SOS confirmation spec (§3.3) instead of just closing the dialog.
- **Appointment deletion confirms first**, via the same confirm dialog pattern medications and messages already used -- previously it deleted immediately with no confirmation step.
- **"✓ Taken!" inline confirmation** on the medication card's mark-as-taken toggle, matching the design system's inline status feedback pattern (§6.3.8) already used by the Dashboard check-in and Activity refresh.
- **A real TextTheme** in `app_theme.dart` implementing the Assignment 3 typography scale (§6.2: h1 32/800 ... caption 12/500, label 12/600 uppercase), applied as the app-wide `ThemeData.textTheme` instead of screens each hand-rolling ad-hoc font sizes.
- **Tests** (`test/`): unit tests for `AppState`'s business logic (medications, appointments, activity logging, message read/unread/ archive/delete, settings, sign-in/sign-out, and the injected-clock timestamp formatting) plus widget tests for every screen: Landing, Sign In/Sign Up (validation and successful sign-in/sign-up navigation), Dashboard (check-in, alerts, the medication tile toggle, Customize, and "View all" navigation), Medications and Appointments (add/edit/delete, including validation), Medication detail and Appointment detail (list-to-detail data hand-off, mark-as-taken, edit-in-place, and delete returning to the list), Activity (filtering and refresh), Messages and Message detail (compose, reply, archive, delete, the read/unread toggle, and list-to-detail data hand-off), Archived messages (the archive entry point's lack of a count badge, filtering to just archived messages, and unarchiving back to the inbox), the Settings sheet, and the shared `TapButton` / `CCFormField` / card components. `mocktail` mocks callback dependencies (e.g. verifying a button's `onPressed` fires exactly once) where that is a more direct check than inferring it from a side effect. TapButton's interaction states are covered directly: disabled 40% opacity, hover/press token colors, and the keyboard focus ring (including the destructive variant ringing in `--destructive`).

## Project structure

```
lib/
├── main.dart                  # App entry, named-route navigation, demo seed data
├── models/app_state.dart      # State model (meds, appointments, activity, messages)
├── theme/
│   ├── tokens.dart            # Design tokens from the Figma system
│   └── app_theme.dart         # Light/dark ThemeData builders
├── widgets/
│   ├── tap_button.dart        # Primary button component (5 variants, 3 sizes)
│   ├── form_field.dart        # Labelled fields + inputs
│   ├── cards.dart             # Logo, StatCard, AlertCard
│   ├── app_shell.dart         # Header, nav (phone/tablet), SOS, AppTab enum
│   └── settings_drawer.dart   # Settings sheet (hand mode, theme, text size)
└── screens/                   # Landing, auth, Dashboard, Medications,
                                # Appointments, Activity, Messages, Message
                                # detail, Medication detail, Appointment
                                # detail, Archived messages

test/
├── models/
│   ├── app_state_test.dart            # Unit tests for AppState's business logic
│   └── medication_test.dart           # Unit tests for Medication.copyWith
├── support/test_app.dart              # Shared test harness: full named-route app + seed data
└── widget/
    ├── navigation_test.dart           # Nav, Left-Hand Mode, message detail data hand-off
    ├── dashboard_screen_test.dart
    ├── medications_screen_test.dart
    ├── appointments_screen_test.dart
    ├── medication_detail_screen_test.dart
    ├── appointment_detail_screen_test.dart
    ├── activity_screen_test.dart
    ├── messages_screen_test.dart
    ├── message_detail_screen_test.dart
    ├── archived_messages_screen_test.dart
    ├── auth_screens_test.dart
    ├── landing_screen_test.dart
    ├── settings_drawer_test.dart
    ├── tap_button_test.dart
    ├── form_field_test.dart
    └── cards_test.dart
```

## Running the app

Requires the [Flutter SDK](https://docs.flutter.dev/get-started/install)(3.27+ / Dart 3.6+).

## Week 6 accessibility and E2E evidence

- Flutter uses semantic labels/roles, visible focus states, 48dp minimum primary controls, live validation feedback, and a 200% text-size option.
- `test/accessibility/accessibility_guidelines_test.dart` exercises Flutter's Android target-size and labelled-control guidelines.
- `integration_test/critical_workflows_test.dart` covers sign-in and the daily check-in workflow. Run it with `flutter test integration_test` on a configured target.
- Maestro flows are in [`../maestro/`](../maestro/) and use Android package `com.example.careconnect`.
- The accessibility test report and Maestro evidence record are in [`../docs/week6/`](../docs/week6/). The VPAT and TalkBack recordings are part of the team's Week 6 submission document.

```bash
cd mobile-flutter
flutter create . --platforms=android,ios --project-name careconnect   # one-time: generates android/ + ios/ shells
flutter pub get
flutter run                    # or: flutter run -d chrome for a quick web preview
```

> `flutter create .` generates the native `android/` and `ios/` folders (not checked in until you run it). Run it once after cloning, then commit the generated folders so teammates don't need to regenerate them.

## Running the tests

```bash
cd mobile-flutter
flutter pub get
flutter test --coverage
```

This runs every file under `test/` and writes `coverage/lcov.info`.

### Generating the HTML coverage report

`lcov.info` is a plain-text summary, not the report the assignment asks for. Turn it into an HTML page one of these ways:

- **VS Code, no install needed:** the "Coverage Gutters" extension reads `coverage/lcov.info` directly and shows a percentage plus inline highlighting in the editor. Fastest option if the team is on VS Code already.

- **Node (already installed for the** `web/` **project on this repo):**

  ```bash
  npx --yes @lcov-viewer/cli lcov coverage/lcov.info -o coverage/html
  ```

  then open `coverage/html/index.html`. This works the same on Windows, macOS, and Linux without installing `lcov`/`genhtml` separately.

- **macOS/Linux with** `lcov` **installed** (`brew install lcov` or `apt install lcov`), or Windows via WSL:

  ```bash
  genhtml coverage/lcov.info -o coverage/html
  ```

Whichever method is used, the report's summary page shows the overall line percentage plus per-file, per-line detail.

## Test coverage evidence

The assignment's minimum is **60% line coverage**. To get the overall percentage without installing `lcov`/`genhtml`, sum the `LF`/`LH` totals straight out of `coverage/lcov.info` after running `flutter test --coverage`:

```bash
awk -F: '/^LF:/{lf+=$2} /^LH:/{lh+=$2} END{printf "Lines: %d/%d (%.1f%%)\n", lh, lf, 100*lh/lf}' coverage/lcov.info
```

**Overall line coverage: 93.9% (2029 / 2160 lines)** — all 128 tests passing. Generated 2026-09-08 from commit `0ea16d2` on `feat/flutter-app`via `flutter test --coverage`, then `npx --yes @lcov-viewer/cli lcov coverage/lcov.info -o coverage/html` for the HTML report referenced below.

Per-file breakdown (lines covered / total):

| File                                         | Coverage        |
| -------------------------------------------- | --------------- |
| `lib/widgets/app_shell.dart`                 | 145/228 — 63.6% |
| `lib/screens/dashboard_screen.dart`          | 321/353 — 90.9% |
| `lib/theme/app_theme.dart`                   | 13/14 — 92.9%   |
| `lib/models/app_state.dart`                  | 129/134 — 96.3% |
| `lib/screens/archived_messages_screen.dart`  | 43/44 — 97.7%   |
| `lib/screens/auth_screens.dart`              | 147/149 — 98.7% |
| `lib/screens/landing_screen.dart`            | 78/79 — 98.7%   |
| `lib/widgets/cards.dart`                     | 78/79 — 98.7%   |
| `lib/widgets/tap_button.dart`                | 92/93 — 98.9%   |
| `lib/screens/activity_screen.dart`           | 105/106 — 99.1% |
| `lib/screens/messages_screen.dart`           | 151/152 — 99.3% |
| `lib/screens/appointments_screen.dart`       | 187/188 — 99.5% |
| `lib/screens/medications_screen.dart`        | 190/191 — 99.5% |
| `lib/screens/appointment_detail_screen.dart` | 69/69 — 100%    |
| `lib/screens/medication_detail_screen.dart`  | 70/70 — 100%    |
| `lib/screens/message_detail_screen.dart`     | 80/80 — 100%    |
| `lib/theme/tokens.dart`                      | 1/1 — 100%      |
| `lib/widgets/form_field.dart`                | 44/44 — 100%    |
| `lib/widgets/settings_drawer.dart`           | 86/86 — 100%    |

`lib/main.dart` (224 lines: app entry point, route table, and demo seed data) does not appear in `lcov.info` at all — it's never imported by a test file. `test/support/test_app.dart` deliberately mirrors its route table in a lighter test harness instead of importing it directly (see the comment there), so its 93.9%/2160-line total is coverage over the 19 files that are exercised by tests, not literally every line in `lib/`. `app_shell.dart` is the lowest-covered file at 63.6%, still above the 60% bar on its own.

The generated `coverage/html/index.html` (from the command above) has the same numbers with per-line highlighting; `coverage/` is gitignored, since it's build output rather than source.

## Known issues and limitations

- **TalkBack was manually tested on an Android emulator** in the Week 6 walkthrough; see [`docs/week6/ACCESSIBILITY_TEST_REPORT.md`](../docs/week6/ACCESSIBILITY_TEST_REPORT.md) and [`MAESTRO_EVIDENCE.md`](../docs/week6/MAESTRO_EVIDENCE.md). **iOS VoiceOver has not been tested** in the evidence located for this submission. Repeat the manual checks on the final builds before claiming current cross-platform assistive-technology coverage.
- **The assistant chat on the Landing screen is a scripted, canned-reply demo**, not a real chatbot integration and is really just a placeholder from the initial CareConnect design.

## Team contributions (Week 4)

Per the team charter's rotation for weeks 3 to 4, Wiliss Tako is Technical Lead, Dom Puller is QA / Testing Lead, and Upneet Bir is Documentation Lead for this cycle.

- **Dom Puller** - QA / Testing Lead
- **Upneet Bir** - Documentation Lead
- **Wiliss Tako** - Technical Lead

## AI Usage Disclosure

Claude and Figma Make was used as intial generative design and coding tools across this Flutter implementation. All AI-assisted code was reviewed before being committed.

## Design source

Screens are ported from the team's Figma Make prototype (`SWEN661-T1-MobileTabletUIImplementation`), which stays the source of truth for design and feature changes; the Flutter build is kept in sync with it by hand. See [docs/week3-design-notes.md](../docs/week3-design-notes.md)for the original design decisions and persona mapping, and the root [README.md](../README.md) for overall project context.
