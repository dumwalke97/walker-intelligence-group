"""Generate the inner pages (services, about, contact) and sitemap.xml.

Edit the content below, then run from the repo root:
    python3 tools/build_pages.py
Commit the generated files. Netlify serves them as-is (no build step).
"""
import html
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://walkerig.com"
PHONE_DISPLAY = "317-531-7681"
PHONE_TEL = "+13175317681"
EMAIL = "dustin@walkerig.com"
TODAY = date.today().isoformat()
FONTS = ("https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;"
         "1,300;1,400&family=DM+Mono:wght@300;400&display=swap")
CONSULT = "Book a free 30-minute consult"
GA_ID = "G-RJ7RK3Y0N4"  # Google Analytics 4, Walker Intelligence Group property
ANALYTICS = """  <!-- Google Analytics 4 + lead tracking -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA_ID}');
    // A form submission returns here with ?sent=1 (read before page scripts strip it)
    if (new URLSearchParams(location.search).get('sent') === '1') {{
      gtag('event', 'generate_lead', {{ form_location: location.pathname }});
    }}
    document.addEventListener('click', function (e) {{
      var a = e.target.closest && e.target.closest('a[href]');
      if (!a) return;
      var href = a.getAttribute('href');
      if (href.indexOf('tel:') === 0) gtag('event', 'phone_click', {{ link_text: a.textContent.trim() }});
      else if (href.indexOf('mailto:') === 0) gtag('event', 'email_click', {{ link_text: a.textContent.trim() }});
      else if (href === '/contact/') gtag('event', 'consult_click', {{ link_text: a.textContent.trim() }});
    }});
  </script>
""".format(GA_ID=GA_ID)

# ── SERVICE CONTENT ──────────────────────────────────────────────────────────
SERVICES = [
    {
        "slug": "ai-integration",
        "name": "AI Integration",
        "title": "AI Integration Services in Indianapolis | Walker IG",
        "desc": "We find where AI saves your team time, then build and run the tools: document review, data extraction, summaries, and private AI assistants. Indianapolis.",
        "h1": "AI integration that does <em>real work</em> for your team.",
        "lede": "We find the places where AI actually saves time in your business, then build the tools, connect them to your systems, and keep them running. No demos that go nowhere.",
        "card": "Put AI to work on documents, email, and repetitive knowledge work.",
        "problem": [
            "Most businesses have tried ChatGPT. Very few have turned it into something the whole team uses every day. The gap is not the AI. It is the work of fitting it into your real processes, your data, and your security rules.",
            "That is the part we do. We look at how work moves through your business, pick the tasks where AI gives a clear return, and build tools your people can use without training manuals.",
        ],
        "offer": [
            ("Document review and extraction", "Pull key details out of contracts, invoices, applications, and forms, and drop them into the systems you already use."),
            ("Summaries and drafting", "Turn long emails, call notes, and reports into short summaries and first drafts your team can approve and send."),
            ("Internal AI assistants", "A private assistant that answers questions from your own policies, manuals, and past work, so people stop digging through folders."),
            ("AI inside your existing tools", "Add AI steps to the software you already pay for, instead of adding another app to log into."),
        ],
        "examples": [
            "An intake process where AI reads incoming PDFs and fills in your CRM or spreadsheet",
            "A quoting assistant that drafts proposals from your past jobs and price list",
            "An inbox helper that sorts, tags, and drafts replies to common customer questions",
            "A searchable knowledge base built from your SOPs and training documents",
        ],
        "faq": [
            ("Is our data safe if we use AI?", "Yes, if it is set up correctly. We choose tools and settings based on how sensitive your data is, keep your information out of public model training, and limit who can access what. Your data stays yours."),
            ("Do we need to hire someone technical to run it?", "No. We build, host, and maintain what we deliver. Your team just uses it."),
            ("How long does an AI project take?", "Most first projects take a few weeks from kickoff to something your team is using. We start small, prove the value, and then expand."),
            ("What if AI is not a good fit for us?", "Then we will tell you. Sometimes simple automation solves the problem better and for less money."),
        ],
        "related": ["workflow-automation", "ai-advisory", "websites-custom-apps"],
    },
    {
        "slug": "workflow-automation",
        "name": "Workflow Automation",
        "title": "Workflow Automation for Indianapolis Businesses | Walker IG",
        "desc": "Stop paying people to do what software can handle. We automate data entry, reporting, follow-ups, and handoffs between your tools. Indianapolis based.",
        "h1": "Workflow automation that gives your team <em>hours back</em>.",
        "lede": "Data entry, copy and paste between systems, chasing approvals, building the same report every week. We automate the repetitive work so your people can focus on the work that needs them.",
        "card": "Automate data entry, reporting, routing, and follow-ups.",
        "problem": [
            "Every business has a few processes held together by spreadsheets, email threads, and one person who knows how it all works. They are slow, error-prone, and they break when that person is out.",
            "We map those processes, find the steps a computer should be doing, and build automations that run on their own. You get faster turnaround, fewer mistakes, and a process that does not depend on memory.",
        ],
        "offer": [
            ("Data entry and syncing", "Move information between your CRM, accounting, scheduling, and spreadsheets automatically, so it is entered once and correct everywhere."),
            ("Routing, notifications, and follow-ups", "New lead, new order, overdue invoice. The right person gets notified and the follow-up goes out on time, every time."),
            ("Automated reporting", "Reports and dashboards that build themselves on a schedule, instead of someone assembling them by hand."),
            ("Paper and email to digital", "Replace paper forms and email chains with online forms and tracked workflows."),
        ],
        "examples": [
            "Web form leads that land in your CRM, get assigned, and get a same-day reply",
            "Invoices and receipts that are captured, categorized, and sent to accounting",
            "A weekly sales or operations report delivered to your inbox every Monday",
            "Onboarding checklists that kick off automatically when a new client signs",
        ],
        "faq": [
            ("What tools can you automate?", "Most modern business software can be connected, including Microsoft 365, Google Workspace, QuickBooks, popular CRMs, and anything with an API or email. If it has no connection point, we will find a workaround or tell you upfront."),
            ("Will automation replace my staff?", "It replaces tasks, not people. The goal is to free your team from busywork so they can spend time on customers and growth."),
            ("What happens if an automation breaks?", "We monitor what we build and fix issues as part of ongoing support. You are not left with a black box."),
            ("Where do we start?", "With a free consult. We will talk through your most time-consuming processes and point out the ones with the fastest payback."),
        ],
        "related": ["ai-integration", "cost-optimization", "websites-custom-apps"],
    },
    {
        "slug": "websites-custom-apps",
        "name": "Websites & Custom Apps",
        "title": "Websites & Custom Apps in Indianapolis | Walker IG",
        "desc": "Fast websites that generate leads, plus client portals, online forms, dashboards, and custom tools built around your process. Built and hosted in Indianapolis.",
        "h1": "Websites and custom apps that <em>work for your business</em>.",
        "lede": "A website that brings in leads, and custom tools built around the way you actually work. We design it, build it, host it, and keep it updated.",
        "card": "Lead-generating websites, portals, dashboards, and custom tools.",
        "problem": [
            "A lot of small business websites look fine but do nothing. They load slowly, do not show up in search, and make it hard for a customer to reach you. Off-the-shelf software has the same problem. It almost fits, so your team works around it every day.",
            "We build websites that are fast, easy to find on Google, and designed to turn visitors into calls and form submissions. When software does not fit, we build the tool you actually need.",
        ],
        "offer": [
            ("Lead-generating websites", "Clean, fast sites with clear calls to action, search engine basics done right, and contact forms that reach you."),
            ("Client portals and online forms", "Give customers a place to submit requests, upload files, sign documents, or check status without calling you."),
            ("Dashboards", "See the numbers that matter in one place, pulled live from the systems you already use."),
            ("Custom internal tools", "Small, focused apps built around your exact process, replacing the spreadsheet that has grown out of control."),
        ],
        "examples": [
            "A new website for a service business with online quote requests",
            "A customer portal for uploading documents and tracking job status",
            "An owner dashboard with sales, cash, and pipeline in one view",
            "A scheduling or inventory tool that replaces a shared spreadsheet",
        ],
        "faq": [
            ("Do you handle hosting and updates?", "Yes. We host what we build and handle updates, security, and backups, so you do not have to manage another vendor."),
            ("Can you redo our existing website?", "Yes. We can rebuild it, improve it, or move it to faster and cheaper hosting while keeping what already works."),
            ("Will my site show up on Google?", "We build every site with search basics in place: fast load times, clean structure, local business details, and pages for the services you offer. Ranking also takes time and content, and we can help with that too."),
            ("Can a custom app connect to our other software?", "Usually, yes. We design custom tools to connect to the systems you already rely on."),
        ],
        "related": ["workflow-automation", "ai-integration", "technology-infrastructure"],
    },
    {
        "slug": "ai-advisory",
        "name": "AI Advisory",
        "title": "AI Strategy & Advisory in Indianapolis | Walker IG",
        "desc": "Cut through the AI hype. Get a plain-English assessment, the highest-ROI AI opportunities, and a clear plan. Then we help you build it. Indianapolis.",
        "h1": "AI strategy in <em>plain English</em>.",
        "lede": "Cut through the hype and get a clear plan that makes sense for your business. We assess where you are, show you where AI pays off, and then help you build it.",
        "card": "A clear, practical AI plan for your leadership team.",
        "problem": [
            "Leadership teams are being told they need an AI strategy, usually by people selling something. It is hard to know what is real, what is safe, and what is worth the money.",
            "We give you an honest outside view. We look at your operations, your data, and your goals, and tell you where AI will make a measurable difference and where it will not. Then, unlike most advisors, we can build what we recommend.",
        ],
        "offer": [
            ("Technology and readiness assessment", "A plain-English review of your current tools, data, and processes, and how ready they are for AI."),
            ("Opportunity mapping", "A short list of AI and automation opportunities ranked by return, cost, and risk."),
            ("Tool and vendor guidance", "Recommendations based on your data sensitivity and budget, so you do not overpay or put data at risk."),
            ("AI policy and guardrails", "Simple rules for how your team can use AI safely, so adoption does not create new risk."),
            ("Ongoing advisory", "A trusted partner to check in with as the technology changes, without a full-time hire."),
        ],
        "examples": [
            "A leadership workshop that ends with a prioritized AI roadmap",
            "A review of AI tools your team is already using, with a safe-use policy",
            "A second opinion on a vendor proposal before you sign",
            "Quarterly check-ins to adjust the plan as tools and costs change",
        ],
        "faq": [
            ("What do we get at the end?", "A written roadmap with prioritized opportunities, expected impact, rough costs, and clear next steps. Not a slide deck full of buzzwords."),
            ("Do you only advise, or do you build too?", "Both. We are an AI consulting and implementation firm. You can take the plan and run with it, or have us build it."),
            ("Are you tied to any AI vendor?", "No. We recommend what fits your needs and data, not what pays us a commission."),
            ("Is this only for large companies?", "No. Most of our work is with small and mid-sized organizations that need practical answers, not an enterprise program."),
        ],
        "related": ["ai-integration", "cost-optimization", "technology-infrastructure"],
    },
    {
        "slug": "technology-infrastructure",
        "name": "Technology Infrastructure",
        "title": "IT Infrastructure & Cloud Setup, Indianapolis | Walker IG",
        "desc": "Cloud setup, tested backups, security assessments, and technology audits for Indianapolis businesses. Know what you have, what is at risk, and fix it.",
        "h1": "A secure foundation your business <em>can rely on</em>.",
        "lede": "Cloud setup, backups, security, and a clear picture of what you have. We organize your technology so it is safe, reliable, and ready to grow, including for AI.",
        "card": "Cloud setup, backups, security, and technology audits.",
        "problem": [
            "Many businesses run on technology that grew one decision at a time. Shared passwords, files in three places, no tested backups, and nobody sure what is still being paid for. It works until it does not.",
            "We take inventory, close the obvious risks, and set up a clean, documented foundation. It is also the step that makes AI and automation safe to add later.",
        ],
        "offer": [
            ("Technology audit", "A full inventory of your systems, accounts, devices, and subscriptions, with a plain list of what is at risk."),
            ("Cloud setup and migration", "Move files and email to well-organized cloud services with the right permissions."),
            ("Backups and recovery", "Automatic backups that are actually tested, so a lost laptop or ransomware is an inconvenience and not a disaster."),
            ("Security assessment and hardening", "Multi-factor login, access controls, and basic protections that stop the most common attacks."),
            ("Scalable systems", "Infrastructure that grows with you, without big upfront hardware costs."),
        ],
        "examples": [
            "Moving a team off a local file server and onto organized cloud storage",
            "Setting up multi-factor login and a password manager for the whole team",
            "Tested backups for key systems with a simple recovery plan",
            "A technology audit before a merger, new hire wave, or AI project",
        ],
        "faq": [
            ("Are you a managed IT provider?", "We focus on getting your foundation right and supporting the systems we set up. For day-to-day help desk needs, we can work alongside your existing IT provider."),
            ("How do we know if we are at risk?", "Start with an audit. Most businesses find a few high-risk gaps that are quick and inexpensive to fix."),
            ("Do we need this before doing AI?", "Often, yes. AI is only as safe as the data and access rules behind it. A solid foundation makes AI projects faster and safer."),
            ("Can you work with Microsoft 365 or Google Workspace?", "Yes. We work with both and help you get far more out of the one you already pay for."),
        ],
        "related": ["cost-optimization", "ai-advisory", "workflow-automation"],
    },
    {
        "slug": "cost-optimization",
        "name": "Cost Optimization",
        "title": "Technology Cost Optimization in Indianapolis | Walker IG",
        "desc": "Cut technology waste. We audit subscriptions, remove redundant tools, right-size cloud spend, and replace manual work with automation. Indianapolis.",
        "h1": "Spend less on technology. <em>Get more from it.</em>",
        "lede": "We find the software you are paying for and not using, the overlapping tools, and the manual work that automation can replace. Then we help you cut it.",
        "card": "Cut software waste, right-size cloud spend, automate manual work.",
        "problem": [
            "Software costs creep up quietly. A new subscription for every team, licenses for people who left, two tools that do the same job, and cloud bills nobody reviews.",
            "We review what you pay for, what you actually use, and where people are doing work by hand that software could do. You get a clear list of savings and help making the changes.",
        ],
        "offer": [
            ("Subscription audit", "A full list of your software and services, who uses them, and what each one really costs."),
            ("Tool consolidation", "Replace overlapping tools with fewer, better ones, and cancel what is not pulling its weight."),
            ("Cloud right-sizing", "Match your cloud and hosting spend to what you actually need."),
            ("Automation for savings", "Replace labor-intensive manual processes with automation that pays for itself."),
            ("ROI-ranked investment plan", "When you do spend, put money into the AI and technology investments with the fastest return."),
        ],
        "examples": [
            "Finding unused licenses and duplicate tools across departments",
            "Moving a website or app to hosting that costs a fraction of the old plan",
            "Replacing an expensive niche tool with features you already own",
            "Automating a manual process to free up hours every week",
        ],
        "faq": [
            ("How much can we save?", "It depends on your setup, so we will not promise a number upfront. The audit gives you a specific list of savings before you commit to any changes."),
            ("Will cutting tools disrupt our team?", "We plan changes carefully, move data for you, and help your team switch over so work keeps moving."),
            ("Is this a one-time project?", "The audit is one-time. Many clients have us review costs once or twice a year as their needs change."),
            ("Can savings fund an AI project?", "Often, yes. Cutting waste is a common way to pay for the first automation or AI project without a new budget line."),
        ],
        "related": ["technology-infrastructure", "workflow-automation", "ai-advisory"],
    },
]
BY_SLUG = {s["slug"]: s for s in SERVICES}

PROCESS = [
    ("01", "Discovery & Strategy", "We learn how your business runs, where time and money are going, and what success looks like. You get a short, prioritized plan."),
    ("02", "Assessment & Design", "We review the tools and data involved and design a solution that fits your systems, budget, and security needs."),
    ("03", "Build, Deploy & Support", "We build it, launch it, host it, and keep it running. You get a working result, not a stack of recommendations."),
]


# ── SHARED PIECES ────────────────────────────────────────────────────────────
def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    return s.replace("<em>", "").replace("</em>", "")


def head(title, desc, path, schema):
    url = SITE + path
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
{ANALYTICS}  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}" />
  <link rel="canonical" href="{url}" />
  <meta name="theme-color" content="#0b0c0e" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Walker Intelligence Group" />
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(desc)}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{SITE}/og-image.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="apple-touch-icon" href="/wig-logo-144.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{FONTS}" rel="stylesheet" />
  <link href="/assets/site.css" rel="stylesheet" />
  <script type="application/ld+json">
{json.dumps(schema, indent=2, ensure_ascii=False)}
  </script>
</head>
<body>
"""


def header(current=""):
    def cur(p):
        return ' aria-current="page"' if p == current else ""
    svc_links = "\n".join(
        f'        <a href="/{s["slug"]}/">{esc(s["name"])}</a>' for s in SERVICES)
    return f"""<header class="site-header">
  <a class="brand" href="/" aria-label="Walker Intelligence Group home">
    <span class="brand-top">AI Consulting &amp; Implementation</span>
    <span class="brand-main">Walker <span>Intelligence Group</span></span>
  </a>
  <nav class="site-nav" aria-label="Main">
    <a href="/#services"{cur('services')}>Services</a>
    <a href="/about/"{cur('about')}>About</a>
    <a href="/contact/"{cur('contact')}>Contact</a>
    <a class="btn" href="/contact/">Free consult</a>
  </nav>
  <details class="menu">
    <summary>Menu</summary>
    <div class="menu-panel">
      <span class="menu-label">Services</span>
{svc_links}
      <span class="menu-label">Company</span>
      <a href="/about/">About</a>
      <a href="/contact/">Contact</a>
      <a href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </div>
  </details>
</header>
"""


def footer():
    svc = "\n".join(f'          <li><a href="/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in SERVICES)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-cols">
      <div>
        <h4>Walker Intelligence Group</h4>
        <ul>
          <li>AI consulting &amp; implementation</li>
          <li>Indianapolis, IN</li>
          <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
{svc}
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/about/">About</a></li>
          <li><a href="/contact/">Contact</a></li>
          <li><a href="/privacy/">Privacy Policy</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-base">&copy; 2026 Walker Intelligence Group &middot; Indianapolis, Indiana</div>
  </div>
</footer>
</body>
</html>
"""


def cta_band(heading="Let's talk about <em>your</em> business.",
             text="Tell us what is slowing your team down. In a free 30-minute call, we will point out where AI and automation can help and what it would take. No pressure and no jargon."):
    return f"""  <section class="cta-band">
    <div class="wrap">
      <h2>{heading}</h2>
      <p class="lede">{text}</p>
      <div class="cta-row">
        <a class="btn" href="/contact/">{CONSULT}</a>
        <a class="btn btn-ghost" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
      </div>
    </div>
  </section>
"""


def breadcrumb_schema(items):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p}
            for i, (n, p) in enumerate(items)
        ],
    }


PROVIDER = {"@id": f"{SITE}/#business"}
FOUNDER = {
    "@type": "Person",
    "@id": f"{SITE}/#founder",
    "name": "Dustin Walker",
    "jobTitle": "Founder",
    "description": "Technology leader with more than 25 years of experience in technology implementation, administration, and leadership.",
    "alumniOf": {"@type": "CollegeOrUniversity", "name": "Purdue University"},
    "knowsAbout": ["Artificial intelligence", "Technology implementation", "Systems administration", "IT leadership", "Workflow automation"],
    "worksFor": PROVIDER,
    "url": f"{SITE}/about/",
}


def write(path, content):
    out = ROOT / path.strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content)
    print("wrote", out.relative_to(ROOT))


# ── PAGES ────────────────────────────────────────────────────────────────────
def service_page(s):
    path = f"/{s['slug']}/"
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "@id": f"{SITE}{path}#service",
                "name": s["name"],
                "serviceType": s["name"],
                "description": s["desc"],
                "url": SITE + path,
                "provider": PROVIDER,
                "areaServed": [{"@type": "City", "name": "Indianapolis"}, {"@type": "State", "name": "Indiana"}],
            },
            breadcrumb_schema([("Home", "/"), ("Services", "/#services"), (s["name"], path)]),
        ],
    }
    offer = "\n".join(
        f'        <div class="card"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in s["offer"])
    examples = "\n".join(f"        <li>{esc(e)}</li>" for e in s["examples"])
    problem = "\n".join(f"        <p>{esc(p)}</p>" for p in s["problem"])
    process = "\n".join(
        f'        <div class="card"><span class="num">{n}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
        for n, t, d in PROCESS)
    faq = "\n".join(
        f"        <details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in s["faq"])
    related = "\n".join(
        f'        <a class="card" href="/{r}/"><h3>{esc(BY_SLUG[r]["name"])}</h3>'
        f'<p>{esc(BY_SLUG[r]["card"])}</p><span class="more">Learn more &rarr;</span></a>'
        for r in s["related"])
    body = f"""{header('services')}
<main>
  <div class="wrap crumbs"><a href="/">Home</a> / <a href="/#services">Services</a> / {esc(s['name'])}</div>

  <section class="hero">
    <div class="wrap">
      <span class="eyebrow">{esc(s['name'])} &middot; Indianapolis</span>
      <h1>{s['h1']}</h1>
      <p class="lede">{esc(s['lede'])}</p>
      <div class="cta-row">
        <a class="btn" href="/contact/">{CONSULT}</a>
        <span class="cta-note">Or call {PHONE_DISPLAY}</span>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap prose">
      <h2>The problem we solve</h2>
{problem}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>What we <em>build</em> for you</h2>
      <div class="grid">
{offer}
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Common projects</h2>
      <ul class="checks">
{examples}
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>How we work</h2>
      <p class="lede">We plan it with you, build it, and keep it running. One partner from first conversation to working solution.</p>
      <div class="grid">
{process}
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Questions we hear</h2>
      <div class="faq">
{faq}
      </div>
    </div>
  </section>

{cta_band()}
  <section>
    <div class="wrap">
      <h2>Related services</h2>
      <div class="grid">
{related}
      </div>
    </div>
  </section>
</main>
"""
    write(path, head(s["title"], s["desc"], path, schema) + body + footer())


def about_page():
    path = "/about/"
    desc = ("Indianapolis AI consulting and implementation firm founded by Dustin Walker, a Purdue-trained "
            "technology leader with 25+ years of experience.")
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "AboutPage", "@id": SITE + path, "url": SITE + path,
             "name": "About Walker Intelligence Group", "about": PROVIDER,
             "mainEntity": {"@id": f"{SITE}/#founder"}},
            FOUNDER,
            breadcrumb_schema([("Home", "/"), ("About", path)]),
        ],
    }
    body = f"""{header('about')}
<main>
  <div class="wrap crumbs"><a href="/">Home</a> / About</div>

  <section class="hero">
    <div class="wrap">
      <span class="eyebrow">About &middot; Indianapolis</span>
      <h1>A partner who plans it <em>and builds it</em>.</h1>
      <p class="lede">Walker Intelligence Group is an AI consulting and implementation firm based in Indianapolis. We help organizations figure out where AI and modern technology fit, then we build, deploy, and support the solution.</p>
    </div>
  </section>

  <section>
    <div class="wrap prose">
      <h2>Meet the founder</h2>
      <p>Walker Intelligence Group was founded in 2026 by Dustin Walker, a technology leader with more than 25 years of experience implementing, administering, and leading technology for organizations. Over that career he has worked hands-on across many roles and many generations of technology, from running the systems businesses depend on every day to leading the teams and projects that put new ones in place.</p>
      <p>Dustin holds a degree in Computer and Information Technology from Purdue University. That combination of formal training and decades of real-world delivery is why WIG can both advise and build. He has seen plenty of technology waves come and go, and he knows the difference between hype and tools that actually change how a business runs.</p>
      <p>He started Walker Intelligence Group because he is passionate about helping small and medium-sized businesses see what is possible with AI and technology innovation. Large companies have whole departments for this. Most growing businesses do not. WIG gives them a senior, hands-on partner who explains things in plain English and then gets the work done.</p>
      <ul class="checks">
        <li>25+ years in technology implementation, administration, and leadership</li>
        <li>Degree in Computer and Information Technology, Purdue University</li>
        <li>Based in Indianapolis, working with small and mid-sized businesses</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>What we <em>believe</em></h2>
      <div class="grid">
        <div class="card"><h3>Plain English, no hype</h3><p>You should understand what you are buying and why. We explain things clearly and tell you when AI is not the answer.</p></div>
        <div class="card"><h3>Build, don't just advise</h3><p>A plan only matters if it gets done. We build, launch, host, and support what we recommend.</p></div>
        <div class="card"><h3>Your data stays yours</h3><p>We choose tools and settings based on how sensitive your information is, and we keep it out of public AI training.</p></div>
        <div class="card"><h3>Start small, prove value</h3><p>We begin with a focused project that pays off quickly, then grow from there.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>How we work</h2>
      <div class="grid">
""" + "\n".join(
        f'        <div class="card"><span class="num">{n}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
        for n, t, d in PROCESS) + f"""
      </div>
    </div>
  </section>

{cta_band()}</main>
"""
    write(path, head("About Walker Intelligence Group | Indianapolis AI Firm",
                     desc, path, schema) + body + footer())


def contact_page():
    path = "/contact/"
    desc = ("Book a free 30-minute consult with an Indianapolis AI consulting and implementation firm. "
            f"Call {PHONE_DISPLAY} or send a message. We reply within one business day.")
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "ContactPage", "@id": SITE + path, "url": SITE + path,
             "name": "Contact Walker Intelligence Group", "about": PROVIDER},
            breadcrumb_schema([("Home", "/"), ("Contact", path)]),
        ],
    }
    options = "\n".join(f'              <option>{esc(s["name"])}</option>' for s in SERVICES)
    body = f"""{header('contact')}
<main>
  <div class="wrap crumbs"><a href="/">Home</a> / Contact</div>

  <section class="hero">
    <div class="wrap contact-grid">
      <div>
        <span class="eyebrow">Free consult &middot; Indianapolis</span>
        <h1>Let's find where AI <em>pays off</em> for you.</h1>
        <p class="lede">Book a free 30-minute consult. Tell us what is slowing your team down and we will share practical ideas, whether or not you hire us.</p>
        <div class="contact-lines">
          <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
          <span class="cta-note">Indianapolis, Indiana &middot; serving businesses across Central Indiana and remotely</span>
        </div>
        <h3>What happens next</h3>
        <ul class="checks">
          <li>We reply within one business day to set up a time.</li>
          <li>On the call, we learn about your business and the problems you want solved.</li>
          <li>You leave with clear next steps and, if it makes sense, a simple proposal.</li>
        </ul>
      </div>
      <div>
        <form class="form" id="contactForm" action="https://formsubmit.co/{EMAIL}" method="POST">
          <input type="hidden" name="_subject" value="Free consult request from walkerig.com" />
          <input type="hidden" name="_next" value="{SITE}/contact/?sent=1" />
          <input type="hidden" name="_captcha" value="false" />
          <input type="hidden" name="_template" value="table" />
          <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true" />
          <div class="field">
            <label for="f-name">Name</label>
            <input type="text" id="f-name" name="name" autocomplete="name" required />
          </div>
          <div class="field">
            <label for="f-email">Email</label>
            <input type="email" id="f-email" name="email" autocomplete="email" required />
          </div>
          <div class="field">
            <label for="f-phone">Phone (optional)</label>
            <input type="tel" id="f-phone" name="phone" autocomplete="tel" />
          </div>
          <div class="field">
            <label for="f-company">Company (optional)</label>
            <input type="text" id="f-company" name="company" autocomplete="organization" />
          </div>
          <div class="field">
            <label for="f-interest">What are you interested in?</label>
            <select id="f-interest" name="interest">
              <option>Not sure yet</option>
{options}
            </select>
          </div>
          <div class="field">
            <label for="f-message">What would you like help with?</label>
            <textarea id="f-message" name="message" required></textarea>
          </div>
          <button class="btn" type="submit">Request my free consult</button>
        </form>
      </div>
    </div>
  </section>
</main>
<script>
  if (new URLSearchParams(location.search).get('sent') === '1') {{
    history.replaceState(null, '', location.pathname);
    document.getElementById('contactForm').outerHTML =
      '<p class="form-done">Thanks. Your message is on its way and we will be in touch within one business day.</p>';
  }}
</script>
"""
    write(path, head("Free AI Consult in Indianapolis | Contact Walker IG",
                     desc, path, schema) + body + footer())


def privacy_page():
    path = "/privacy/"
    desc = "How Walker Intelligence Group collects, uses, and protects information on walkerig.com, including contact forms and Google Analytics."
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebPage", "@id": SITE + path, "url": SITE + path,
             "name": "Privacy Policy", "about": PROVIDER},
            breadcrumb_schema([("Home", "/"), ("Privacy Policy", path)]),
        ],
    }
    body = f"""{header()}
<main>
  <div class="wrap crumbs"><a href="/">Home</a> / Privacy Policy</div>

  <section class="hero">
    <div class="wrap prose">
      <span class="eyebrow">Effective October 14, 2026</span>
      <h1>Privacy policy</h1>
      <p>Walker Intelligence Group ("we", "us") runs walkerig.com. This page explains what information we collect on this website, how we use it, and the choices you have. We keep it short and in plain English.</p>
    </div>
  </section>

  <section>
    <div class="wrap prose">
      <h2>Information you give us</h2>
      <p>When you fill out a contact form, we collect what you enter, such as your name, email, phone number, company, and message. Forms are delivered to our email by FormSubmit, a third-party form service. We use this information only to respond to you and to provide the services you ask about.</p>
      <p>When you email or call us, we keep that correspondence so we can follow up and serve you.</p>
    </div>
  </section>

  <section>
    <div class="wrap prose">
      <h2>Analytics and cookies</h2>
      <p>We use Google Analytics to understand how visitors use this site, for example which pages are viewed, how people found us, and whether a contact form was completed. Google Analytics uses cookies and collects information such as your browser type, device, approximate location, and pages visited. It does not give us your name or contact details.</p>
      <p>You can learn how Google uses this data at <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">policies.google.com/technologies/partner-sites</a>, and you can opt out with the <a href="https://tools.google.com/dlpage/gaoptout" rel="noopener">Google Analytics opt-out browser add-on</a>. You can also block or delete cookies in your browser settings.</p>
    </div>
  </section>

  <section>
    <div class="wrap prose">
      <h2>How we share information</h2>
      <p>We do not sell or rent your personal information. We share it only with service providers that help us run this website and our business, such as our website host, form service, and analytics provider, or when required by law.</p>
    </div>
  </section>

  <section>
    <div class="wrap prose">
      <h2>Your choices</h2>
      <p>You can ask us to see, correct, or delete the personal information you have sent us. Just email <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
      <p>This website is meant for businesses and is not directed at children under 13.</p>
      <p>If we change this policy, we will update the effective date at the top of this page.</p>
    </div>
  </section>
</main>
"""
    write(path, head("Privacy Policy | Walker Intelligence Group", desc, path, schema) + body + footer())


def sitemap():
    urls = ["/"] + [f"/{s['slug']}/" for s in SERVICES] + ["/about/", "/contact/", "/privacy/"]
    entries = "\n".join(
        f"  <url>\n    <loc>{SITE}{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n  </url>" for u in urls)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}\n</urlset>\n")
    print("wrote sitemap.xml")


if __name__ == "__main__":
    for s in SERVICES:
        service_page(s)
    about_page()
    contact_page()
    privacy_page()
    sitemap()
