#!/usr/bin/env python3
"""Static-site generator for the Michael A. Pyle recreation.

Run:  python3 site/build.py
Emits the static .html files into site/. The shipped artifact is plain
HTML/CSS/JS — this script only exists to keep the shared nav/footer/head
identical across pages (DRY) and to make future edits safe.

All body copy is reproduced verbatim from the live-site crawl. No invented
copy. See site/CONTENT.md for the source inventory and .agents/product-marketing.md
for the honesty rules.
"""
from pathlib import Path

SITE = Path(__file__).resolve().parent
BASE_URL = "https://www.michaelapyle.com"

NAV_LINKS = [
    ("/", "index.html", "Home"),
    ("/about", "about.html", "About"),
    ("/contact", "contact.html", "Contact"),
]
BOOKS = [
    ("03", "giga-trouble.html", "Giga Trouble"),
    ("02", "cuban-roots.html", "Cuban Roots"),
    ("01", "white-sugar-brown-sugar.html", "White Sugar, Brown Sugar"),
]


def brand(in_footer=False):
    cls = "brand"
    return f'''<a class="{cls}" href="index.html" aria-label="Michael A. Pyle — home">
        <span class="brand__mark" aria-hidden="true"><span></span><span></span><span></span></span>
        <span class="brand__name">Michael A. Pyle</span>
      </a>'''


def nav(active):
    def link(href, label):
        cur = ' aria-current="page"' if active == href else ""
        return f'<a class="nav__link" href="{href}"{cur}>{label}</a>'

    books_current = active in {b[1] for b in BOOKS}
    cur = ' aria-current="page"'
    books_sub = "".join(
        f'<a href="{href}"{cur if active == href else ""}>'
        f'<span class="num">{num}/</span><span>{title}</span></a>'
        for num, href, title in BOOKS
    )
    books_cur_attr = ' aria-current="page"' if books_current else ""
    return f'''<header class="nav" data-nav data-open="false">
    <div class="container nav__inner">
      {brand()}
      <button class="nav__toggle" type="button" aria-label="Menu" aria-expanded="false" aria-controls="nav-menu">
        <span></span><span></span><span></span>
      </button>
      <nav id="nav-menu" class="nav__menu" aria-label="Primary">
        {link("index.html", "Home")}
        {link("about.html", "About")}
        <div class="nav__books">
          <span class="nav__link nav__group-toggle"{books_cur_attr}>Books</span>
          <div class="nav__sub">{books_sub}</div>
        </div>
        {link("news.html", "News")}
        {link("contact.html", "Contact")}
      </nav>
    </div>
  </header>'''


FOOTER = f'''<footer class="footer">
    <div class="container">
      <div class="footer__top">
        <div>
          {brand(in_footer=True)}
          <p class="footer__blurb">Unflinching, lyrical storyteller who turns hard histories into intimate, redemptive journeys. With precise, lean prose and a deep ear for voice, he renders ordinary lives with uncommon grace.</p>
          <div class="social">
            <a href="https://www.facebook.com" target="_blank" rel="noopener" aria-label="Facebook">
              <img src="images/fb.svg" alt="" width="18" height="18">
            </a>
          </div>
        </div>
        <div class="footer__col">
          <h3>Menu</h3>
          <a href="index.html">Home</a>
          <a href="about.html">About</a>
          <a href="news.html">News &amp; Events</a>
          <a href="contact.html">Contact</a>
        </div>
        <div class="footer__col">
          <h3>Books</h3>
          <a href="giga-trouble.html">Giga Trouble</a>
          <a href="cuban-roots.html">Cuban Roots</a>
          <a href="white-sugar-brown-sugar.html">White Sugar, Brown Sugar</a>
        </div>
      </div>
      <div class="footer__bottom">© 2025 Michael A. Pyle. All rights reserved.</div>
    </div>
  </footer>'''


def page(slug_file, title, description, body, jsonld="", canonical_path="/"):
    canonical = BASE_URL + canonical_path
    og_image = BASE_URL + "/images/og-michael-pyle.png"
    jsonld_block = (
        f'\n  <script type="application/ld+json">\n{jsonld}\n  </script>' if jsonld else ""
    )
    active = slug_file
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Michael A. Pyle">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og_image}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{og_image}">
  <link rel="icon" type="image/png" href="images/favicon.png">
  <link rel="apple-touch-icon" href="images/webclip.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">{jsonld_block}
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  {nav(active)}
  <main id="main">
{body}
  </main>
  {FOOTER}
  <script src="js/nav.js" defer></script>
</body>
</html>
'''


# --------------------------------------------------------------------------
# JSON-LD
# --------------------------------------------------------------------------
PERSON_LD = '''{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Michael A. Pyle",
    "jobTitle": "Author",
    "birthDate": "1953",
    "birthPlace": "Daytona Beach, Florida",
    "alumniOf": "University of Florida",
    "url": "https://www.michaelapyle.com/",
    "email": "info@michaelapyle.com",
    "description": "Michael A. Pyle draws on fiction writing, linguistics, law and international travel to weave multi-cultural, suspense and inspirational narratives.",
    "knowsAbout": ["Fiction writing", "Linguistics", "Law", "Cuban history"],
    "sameAs": ["https://www.facebook.com"]
  }'''


def book_ld(name, tagline, description, amazon, language="en", review=None, award=None):
    parts = [
        '"@context": "https://schema.org"',
        '"@type": "Book"',
        f'"name": {q(name)}',
        '"author": {"@type": "Person", "name": "Michael A. Pyle"}',
        '"bookFormat": "https://schema.org/Paperback"',
        f'"inLanguage": "{language}"',
        f'"alternativeHeadline": {q(tagline)}',
        f'"description": {q(description)}',
        f'"url": "{BASE_URL}/{slugify(name)}"',
        f'"workExample": {{"@type": "Book", "isbn": "", "potentialAction": {{"@type": "BuyAction", "target": "{amazon}"}}}}',
    ]
    if review:
        parts.append(
            '"review": {"@type": "Review", "reviewBody": %s, "author": {"@type": "Organization", "name": %s}}'
            % (q(review[0]), q(review[1]))
        )
    if award:
        parts.append(f'"award": {q(award)}')
    return "{\n    " + ",\n    ".join(parts) + "\n  }"


def q(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def slugify(name):
    return {
        "Giga Trouble": "giga-trouble",
        "Cuban Roots": "cuban-roots",
        "White Sugar, Brown Sugar": "white-sugar-brown-sugar",
    }[name]


# --------------------------------------------------------------------------
# CTA helpers (accessible labels)
# --------------------------------------------------------------------------
def cta_button(href, label, accessible):
    return f'''<a class="btn btn--grad" href="{href}" aria-label="{accessible}">
        <span>{label}</span>
        <img class="btn__arrow" src="images/arrow-right-white.svg" alt="" width="22" height="22">
      </a>'''


def cta_link(href, label, accessible):
    return f'''<a class="cta-link" href="{href}" aria-label="{accessible}">
          <span>{label}</span>
          <img class="btn__arrow" src="images/arrow-right-grad.svg" alt="" width="22" height="22">
        </a>'''


def amazon(href, title):
    return f'''<a class="amazon-link" href="{href}" target="_blank" rel="noopener" aria-label="Buy {title} on Amazon">
        <img src="images/available-at-amazon.png" alt="Available at Amazon" width="148">
      </a>'''


def paras(text):
    """Verbatim author text -> <p> blocks. Blank line separates paragraphs."""
    out = []
    for block in text.strip().split("\n\n"):
        out.append("<p>" + block.strip() + "</p>")
    return "\n        ".join(out)


# import page bodies
from content import build_pages  # noqa: E402

if __name__ == "__main__":
    pages = build_pages(globals())
    for filename, html in pages.items():
        (SITE / filename).write_text(html, encoding="utf-8")
        print("wrote", filename)
