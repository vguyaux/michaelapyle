# michaelapyle.com — "As-Is" Findings (crawl date: 2026-06-22)

Source: live crawl of `https://www.michaelapyle.com` (6 pages). Platform: **Webflow**.
All copy below is captured **verbatim** from the live site. Nothing invented.

---

## 1. Site map / navigation

Primary nav (same on every page):

| Label | URL |
|---|---|
| Home | `/` |
| About | `/about` |
| Giga Trouble | `/giga-trouble` |
| Cuban Roots | `/cuban-roots` |
| White Sugar, Brown Sugar | `/white-sugar-brown-sugar` |
| Contact | `/contact` |

Nav also exposes a **"Books"** grouping that lists the three titles numbered `03/ Giga Trouble`, `02/ Cuban Roots`, `01/ White Sugar, Brown Sugar` (i.e. newest → oldest).

Footer (every page) has two columns + social:
- **Menu:** Home, About, Contact
- **books:** Giga Trouble, Cuban Roots, White Sugar, Brown Sugar
- **Social:** Facebook → `https://www.facebook.com` *(generic FB homepage, not a real profile — see flags)*
- Copyright: `© 2025 All Rights Reserved By Michael A. Pyle`
- Original site has a builder attribution link to `conversionflow.co` (will be dropped).

**7 pages total to build:** Home, About, Giga Trouble, Cuban Roots, White Sugar Brown Sugar, Contact, + 404.

---

## 2. Page-by-page content

### HOME (`/`)
- `<title>`: **Michael A. Pyle**
- Meta description: *"Michael A. Pyle draws on fiction writing, linguistics, law and international travel to weave multi-cultural, suspense and inspirational narratives."*
- H1: **A Passion for Writing Fiction**
- Sub: *"Michael A. Pyle draws on fiction writing, linguistics, law and international travel to weave multi-cultural, suspense and inspirational narratives."*
- Badge: **INSPIRATIONAL FICTION CATEGORY — American Legacy Book Finalist** "For *White Sugar, Brown Sugar*"
- Quote: *"A book about the triumph of the human spirit"* — John Williamson
- Featured new book **Giga Trouble** — "Currents, Code, and Conspiracy"; Kirkus pull-quote *"A swift, outlandish adventure both on and off the water that keeps the reader guessing."*; tagline *"At COVID's dawn, a security analyst dives overboard and leads a covert mission to dismantle a yacht-borne cyber conspiracy."*
- Prior books cards: **Cuban Roots** ("After Castro: A Cuban Reckoning"; *"A novel grounded in decades of research and vetted by Havana's Institute of Cuban History"*; quote — Louis Roppolo) and **White Sugar, Brown Sugar** ("Crossing Daytona Beach's Color Line"; *"In the 60s, two boys cross the tracks, battle addiction, and rebuild their lives."*; quote — John Williamson)
- Footer bio: *"Unflinching, lyrical storyteller who turns hard histories into intimate, redemptive journeys. With precise, lean prose and a deep ear for voice, he renders ordinary lives with uncommon grace."*
- CTAs: Contact (primary), per-book "read more" links, "available at amazon" badges.

### ABOUT (`/about`)
- Headings: **About Michael A. Pyle** / **Biography** / **First Essay**
- Biography (verbatim): *"Michael A. Pyle was born in 1953 in Daytona Beach, Florida. He earned a bachelor's degree in English from the University of Florida, with a minor in creative writing. He obtained a master's degree in Linguistics, was an associate professor of English as a Second Language, and later graduated from with a Juris Doctor degree from the School of Law, all at the same university. He wrote Cliffs TOEFL Preparation Guide and two similar textbooks for foreign students, published by Cliffs Notes and its successors. In 2012, he published his historical fiction novel White Sugar, Brown Sugar… In 2018, he published Cuban Roots… In 2025, he launched his third book, Giga Trouble. Both novels were published through his small publishing company, Armstrong Media Group, LLC. After practicing law for 40 years and retiring in 2023, Pyle has turned to writing general fiction. His recent works feature characters from his previous books."*
- "First Essay" section currently only holds the Louis Roppolo quote (no essay body on the live site).

### GIGA TROUBLE (`/giga-trouble`) — Book #3
- "Michael A. Pyle's third book" · **Giga Trouble** · "Currents, Code, and Conspiracy"
- Full **Synopsis** (7 paras, captured verbatim).
- **"We asked Michael A. Pyle: Why have you written this book?"** — long first-person essay (cybercrime/COVID origin story, ~9 paras, captured verbatim).
- **Review** — Kirkus (long multi-paragraph review, captured verbatim) — *"A swift, outlandish adventure…"* … *"there are several compelling twists in store before the final page."* — Kirkus Review
- Buy: **Amazon** → `https://a.co/d/eagN1r6`

### CUBAN ROOTS (`/cuban-roots`) — Book #2
- "Michael A. Pyle's second book" · **Cuban Roots** · "After Castro: A Cuban Reckoning" · *"A novel grounded in decades of research and vetted by Havana's Institute of Cuban History"*
- **Synopsis** (verbatim, incl. Institute of Cuban History credibility note + two symposium invitations).
- **Review:** *"Pyle has a gifted way of making it all come to life from every page he writes."* — Louis Roppolo
- **Context** quote (verbatim, — Michael A. Pyle).
- **"Why have you written this book?"** — very long first-person essay on Cuba research, Peter Pan flights, travel, immigration encounters, Batista/Daytona history (captured verbatim).
- Buy: **Amazon** → `https://a.co/d/e1pcPQa`

### WHITE SUGAR, BROWN SUGAR (`/white-sugar-brown-sugar`) — Book #1
- "Michael A. Pyle's first book" · "Crossing Daytona Beach's Color Line" · *"In the 60s, two boys cross the tracks, battle addiction, and rebuild their lives."*
- **Synopsis** (verbatim).
- **Recognition:** INSPIRATIONAL FICTION CATEGORY — American Legacy Book Finalist; **#2 — 2013 Reader's Choice Award**.
- Quote: *"Sometimes a debut novel really surprises the reader with its scope and depth."* — John Williamson
- **"Why have you written this book?"** — first-person essay (typewriter at 18, Sterling Watson, self-pub 2012 at age 59; captured verbatim).
- **Review** — Kirkus (long, verbatim): *"Pyle's narrative has the powerful ring of truth"* … *"A bracing tale that will shake the reader."* — Kirkus Review
- **"Who is E.G. Tripp?"** — pen-name explanation (verbatim).
- Buy: **Amazon** → `https://a.co/d/07McNu4`

### CONTACT (`/contact`)
- Heading: **Contact Michael A. Pyle**
- Body: the footer-bio sentence ("Unflinching, lyrical storyteller…").
- **Contact form** (Webflow): fields Name, Email, Message + submit; success msg "Thank you! We will get back to you shortly!"; error msg "Oops! Something went wrong while sending your message."
- Email visible: **info@michaelapyle.com**

---

## 3. Visual design (fonts / colors / assets)

- **Web font loaded:** **Merriweather** (300/400/700/900 + italics) via Google Fonts WebFont loader. ("Inter" also referenced as a secondary/UI font.) → classic literary serif look.
- Layout: hero + stacked sections, book "cards", numbered books list (`01/ 02/ 03/`), right-arrow link affordances, badge images (American Legacy, "available at amazon", star rating), Kirkus / WSJ logos as review credibility marks.
- **Colors: UNKNOWN.** The entire stylesheet (`…/css/michael-a-pyle.webflow.shared.578b7770b.css`) is hosted on `cdn.prod.website-files.com`, which is **blocked** (403 / "Host not in allowlist"). No inline colors exist in the HTML, so I can't read the exact palette yet. → **see flags.**

### Assets (all on the blocked CDN `cdn.prod.website-files.com`)
- Logo SVGs (`…_1.svg`, `_2.svg`, `_3.svg`)
- Author photo `…_Michael A Pyle.png`
- Book covers: Giga Trouble `…_Giga Trouble.png`, Cuban Roots `…_KDP Cuban Roots…avif`, White Sugar `…_WhiteSugarBrownSugar_frontcover…avif`
- Badges: American Legacy (`…_american leagcy_bw.png`), "available at amazon" (`…_available at amazon.png`), star rating SVG, Kirkus logo (`.webp`), Facebook icon SVG, footer vector SVGs
- OG image: `…_michael a pyle writer.png`

---

## 4. External / outbound links
- Amazon (per book): `a.co/d/eagN1r6` (Giga), `a.co/d/e1pcPQa` (Cuban), `a.co/d/07McNu4` (White Sugar)
- Facebook: `https://www.facebook.com` (generic)
- Email: `info@michaelapyle.com`

---

## 5. ⚠️ Flags / blockers / proposed changes (need your OK)

**BLOCKER — allowlist needed:**
- `cdn.prod.website-files.com` — hosts **the CSS (for exact colors), all images (logos, author photo, 3 book covers, badges, Kirkus/WSJ logos, OG image), and font files.** Currently 403 via both curl and WebFetch. **I cannot match the exact palette or pull the real cover images / author photo without this.** Please add it.
- `fonts.googleapis.com` + `fonts.gstatic.com` — for Merriweather. (The final site can load these via `<link>` at view time regardless, but I'd want them allowlisted to verify screenshots locally.)

**Proposed faithful-but-improved changes (light, flag-for-approval):**
1. **Contact form** → static HTML can't process submissions. Plan: a real, accessible form whose action points to a placeholder + a `mailto:info@michaelapyle.com` fallback link, with a clear code comment marking where a **Formspree/Netlify Forms** handler endpoint goes. (Matches your stated preference.)
2. **SEO/Schema (additions, no copy change):** add `Person` JSON-LD (Michael A. Pyle) on About/Home and `Book` JSON-LD on each book page (title, author, award, review). Keep existing title/meta; add per-page titles + canonical + OG/Twitter tags (home OG already exists).
3. **Facebook link** is just `facebook.com`. Keep as-is, or remove until you give a real profile URL? (Recommend: keep but flag.)
4. **Builder attribution** (`conversionflow.co`) in footer → drop.
5. **CTAs/CRO (wording tweaks only where it helps conversion, no invented claims):** e.g. Amazon badges get descriptive accessible labels like "Buy Giga Trouble on Amazon"; primary "Contact" CTA kept. Will list every wording change in a CHANGES note for your approval before finalizing.
6. **Newsletter:** the live site has **no** newsletter signup — I will NOT add one unless you ask.

**Image strategy if CDN stays blocked:** I can (a) wait for allowlist and download originals, or (b) build with same layout using neutral placeholders + alt text and you drop real images in later. Recommend (a).
