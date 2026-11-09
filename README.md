# PCC Interactive Map & Day Planner — Prototype, Version 2

Version 2 focuses on one job: **building a great itinerary for each guest**. Ticket and package
recommendations are out of scope. Version 1
([setokin007/interactive-map-prototype](https://github.com/setokin007/interactive-map-prototype),
live at https://interactive-map-prototype-blush.vercel.app) is kept for reference.

**Live:** https://interactive-map-prototype-v2.vercel.app (Vercel project `interactive-map-prototype-v2`)

| Page | What it does | Route | Design source |
| --- | --- | --- | --- |
| Plan your day | Explore the Center, then generate and edit an itinerary, with or without a ticket | `/` (also `/plan`, `/myday`; `?b=PCC-48213` pulls up a ticket) | `design/plan-your-day.dc.html` |
| PCC app screens (iOS and Android) | Today (runs on the saved day), Map, Running behind, Schedule change | `/app`, `/app-map`, `/app-replan`, `/app-alert` | `design/app-*.dc.html` |
| Version 1 pages (archive) | Packages page and day builder, no longer linked | `/v1/packages`, `/v1/planner` | `design/your-day-and-tickets.dc.html`, `design/plan-my-day.dc.html` |

## How the itinerary is built

1. **Four numbered steps** produce a day: who's coming (couple, family with young kids, group),
   the date (the next 10 days, or any date up to a year out from a date picker; closed Sundays
   and Wednesdays are refused with the next open day suggested), how long they can stay, and where they're staying (cruise guests add their
   all-aboard time).
2. **Optional choices** sharpen it: the evening (lūʻau and HĀ, buffet and HĀ, just HĀ, or none),
   pace (Relaxed adds breaks and fewer stops, See it all packs the day), must-sees (any village,
   Huki, the canoe tour, Iosepa, the Mission Settlement) and interests (shows, trying things,
   food, history, kid favorites).
3. **A ticket** can be pulled up by confirmation number or from the email link. Its date, party
   and set times (lūʻau, buffet, HĀ, guided tour, coach arrival at noon) become fixed points and
   the rest of the day is planned around them.
4. **The generator** (in the page's script) fills the day in time order: it fixes the evening and
   ticket items, adds Huki, then repeatedly picks the best next stop that can be reached in time,
   scoring each candidate by the guest's must-sees, interests and party, favoring villages not yet
   seen, and penalizing waiting and walking. Walking times come from the map at an easy pace.
5. **The canoe ride moves you across the Center.** A ride takes about 20 minutes and runs from
   the South Canoe Landing (near Huki) to the North Canoe Landing (near Hawaiʻi and Iosepa), or
   the other way. The rest of the day continues from wherever the guest lands: walking times,
   gaps, conflicts and suggestions all start from the far landing. The generator favors a ride
   that lands the guest near villages they haven't seen yet, and adding "Canoe ride" to
   "Don't let me miss" puts one in. On the map, walks are dotted and the ride is a solid blue
   line along the lagoon; its stop number shows at both landings. Landing positions are
   estimates from the gate handout.
6. **The map is the centerpiece.** It fills the width of the page and fills its frame: drag to
   pan, + and − to zoom (− all the way shows the whole map), a button to center on the day and
   one to make the map taller. Every place is a pin; stops in the day are numbered in order with
   the walking route drawn between them. Tapping a place opens a card on the map with what's on
   there that day, an "Add at …" button that finds the first time it fits around the day, and
   "Don't let me miss it". Tapping a stop opens its card with times, walk, reason, swap options
   and previous/next. A horizontal day strip under the map shows the day on a time line; drag a
   stop along it to retime it, or tap + in a gap. A step-by-step list follows below.
7. **Editing**: select a stop to see why it's there, move it to an earlier or later showtime, remove
   it, or swap it for something that fits the same gap. Tap a free gap to add something. Drag a stop
   to another time; it snaps to the nearest real showtime. Overlaps and too-short walks are flagged.
   Hand edits are kept when the guest changes their answers; "Start fresh" clears them.
8. **Return visits**: Islands of Polynesia tickets allow a free return to the villages within 3 days.
   The page says so and lists what the day leaves out; the saved day is stored as a list of days
   so a second day can be added later.

Event times are sample data in `EVENTS`, in the shape PCC's scheduling app is expected to supply.

## Updating the site after design changes

Edit on the "PCC Interactive Map — Version 2" design canvas, then export each changed page:

```bash
python3 tools/export-page.py <canvas page>.dc.html site/<Page>.dc.html site/assets
```

The script swaps the canvas image ids for the files in `site/assets/` and adds the local React
scripts. Commit and push; Vercel redeploys.

The rest of this README describes the Version 1 pages this copy started from.

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
