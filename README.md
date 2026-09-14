# Andy Nkumane — Portfolio

A responsive personal portfolio presenting my backend engineering experience, technical skills, selected projects, and contact details.

Live site: [andy-nkumane.github.io](https://andy-nkumane.github.io/)

## Features

- Responsive layout for desktop, tablet, and mobile screens
- Semantic HTML structure with keyboard-accessible navigation
- About, skills, projects, and contact sections
- Project technology tags and outcome summaries
- Featured Buddy Budget project with an expandable, source-linked engineering case study
- Fleet Management System API prototype with implementation evidence and explicit limitations
- Direct links from overlapping portfolio projects to their interactive or rendered Project Lab experiences
- Optimized WebP images with lazy loading
- Open Graph metadata for link previews
- Reduced-motion support

## Technology

The site is intentionally lightweight:

- HTML5
- CSS3
- GitHub Pages

It has no JavaScript runtime or package dependencies.

## Project structure

    .
    ├── .github/workflows/    # Automated site validation
    ├── images/               # Active portfolio and social assets
    ├── scripts/              # Dependency-free static-site checker
    ├── index.html            # Site content and semantic structure
    ├── style.css             # Visual design and responsive layouts
    ├── PORTFOLIO-AUDIT.md    # Review evidence and remaining work
    └── README.md             # Project documentation

## Run locally

The site can be opened directly from `index.html`. To test it through a local web server, run `python -m http.server 8000`, then visit `http://localhost:8000`.

## Deployment

The repository is deployed with GitHub Pages. Changes published to the configured Pages branch become available at the live-site URL.

## Validation

Run `python scripts/check_site.py` to check HTML nesting, duplicate IDs, local links, anchor targets, image attributes, CSS asset references, and unreferenced files in `images/`. The same check runs in GitHub Actions on pushes and pull requests. It uses only the Python standard library and adds no site runtime dependencies.

Before publishing, also check keyboard navigation, narrow and wide layouts, and external project destinations in a browser. The script does not validate external URLs or replace a full HTML or accessibility audit.

## Project evidence and image provenance

Buddy Budget's case study was reviewed against [commit `4bb6b78`](https://github.com/Andy-Nkumane/buddy-budget/tree/4bb6b786b88f117f9036200317ce9cf769c9839b). Its source links are pinned to that revision so readers can inspect the implementation described. Review the case study before updating those links; do not infer passing tests or production usage from source alone.

`images/buddy-budget.webp` is an optimized copy of that repository's `public/screenshots/desktop-budget.png` (1440 × 1024). It shows the landing page with sample budget figures, not an authenticated account. See [PORTFOLIO-AUDIT.md](PORTFOLIO-AUDIT.md) for evidence, resolved findings, and remaining content gaps.

Fleet Management System was reviewed against [commit `4e0a4c7`](https://github.com/Andy-Nkumane/Fleet-Management-System/tree/4e0a4c7538c018857548a14d8e1dab72921db053). It is presented as a local API prototype with simulated movement, not a deployed GPS service. The case study links to the controller, dashboard, and current test code; no passing-test or production-readiness claim is made. No screenshot or live deployment was verified. `images/fleet-management.webp` is an optimized conceptual fleet-location illustration generated with the built-in image generation tool; it is not an application screenshot.

## TODO

- [ ] Add a current résumé/CV link to the hero section.
- [ ] Add relevant recruiter context, such as location, preferred role type, and work arrangement.

## Contact

- Email: [nkumaneandy@gmail.com](mailto:nkumaneandy@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/andy-nkumane-405163185)
- [GitHub](https://github.com/Andy-Nkumane)
