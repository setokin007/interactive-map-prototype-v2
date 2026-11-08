# PCC Interactive Map & Day Planner — Prototype, Version 2

Version 2 starts as an exact copy of Version 1
([setokin007/interactive-map-prototype](https://github.com/setokin007/interactive-map-prototype),
live at https://interactive-map-prototype-blush.vercel.app). It will be reworked around the
guest's journey, as set out in the PRD's *Version 2: one guest, five stages* section:

| Stage | Guest's question | Where it lives |
| --- | --- | --- |
| 1 · Dreaming | Is this worth a day of my trip? | Website: explore the map |
| 2 · Comparing | What would my day look like? | Website: "Shape your day in three taps" |
| 3 · Booking | Which package fits that day? | Website: package from the shaped day |
| 4 · Booked, preparing | How do I make the most of it? | Website: My Day, opened from the confirmation email or number |
| 5 · On the day | What's next and where is it? | PCC app screens |

Event times will come from PCC's scheduling app; until it can be read, the prototype uses
sample data. Live at https://interactive-map-prototype-v2.vercel.app (Vercel project
`interactive-map-prototype-v2`). Until the rework lands, everything below describes the copied Version 1.

---

A clickable prototype of the **"Plan my day"** experience for polynesia.com: an interactive
map of the Polynesian Cultural Center tied to an itinerary builder. Guests explore the
six island villages and evening options, add the moments they want to a day timeline, and
are handed off to the right ticket package.

> **Status:** design prototype, not production code. Schedules, durations, walking times
> and prices are placeholders, and village content is a draft awaiting cultural review.

## What's in it

Two linked pages that share one itinerary:

| Page | Purpose | Live site | Design source |
| --- | --- | --- | --- |
| 1 · Your day & tickets | Understand the day at the Center, then choose a package | `site/Discover.dc.html` (`/tickets`) | `design/your-day-and-tickets.dc.html` |
| 2 · Plan my day | Map, things to do and the "Your day" timeline; send the day to the app | `site/Main.dc.html` (`/` and `/plan`) | `design/plan-my-day.dc.html` |

| Folder | What it is |
| --- | --- |
| `site/` | **The deployable site.** Standalone exports of both pages with their runtime (`support.js`, `vendor/react*.js`) and images. This is what Vercel serves. |
| `design/` | The design-canvas source of both pages, the canvas layout and the PCC Legacy tokens. Edit the prototype on the canvas, then re-export into `site/`. |
| `assets/` | The same 13 images with readable names, for reuse elsewhere. |

A day built on **Plan my day** is saved in the browser and picked up by **Your day & tickets**
("You started a day in the planner with 8 stops…").

Key features of **Plan my day**:

- The gate handout map as the base layer, with a pin for every village, show, venue and
  exhibit, plus zoom and a walking route for the guest's day.
- **Place markers** shared by the map, the timeline and the place cards: each island culture
  has its own colour and two-letter code (SA, AO, TO, FJ, TA, HI); dinner, the HĀ show and
  "around the Center" places have theirs. Type icons mark shows, activities, exhibits, food,
  tours and shopping. Alert colours (red, orange, amber, info navy) are kept for messages only.
- **How long are you staying?** filters the day to the guest's hours, with an overview of
  how the day flows (Marketplace, villages, dinner, HĀ).
- **Things to do** grouped by part of the day, with village panels that inform without
  spoiling ("What to expect", "The rest we'll save for your visit").
- **Your day** — a pinned, scrollable timeline in the right rail with walking times between
  stops, overlap flags, drag-to-reschedule, ticket and coach-pickup summary, and a pinned
  "See packages for this day" bar.
- A section menu on the left that jumps to each section; the eye button hides or shows one.

`design/canvas.json` lays the two pages out on the design canvas. `design/ds/pcc-legacy/tokens.json`
holds the PCC Legacy design tokens the pages were started from.

## Run it locally

The pages load their scripts, so serve the folder rather than opening the file:

```bash
cd site
python3 -m http.server 8080
# then open http://localhost:8080/Main.dc.html
```

## Deploy on Vercel

The repository is ready to deploy as a static site with no build step. `vercel.json`
serves the `site/` folder, maps `/` and `/plan` to Plan my day and `/tickets` to Your day
& tickets, and caches the images for a year.

1. In Vercel, choose **Add New → Project** and import `setokin007/interactive-map-prototype-v2`.
2. Leave **Framework Preset** as *Other* and the build command empty. The output folder
   comes from `vercel.json`.
3. Deploy. Every push to `main` redeploys; pull requests get preview links.

## Updating the site after design changes

1. Make the change on the design canvas.
2. On each changed page, use the artboard's download menu → **HTML (.zip)**.
3. Replace the page file (`Main.dc.html` or `Discover.dc.html`) and any new images under
   `site/` with the export's contents, and copy the canvas source into `design/`.
4. Commit and push; Vercel redeploys.

## Path to production

This is a reference prototype. For polynesia.com, rebuild the pages as components in the
site's stack (Brightspot), using the PRD's recommended map approach: illustrated tiles on
MapLibre GL JS, with pins, outlines and schedules served from the CMS.

## Before anyone outside the team sees it

- Confirm every presentation time, duration and seating time with Operations.
- Have each village's cultural advisors approve their copy, images and marker colour.
- Replace placeholder prices (`[TOTAL]`, `[PRICE]`) and the sample booking numbers.
- Measure real walking distances from a scaled site plan; current times are estimates.

## Related

- PRD: *PRD — Interactive Map of the Polynesian Cultural Center* (Claude Docs)
- Live prototype: the "PCC Interactive Map — Prototype" design canvas
