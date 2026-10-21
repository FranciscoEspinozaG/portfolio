# Francisco Espinoza — Portfolio

Responsive Next.js App Router portfolio implemented from [the Figma design](https://www.figma.com/design/frFWuqb8XC2ZB6MKRGVdOI/Francisco-Espinoza---Portafolios?node-id=2001-7).

## Run locally

Requires Node.js 20.9 or later.

```sh
npm install
cp .env.example .env.local
npm run dev
```

Open http://localhost:3000. Contact destinations are configured in `.env.local`; the supplied LinkedIn and email are included in `.env.example`.

```sh
npm run build
npm run typecheck
npm start
```

Uses the original Figma portrait, SENTUA image, timeline SVGs, and project arrows, all stored locally. Clarity City fonts are distributed with their license in `public/assets/FONT-LICENSE.txt`.

Includes section navigation with active states, an Escape-dismissible mobile menu, reduced-motion support, keyboard focus styles, Spanish metadata, and working contact links. Figma contains one featured project; Swiper automatically enables navigation when more project entries are added.

## Editing modules

- `app/page.tsx` composes the six independent section modules in `components/sections/`.
- `data/portfolio.ts` contains technologies, projects, about paragraphs, statistics, navigation entries, and experience.
- Add, remove, or reorder objects in `technologies`; each entry renders through `components/highlight-item/HighlightItem.tsx`. Use `description` for an optional subtitle.
- Add a project object to `projects` with a unique `id`, title, local image metadata, platform, and role. An optional `url` makes its title a link. Each entry renders as its own Swiper slide through `components/project-card/ProjectCard.tsx`.
- `components/projects-carousel/ProjectsCarousel.tsx` owns Swiper interaction and accessible controls. It supports touch, keyboard, and previous/next buttons; controls disable at the first/last slide, including when there is only one project.
- `components/navigation/Navigation.tsx` owns menu state independently; the page and static sections remain server components.

## Component folders

Each reusable component owns a folder and its styles:

- `components/highlight-item/` — labels and optional subtitles for stats and technologies.
- `components/experience-item/` — individual career timeline entries, with years, company, and roles as props.
- `components/project-card/` — project image and glass caption.
- `components/projects-carousel/` — Swiper, controls, caption fades, and slide containment.
- `components/navigation/` — section links and mobile menu.
- `components/footer/` — page footer.

Section composition lives in individual folders under `components/sections/`. Shared foundations, glass styling, and page scroll snapping remain in `app/globals.css`.
