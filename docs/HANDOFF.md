# Michael A. Pyle — Project Handoff (for the next agent)

You are picking up an ongoing project: the personal author website of **Michael A. Pyle**
plus a set of marketing pieces (Facebook cover, table poster, letter-size flyer).
Read this whole file first. It is the source of truth for where things live, how the
site is built, what has been done, and the conventions to follow.

---

## 1. Who / what this is

- **Michael A. Pyle** — retired Daytona Beach, FL estate-planning attorney (practiced 40
  years, retired 2023), former ESL professor (wrote Cliffs TOEFL prep books), now a
  novelist. This is his **personal author site**, NOT his old law firm (pylelegal.com).
- Imprint / publisher: **Armstrong Media Group, LLC**.
- Books: **White Sugar, Brown Sugar** (2012, reprinted 2025), **Cuban Roots** (2018),
  **Giga Trouble** (2025).
- Contact email: **info@michaelapyle.com**. Facebook link on the site is a generic
  `https://www.facebook.com` (no real profile URL provided).

## 2. Where everything lives

| Thing | Location |
|---|---|
| GitHub repo | **https://github.com/vguyaux/michaelapyle** (scope: `vguyaux/michaelapyle`) |
| Live website | **https://michaelapyle.com** (also `https://vguyaux.github.io/michaelapyle`) |
| Hosting | **GitHub Pages**, served from branch **`main`** (see `CNAME` = michaelapyle.com, `.nojekyll` present) |
| User's local clone (their Mac) | `~/Documents/github/michaelapyle` |
| This sandbox clone | `/home/user/michaelapyle` |
| Original site being recreated | The site was rebuilt from the old Webflow site at michaelapyle.com; crawl notes in `docs/as-is-findings.md` |

- **The live site is on `main`.** Changes must land on `main` to go live (GitHub Pages
  rebuilds automatically, ~1–2 min). Verify with `curl -sS https://michaelapyle.com/<page>.html`.
- The user also edits/pushes from their Mac, so **always `git fetch origin main` and rebase
  before committing** to avoid divergence.

## 3. The website — build system (IMPORTANT)

**The HTML files are GENERATED. Do not hand-edit the `.html` files as the source.**

- **Source of truth: `content.py`** — contains all page bodies and copy.
- **`build.py`** — run `python3 build.py` from the repo root to regenerate every `.html`
  (it injects the shared nav/head/footer and writes the files next to it). Always rebuild
  after editing `content.py`, and commit both `content.py` and the regenerated `.html`.
- `CONTENT.md` — inventory of where copy came from (all copy is faithful to the live site;
  nothing invented).
- `CHANGES.md` — log of intentional deviations from the original (keep updating it).
- Build is deterministic: after `python3 build.py`, `git diff` should show only your
  intended change plus its regenerated page(s). If it shows unrelated churn, investigate.

### Pages
`index.html` (home), `about.html`, `giga-trouble.html`, `cuban-roots.html`,
`white-sugar-brown-sugar.html`, `white-sugar-brown-sugar-reviews.html`, `contact.html`,
`news.html` (News & Events), `404.html`.

### Design system (`css/styles.css`)
- Font: **Merriweather** (serif) via Google Fonts.
- Brand gradient (purple→pink→orange→amber): `#b16cea → #ff5e69 → #ff8a56 → #ffa84b`.
- Dark `#0d0e10`, paper `#f8f4f0`, ink `#0d0e10`, muted `#555a61`.
- `js/nav.js` = mobile nav toggle. `js/htmx.min.js` + `js/idiomorph-ext.min.js` present.
- Contact form is static → uses a `mailto:` fallback (no server). A Formspree/Netlify
  handler could be wired in later.
- SEO: per-page title/meta/canonical/OG/Twitter; Person + Book JSON-LD on relevant pages.

### Amazon buy links
Giga Trouble `https://a.co/d/eagN1r6` · Cuban Roots `https://a.co/d/e1pcPQa` ·
White Sugar, Brown Sugar `https://a.co/d/07McNu4`.

## 4. Awards / accolades reference (all for *White Sugar, Brown Sugar*)

Newest first (this is the order used on the News page and the print pieces):
- **Silver — Fiction Category, 2026 Living Now Book Awards (Evergreen Categories)** —
  medalists named **August 7, 2026**. Seal: `images/living-now-finalist.webp` (green
  "Finalist" seal; the site shows it **grayscale** on home + book page to avoid adding a
  new color, and **green** on the News page). Note: the official seal reads "Finalist," so
  the heading says "Silver Medal & Finalist" to reconcile.
- **Kirkus Reviews** feature — **May 1, 2026** (Volume XCIV, No. 9), "Get It" verdict.
  Logo: `images/kirkus-reviews.webp`.
- **First Place — 2026 IndieReader Discovery Awards (Inspirational Fiction)** — **May 2026**.
  Seal: `images/irda-winner-badge.webp` (gold WINNER seal).
- **American Legacy Book Finalist (Inspirational Fiction)** — **2024**.
  Seal: `images/american-legacy-bw.png`; certificate: `images/american-legacy.jpeg`.
- **#2 in Best Books of the Year — 2013 Reader's Choice Award** (featured in *The Wall
  Street Journal*). Logo: `images/wsj-logo.png`.

Photos in repo: `images/IMG_0808.JPG` (Michael holding the book), `images/35-bistro-giga-trouble.jpg`
(35 Bistro event), `images/white-sugar-cover.avif`, `images/michael-pyle-hero.png`.

## 5. What has been done so far (summary)

- Recreated the site from the old Webflow site (faithful copy) — earlier work already on `main`.
- **News page**: added the Living Now Silver card (with green seal), gave it the Aug 7, 2026
  date, sorted "Recent News & Past Events" newest-first, and it already had the IRDA card,
  Kirkus card, and the two Giga Trouble presentation cards (incl. the 35 Bistro photo).
- **Book page** (`white-sugar-brown-sugar.html`): added Living Now Silver to the Recognition
  panel (grayscale seal).
- **Home hero**: added the Living Now award badge before the American Legacy badge (two
  stacked award badges sharing one divider); grayscaled the Living Now seal; dropped the
  date so it matches the American Legacy badge.
- Latest `main` commits (tip `84d2fd0`): see `git log origin/main`.

### Marketing collateral (NOT in the git repo — one-off deliverables)
These were generated in the sandbox's `/tmp` and delivered to the user as files. **`/tmp`
is wiped when the sandbox recycles, so these working files will NOT be here for you — you
must regenerate them if changes are needed.** (Recommendation: consider committing the
generators + a copy of the assets into the repo, e.g. a `print/` folder, so they're
reproducible. Not yet done.)

- **Facebook cover** — `/tmp/fbcover/` (gen scripts `gen.py`, `gen3.py`, `gen4.py`).
  Final = `fb-cover-720.png`, **1640×720**. Design: dark gradient background, two award
  medals stacked on the LEFT (IRDA gold + Living Now grayscaled to read as silver, equal
  158px), author name + two award lines center, Michael's photo (from `IMG_0808.JPG`) in a
  gradient frame on the right, `michaelapyle.com` gradient pill. Built to the FB **safe
  zone**: 1640×720 covers desktop (820×312) and mobile (640×360); all content inside the
  central 1280×624; bottom-left kept clear for the profile picture; background bleeds to all
  edges.
- **Poster (9×15 in) + Letter (8.5×11 in)** — `/tmp/poster/gen_poster.py` generates
  `poster.html` and `letter.html` from ONE template + a `CONFIG` dict (per-format
  `ROOT`/`COVER`/`SEAL`/`PAD`/`AWPAD`). Rendered to PDF with headless Chromium
  `--print-to-pdf`. Final PDFs: `Michael-A-Pyle-Poster-9x15.pdf`,
  `Michael-A-Pyle-Awards-Letter-8.5x11.pdf`. Layout: dark banner (brand mark + name +
  "Award-Winning Fiction"), full-width gradient rule, **book cover LEFT + intro-about-Michael
  RIGHT** (title, subtitle "Crossing Daytona Beach's Color Line," intro paragraph, byline),
  then "The 2024 Printing" (Living Now, Kirkus, IndieReader, American Legacy) and "The 2012
  Printing" (WSJ #2) as award rows with generous padding, full-width gradient section
  dividers, and a footer (`michaelapyle.com` + Armstrong Media Group) with a full-width
  gradient line above it. Order is newest-on-top per the user's request.

## 6. Rendering pipeline + hard-won gotchas (for print/image generation)

- Headless Chromium: `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`.
  Flags: `--headless=new --no-sandbox --allow-file-access-from-files --hide-scrollbars`.
  - Screenshot: `--screenshot=out.png --window-size=W,H --force-device-scale-factor=2 --virtual-time-budget=4000`.
  - PDF: `--print-to-pdf=out.pdf` with `@page { size: W H; margin:0; }` in the CSS.
- **Fonts must be embedded**: Chromium may not fetch web fonts at render time. `mw-embed.css`
  is Merriweather with the woff2 files base64-inlined into `@font-face` (fetched from Google
  Fonts CSS2 with a desktop Chrome User-Agent, then base64-embedded). Reuse it.
- **Chromium print/screenshot quirks that wasted time — avoid these:**
  - A gradient-**background** "pill" and flex `margin-top:auto` / `justify-content:space-between`
    footers render UNRELIABLY (boxes collapse to a thin line or clip at the page edge).
    Use **block flow**, gradient-**clip text** or **solid color** for the footer, and put a
    full-width gradient `<div>` line (background gradient) where you want a rule.
  - The **2× render is ~30px taller** than a 1× auto-height measurement, so leave **~40–60px
    of slack** below the last element or the footer clips. Measure natural height by
    rendering with `height:auto; overflow:visible` at scale 1 and finding the content bbox
    (PIL `ImageChops.difference` vs the paper color), then size to fit.
  - `.avif` renders fine in Chromium.
- Pasted-in-chat images and files at `/Users/...` (the user's Mac) are **not** on the
  sandbox disk. To use such a file you must either have the user push it to the repo, or —
  if it's in their Google Drive — pull it via the **Google Drive MCP** (that's how the 35
  Bistro badge was fetched). `SendUserFile` delivers generated files to the user.

## 7. Environment / egress

- Outbound egress is allowlisted per host. Currently allowed: `michaelapyle.com`,
  `www.michaelapyle.com`, `cdn.prod.website-files.com` (old Webflow asset CDN),
  `fonts.googleapis.com`, `fonts.gstatic.com`. `livingnowawards.com` is **blocked**
  (used WebSearch instead). If you hit a blocked host, tell the user the exact hostname to
  add and pause.
- The sandbox recycles between/within sessions: `/tmp` is wiped and pip packages (Pillow)
  may need reinstalling (`pip install --quiet Pillow`). The repo working tree persists on
  the branch, but uncommitted local work can be lost — commit/push often.
- Pushing from the sandbox to `main` has generally worked via `git push origin HEAD:main`,
  but was intermittently blocked (HTTP 403 at the git proxy) earlier in the project. If a
  push 403s, it usually clears on retry or after the environment refreshes; the user can
  also apply/push from their Mac. Reads (fetch) always work.

## 8. Conventions

- **Git**: the live site is `main`. Follow this session's designated-branch rules; when the
  goal is to ship to the live site, commit and `git push origin HEAD:main` (fetch/rebase
  first). Keep `content.py` as the source and rebuild with `build.py`.
- **All copy stays faithful** to the real site / the user's provided text (no invented
  reviews, awards, or claims). Light copy/CRO/SEO polish is OK but log deviations in
  `CHANGES.md` and flag anything non-obvious to the user.
- **Commit message trailers** (end every commit with):
  ```
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01LaMN4whUQnSWAxATwFMTBK
  ```
- **PR descriptions** end with: `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
  Do not open a PR unless asked.

## 9. Open / optional follow-ups the user may want

- Add the **IndieReader First Place** award to the book page's Recognition panel (currently
  only on the News page).
- Add the new wins to the book's **Book JSON-LD `award`** field (SEO; currently lists only
  American Legacy).
- Print pieces: option to swap award seals to grayscale for a uniform look, add the American
  Legacy **certificate** image, tweak the intro paragraph, or output the poster at a
  different size (e.g., 12×18, 11×17) — regenerate via `/tmp/poster/gen_poster.py` `CONFIG`.
- Consider committing the marketing generators + assets into the repo (e.g. `print/`) so
  they survive and are reproducible.
- The Living Now results Google Doc (shared with the user, owner allisonroberts906@gmail.com)
  is the source for the Living Now win; the doc is a Google Docs *edit* link on the News card.
