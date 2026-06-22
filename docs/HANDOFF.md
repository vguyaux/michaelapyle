# Handoff prompt — michaelapyle.com static rebuild

> Paste the block below into the **new** Claude Code on the web session
> (started on branch `claude/funny-franklin-g4dft2`). It is self-contained.

---

## TASK
Recreate the website **https://www.michaelapyle.com** as a **static site in pure
HTML + CSS** (vanilla JS only if strictly necessary, e.g. mobile nav). It must be
a **faithful, honest** recreation of the real site — no invented copy, no fake
testimonials, no embellished claims. Mobile-first, responsive, accessible, fast.

Build into THIS repo on branch **`claude/funny-franklin-g4dft2`**. Commit and
push. **Do NOT open a pull request.**

## WHO / CONTEXT
- Subject: **Michael A. Pyle** — retired Daytona Beach estate-planning attorney
  (practiced 40 yrs, retired 2023) turned novelist; former ESL professor who
  wrote TOEFL prep books. This is his **personal author site**, NOT his law firm
  (pylelegal.com). Imprint: **Armstrong Media Group, LLC**.
- Books: **White Sugar, Brown Sugar** (2012), **Cuban Roots** (2018),
  **Giga Trouble** (2025).
- Platform of the original: **Webflow**. Web font: **Merriweather** (serif).

## WHAT'S ALREADY DONE (don't redo)
1. The 45 marketing skills from coreyhaines31/marketingskills are installed at
   `.claude/skills/` on this branch. **Use them.**
2. **Step 1 (crawl + findings) is COMPLETE.** A full verbatim "as-is" content
   inventory of all 6 live pages is committed at **`docs/as-is-findings.md`**
   (commit 6c15679). READ IT FIRST — it has the sitemap, all verbatim copy
   (incl. the long first-person "Why have you written this book?" essays, full
   Kirkus reviews, the "Who is E.G. Tripp?" note, About bio), every asset URL,
   the font, CTAs, and the flags list. The user already reviewed and approved it.
3. The user APPROVED these decisions (apply them):
   - **Light improvements: YES, all of them** — but log every copy/CTA wording
     change in a CHANGES note for review. Improvements = mailto-based contact
     form, Person + Book JSON-LD schema, per-page titles/meta/canonical/OG/
     Twitter tags, drop the `conversionflow.co` builder attribution, descriptive
     accessible CTA labels ("Buy Giga Trouble on Amazon").
   - **Assets: match the real site exactly** — download the real CSS (for the
     exact color palette) + all real images from the CDN once it's reachable.
   - **Contact form**: static can't submit → real accessible form with a
     `mailto:info@michaelapyle.com` fallback + a code comment marking where a
     Formspree/Netlify Forms handler endpoint plugs in.
   - **No newsletter** exists on the live site — do NOT add one.
   - **Facebook link** is just `https://www.facebook.com` (generic) — keep
     as-is and flag; user has not provided a real profile URL.

## THE BLOCKER THAT WAS JUST RESOLVED
- The Webflow asset/CSS CDN host **`cdn.prod.website-files.com`** was blocked by
  the environment egress proxy ("Host not in allowlist"). The user has now
  **added it to the network egress allow-list**, and this fresh session should
  pick it up. (`fonts.googleapis.com` + `fonts.gstatic.com` are also allowed.)
- **FIRST ACTION: verify the CDN is reachable**, e.g.:
  `curl -sS -o /tmp/mp.css -w "%{http_code}\n" "https://cdn.prod.website-files.com/68e15b12b1c0636b748f7679/css/michael-a-pyle.webflow.shared.578b7770b.css"`
  Expect HTTP 200. If it's still 403 with body "Host not in allowlist", tell the
  user it didn't propagate and pause. If 200, proceed.

## WHAT TO DO NEXT (Step 2 — build)
1. Re-confirm branch is `claude/funny-franklin-g4dft2`. Read `docs/as-is-findings.md`.
2. Verify CDN access (above). Then **download all real assets** into the repo
   (e.g. `assets/img/`, `assets/css-ref/`): the logo SVGs, author photo
   (`…_Michael A Pyle.png`), the 3 book covers (Giga Trouble .png, Cuban Roots
   .avif, White Sugar .avif), badges (American Legacy, "available at amazon",
   star rating), Kirkus/WSJ logos, Facebook icon, OG image
   (`…_michael a pyle writer.png`). All URLs are listed in the findings doc.
   Also download the real stylesheet `michael-a-pyle.webflow.shared.*.css` to
   **extract the exact color palette and type scale** (reference only — write
   your own clean CSS, don't ship Webflow's bloat).
3. Write `.agents/product-marketing.md` FIRST (use the product-marketing skill),
   then apply: site-architecture, copywriting, copy-editing, cro, seo-audit +
   schema (Book/Person JSON-LD). Keep all copy faithful/verbatim.
4. Scaffold the static site (NO framework, NO build step): one HTML file per page
   — `index.html`, `about.html`, `giga-trouble.html`, `cuban-roots.html`,
   `white-sugar-brown-sugar.html`, `contact.html`, plus `404.html`; shared
   `assets/css/styles.css`; minimal vanilla JS only for mobile nav if needed.
   Add `robots.txt`, `sitemap.xml`, favicon.
5. Build pages **one at a time**, faithful to the original structure:
   - Sitewide nav: Home, About, Giga Trouble, Cuban Roots, White Sugar Brown
     Sugar, Contact. Footer: Menu (Home/About/Contact) + books (newest→oldest
     03/02/01) + Facebook + `© 2025 All Rights Reserved By Michael A. Pyle`
     (drop conversionflow.co attribution).
   - Home: H1 "A Passion for Writing Fiction", subhead, American Legacy badge,
     featured Giga Trouble, prior-books cards, footer bio. Amazon CTAs.
   - Book pages: title/subtitle/tagline, full Synopsis, "Why have you written
     this book?" essay, Review block, Amazon buy button. (White Sugar also:
     Recognition + "Who is E.G. Tripp?". Cuban Roots also: Context quote.)
   - About: Biography + the Roppolo quote.
   - Contact: heading + bio + mailto form (see decision above).
   Amazon links: Giga `https://a.co/d/eagN1r6`, Cuban `https://a.co/d/e1pcPQa`,
   White Sugar `https://a.co/d/07McNu4`. Email `info@michaelapyle.com`.
6. Polish: responsive (mobile-first), a11y (semantic landmarks, alt text, focus
   states, color contrast), SEO (per-page meta/canonical/OG/Twitter), JSON-LD.
7. **Verify locally with screenshots vs. the original** before finalizing.
8. Write a short **CHANGES.md** listing every deviation from the original
   (wording tweaks, added schema/meta, dropped attribution, form handling) so
   the user can approve.
9. Commit in logical chunks and push to `claude/funny-franklin-g4dft2`. NO PR.

## GIT
- Develop on `claude/funny-franklin-g4dft2` (skills + findings live here).
- `git push -u origin claude/funny-franklin-g4dft2`; retry on network errors
  with backoff (2s/4s/8s/16s). Do NOT push to other branches. Do NOT open a PR.

## IF CDN STILL BLOCKED
Tell the user the exact host (`cdn.prod.website-files.com`) still isn't
reachable and pause — OR, only if the user says so, fall back to neutral
placeholder images + a Merriweather-based literary palette and build anyway.
