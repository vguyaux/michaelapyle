# michaelapyle.com — static recreation

A faithful, dependency-free static recreation of
[www.michaelapyle.com](https://www.michaelapyle.com) — author site for Michael A.
Pyle (novels *White Sugar, Brown Sugar*, *Cuban Roots*, *Giga Trouble*).

Pure HTML + CSS, with ~20 lines of vanilla JS for the mobile menu. Mobile-first,
responsive, accessible, and fast (no jQuery, no framework, no runtime CDN
dependency — all assets are self-hosted).

## Run it

It's static — open `index.html` in a browser, or serve the folder:

```bash
cd site
python3 -m http.server 8080
# visit http://localhost:8080
```

## Layout

```
site/
  index.html  about.html  contact.html
  giga-trouble.html  cuban-roots.html  white-sugar-brown-sugar.html  404.html
  css/styles.css      # single hand-authored stylesheet
  js/nav.js           # mobile menu toggle (progressive enhancement)
  images/             # all artwork, self-hosted
  assets/             # essay PDF
  build.py            # generator (keeps shared chrome DRY)
  content.py          # verbatim page copy
  CONTENT.md          # source content inventory
  CHANGES.md          # every deviation from the original
```

## Editing

The committed `.html` files are the deliverable and are fully static. To change
shared chrome (nav/footer/head) or copy, edit `build.py` / `content.py` and
regenerate:

```bash
python3 build.py
```

All body copy is reproduced verbatim from the live site — see `CONTENT.md` and the
honesty rules in `../.agents/product-marketing.md`. Do not invent copy.

## Improvements over the original

Working `mailto:` contact form, JSON-LD (Person/Book), per-page meta + Open Graph,
accessibility (skip link, ARIA, focus styles, labelled CTAs), and the dropped
`conversionflow.co` footer attribution. Full list in `CHANGES.md`.
