"""Page bodies for the Michael A. Pyle static recreation.

All prose is verbatim from the live-site crawl (March 2026 publish). Italics,
links, and the author's own phrasing/typos are preserved deliberately — see
.agents/product-marketing.md (no invented copy).
"""


def _stars(n, variant="amazon"):
    cls = "stars stars--goodreads" if variant == "goodreads" else "stars"
    return f'<span class="{cls}" aria-label="{n} out of 5 stars">{"★" * n}</span>'


def _review_paras(text):
    return "\n".join(f"<p>{block.strip()}</p>" for block in text.strip().split("\n\n"))


def _amazon_bar_row(label, pct):
    return f'''<div class="review-amazon__bar-row">
              <span>{label}</span>
              <div class="review-amazon__bar-track"><div class="review-amazon__bar-fill" style="width:{pct}%"></div></div>
              <span>{pct}%</span>
            </div>'''


def _amazon_sidebar(rating_text, rating_count, bars, buy_href):
    bar_rows = "\n".join(_amazon_bar_row(label, pct) for label, pct in bars)
    return f'''<aside class="review-amazon__sidebar">
            <h3>Product Details</h3>
            <div class="review-amazon__product">
              <img src="images/white-sugar-cover.avif" alt="White Sugar, Brown Sugar book cover" width="72">
              <div>
                <p class="review-amazon__product-title">White Sugar, Brown Sugar</p>
                <p class="review-amazon__product-author">by Michael A. Pyle</p>
              </div>
            </div>
            <div class="review-amazon__rating-summary">
              {_stars(5)}
              <span class="review-amazon__rating-text">{rating_text}</span>
            </div>
            <p class="review-amazon__rating-count">{rating_count}</p>
            <div class="review-amazon__bars">
              {bar_rows}
            </div>
            <a class="review-amazon__buy" href="{buy_href}" target="_blank" rel="noopener">See All Buying Options</a>
          </aside>'''


def build_pages(g):
    page = g["page"]
    nav = g["nav"]
    paras = g["paras"]
    cta_button = g["cta_button"]
    cta_link = g["cta_link"]
    amazon = g["amazon"]
    book_ld = g["book_ld"]
    PERSON_LD = g["PERSON_LD"]

    GIGA_AMZN = "https://a.co/d/eagN1r6"
    CUBAN_AMZN = "https://a.co/d/e1pcPQa"
    WSBS_AMZN = "https://a.co/d/07McNu4"

    pages = {}

    # =====================================================================
    # HOME
    # =====================================================================
    home_body = f'''    <section class="hero">
      <div class="container hero__grid">
        <div class="hero__col">
          <h1>A Passion for Writing Fiction</h1>
          <p class="hero__lead">Michael A. Pyle draws on fiction writing, linguistics, law and international travel to weave multi-cultural, suspense and inspirational narratives.</p>
          {cta_button("contact.html", "Contact", "Contact Michael A. Pyle")}
          <div class="badge">
            <img src="images/american-legacy-bw.png" alt="American Legacy Book Awards seal" width="72">
            <div>
              <p class="badge__kicker">Inspirational Fiction Category</p>
              <p class="badge__title">American Legacy Book Finalist</p>
              <p class="badge__for">For <em>White Sugar, Brown Sugar</em></p>
            </div>
          </div>
        </div>
        <div class="hero__media">
          <div class="hero__glow" aria-hidden="true"></div>
          <img class="hero__img" src="images/michael-pyle-hero.png" alt="Author Michael A. Pyle" width="1152" height="768">
          <figure class="hero__quote">
            <img class="stars" src="images/stars.svg" alt="" width="110">
            <p class="label">About <em>White Sugar, Brown Sugar</em></p>
            <blockquote>&ldquo;A book about the triumph of the human spirit&rdquo;</blockquote>
            <cite>— John Williamson</cite>
          </figure>
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container cta-band__inner">
        <div>
          <p class="cta-band__eyebrow">Next event</p>
          <h2 class="cta-band__title">A Talk on <em>Giga Trouble</em> — Florida Vistas Book Club</h2>
          <p class="cta-band__detail">Thursday, August 20, 2026 · 2:00 p.m. · Halifax Historical Society Museum, Daytona Beach</p>
        </div>
        <a class="btn btn--on-grad" href="news.html" aria-label="See details for the August 20 Florida Vistas Book Club talk">See event details</a>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="callout-h">New Book!</h2>
        <div class="book-row">
          <div class="book-row__cover">
            <img src="images/giga-trouble-cover.png" alt="Giga Trouble book cover" width="1164">
          </div>
          <div>
            <h3 class="book-row__title"><a class="grad-text" href="giga-trouble.html">Giga Trouble</a></h3>
            <p class="book-row__tagline">Currents, Code, and Conspiracy</p>
            <p class="book-row__desc">At COVID&rsquo;s dawn, a security analyst dives overboard and leads a covert mission to dismantle a yacht-borne cyber conspiracy.</p>
            <div class="minicard">
              <blockquote>&ldquo;A swift, outlandish adventure both on and off the water that keeps the reader guessing.&rdquo;</blockquote>
              <cite>— Kirkus Review</cite>
            </div>
            <a class="read-more" href="giga-trouble.html">Read more about Giga Trouble →</a>
            <br>
            {amazon(GIGA_AMZN, "Giga Trouble")}
          </div>
        </div>
      </div>
    </section>

    <section class="section section--tint">
      <div class="container">
        <h2 class="callout-h">Prior Books</h2>
        <div class="book-row">
          <div class="book-row__cover">
            <img src="images/cuban-roots-cover.avif" alt="Cuban Roots book cover" width="600">
          </div>
          <div>
            <h3 class="book-row__title"><a class="grad-text" href="cuban-roots.html">Cuban Roots</a></h3>
            <p class="book-row__tagline">After Castro: A Cuban Reckoning</p>
            <p class="book-row__desc">A novel grounded in decades of research and vetted by Havana&rsquo;s Institute of Cuban History</p>
            <div class="minicard">
              <blockquote>&ldquo;Pyle has a gifted way of making it all come to life from every page he writes.&rdquo;</blockquote>
              <cite>— Louis Roppolo</cite>
            </div>
            <a class="read-more" href="cuban-roots.html">Read more about Cuban Roots →</a>
            <br>
            {amazon(CUBAN_AMZN, "Cuban Roots")}
          </div>
        </div>
        <div class="book-row">
          <div class="book-row__cover">
            <img src="images/white-sugar-cover.avif" alt="White Sugar, Brown Sugar book cover" width="600">
          </div>
          <div>
            <h3 class="book-row__title"><a class="grad-text" href="white-sugar-brown-sugar.html">White Sugar, Brown Sugar</a></h3>
            <p class="book-row__tagline">Crossing Daytona Beach&rsquo;s Color Line</p>
            <p class="book-row__desc">In the 60s, two boys cross the tracks, battle addiction, and rebuild their lives.</p>
            <div class="minicard">
              <blockquote>&ldquo;Sometimes a debut novel really surprises the reader with its scope and depth..&rdquo;</blockquote>
              <cite>— John Williamson</cite>
            </div>
            <a class="read-more" href="white-sugar-brown-sugar.html">Read more about White Sugar, Brown Sugar →</a>
            <br>
            {amazon(WSBS_AMZN, "White Sugar, Brown Sugar")}
          </div>
        </div>
      </div>
    </section>'''
    pages["index.html"] = page(
        "index.html",
        "Michael A. Pyle",
        "Michael A. Pyle draws on fiction writing, linguistics, law and international travel to weave multi-cultural, suspense and inspirational narratives.",
        home_body,
        jsonld=PERSON_LD,
        canonical_path="/",
    )

    # =====================================================================
    # ABOUT
    # =====================================================================
    bio = '''Michael A. Pyle was born in 1953 in Daytona Beach, Florida. He earned a bachelor&rsquo;s degree in English from the University of Florida, with a minor in creative writing. He obtained a master&rsquo;s degree in Linguistics, was an associate professor of English as a Second Language, and later graduated from with a Juris Doctor degree from the School of Law, all at the same university.

He wrote Cliffs TOEFL Preparation Guide and two similar textbooks for foreign students, published by Cliffs Notes and its successors.

In 2012, he published his historical fiction novel <em>White Sugar, Brown Sugar</em>, about racial issues, drug abuse, and recovery in 1950s and 60s Florida. It follows the loss of innocence of the characters, submergence to the depths of desperation, and eventual emergence as recovering adults. It is a story of friendship, hope, strength, and inspiration.

In 2018, he published <em>Cuban Roots</em> after performing extensive research and interviews in the United States and throughout Cuba.

In 2025, he launched his third book, <em>Giga Trouble</em>,

Both novels were published through his small publishing company, Armstrong Media Group, LLC.

After practicing law for 40 years and retiring in 2023, Pyle has turned to writing general fiction. His recent works feature characters from his previous books.'''

    about_body = f'''    <section class="container layout layout--2col">
      <article class="prose">
        <h2>Biography</h2>
        <img class="divider" src="images/divider.svg" alt="" width="240">
        {paras(bio)}
      </article>
      <aside class="aside">
        <h2>First Essay</h2>
        <a class="essay-figure" href="assets/eloises-day-in-court.pdf" target="_blank" rel="noopener" aria-label="Read the essay “Eloise's Day in Court” (PDF)">
          <img src="images/elder-law-advocate.png" alt="Elder Law Advocate magazine">
          <img src="images/eloise.png" alt="“Eloise's Day in Court” essay illustration">
        </a>
        <p class="lead-q"><strong>&ldquo;Pyle has a gifted way of making it all come to life from every page he writes.</strong>&rdquo;</p>
        <p class="attribution">— Louis Roppolo</p>
        {cta_link("contact.html", "Contact", "Contact Michael A. Pyle")}
      </aside>
    </section>'''
    pages["about.html"] = page(
        "about.html",
        "About Michael A. Pyle",
        "Michael A. Pyle draws on fiction writing, linguistics, law and international travel to weave multi-cultural, suspense and inspirational narratives.",
        about_body,
        jsonld=PERSON_LD,
        canonical_path="/about",
    )

    # =====================================================================
    # CONTACT
    # =====================================================================
    contact_body = '''    <section class="container contact">
      <h1>Contact Michael A. Pyle</h1>
      <p class="contact__email"><a href="mailto:info@michaelapyle.com">info@michaelapyle.com</a></p>
      <form class="form-grid" hx-boost="false" action="mailto:info@michaelapyle.com" method="post" enctype="text/plain" aria-label="Contact form">
        <p class="form-note" id="form-help">Send a message. This form opens your email app with the details filled in.</p>
        <div class="form-row">
          <div>
            <label for="full-name">Full Name</label>
            <input class="field" type="text" id="full-name" name="Full-Name" placeholder="Full Name" maxlength="256" required>
          </div>
          <div>
            <label for="email">Email Address</label>
            <input class="field" type="email" id="email" name="Email-Address" placeholder="Email Address" maxlength="256" required>
          </div>
        </div>
        <div>
          <label for="message">Message</label>
          <textarea class="field" id="message" name="Message" placeholder="Message" maxlength="5000" required></textarea>
        </div>
        <div>
          <button class="btn btn--grad" type="submit">Send now</button>
        </div>
      </form>
    </section>'''
    pages["contact.html"] = page(
        "contact.html",
        "Contact Michael A. Pyle",
        "Get in touch with author Michael A. Pyle at info@michaelapyle.com.",
        contact_body,
        jsonld=PERSON_LD,
        canonical_path="/contact",
    )

    # =====================================================================
    # GIGA TROUBLE
    # =====================================================================
    giga_syn = '''In early 2020, as a global pandemic begins to cause turmoil around the world, Michele Morales has come to the conclusion that her employer, a global security firm, is likely behind a digital crime scheme.

Her unease deepens when she and her co-workers are forced to board the company&rsquo;s huge yacht. After a few hours of watching lines of co-workers taken behind closed doors and then returning under the influence of some mind-altering substance, she knows the worst is yet to come.

As the yacht leaves the dock and heads toward the open sea, Michele escapes, propelling herself into a shadowy world of secrets, betrayal, and escalating danger

Is the real danger coming from her employer&rsquo;s agents, or is there something far more sinister at play, lurking in the unseen world of cyberspace?

Every second counts as Michele unravels a conspiracy that could shatter everything she thought she knew about her company, her colleagues, and herself.

From Miami to Havana to the Bahamian isles and Washington D.C., they face attacks by those behind the criminal enterprise but also their own government.

Michele and her partners must uncover the truth, decide whom to trust and side-step a threat that could shake the foundations of international security.'''

    giga_why = '''I am certainly not a computer or internet geek. In about 1986, my dad&rsquo;s law firm in which I was a junior associate, put word processors on each attorney&rsquo;s desk. The old guys were lost and afraid. I was not. Soon, we received quite basic computers. Fortunately, my good friend who lived next door to my house was a retired computer programmer. He taught me everything. I remember that he liked to read computer magazines and one day while sitting outside with him and looking at a colorful magazine cover about Windows, I said what is Windows? He responded that it was a bunch of nonsense. It wasn&rsquo;t real computing. And it would never go anywhere.

Later, came to be and over the years they became more and more. I recall the first time I personally received a letter in the mail (that is snail mail) from Nigeria. It was a ridiculous story about a widow who&rsquo;d inherited millions and she wanted to share it with me or at least let me share in it by charging fees.  I received a few like that.

But then, I had a husband and wife come to see me one day. I&rsquo;d prepared the estate plan leaving their modest estate to their family. But they&rsquo;d been duped, also by paper mail and phone calls, to send money to a foreign country in order to receive a huge amount.  They kept being told they needed to send more, so they did, and when they ran out of money in their savings account, they took out a line of credit on their home. And when they came to see me they were broke and couldn&rsquo;t pay the mortgage payment.

Then a widower came in. His bank had called his kids to warn that he was sending his money away. He promised me that he would not send any more, but he did.  And then he did because of the executor of a family member&rsquo;s estate. I was afraid to let him serve as the executor, but under the law, I couldn&rsquo;t report his past stupidity to the court or the beneficiaries. Again, he promised that he would not send estate money to the court.  So I managed to hold the money in the law firm trust account.  But he did receive distribution of a bank account directly to him and before I knew it, he&rsquo;d sent it away.

Then in the last six years, our law firm was involved in a large real estate transaction. We represented the seller only. Another law firm was the escrow holder.  Somehow, a scammer got into the e-mail string. This was after title companies were already insisting that no agent could order a wire transfer via email. It had to be in paper form sent via overnight mail.  But the hacker that got into the email string and e-mailed the other law firm, telling them where to send the money, and ignoring what we had sent to the other law firm by paper. So, the large amount of money that was to go to the seller went to a U.S. person who was being paid to run money through her account and soon the money was in the far-east. Our federal government did find the money and got back a good part of it, but not all.

In the 90s, I started giving talks that I called Shams, Flams and Flim-Flams and people were still not so concerned about such things.

In the early months of the COVID-19 Pandemic, I, like many, were watching our state and federal government, business, hospitals and the common people at odds with everybody about what to do. I was traveling internationally and became ill with COVID twice. At the same time, probably only by coincidence, I was seeing many news stories about all kinds of internet crime. I started thinking that there was an interesting comparison in the way people fought over the human virus and computer and internet viruses.  So I started playing with the idea. I read many non-fiction cybercrime books as well as many fiction cybercrime books.

And then I decided that I loved the characters from my prior books and even though the main characters were much older now, their kids, who were young in those books would be about my kids&rsquo; ages, nearing 40. So I gathered together those now-adult offspring into this new story. And, I also determined that I wanted a female to be the principal character.

I had no real plan for what was going to happen. I usually do not outline a whole book when I start. I just used some facts that I had developed in the older books, added Cuba to the mix, because it could be interesting to do so, and built it little by little.

I also ran tech things by my brother, who is much younger than I and was a fledgling computer genius as a teenager. He helped a lot. And later I also added a good friend who has a cyber protection company to help me with vocabulary, etc.I also like the water and boats, so of course I used that idea as well. And of course, I needed a little bi-racial romance, something a little funny, and a May-December romance that would annoy the family of the male.

I&rsquo;ve received pretty good reviews, including from the well-known company, Kirkus.'''

    giga_review = '''&ldquo;A modern tech thriller about a secretive company and its malicious intentions from author Pyle.

The year is 2020. Michele Morales works for an international company called Giga-BATS. Rather unexpectedly, when Michele and her colleagues show up for work one day, they are told they are having a company meeting offsite; the meeting is to take place on the company yacht Giga Blue.

This is Miami, so yachts are commonplace, but a surprise compulsory company meeting on a boat is unprecedented—Michele is concerned. As the yacht sets sail, she jumps ship and is picked up by a small speedboat. Soon, she is in contact with her father, an attorney named Franklin Morales. Franklin agrees that the whole thing is highly suspicious.

Meanwhile, back on Giga Blue, Michele&rsquo;s friends Kim and Tad are being forced to participate in nefarious internet schemes, &ldquo;using private information that the company had acquired for inappropriate purposes.&rdquo; It occurs to Tad that &ldquo;All he could do was pray that&rdquo; somehow, he&rsquo;d &ldquo;find a way out of this labyrinth of lies and corruption before it consumed him entirely.&rdquo;

The story&rsquo;s premise is bizarre; a company kidnapping staff and forcing them to work on things like malware feels over-the-top. Nevertheless, readers will be intrigued to discover where this is all going, particularly as events move to Cuba and the technological aspects of the plot intensify. The narrative moves quickly and builds anticipation effectively; … there are several compelling twists in store before the final page.&rdquo;'''

    giga_ld = book_ld(
        "Giga Trouble",
        "Currents, Code, and Conspiracy",
        "At COVID's dawn, a security analyst dives overboard and leads a covert mission to dismantle a yacht-borne cyber conspiracy.",
        GIGA_AMZN,
        review=("A swift, outlandish adventure both on and off the water that keeps the reader guessing.", "Kirkus Reviews"),
    )

    giga_body = f'''    <section class="hero">
      <div class="container hero__grid">
        <div class="hero__col">
          <p class="hero__eyebrow">Michael A. Pyle&rsquo;s third book</p>
          <h1>Giga Trouble</h1>
          <p class="hero__tagline">Currents, Code, and Conspiracy</p>
          <p class="hero__desc">At COVID&rsquo;s dawn, a security analyst dives overboard and leads a covert mission to dismantle a yacht-borne cyber conspiracy.</p>
          {amazon(GIGA_AMZN, "Giga Trouble")}
        </div>
        <div class="hero__media">
          <div class="hero__glow" aria-hidden="true"></div>
          <img class="hero__img" src="images/giga-trouble-cover.png" alt="Giga Trouble book cover" width="1164">
        </div>
      </div>
    </section>

    <section class="container layout layout--2col">
      <article class="prose">
        <h2>Synopsis</h2>
        <img class="divider" src="images/divider.svg" alt="" width="240">
        {paras(giga_syn)}
        <p class="aside-label">We asked Michael A. Pyle:</p>
        <h2>Why have you written this book?</h2>
        <img class="divider" src="images/divider-2.png" alt="" width="240">
        {paras(giga_why)}
      </article>
      <aside class="aside">
        <h2>Review</h2>
        <img class="quotes-mark" src="images/quotes.svg" alt="" width="56">
        <img class="review-logo" src="images/kirkus-reviews.webp" alt="Kirkus Reviews" width="220">
        <p class="lead-q">&ldquo;A swift, outlandish adventure both on and off the water that keeps the reader guessing.&rdquo;</p>
        <div class="review-body">
        {paras(giga_review)}
        </div>
        <p class="attribution">— Kirkus Review</p>
        {cta_link("contact.html", "Contact", "Contact Michael A. Pyle")}
        <img src="images/giga-trouble-cover.png" alt="Giga Trouble book cover" width="940" style="margin:2rem 0; max-width:260px;">
        {cta_link("about.html", "About Michael A. Pyle", "About the author Michael A. Pyle")}
      </aside>
    </section>'''
    pages["giga-trouble.html"] = page(
        "giga-trouble.html",
        "Giga Trouble from Michael A. Pyle",
        "Giga Trouble by Michael A. Pyle — at COVID's dawn, a security analyst dives overboard and leads a covert mission to dismantle a yacht-borne cyber conspiracy.",
        giga_body,
        jsonld=giga_ld,
        canonical_path="/giga-trouble",
    )

    # =====================================================================
    # CUBAN ROOTS
    # =====================================================================
    cuban_syn = '''<em>Cuban Roots</em> is a historical novel, based mostly in Cuba and also in Florida, including Daytona Beach.

Luis Morales is an eighty-four year old lawyer, born in Cuba, living in Miami. He regularly travels to Cuba to deliver funds inherited by Cubans. He gives an interview to a reporter regarding his interpretation of the feeling of the people living on the island about Fidel Castro&rsquo;s death, and some strongly criticize his words.

After being hounded and attacked, he suffers a medical crisis, and while seemingly unconscious, relives the good and bad experiences of his youth in the country of his birth, the country that he loves, Cuba.

Michael A. Pyle, author of <a href="white-sugar-brown-sugar.html"><em>White Sugar, Brown Sugar</em></a>, began writing <em>Cuban Roots</em> over thirty years ago. He has traveled all over Cuba numerous times, interviewing people, visiting museums and performing research.

Senior officers of the Institute of Cuban History in Havana, Cuba have read the manuscript and found the historical references credible. The Institute has invited him twice to present the book to its annual international symposium.'''

    cuban_why = '''<em>Cuban Roots</em> came about because I learned about Cuba and the trauma its &ldquo;Revolution&rdquo; caused my wife of 38 years and her family. I was in my twenties when we married, and I never knew much about or even cared about Cuba or anyplace else.

It&rsquo;s funny that my classmates from elementary school in the 50&rsquo;s and early 60&rsquo;s have told me in recent years how we had to get below our desks to prepare for the Russian Missiles to attack.  Some even told me we had actual dog tags in my elementary school. I generally remember everything from the past including the faces and names of every teacher, but I don&rsquo;t remember that.

I remember that the teachers brought televisions into our 6th grade classroom the day the John F. Kennedy was assassinated.

After we married, especially when her parents would come to visit from Venezuela, they would talk about what happened in Cuba after Fidel Castro took control in 1960. I vaguely knew that in 1961, she and her brother, ages 7 and 8, had been sent to Spain to live in Catholic boarding schools.  Many other Cuban children of 6 to 8 years of age were sent alone on the &lsquo;Peter Pan Flights&rsquo; to the United States, to live in foster homes all over the country. Why? Because there had been a rumor spread throughout the streets in Cuba that kids in that age range would be sent to Russia for indoctrination.

Although I wasn&rsquo;t sure who started that rumor, I am now convinced after much study that the &lsquo;rumor&rsquo; really happened and that it was the United States&rsquo; CIA that spread the rumor. My wife&rsquo;s mother and the two younger daughters, ages two and four, remained in Cuba, and the entire family reunited 7 years later in the Andes of Venezuela.

I met my wife because I was a professor of English to Speakers of Other Languages at the University of Florida.  She came to study for a Master&rsquo;s Degree in Microbiology on a scholarship from the Venezuelan government (that&rsquo;s when it was rich with oil).

Over the years I had also met a cousin of my wife who lived in Miami. I learned that he had escaped Cuba by raft, from a city in southeast Cuba to the U.S. base in Guantanamo. That&rsquo;s the first time I realized that under the &lsquo;wet-foot, dry-foot&rsquo; rule, a Cuban could stay in the U.S. upon touching its soil, including touching the coil of the base in Guantanamo because it was U.S. land.

Also, in the 1970&rsquo;s, we were in Miami one time and had to stop at the house of one of her relatives to pick up something. There was a party going on, and my wife informed me that all the people there, gray-haired and blue-haired elders, had been in Cuban prisons together. I couldn&rsquo;t believe that these calm old smiling people could have endured that.

I became quite interested in the history and started writing a book, although I knew very little. I would travel to Miami and meet with her cousin and have him draw me maps showing the bay at Santiago de Cuba and the mountains that surrounded that city. I had learned of an attack initiated by Castro, in the same city in 1953, and I would ask him to describe for me whether they could hear the sound of gunfire from their home. My wife had lived in the same neighborhood where he did, but she was born in 1953.

I would use internet aerial maps to locate places in Cuba, but this was in the 80s, and the internet wasn&rsquo;t that good; AND supposedly the Cuban government did not share what was where, and where Fidel and his family really lived. In fact, when I first visited Cuba in 2010 I was warned not to take any device with GPS because it was illegal. (I don&rsquo;t know that it was true, but the Cuban people were afraid, just like they were afraid to say anything negative about the government, even in private.)

After learning much from my vast collection of books on Cuban history and interviews with the relatives, I learned in 2010 that President Obama was opening the door for Cubans to return home to see their families without violating U.S. laws.  This was before other general citizens of the U.S. were allowed to go there (without having to sneak by going through Canada, the Bahamas, or other countries).

So, I said to myself, I need to go, to visit the real places that are part of the story I was writing, and learn the view of the people who still resided there. And I also determined that even though my wife didn&rsquo;t travel with me (because she did not want to return to that country), her family was my family.

On the return from my first trip in January 2010, on what they called Charter Flights at the time, I came into Miami International Airport. Arriving in immigration, a man who looked to me to be of Cuban heritage, stood in uniform in front of me. &ldquo;Where were you visiting?&rdquo; &ldquo;Cuba.&rdquo; &ldquo;You cannot go to Cuba.&rdquo; &ldquo;Yes, I can. I traveled under the Family Visit rule.&rdquo; &ldquo;You obviously are not Cuban.&rdquo; &ldquo;My wife is.&rdquo; &ldquo;Where is she? Why is she not with you?&rdquo; &ldquo;Her family is my family. She doesn&rsquo;t have to travel with me.&rdquo;

After glaring at me for a few moments, he called over a non-Cuban officer and told him the story. He told the other officer that he intended to arrest me for having visited Cuba illegally. I again explained that I visited on the Family Visit rule, and being a lawyer, recited the law that permitted that.

Finally, he almost viciously waived me past.  Two months later I returned from my second visit and the same immigration officer stood in front of me, glaring. He recognized me, didn&rsquo;t ask me anything, and didn&rsquo;t look at anything; with a fiercely aggravated facial expression he waived his arms to permit me enter my country.

I fell in love with Cuba, mostly because it was or could have been beautiful, but it was in decay, and I loved the people, the old cars, the strange rules. In those years the only restaurants were government owned and operated and the food was awful. Beef was illegal to have or sell. The Cuban people survived on $20 to $30 dollars a month (they still do), and the ration books were had many more items than they do now. And even later as beef became legal, it was so tough one couldn&rsquo;t eat it.  The only private food establishments were called Paladars, and they were little places inside people&rsquo;s homes.  But they had to get their food from the government, so it was awful.  I got food poisoning quite a few times when I first started visiting.

On my first visit to Havana, my wife had arranged for a second cousin of hers in Havana to take me all around the city, walking for 7 days.  The law had just opened up that would allow a Cuban to stay in a tourist hotel. I wanted to go to the city where my wife had been born, Santiago de Cuba, which is far away from Havana, and it was where many historical battles had occurred.  So, the cousin took his first plane flight with me and stayed in the first hotel he&rsquo;d ever been in (I had to explain everything including how to use the plastic key card to open the door). Then, we walked seven days around Santiago de Cuba and finally found where my wife&rsquo;s cousin still lived, in the same neighborhood where she had lived.

I met another relative there, who has actually been my book editor ever since. She and her boyfriend introduced me to historians, gave me multiple books and photos, etc.Later, when I was finalizing my book, Cuban Roots, I was invited to a meeting at the Instituto de Historia de Cuba, where I met very interesting people.  They were sincere about their beliefs, like many who had always lived on the Island and loved their country. I learned what they believed and researched the different points of view.  I believe strongly that our CIA did start the famous rumor about kids being sent to Russia and found that it was similar to many other acts it took to counter politics in South American countries. But there were other beliefs that I took as propaganda of Cuba and thus did not find real.I do not take sides in Cuban Roots. I try to show how some people, like the &lsquo;exile community&rsquo; in Miami and their descendants, are totally against anything involving Cuba, including the fact that they consider the people who were born and raised and still live in Cuba as being socialist or communist. I also try to show the beliefs of other Cubans who remain on the Island, who are usually younger and have left or tried to leave Cuba in recent years.

Another major reason for my interest in Cuba is that the former President / Dictator, Batista lived in Daytona from about 1943 until the day he had to leave Cuba and tried to return here. He had purchased two large houses on the river in Daytona from race car driver Ransom Olds. He was very popular here and the recipient of fancy dinners, parades and other love from the people of Daytona Beach.

He brought a trove of most would call stolen art, which is now in the local museum.  He invited the entire city commission, city attorney (my father&rsquo;s law partner) and the Mayor to Havana and feted them to a banquet in the Presidential Palace. He gifted one of the houses and its contents including the art to the City of Daytona during that banquet.  I have a copy of the deed, which was acknowledged in the presence of the U.S. Consul during that feast.

My book has received some bad reviews, generally from those who believe that one should never support or help anybody in Cuba and should never travel there.

I was invited twice to present my book at the Instituto de Historia de Cuba in Havana, and appreciated their acceptance of the book. It is fiction but based upon many historical facts.

But the government of Cuba began worrying about my intentions because I put money on people&rsquo;s cell phones every two weeks for years. I suppose it thought that my giving them access to internet meant I was promoting dissidents.

The government began interrogating me every time I returned and also began ordering some of the recipients of the phone recharges to go to the military police department for interrogation. I was actually only helping people communicate. Therefore, I have not returned to the Island for almost three years now, and do not intend to visit again.I did use my knowledge of Cuba again in my newest book, <a href="giga-trouble.html"><em>Giga Trouble</em></a>, but it is not historical although the suspicions of the U.S. government and the Cuban government even today are played out in that book also.'''

    cuban_ld = book_ld(
        "Cuban Roots",
        "After Castro: A Cuban Reckoning",
        "A novel grounded in decades of research and vetted by Havana's Institute of Cuban History.",
        CUBAN_AMZN,
        review=("Pyle has a gifted way of making it all come to life from every page he writes.", "Louis Roppolo"),
    )

    cuban_body = f'''    <section class="hero">
      <div class="container hero__grid">
        <div class="hero__col">
          <p class="hero__eyebrow">Michael A. Pyle&rsquo;s second book</p>
          <h1>Cuban Roots</h1>
          <p class="hero__tagline">After Castro: A Cuban Reckoning</p>
          <p class="hero__desc">A novel grounded in decades of research and vetted by Havana&rsquo;s Institute of Cuban History</p>
          {amazon(CUBAN_AMZN, "Cuban Roots")}
        </div>
        <div class="hero__media">
          <div class="hero__glow" aria-hidden="true"></div>
          <img class="hero__img" src="images/cuban-roots-cover.avif" alt="Cuban Roots book cover" width="600">
        </div>
      </div>
    </section>

    <section class="container layout layout--2col">
      <article class="prose">
        <h2>Synopsis</h2>
        <img class="divider" src="images/divider.svg" alt="" width="240">
        {paras(cuban_syn)}
      </article>
      <aside class="aside">
        <h2>Review</h2>
        <img class="quotes-mark" src="images/quotes.svg" alt="" width="56">
        <p class="lead-q"><strong>&ldquo;Pyle has a gifted way of making it all come to life from every page he writes.</strong>&rdquo;</p>
        <p class="attribution">— Louis Roppolo</p>
        <h2>Context</h2>
        <p class="lead-q"><strong>&ldquo;I wrote <em>Cuban Roots</em> after marrying into a Cuban family and spending years researching and traveling, documenting exile trauma (e.g., Peter Pan flights) and presenting both exile and island perspectives from Santiago and Havana to Batista-era ties with Daytona. My work drew invitations from Havana&rsquo;s history institute and scrutiny from U.S. and Cuban authorities; I no longer visit the island and later used this knowledge in </strong><a href="giga-trouble.html"><strong>Giga Trouble</strong></a><strong>.</strong>&rdquo;</p>
        <p class="attribution">— Michael A. Pyle</p>
        {cta_link("contact.html", "Contact", "Contact Michael A. Pyle")}
      </aside>
    </section>

    <section class="container layout layout--2col">
      <article class="prose">
        <p class="aside-label">We asked Michael A. Pyle:</p>
        <h2>Why have you written this book?</h2>
        <img class="divider" src="images/divider-2.png" alt="" width="240">
        {paras(cuban_why)}
      </article>
      <aside class="aside">
        <img src="images/cuban-roots-cover.avif" alt="Cuban Roots book cover" width="600" style="margin-bottom:1.5rem;">
        {cta_link("about.html", "About Michael A. Pyle", "About the author Michael A. Pyle")}
      </aside>
    </section>'''
    pages["cuban-roots.html"] = page(
        "cuban-roots.html",
        "Cuban Roots from Michael A. Pyle",
        "Cuban Roots by Michael A. Pyle — a historical novel grounded in decades of research and vetted by Havana's Institute of Cuban History.",
        cuban_body,
        jsonld=cuban_ld,
        canonical_path="/cuban-roots",
    )

    # =====================================================================
    # WHITE SUGAR, BROWN SUGAR
    # =====================================================================
    wsbs_syn = '''In 1960s Florida, two boys meet by chance while fishing outside a yacht club where only one of them would be allowed inside.

One is white, from a beach-side family of moderate financial means. The other is Black, from the neighborhood west of the railroad tracks where segregation confined his community.

Despite the racial divide that defines their world, they become true friends—bonded by something deeper than either understands. Both are sons of struggling mothers: one lost to drugs, the other drowning in alcohol. Both have sworn they&rsquo;ll never follow that path. But addiction doesn&rsquo;t honor promises or boundaries.

As the boys descend into the same darkness they&rsquo;d vowed to avoid, their friendship endures through arrests, overdoses, and tragic loss. When they finally face the choice between destruction and redemption, an unexpected ally helps them both claw their way back.

White Sugar, Brown Sugar is a raw, unflinching story of friendship across the color line, the universality of addiction, and the hard-won hope of recovery. It&rsquo;s about two boys who lose everything—and find their way home together.'''

    wsbs_why = '''I began writing <em>White Sugar, Brown Sugar</em>, at the age of 18, on an old black underwood typewriter. I was bound and determined to become a Hemingway.

After doing too many drugs after my parents divorced, I thought I was cured and I could help others avoid or stop using drugs.  But it turns out that I wasn&rsquo;t ready to be trying to help anybody at that time

Once I did clean up, I continued writing the book for quite a while, including while studying creative writing at the University of Florida as part of my undergraduate studies in English.

I recall reading portions of it in class and getting good feedback. I received some great advice from the professor, Sterling Watson. I attended a talk in which Mr. Watson spoke at the Miami International Book Fair a few years ago and thanked him for writing, &lsquo;Get closer to his head&rsquo; at the top right-hand corner of a short story that was part of the book.

I continued writing the book for many, many years, and sent it to the editor of my first non-fiction books, TOEFL Preparation Guide and its successors, published by Cliffs Notes, Inc. My editor pointed out correctly that my fiction book wasn&rsquo;t deep enough. So, I kept writing.

In the book, I presented that we white kids on the beachside of Daytona Beach had certain types of drugs, like psychedelics, but when we wanted to go to narcotic drugs, we needed to go across the river and the railroad tracks. So, there were two different cultures now involved, and I decided to show how Blacks were discriminated against in oceanfront cities across Florida.

After working on that new interracial view for a few years, I was driving the family van on the northeast coast of the U.S when I was in my 30s, with the young kids fighting in the back seat, and I suddenly told myself that there was something wrong. I was dealing with race and the difference of cultures through only a white boy&rsquo;s eyes. I needed a black character.

I used the first name of a teenager who was in drug rehab with me. And that guy had reddish hair, so everybody called him Red. So, he became a new character, and I created a family around him. I also had worked in a cafeteria chain founded in Mobile, Alabama as a teenager, and I thought it was racist, so I used that as well.

Much of the book is at least based partially upon many events that really happened, and people who really existed, but I embellished (or made more horrific) whatever I remembered, so it still is truly fiction. But my friends who read it knew instantly that I was describing much about my mother and father as well as myself. And many realized instantly that I was referring to a well-known Baptist Minister in the Daytona Beach area who founded a drug rehab center.

I finally self-published <em>White Sugar, Brown Sugar </em>in 2012, when I was 59 years old. You will realize that the characters have bit parts in my second book <a href="cuban-roots.html"><em>Cuban Roots</em></a> and they and their children, who were young in <em>White Sugar, Brown Sugar</em>, are major characters in my third book, <a href="giga-trouble.html"><em>Giga Trouble</em></a>.'''

    wsbs_review = '''&ldquo;Two young men struggle with addiction in Pyle&rsquo;s historical novel. The story begins in the 1960s in Daytona Beach, Florida. Jude Armstrong is a white kid from a messed-up middle-class family. His mother has pretty much given herself over to drink and partying; his straightlaced lawyer father has moved out. (Lansing Armstrong is not a bad dad, but he is temperamentally aloof and incapable of connecting with his son.)

Jude&rsquo;s friend Roosevelt Harris is a poor Black kid whose mother turns tricks to feed her habit. The boys&rsquo; addictions begin with glue sniffing and pot smoking and quickly ramp up from there. The two have become friends by happenstance, and soon they&rsquo;re running with other drugged-out teens who are into much more dangerous stuff.

At one point, a girl OD&rsquo;s while they&rsquo;re bingeing, and the cops catch them, but even that&rsquo;s not enough to break the grip of the illicit substances. A second drug bust is enough to scare Roosevelt straight, but not Jude, who has to bounce along rock bottom until Roosevelt finally drags him to an A.A. meeting. The real strength of this well-written book is in its descriptions of wild drug orgies (&ldquo;His brain crackled like the time he&rsquo;d eaten a spoonful of horseradish. Zoooom. He was going in high speed&rdquo;) and what it&rsquo;s like to be a slave to your next fix (or, in the long, drawn-out case of Jude, your next drink). The author deftly catalogs all the excuses that addicts give themselves, the fleeting euphoria that rules their lives, the wallowing in self-pity, the resentment toward those who try to help, and the awful harm that they inflict on those close to them.

Lansing and Roosevelt are often close to giving up on Jude, but they stick by him; this is a story of heroic caring and friendship. And yet, the final pages recount apoignant sailing trip during which Jude again faces a diabolical temptation—Pyle&rsquo;s narrative has the powerful ring of truth.

A bracing tale that will shake the reader.&rdquo;'''

    wsbs_tripp = '''Michael A. Pyle originally published <em>White Sugar, Brown Sugar</em> under a pen name because as a practicing lawyer with older clients, he was afraid that if anybody read it and realized he was the author and probably one of the characters, he&rsquo;d lose clients.

However, after a local newspaper revealed who he really was and readers began making only positive comments and writing positive reviews, he republished it under his real name.'''

    wsbs_ld = book_ld(
        "White Sugar, Brown Sugar",
        "Crossing Daytona Beach's Color Line",
        "In the 60s, two boys cross the tracks, battle addiction, and rebuild their lives.",
        WSBS_AMZN,
        review=("Pyle's narrative has the powerful ring of truth", "Kirkus Reviews"),
        award="American Legacy Book Finalist, Inspirational Fiction Category",
    )

    wsbs_body = f'''    <section class="hero">
      <div class="container hero__grid">
        <div class="hero__col">
          <p class="hero__eyebrow">Michael A. Pyle&rsquo;s first book</p>
          <h1>White Sugar, Brown Sugar</h1>
          <p class="hero__tagline">Crossing Daytona Beach&rsquo;s Color Line</p>
          <p class="hero__desc">In the 60s, two boys cross the tracks, battle addiction, and rebuild their lives.</p>
          {amazon(WSBS_AMZN, "White Sugar, Brown Sugar")}
        </div>
        <div class="hero__media">
          <div class="hero__glow" aria-hidden="true"></div>
          <img class="hero__img" src="images/white-sugar-cover.avif" alt="White Sugar, Brown Sugar book cover" width="600">
        </div>
      </div>
    </section>

    <section class="container layout layout--2col">
      <article class="prose">
        <h2>Synopsis</h2>
        <img class="divider" src="images/divider.svg" alt="" width="240">
        {paras(wsbs_syn)}
      </article>
      <aside class="aside recognition">
        <h2>Recognition</h2>
        <div class="badge" style="border:0;padding:0;margin:0 0 1.5rem;">
          <img src="images/american-legacy-bw.png" alt="American Legacy Book Awards seal" width="72" style="filter:none;">
          <div>
            <p class="aside-label" style="text-transform:uppercase;letter-spacing:.1em;font-style:normal;font-size:.72rem;">Inspirational Fiction Category</p>
            <p style="font-weight:900;margin:.15rem 0;">American Legacy Book Finalist</p>
            <p class="aside-label">For <em>White Sugar, Brown Sugar</em></p>
          </div>
        </div>
        <img src="images/american-legacy.jpeg" alt="American Legacy Book Awards" width="1280">
        <img class="review-logo" src="images/wsj-logo.png" alt="The Wall Street Journal" width="220">
        <p class="award-num">#2</p>
        <p class="award-label">2013 Reader&rsquo;s Choice Award</p>
        <img class="quotes-mark" src="images/quotes.svg" alt="" width="56">
        <p class="lead-q"><strong>&ldquo;Sometimes a debut novel really surprises the reader with its scope and depth..&rdquo;</strong></p>
        <p class="attribution">— John Williamson</p>
        {cta_link("contact.html", "Contact", "Contact Michael A. Pyle")}
      </aside>
    </section>

    <section class="container layout layout--2col">
      <article class="prose">
        <p class="aside-label">We asked Michael A. Pyle:</p>
        <h2>Why have you written this book?</h2>
        <img class="divider" src="images/divider-2.png" alt="" width="240">
        {paras(wsbs_why)}
      </article>
      <aside class="aside">
        <h2>Review</h2>
        <img class="quotes-mark" src="images/quotes.svg" alt="" width="56">
        <img class="review-logo" src="images/kirkus-reviews.webp" alt="Kirkus Reviews" width="220">
        <p class="lead-q"><strong>&ldquo;Pyle&rsquo;s narrative has the powerful ring of truth&rdquo;</strong></p>
        <div class="review-body">
        {paras(wsbs_review)}
        </div>
        <p class="attribution">— Kirkus Review</p>
        {cta_link("white-sugar-brown-sugar-reviews.html", "More reader reviews", "Read White Sugar, Brown Sugar reader reviews on Amazon and Goodreads")}
        <h2 class="grad-text" style="color:transparent;">Who is E.G. Tripp?</h2>
        {paras(wsbs_tripp)}
        <img src="images/white-sugar-cover.avif" alt="White Sugar, Brown Sugar book cover" width="600" style="margin:1.5rem 0;max-width:260px;">
        {cta_link("about.html", "About Michael A. Pyle", "About the author Michael A. Pyle")}
      </aside>
    </section>'''
    pages["white-sugar-brown-sugar.html"] = page(
        "white-sugar-brown-sugar.html",
        "White Sugar, Brown Sugar from Michael A. Pyle",
        "White Sugar, Brown Sugar by Michael A. Pyle — in the 60s, two boys cross the tracks, battle addiction, and rebuild their lives. American Legacy Book Finalist.",
        wsbs_body,
        jsonld=wsbs_ld,
        canonical_path="/white-sugar-brown-sugar",
    )

    # =====================================================================
    # NEWS & EVENTS
    # =====================================================================
    VIMEO_1 = "https://vimeo.com/1203959038"
    VIMEO_2 = "https://vimeo.com/1203959039"

    news_body = f'''    <section class="container page-intro">
      <h1>News &amp; Events</h1>
      <p class="page-intro__lead">Upcoming appearances, recent press, and past events with Michael A. Pyle.</p>
    </section>

    <section class="container events-page">
      <div class="events-group">
        <h2>Upcoming</h2>
        <div class="events-list">

          <article class="event event--upcoming">
            <div class="event__head">
              <span class="event__type">Book Club Talk</span>
              <span class="event__date">Thursday, August 20, 2026 · 2:00 p.m.</span>
            </div>
            <h3 class="event__title">Florida Vistas Book Club — A Talk on <em>Giga Trouble</em></h3>
            <p class="event__meta">Halifax Historical Society Museum, 252 S. Beach Street, Daytona Beach, FL 32114</p>
            <p class="event__desc">Michael A. Pyle gives a talk about <em>Giga Trouble</em> to the Florida Vistas Book Club, which now meets at the Halifax Historical Society Museum.</p>
          </article>

          <article class="event event--upcoming">
            <div class="event__head">
              <span class="event__type">Book Fair</span>
              <span class="event__date">November 20–22, 2026</span>
            </div>
            <h3 class="event__title">Miami Book Fair — Street Fair Booth</h3>
            <p class="event__meta">Downtown Miami, Florida</p>
            <p class="event__desc">Michael will have a booth to show and sell all of his books at the Miami Book Fair Street Fair — a large annual festival he has taken part in before. The dedicated page for the 2026 fair isn&rsquo;t posted yet; the link below goes to the main festival site.</p>
            <div class="event__links">
              <a class="event__link" href="https://miamibookfair.com/" target="_blank" rel="noopener">Miami Book Fair website →</a>
            </div>
          </article>

        </div>
      </div>

      <div class="events-group">
        <h2>Recent News &amp; Past Events</h2>
        <div class="events-list">

          <article class="event">
            <div class="event__head">
              <span class="event__type">Press</span>
              <span class="event__date">June 2026</span>
            </div>
            <h3 class="event__title"><em>White Sugar, Brown Sugar</em> Reader Reviews</h3>
            <p class="event__meta">Online — Goodreads &amp; Amazon</p>
            <p class="event__desc">IndieReader has gathered a fresh round of third-party reviews of <em>White Sugar, Brown Sugar</em>, posted on Goodreads and Amazon — five so far, with more on the way. One of them calls the book &ldquo;unputdownable.&rdquo;</p>
            <div class="event__links">
              <a class="event__link" href="white-sugar-brown-sugar-reviews.html">Read the reviews →</a>
            </div>
          </article>

          <article class="event">
            <div class="event__head">
              <span class="event__type">Award</span>
              <span class="event__date">May 2026</span>
            </div>
            <h3 class="event__title">First Place — IndieReader Discovery Awards (Inspirational Fiction)</h3>
            <p class="event__meta">IndieReader Discovery Awards (IRDA)</p>
            <p class="event__desc"><em>White Sugar, Brown Sugar</em> won first place in the Inspirational Fiction category of the 2026 IndieReader Discovery Awards.</p>
            <div class="event__links">
              <a class="event__link" href="https://indiereader.com/irda26-winners/" target="_blank" rel="noopener">IRDA 2026 winners →</a>
            </div>
            <figure class="event__award">
              <img src="images/irda-winner-badge.webp" alt="IndieReader Discovery Awards Winner seal" width="1441" height="1440" loading="lazy">
            </figure>
          </article>

          <article class="event">
            <div class="event__head">
              <span class="event__type">Review</span>
              <span class="event__date">Friday, May 1, 2026</span>
            </div>
            <h3 class="event__title">Kirkus Reviews Features <em>White Sugar, Brown Sugar</em></h3>
            <p class="event__meta">Kirkus Reviews — Volume XCIV, No. 9</p>
            <p class="event__desc">Kirkus placed <em>White Sugar, Brown Sugar</em> (reprinted in 2025) in its May 1, 2026 print magazine, and posted a review on its website with a &ldquo;Get It&rdquo; verdict.</p>
            <div class="event__links">
              <a class="event__link" href="https://www.kirkusreviews.com/book-reviews/michael-pyle/white-sugar-brown-sugar/" target="_blank" rel="noopener">Read the Kirkus review →</a>
              <a class="event__link" href="https://issuu.com/kirkus-reviews/docs/may_1_2026_volume_xciv_no._9" target="_blank" rel="noopener">View the magazine issue →</a>
            </div>
          </article>

          <article class="event">
            <div class="event__head">
              <span class="event__type">Presentation &amp; Book Signing</span>
            </div>
            <h3 class="event__title">Second <em>Giga Trouble</em> Presentation — 35 Bistro</h3>
            <p class="event__meta">35 Bistro, Daytona Beach, Florida</p>
            <p class="event__desc">The second public presentation of <em>Giga Trouble</em>, which was printed in September 2025.</p>
            <figure class="event__photo">
              <img src="images/35-bistro-giga-trouble.jpg" alt="Group photo at the Giga Trouble presentation and book signing at 35 Bistro, Daytona Beach" width="2048" height="1536" loading="lazy">
            </figure>
          </article>

          <article class="event">
            <div class="event__head">
              <span class="event__type">Presentation &amp; Book Signing</span>
              <span class="event__date">Saturday, November 22, 2025</span>
            </div>
            <h3 class="event__title">First <em>Giga Trouble</em> Presentation — Madeline&rsquo;s Wine Bar</h3>
            <p class="event__meta">Madeline&rsquo;s Wine Bar, Daytona Beach, Florida</p>
            <p class="event__desc">The first public presentation of <em>Giga Trouble</em> (printed September 2025), shared with friends and family. Two short videos from the evening are available: a brief clip showing the crowd, and an eight-minute discussion of the book.</p>
            <div class="event__links">
              <a class="event__link" href="{VIMEO_1}" target="_blank" rel="noopener">Watch the first video (Vimeo) →</a>
              <a class="event__link" href="{VIMEO_2}" target="_blank" rel="noopener">Watch the second video (Vimeo) →</a>
            </div>
          </article>

        </div>
      </div>
    </section>'''

    events_ld = '''[
    {
      "@context": "https://schema.org",
      "@type": "Event",
      "name": "Florida Vistas Book Club — A Talk on Giga Trouble",
      "startDate": "2026-08-20T14:00",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "location": {"@type": "Place", "name": "Halifax Historical Society Museum", "address": "252 S. Beach Street, Daytona Beach, FL 32114"},
      "performer": {"@type": "Person", "name": "Michael A. Pyle"},
      "about": {"@type": "Book", "name": "Giga Trouble"}
    },
    {
      "@context": "https://schema.org",
      "@type": "Event",
      "name": "Miami Book Fair — Street Fair Booth",
      "startDate": "2026-11-20",
      "endDate": "2026-11-22",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "location": {"@type": "Place", "name": "Miami Book Fair", "address": "Downtown Miami, Florida"},
      "performer": {"@type": "Person", "name": "Michael A. Pyle"},
      "url": "https://miamibookfair.com/"
    }
  ]'''

    pages["news.html"] = page(
        "news.html",
        "News & Events — Michael A. Pyle",
        "Upcoming appearances, recent press, and past events with author Michael A. Pyle — book talks, signings, the Miami Book Fair, Kirkus, and IndieReader Discovery Award news.",
        news_body,
        jsonld=events_ld,
        canonical_path="/news",
    )

    # =====================================================================
    # WHITE SUGAR, BROWN SUGAR — READER REVIEWS
    # =====================================================================
    WSBS_REVIEWS_AMZN = "https://a.co/d/07McNu4"

    alejandro_body = """A yacht club basin in Daytona Beach becomes the unlikely meeting point in WHITE SUGAR, BROWN SUGAR — Jude fishing from the docks beside the moored boats he'll never own, Roosevelt and his family casting cane poles from the public wall on the other side of the divide segregation drew through the town. Michael A. Pyle builds the novel's entire moral architecture from that single image: two boys positioned on opposite sides of a line neither chose, finding in each other something the line was designed to prevent. The friendship that develops carries the book through the damage, surviving arrests, an overdose witnessed at close range, and the particular cruelty of watching someone you love choose the same self-destruction that you did. What struck me reading this was how evenly Pyle distributes the damage. Jude's mother disappears into alcohol while his father retreats into a competent, distant kind of failure. Roosevelt's mother is lost to addiction in a different register entirely, shaped by poverty and the absence of any safety net. Both boys inherit a lot to avoid exactly what consumes them, and both break it, which gives the novel's central tragedy its inevitability without ever feeling manipulative.

The depiction of addiction itself is the book's most unflinching achievement. Pyle catalogues the self-justifications, the resentment, the shallow bliss, with a precision that reads like testimony. The drug scenes are visceral enough to unsettle, and the slower recovery of Jude's sobriety is rendered with the same patience the factor, more chemical descent into harder substances shows elsewhere. Roosevelt's hard-won sobriety emerges from Jude's in ways that feel earned— you buy the floor sooner, the other has to keep falling. The Florida setting, with its segregated signage and casual cruelty from those meant to enforce order, anchors the personal story in something larger without letting that larger story crowd out the friendship at its centre.

WHITE SUGAR, BROWN SUGAR earns its title on every register it's written in — racial, chemical, generational. Pyle has written something that hurts to read and refuses to let that hurt go to waste."""

    lizzy_body = """White Sugar, Brown Sugar is an emotional and heartbreaking tale of friendship, addiction, loss, and hope. The story begins in the 1960s when a young black boy and a young white boy strike up an unlikely friendship. Both boys come from families struggling with addictions; this story shows the generational cycle of crime and addictions, yet also shows hope of recovery and rehabilitation. This novel has powerful storytelling that is hauntingly realistic and accurate. It highlights the darkness people struggle with, which is often hushed up and ignored.

From the get-go, this book is immersive with flawed characters, dark themes, and inspirational messages. Race, social class, and differing opportunities play a part in this book, and the author portrays an accurate historical depiction of the 1960s with the racial divide layered into the writing. Yet despite this, we see how addictions don't see race, how anyone can fall victim to them. Further, throughout the book, the author does an amazing job of breaking everything down to a simple message. Everyone is human. Regardless of race, friendships last a lifetime can be made; people with seemingly better opportunities can still suffer, and we can all hit the same rock bottom.

I highly recommend this book. It is artfully written, so much so that it feels like it could be based on real people. It is compelling and emotional and, in part, uncomfortable, but it is a very human story that shows the darker parts of life and history."""

    antony_body = """White Sugar, Brown Sugar is a metaphorically befitting title, especially considering the book's coexistence narrative at a time when intolerance was a norm.

The main characters are two young boys about eleven years old: Roosevelt Harris is a black boy from a poor background, while David 'Jude' Armstrong is a white privileged boy. The two opposites meet while fishing at a streetside of a basin and they instantly hit off despite discouragement from their respective families. Nevertheless, the boys' friendship grows by leaps and bounds, shaped by their kindred spirits, peer pressure, substance dependence and addiction, relapses and legal problems, despite trying to stay away from the very vices affecting their mothers.

I liked how the adult Roosevelt became influential, including coaching kids in danger and giving back to the community through juvenile centers and rehab facilities. I also liked how he supported his longtime friend Jude's family when they needed a shoulder to lean on.

There are some strong words and sensitive scenes that, alongside the word choice, I nevertheless found realistic.

This insightful book lays bare the social, legal, physical, mental and financial costs of substance abuse."""

    raisa_body = """WHITE SUGAR, BROWN SUGAR is a powerful and often heartbreaking novel that explores friendship, addiction, and resilience against the backdrop of a deeply divided America. Set in segregated Florida, the story follows Jude and Roosevelt, two boys from vastly different backgrounds whose bond defies the racial boundaries imposed by society. As they grow older, both find themselves caught in cycles of substance abuse, family dysfunction, and self-destruction, creating a narrative that is as emotionally challenging as it is compelling. Michael A. Pyle does not shy away from the harsh realities of addiction, portraying its devastating impact on individuals and the people who care about them.

What makes the novel particularly effective is its refusal to reduce its characters to simple labels or stereotypes. Broken families, absent parents, and generational struggles shape both boys in different ways, yet their friendship remains a constant source of strength throughout the story. I found the depictions of addiction especially convincing because they capture not only the physical dependence but also the denial, guilt, and desperation that accompany it. The novel's historical setting also adds depth, illustrating how race and class influenced opportunities while showing that suffering and addiction recognize no boundaries.

At its core, this is a story about hope surviving in the darkest of circumstances. I was left with a deep appreciation for the novel's message that recovery, redemption, and human connection remain possible even after years of loss and hardship."""

    naomi_body = """White Sugar, Brown Sugar is an emotional and heartbreaking tale of friendship, addiction, loss, and hope. The story begins in the 1960s when a young black boy and a young white boy strike up an unlikely friendship. Both boys come from families struggling with addictions; this story shows the generational cycle of crime and addictions, yet also shows hope of recovery and rehabilitation. This novel has powerful storytelling that is hauntingly realistic and accurate. It highlights the darkness people struggle with, which is often hushed up and ignored.

From the get-go, this book is immersive with flawed characters, dark themes, and inspirational messages. Race, social class, and differing opportunities play a part in this book, and the author portrays an accurate historical depiction of the 1960s with the racial divide layered into the writing. Yet despite this, we see how addictions don't see race, how anyone can fall victim to them. Further, throughout the book, the author does an amazing job of breaking everything down to a simple message. Everyone is human. Regardless of race, friendships that last a lifetime can be made; people with seemingly better opportunities can still suffer, and we can all hit the same rock bottom.

I highly recommend this book. It is artfully written, so much so that it feels like it could be based on real people. It is compelling and emotional and, in part, uncomfortable, but it is a very human story that shows the darker parts of life and history."""

    megan_body = """White Sugar, Brown Sugar is one of those books that really pulled me in emotionally. I expected a story about friendship set during a time of racial division, but what I found was an honest, heartbreaking look at addiction, forgiveness, and the people who stand by us when life falls apart.

Jude and Roosevelt felt like real people. Their friendship begins in childhood and carries them through broken families, bad decisions, addiction, and unimaginable loss. I found myself rooting for both of them, even when they made frustrating choices, because the author does such a good job showing how addiction can slowly take over every part of someone's life.

The story never tried to sugarcoat recovery or make redemption seem easy. It shows the setbacks, the guilt, and the hard work it takes to rebuild a life, making the hopeful moments feel genuinely earned. The historical setting adds depth to the story, highlighting the realities of segregation while also reinforcing that pain, addiction, and the desire for a better life don't discriminate.

Even though this is an emotional read with some difficult moments, I closed the book feeling hopeful. At its core, this is a story about friendship, resilience, and the power of having someone who refuses to give up on you. If you enjoy character-driven historical fiction that isn't afraid to tackle difficult subjects while still leaving you with hope, I think this is well worth reading."""

    wsbs_reviews_body = f'''    <section class="container reviews-page">
      <div class="reviews-page__intro">
        <h1>White Sugar, Brown Sugar Reviews</h1>
        <p class="reviews-page__lead">Reader reviews gathered from Amazon and Goodreads, reproduced here as they appeared on each platform.</p>
        <a class="reviews-page__back" href="white-sugar-brown-sugar.html">&larr; Back to <em>White Sugar, Brown Sugar</em></a>
      </div>

      <div class="reviews-stack">

        <div>
          <span class="review-card__platform review-card__platform--amazon">Amazon.com</span>
          <article class="review-card review-amazon">
            <div class="review-amazon__grid">
              <div class="review-amazon__main">
                <h2 class="review-amazon__heading">Customer Review</h2>
                <p class="review-amazon__reviewer">Alejandro Soto</p>
                {_stars(5)}
                <h3 class="review-amazon__title">Two boys, one undertow, and many kinds of drowning</h3>
                <p class="review-amazon__meta">Reviewed in the United States on June 22, 2026 <span class="review-amazon__verified">Verified Purchase</span></p>
                <div class="review-amazon__body">
                  {_review_paras(alejandro_body)}
                </div>
                <p class="review-amazon__actions"><span>Helpful</span><span>Report</span></p>
              </div>
              {_amazon_sidebar("4.9 out of 5 stars", "47 global ratings", [("5 star", 87), ("4 star", 13), ("3 star", 0), ("2 star", 0), ("1 star", 0)], WSBS_REVIEWS_AMZN)}
            </div>
          </article>
        </div>

        <div>
          <span class="review-card__platform review-card__platform--amazon">Amazon.co.uk</span>
          <article class="review-card review-amazon">
            <div class="review-amazon__grid">
              <div class="review-amazon__main">
                <h2 class="review-amazon__heading">Customer Review</h2>
                <p class="review-amazon__reviewer">Lizzy</p>
                {_stars(5)}
                <h3 class="review-amazon__title">An immersive and powerful read.</h3>
                <p class="review-amazon__meta">Reviewed in the United Kingdom on 29 June 2026 <span class="review-amazon__verified">Verified Purchase</span></p>
                <div class="review-amazon__body">
                  {_review_paras(lizzy_body)}
                </div>
                <p class="review-amazon__actions"><span>Helpful</span><span>Report</span></p>
              </div>
              {_amazon_sidebar("4.8 out of 5", "28 global ratings", [("5 star", 85), ("4 star", 15), ("3 star", 0), ("2 star", 0), ("1 star", 0)], WSBS_REVIEWS_AMZN)}
            </div>
          </article>
        </div>

        <div>
          <span class="review-card__platform review-card__platform--goodreads">Goodreads</span>
          <article class="review-card review-goodreads review-goodreads--page">
            <div class="review-goodreads__header">
              <a href="#">Antony Wairiuko&rsquo;s Reviews</a> &rsaquo; White Sugar, Brown Sugar
            </div>
            <div class="review-goodreads__grid">
              <div class="review-goodreads__cover">
                <img src="images/white-sugar-cover.avif" alt="White Sugar, Brown Sugar book cover" width="120">
                <span class="review-goodreads__cover-btn">Want to Read</span>
              </div>
              <div class="review-goodreads__content">
                <h2 class="review-goodreads__book-title">White Sugar, Brown Sugar</h2>
                <p class="review-goodreads__book-author">by Michael A. Pyle</p>
                <p class="review-goodreads__byline">Antony Wairiuko&rsquo;s review</p>
                <div class="review-goodreads__top">
                  {_stars(5, "goodreads")}
                  <span class="review-goodreads__date">Jun 13, 2026</span>
                </div>
                <h3 class="review-goodreads__title">Cautionary</h3>
                <div class="review-goodreads__body">
                  {_review_paras(antony_body)}
                </div>
              </div>
            </div>
          </article>
        </div>

        <div>
          <span class="review-card__platform review-card__platform--goodreads">Goodreads</span>
          <article class="review-card review-goodreads review-goodreads--list">
            <div class="review-goodreads__grid">
              <div class="review-goodreads__cover">
                <img src="images/white-sugar-cover.avif" alt="White Sugar, Brown Sugar book cover" width="120">
                <span class="review-goodreads__cover-btn">Want to Read</span>
              </div>
              <div class="review-goodreads__profile">
                <div class="review-goodreads__avatar" aria-hidden="true">&#128214;</div>
                <div>
                  <p class="review-goodreads__name">Raisa Mbalule</p>
                  <p class="review-goodreads__stats">113 reviews &middot; 11 followers</p>
                  <span class="review-goodreads__follow">Follow</span>
                </div>
              </div>
              <div class="review-goodreads__content">
                <div class="review-goodreads__top">
                  {_stars(5, "goodreads")}
                  <span class="review-goodreads__date">June 9, 2026</span>
                </div>
                <h3 class="review-goodreads__title">A Powerful Story of Friendship, Addiction, and Redemption</h3>
                <div class="review-goodreads__body">
                  {_review_paras(raisa_body)}
                </div>
              </div>
            </div>
          </article>
        </div>

        <div>
          <span class="review-card__platform review-card__platform--goodreads">Goodreads</span>
          <article class="review-card review-goodreads review-goodreads--list">
            <div class="review-goodreads__grid">
              <div class="review-goodreads__cover">
                <img src="images/white-sugar-cover.avif" alt="White Sugar, Brown Sugar book cover" width="120">
                <span class="review-goodreads__cover-btn">Read</span>
              </div>
              <div class="review-goodreads__profile">
                <div class="review-goodreads__avatar" aria-hidden="true">&#128100;</div>
                <div>
                  <p class="review-goodreads__name">Naomi</p>
                  <p class="review-goodreads__stats">133 reviews &middot; 9 followers</p>
                  <span class="review-goodreads__follow">Follow</span>
                </div>
              </div>
              <div class="review-goodreads__content">
                <div class="review-goodreads__top">
                  {_stars(5, "goodreads")}
                  <span class="review-goodreads__date">June 29, 2026</span>
                </div>
                <div class="review-goodreads__body">
                  {_review_paras(naomi_body)}
                </div>
              </div>
            </div>
          </article>
        </div>

        <div>
          <span class="review-card__platform review-card__platform--goodreads">Goodreads</span>
          <article class="review-card review-goodreads review-goodreads--list">
            <div class="review-goodreads__grid">
              <div class="review-goodreads__cover">
                <img src="images/white-sugar-cover.avif" alt="White Sugar, Brown Sugar book cover" width="120">
                <span class="review-goodreads__cover-btn">Want to Read</span>
              </div>
              <div class="review-goodreads__profile">
                <div class="review-goodreads__avatar" aria-hidden="true">&#128214;</div>
                <div>
                  <p class="review-goodreads__name">Megan</p>
                  <p class="review-goodreads__stats">128 reviews &middot; 5 followers</p>
                  <span class="review-goodreads__follow">Follow</span>
                </div>
              </div>
              <div class="review-goodreads__content">
                <div class="review-goodreads__top">
                  {_stars(5, "goodreads")}
                  <span class="review-goodreads__date">June 29, 2026</span>
                </div>
                <div class="review-goodreads__body">
                  {_review_paras(megan_body)}
                </div>
              </div>
            </div>
          </article>
        </div>

      </div>
    </section>'''

    wsbs_reviews_ld = '''{
    "@context": "https://schema.org",
    "@type": "Book",
    "name": "White Sugar, Brown Sugar",
    "author": {"@type": "Person", "name": "Michael A. Pyle"},
    "review": [
      {"@type": "Review", "author": {"@type": "Person", "name": "Alejandro Soto"}, "reviewBody": "Two boys, one undertow, and many kinds of drowning", "reviewRating": {"@type": "Rating", "ratingValue": 5}},
      {"@type": "Review", "author": {"@type": "Person", "name": "Lizzy"}, "reviewBody": "An immersive and powerful read.", "reviewRating": {"@type": "Rating", "ratingValue": 5}},
      {"@type": "Review", "author": {"@type": "Person", "name": "Antony Wairiuko"}, "reviewBody": "Cautionary", "reviewRating": {"@type": "Rating", "ratingValue": 5}},
      {"@type": "Review", "author": {"@type": "Person", "name": "Raisa Mbalule"}, "reviewBody": "A Powerful Story of Friendship, Addiction, and Redemption", "reviewRating": {"@type": "Rating", "ratingValue": 5}},
      {"@type": "Review", "author": {"@type": "Person", "name": "Naomi"}, "reviewRating": {"@type": "Rating", "ratingValue": 5}},
      {"@type": "Review", "author": {"@type": "Person", "name": "Megan"}, "reviewRating": {"@type": "Rating", "ratingValue": 5}}
    ]
  }'''

    pages["white-sugar-brown-sugar-reviews.html"] = page(
        "white-sugar-brown-sugar-reviews.html",
        "White Sugar, Brown Sugar Reviews — Michael A. Pyle",
        "Reader reviews of White Sugar, Brown Sugar by Michael A. Pyle — reproduced from Amazon and Goodreads.",
        wsbs_reviews_body,
        jsonld=wsbs_reviews_ld,
        canonical_path="/white-sugar-brown-sugar-reviews",
    )

    # =====================================================================
    # 404
    # =====================================================================
    notfound_body = '''    <section class="container notfound">
      <img src="images/clumsy.png" alt="">
      <h1>404</h1>
      <p>We couldn&rsquo;t find that page.</p>
      <a class="btn btn--grad" href="index.html">Back to home</a>
    </section>'''
    pages["404.html"] = page(
        "404.html",
        "Page Not Found — Michael A. Pyle",
        "The page you were looking for could not be found.",
        notfound_body,
        canonical_path="/404",
    )

    return pages
