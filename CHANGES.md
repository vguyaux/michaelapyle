# CHANGES — deviations from the original michaelapyle.com

This static recreation aims to be a faithful copy of the live Webflow site, with a
short list of *approved* improvements. Every deviation is logged here. Content is
verbatim (see `CONTENT.md`); these notes cover structure, behavior, and the
approved enhancements.

## Approved improvements (intentional)

1. **Working contact form (mailto).** The original `<form>` used Webflow's
   `method="get"` pointing at no endpoint, so submissions went nowhere. Replaced
   with `action="mailto:info@michaelapyle.com" method="post" enctype="text/plain"`,
   which opens the visitor's mail client with the message pre-filled. No backend,
   no JavaScript, no tracking. Added a short helper note explaining this. Field
   labels are now associated (`<label for>`).

2. **Dropped the conversionflow.co attribution.** Original footer: "© 2025 All
   Rights Reserved By [Michael A. Pyle]" where the name linked to the web vendor
   `conversionflow.co`. Now: "© 2025 Michael A. Pyle. All rights reserved." (plain
   text, no outbound vendor link).

3. **Structured data (JSON-LD).** Added `Person` schema (Home, About, Contact) and
   `Book` schema (each book page) with real values only — title, author, language,
   tagline, description, Amazon buy action, and the real review/award where one
   exists. The original shipped no structured data.

4. **Per-page meta + Open Graph / Twitter.** Each page now has its own
   `<title>`, `description`, `canonical`, and OG/Twitter tags. The original reused
   one description across pages and had no `canonical`. OG image reuses the
   original's (`michael a pyle writer.png`).

5. **Accessibility.** Added a skip link; `aria-current="page"` on the active nav
   item; meaningful accessible names on every CTA (e.g. "Buy White Sugar, Brown
   Sugar on Amazon", "Contact Michael A. Pyle") instead of bare "Contact" or an
   unlabeled arrow; all decorative images use `alt=""`; the mobile menu button has
   `aria-expanded`/`aria-controls`; visible focus styles; `prefers-reduced-motion`
   respected.

## Structural / technical differences (not visible to a reader)

6. **Hand-written HTML/CSS instead of the Webflow export.** The original ships
   ~300 KB of generated Webflow CSS, jQuery, and three Webflow JS chunks. This
   recreation is a single ~15 KB hand-authored stylesheet, no jQuery, and ~20
   lines of vanilla JS for the mobile menu only. The look (dark hero, the
   purple→pink→orange brand gradient `#b16cea → #ff5e69 → #ff8a56 → #ffa84b`,
   Merriweather type, gradient section headings, pill CTAs) is reproduced from the
   original's palette and layout.

7. **Self-hosted assets.** All images and the essay PDF were downloaded from the
   Webflow CDN into `site/images/` and `site/assets/` so the site has no runtime
   dependency on `website-files.com`. Filenames were made human-readable.

8. **Fonts.** The original calls Webfont.js to load **Merriweather** only (classes
   referencing "Satoshi"/"Plus Jakarta Sans" fall back to system fonts because
   those families are never actually loaded). This recreation loads Merriweather
   from Google Fonts and uses it throughout — matching what the live site renders.

9. **Extensionless URLs → `.html`.** Links use `index.html`, `about.html`, etc., so
   the site works when opened directly from the filesystem and on any static host.

10. **Build step.** `site/build.py` + `site/content.py` generate the static HTML so
    the shared nav/footer/`<head>` stay identical across pages. The generator is a
    dev convenience; the committed `.html` files are the deliverable and are fully
    static.

## Minor visual approximations

11. **Brand mark.** The original's three-line logo SVGs are dark-on-dark / white-on-
    white in the export (effectively invisible without Webflow's runtime styling).
    Recreated as three skewed bars filled with the brand gradient (header) / solid
    dark (footer) so the mark is actually visible.

12. **"Who is E.G. Tripp?"** rendered as a gradient sub-heading (original used a
    small bold label). Same text, slightly more prominent.

13. **Hero rating stars / decorative dividers** reuse the original SVG/PNG assets;
    exact drop-shadow/blur amounts on the hero glow are approximated, not pixel-
    matched to Webflow's interaction styles.

## New content added (not on the original site)

- **News & Events page (`news.html`).** Added at the author's request — a
  dedicated page in the nav/footer listing upcoming appearances and recent press,
  grouped into "Upcoming" and "Recent News & Past Events." All entries are
  author-supplied facts (presentations at Madeline's Wine Bar and 35 Bistro, the
  Florida Vistas Book Club talk, the Miami Book Fair booth, the Kirkus May 2026
  feature/"Get It" verdict, the IndieReader Discovery Award first place, and new
  IndieReader reader reviews). Real outbound links only (Dropbox videos, Facebook
  photos, Kirkus, Issuu, IndieReader, Miami Book Fair). Dates are stated only where
  the author gave one — the 35 Bistro event shows no date because none was provided
  (not guessed). `Event` JSON-LD added for the two upcoming, dated appearances.
- **Pending asset:** the IndieReader endorsement badge image was referenced but not
  supplied; the IndieReader review news is shown as text/links until the badge file
  is provided, at which point it can be dropped into that card.

## Not carried over (intentionally omitted)

- Webflow's scroll/opacity entrance animations (`data-w-id` interactions). The
  content is shown immediately (better for performance and reduced-motion users).
- The Webflow badge, `__WEBFLOW_CURRENCY_SETTINGS`, and generator meta tags.
- Empty/placeholder social slots (Instagram/LinkedIn icons exist as unused assets
  on the CDN but are not linked anywhere on the live site, so they're not shown).
