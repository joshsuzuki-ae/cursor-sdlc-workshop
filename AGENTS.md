# AGENTS.md

## Cursor Cloud specific instructions

### Overview

This is a workshop repository with multiple independent React + Vite frontend apps. There is no backend, no database, and no Docker required.

### Key Services

| Service | Directory | Port | Dev Command |
|---------|-----------|------|-------------|
| Workshop Slides | `workshop-slides/` | 5175 | `npm run dev` |
| LinkedOut (Teams 1-5) | `linkedout/team_X/` | 3001-3005 | `npm run dev` |

### Running the Apps

Each app is self-contained. To run any app:
```bash
cd <app-directory>
npm install
npm run dev
```

### Lint & Build

- **Lint** (workshop-slides only has ESLint configured): `cd workshop-slides && npm run lint`
- **Build** any app: `npm run build` from its directory

### Important Notes

- Node.js v20.19.0+ is required (Vite 7 in workshop-slides needs `^20.19.0 || >=22.12.0`).
- The linkedout team apps use Vite 5 and show a CJS deprecation warning — this is expected and non-blocking.
- Each `linkedout/team_X` folder is an identical copy; testing against `team_1` is representative.
- There are no environment variables or secrets needed for any of the apps.
- Participant project folders under `projects/` and `archive/` each have their own `package.json` and may require separate `npm install`.
