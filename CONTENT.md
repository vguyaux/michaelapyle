# Content inventory — michaelapyle.com

Verbatim content captured from a crawl of the live site (Webflow publish dated
"Fri Mar 13 2026"). This is the source of truth for the static recreation in
`site/`. No copy in the build is invented; everything below comes from the live
pages. Reproduced here so the recreation can be re-verified without re-crawling.

## Pages (6 + 404)

| Page | URL | File | `<title>` |
|------|-----|------|-----------|
| Home | `/` | `index.html` | Michael A. Pyle |
| About | `/about` | `about.html` | About Michael A. Pyle |
| Contact | `/contact` | `contact.html` | Contact Michael A. Pyle |
| Giga Trouble | `/giga-trouble` | `giga-trouble.html` | Giga Trouble from Michael A. Pyle |
| Cuban Roots | `/cuban-roots` | `cuban-roots.html` | Cuban Roots from Michael A. Pyle |
| White Sugar, Brown Sugar | `/white-sugar-brown-sugar` | `white-sugar-brown-sugar.html` | White Sugar, Brown Sugar from Michael A. Pyle |
| 404 | (Webflow 404) | `404.html` | Page Not Found — Michael A. Pyle |

Site-wide meta description (used on Home/About/book pages on the original):
*"Michael A. Pyle draws on fiction writing, linguistics, law and international
travel to weave multi-cultural, suspense and inspirational narratives."*

## Global chrome

- **Nav:** Home · About · Books ▾ (Giga Trouble 03 / Cuban Roots 02 / White Sugar,
  Brown Sugar 01) · Contact. Brand: "Michael A. Pyle" with a three-bar mark.
- **Footer blurb:** "Unflinching, lyrical storyteller who turns hard histories into
  intimate, redemptive journeys. With precise, lean prose and a deep ear for voice,
  he renders ordinary lives with uncommon grace."
- **Footer columns:** Menu (Home/About/Contact) · Books (the three titles).
- **Social:** Facebook (`facebook.com`) — the only social link on the original.
- **Copyright (original):** "© 2025 All Rights Reserved By Michael A. Pyle" — the
  author's name was hyperlinked to `conversionflow.co` (the web vendor). Dropped in
  this recreation (see ../CHANGES.md).

## Books — taglines, one-liners, buy links

| # | Title | Tagline | Amazon |
|---|-------|---------|--------|
| 01 | White Sugar, Brown Sugar | Crossing Daytona Beach's Color Line | https://a.co/d/07McNu4 |
| 02 | Cuban Roots | After Castro: A Cuban Reckoning | https://a.co/d/e1pcPQa |
| 03 | Giga Trouble | Currents, Code, and Conspiracy | https://a.co/d/eagN1r6 |

## Endorsements / awards (real, attributed — no others exist)

- **Kirkus Reviews** — full reviews on Giga Trouble and White Sugar, Brown Sugar.
- **John Williamson** — "A book about the triumph of the human spirit" (WSBS);
  "Sometimes a debut novel really surprises the reader with its scope and depth.."
- **Louis Roppolo** — "Pyle has a gifted way of making it all come to life from
  every page he writes." (Cuban Roots / About)
- **American Legacy Book Finalist**, Inspirational Fiction Category — WSBS.
- **#2, 2013 Reader's Choice Award** — WSBS (shown with WSJ logo on the original).

## Contact

- Email: `info@michaelapyle.com`
- Original form fields: Full Name, Email Address, Message — Webflow `method="get"`
  to no endpoint (non-functional). Submit label "Send now".

## Long-form author text

The first-person "Why have you written this book?" essays (Giga Trouble, Cuban
Roots, White Sugar, Brown Sugar), the About biography, and the "Who is E.G. Tripp?"
note are reproduced verbatim in `content.py`. They are long and idiosyncratic by
design — do not edit them.

## Assets

All images/PDF were downloaded from the Webflow CDN
(`cdn.prod.website-files.com/68e15b12b1c0636b748f7679/...`) into `site/images/`
and `site/assets/` with human-readable filenames. Font: **Merriweather** (the only
family the original actually loads), served from Google Fonts.
