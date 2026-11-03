# CareConnect

A responsive, accessible medical companion application for care recipients (patients) living with short-term memory loss and their caregivers — built across web, mobile, and desktop as a SWEN 661 team project.

CareConnect lowers the daily cognitive load for people who need help remembering, while giving caregivers clear visibility and control over medications and appointments. The patient experience favors recognition over recall (persistent orientation cues, one primary task per screen, always-visible medication status, undo on every action); the caregiver experience is a denser dashboard for managing schedules and monitoring adherence.

## Team

| Name | Email | GitHub | Weeks |
|---|---|---|---|
| Dom Puller | domspencer01@outlook.com | [LaoWai-Fi](https://github.com/LaoWai-Fi) | 1-12 |
| Wiliss Tako | takowiliss@gmail.com | [wilisstako](https://github.com/wilisstako) | 1-12 |
| Rehman Uddin | 89uddinrt@gmail.com | [89uddinrt](https://github.com/89uddinrt) | 6-12 |
| Upneet Bir | upneetbir@gmail.com | [upneetsb](https://github.com/upneetsb) | 1-6 |

Full roles, communication plan, and Git workflow: [docs/team-charter.md](docs/team-charter.md).

## Repository structure

This is a monorepo covering all four platforms required across the course's learning objectives (LO1: mobile, LO2: web, LO3: desktop):

```
careconnect-swen661-T1/
├── web/                  # React + Vite — responsive web app (LO2)
├── mobile-flutter/       # Flutter — Android + iOS (LO1)
├── mobile-rn/            # React Native / Expo — Android + iOS (LO1)
├── desktop-electron/     # Electron — desktop (LO3)
└── docs/
    └── team-charter.md   # team roles, workflow, communication plan
```

`web/` and `mobile-flutter/` are built out; `mobile-rn/` is the Week 5 React Native port of the Flutter app (117 tests, 82% statement coverage, React Navigation, ESLint-clean) — see [web/README.md](web/README.md), [mobile-flutter/README.md](mobile-flutter/README.md), and [mobile-rn/README.md](mobile-rn/README.md) for their setup and feature writeups. `desktop-electron/` contains the Electron desktop app (Week 7 prototype, Week 8 full implementation); see its [README](desktop-electron/README.md) and the [Week 7 submission index](docs/week7/README.md).

**Week 8 (Electron desktop):** setup, testing and packaging are in [desktop-electron/README.md](desktop-electron/README.md), and the submission index (architecture, test report, accessibility testing) is in [docs/week8/README.md](docs/week8/README.md).

**Week 10 (responsive web):** the Part 3 performance and SEO plan is available as [editable Markdown](docs/week10/PART3_PERFORMANCE_SEO.md) and [Word](docs/week10/PART3_PERFORMANCE_SEO.docx); it documents proposed performance budgets, image and code-loading strategy, social metadata, and sitemap/robots structure.

**Week 12 (final documentation):** the [Part 3 submission index](docs/week12/README.md) links to the user and developer guides and WCAG 2.1 A/AA conformance reports for Flutter/React Native, Electron, and React web. It also records evidence limits and remaining human verification.

The two mobile toolchains are compared in [docs/rn-vs-flutter-comparison.md](docs/rn-vs-flutter-comparison.md);

## Setup instructions

Each platform folder is self-contained with its own dependencies and `.gitignore`. Clone the repo, then `cd` into the platform you're working on:

```bash
git clone https://github.com/LaoWai-Fi/careconnect-swen661-T1.git
cd careconnect-swen661-T1

cd web && npm install && npm run dev              # web app — see web/README.md
cd mobile-flutter && flutter create . --platforms=android,ios --project-name careconnect && flutter run   # Flutter mobile app — see mobile-flutter/README.md
cd mobile-rn && npm install && npx expo start     # React Native mobile app — see mobile-rn/README.md
```

## License

MIT — see [web/License](web/License).
