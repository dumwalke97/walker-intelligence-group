"""Generate the inner pages (services, about, contact, insights) and sitemap.xml.

Edit the content below, then run from the repo root:
    python3 tools/build_pages.py
Commit the generated files. Netlify serves them as-is (no build step).
"""
import html
import json
import re
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
        "desc": "We find where AI saves your team time, then build and run the tools: document review, data extraction, summaries, and private AI assistants.",
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
        "related": ["workflow-automation", "technology-strategy", "websites-custom-apps"],
    },
    {
        "slug": "workflow-automation",
        "name": "Workflow Automation",
        "title": "Workflow Automation for Indianapolis Businesses | Walker IG",
        "desc": "Stop paying people to do what software can handle. We automate data entry, reporting, follow-ups, and handoffs between your tools.",
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
        "desc": "Fast websites that generate leads, plus client portals, online forms, dashboards, and custom tools built around your process. Designed, built, and hosted for you.",
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
        "slug": "technology-strategy",
        "name": "Technology Strategy",
        "title": "Technology Strategy & Consulting in Indianapolis | Walker IG",
        "desc": "A plain-English review of your technology, a ranked list of the improvements worth making, and a clear plan your leadership team can act on. Then we build it.",
        "h1": "A technology plan that makes <em>sense for you</em>.",
        "lede": "New tools, automation, cloud, AI. There is no shortage of options. We help you sort out what is worth doing, in what order, and then we help you build it.",
        "card": "A clear, practical technology plan for your leadership team.",
        "problem": [
            "Most leadership teams know their technology could work better, but it is hard to know where to start. Every vendor has a pitch, every tool promises to change everything, and it is tough to tell what is real, what is safe, and what is worth the money.",
            "We give you an honest outside view. We look at your operations, your systems, and your goals, and tell you which improvements will make a measurable difference, whether that is better software, automation, stronger security, or AI. Then, unlike most advisors, we can build what we recommend.",
        ],
        "offer": [
            ("Technology assessment", "A plain-English review of your current tools, systems, data, and processes: what works, what is at risk, and what is holding you back."),
            ("Opportunity roadmap", "A short list of improvements ranked by return, cost, and risk, from quick wins to bigger projects."),
            ("Tool and vendor guidance", "Recommendations that fit your budget and data sensitivity, so you do not overpay or lock yourself into the wrong platform."),
            ("Innovation and AI readiness", "Where newer tools like AI genuinely fit, with simple guardrails so your team can use them safely."),
            ("Ongoing advisory", "A trusted partner to check in with as your business and the technology change, without a full-time hire."),
        ],
        "examples": [
            "A leadership workshop that ends with a prioritized technology roadmap",
            "A second opinion on a software or vendor proposal before you sign",
            "A plan to modernize aging systems without disrupting daily work",
            "A safe-use policy for the AI tools your team is already trying",
        ],
        "faq": [
            ("What do we get at the end?", "A written roadmap with prioritized opportunities, expected impact, rough costs, and clear next steps. Not a slide deck full of buzzwords."),
            ("Do you only advise, or do you build too?", "Both. We are a technology consulting and implementation firm. You can take the plan and run with it, or have us build it."),
            ("Are you tied to any software vendor?", "No. We recommend what fits your needs and data, not what pays us a commission."),
            ("Is this only for large companies?", "No. Most of our work is with small and mid-sized organizations that need practical answers, not an enterprise program."),
        ],
        "related": ["technology-infrastructure", "workflow-automation", "cost-optimization"],
    },
    {
        "slug": "technology-infrastructure",
        "name": "Technology Infrastructure",
        "title": "IT Infrastructure & Cloud Setup, Indianapolis | Walker IG",
        "desc": "Cloud setup, tested backups, security assessments, and technology audits for Indianapolis businesses. Know what you have, what is at risk, and fix it.",
        "h1": "A secure foundation your business <em>can rely on</em>.",
        "lede": "Cloud setup, backups, security, and a clear picture of what you have. We organize your technology so it is safe, reliable, and ready to grow.",
        "card": "Cloud setup, backups, security, and technology audits.",
        "problem": [
            "Many businesses run on technology that grew one decision at a time. Shared passwords, files in three places, no tested backups, and nobody sure what is still being paid for. It works until it does not.",
            "We take inventory, close the obvious risks, and set up a clean, documented foundation. It is also the step that makes new tools, automation, and AI safe to add later.",
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
            "A technology audit before a merger, new hire wave, or big software change",
        ],
        "faq": [
            ("Are you a managed IT provider?", "We focus on getting your foundation right and supporting the systems we set up. For day-to-day help desk needs, we can work alongside your existing IT provider."),
            ("How do we know if we are at risk?", "Start with an audit. Most businesses find a few high-risk gaps that are quick and inexpensive to fix."),
            ("Do we need this before adding new technology?", "Often, yes. New software, automation, and AI are only as safe as the data and access rules behind them. A solid foundation makes every project faster and safer."),
            ("Can you work with Microsoft 365 or Google Workspace?", "Yes. We work with both and help you get far more out of the one you already pay for."),
        ],
        "related": ["cost-optimization", "technology-strategy", "workflow-automation"],
    },
    {
        "slug": "cost-optimization",
        "name": "Cost Optimization",
        "title": "Technology Cost Optimization in Indianapolis | Walker IG",
        "desc": "Cut technology waste. We audit subscriptions, remove redundant tools, right-size cloud spend, and replace manual work with automation.",
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
            ("ROI-ranked investment plan", "When you do spend, put money into the technology investments with the fastest return."),
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
            ("Can savings fund new projects?", "Often, yes. Cutting waste is a common way to pay for a first automation or modernization project without a new budget line."),
        ],
        "related": ["technology-infrastructure", "workflow-automation", "technology-strategy"],
    },
]
SERVICE_ORDER = ["workflow-automation", "websites-custom-apps", "technology-infrastructure",
                 "technology-strategy", "ai-integration", "cost-optimization"]
SERVICES.sort(key=lambda s: SERVICE_ORDER.index(s["slug"]))
BY_SLUG = {s["slug"]: s for s in SERVICES}

PROCESS = [
    ("01", "Discovery & Strategy", "We learn how your business runs, where time and money are going, and what success looks like. You get a short, prioritized plan."),
    ("02", "Assessment & Design", "We review the tools and data involved and design a solution that fits your systems, budget, and security needs."),
    ("03", "Build, Deploy & Support", "We build it, launch it, host it, and keep it running. You get a working result, not a stack of recommendations."),
]

# ── INSIGHTS (articles) ──────────────────────────────────────────────────────
# Section bodies are raw HTML so they can hold links and lists. Escape & as &amp;.
# Newest first. "service" is the service page each article supports.
ARTICLES = [
    {
        "slug": "how-to-choose-an-ai-consultant-indianapolis",
        "title": "How to Choose an AI Consultant in Indianapolis | Walker IG",
        "desc": "Hiring an AI consultant in Indianapolis? Ask these 8 questions first, from who builds the solution to how your data is handled and what happens after launch.",
        "h1": "How to choose an AI consultant in Indianapolis: <em>8 questions to ask</em>",
        "lede": "A good AI partner should make things simpler, not more confusing. These questions help you tell the difference before you sign anything.",
        "card": "Eight questions that separate a useful AI partner from an expensive slide deck.",
        "published": "2026-10-14",
        "modified": "2026-10-14",
        "service": "technology-strategy",
        "sections": [
            ("Why the choice matters", """
        <p>Search for AI consulting in Indianapolis and you will find a mix of local shops, national agencies with a page for every city, and software vendors who call their sales team consultants. They all promise to help you use AI. They do not all mean the same thing. The best partner looks at your technology as a whole, because AI only works when the systems around it do.</p>
        <p>For a small or mid-sized business, the wrong fit is costly. You can spend months on workshops and strategy documents and end up with nothing your team actually uses. The questions below are the ones we would ask if we were in your seat.</p>"""),
            ("1. Will you build it, or just recommend it?", """
        <p>This is the most important question. Some firms stop at advice. They hand you a roadmap and leave you to find someone else to build it. That handoff is where many technology projects stall.</p>
        <p>Ask whether the firm will also set up the tools, connect them to your systems, and keep them running. If they only advise, ask who they expect to do the build and what that will cost.</p>"""),
            ("2. Can we start with one small project?", """
        <p>A good partner should be happy to start small. Pick one process that eats up time, fix it, and measure the result. If it works, you expand. If it does not, you have learned something without betting the budget.</p>
        <p>Be careful with open-ended monthly retainers before any value has been delivered. A fixed scope for a first project protects you and keeps everyone focused.</p>"""),
            ("3. How will you handle our data?", """
        <p>Your customer records, financials, and employee information should not end up somewhere you did not intend. Ask:</p>
        <ul>
          <li>Which AI tools will touch our data, and are they set to keep it out of public model training?</li>
          <li>Who on your side and ours will have access?</li>
          <li>Where is the data stored, and what happens to it if we stop working together?</li>
        </ul>
        <p>A consultant who cannot answer these in plain English is not ready to work with sensitive information.</p>"""),
            ("4. Are you tied to any vendor?", """
        <p>Some consultants resell a specific platform or earn a commission on what they recommend. That is not always a problem, but you should know about it. Ask directly whether they are paid by any of the tools they suggest.</p>"""),
            ("5. Who will actually do the work?", """
        <p>The person who sells the project is not always the person who delivers it. Ask who will be on your project day to day, what their background is, and whether you can talk to them before you start.</p>"""),
            ("6. What happens after launch?", """
        <p>Any new system needs care, whether it is an AI tool, an automation, or a custom app. Software updates, a vendor changes its pricing, or a process changes on your side. Ask who hosts what gets built, who fixes it when something breaks, and who owns the accounts and the code. You should own your data and your systems, even if someone else maintains them.</p>"""),
            ("7. How will we know it worked?", """
        <p>Before any work starts, agree on what success looks like. Good measures are simple: hours saved each week, faster turnaround for customers, fewer errors, or work that no longer needs a person to touch it. If a consultant cannot tell you how they will measure results, they probably will not.</p>"""),
            ("8. Will you tell us when AI is not the answer?", """
        <p>Sometimes the best fix is a simple automation, a cleaner spreadsheet, or a setting in software you already own. A trustworthy partner will say so, even when it means a smaller project. If every answer is a big AI build, keep looking.</p>"""),
            ("A few red flags", """
        <ul>
          <li>Lots of buzzwords and no clear explanation of what you will get</li>
          <li>Pressure to sign a long contract before a first result</li>
          <li>Vague answers about data, security, or who owns what</li>
          <li>No plan for support once the project is live</li>
        </ul>"""),
            ("Does it matter if the consultant is local?", """
        <p>Not always. A lot of technology work can be done remotely. But a partner in the Indianapolis area can sit down with your team, see how work really moves through your business, and be there in person when it matters. It also helps to work with someone who knows the local business community and resources like Indiana's <a href="/insights/indiana-in-ai-initiative-small-business/">IN AI initiative</a>.</p>"""),
            ("How we answer these questions", """
        <p>Walker Intelligence Group is a technology consulting and implementation firm in Indianapolis, and AI is one of the tools we use. We plan the work with you, then build it, host it, and keep it running. We like to start with one focused project that proves its value. We choose tools based on how sensitive your data is, we are not tied to any software vendor, and we will tell you when AI is not the right fit.</p>
        <p>If you want to see how that works for your business, <a href="/contact/">book a free 30-minute consult</a>. Bring these eight questions. We are happy to answer them.</p>"""),
        ],
        "faq": [
            ("What is the difference between AI consulting and AI implementation?", "AI consulting is the planning: finding where AI fits, what it will cost, and what the risks are. Implementation is the doing: setting up the tools, connecting them to your systems, and keeping them running. Many small businesses need both from the same partner."),
            ("How much does an AI consultant cost?", "It depends on the scope. Start by asking for a fixed price on one small project. Our guide on what AI costs for a small business walks through the main cost drivers."),
            ("Do we need an AI strategy before we start?", "Not a big one. A short list of your most time-consuming tasks is enough to find a good first project. The strategy can grow from real results."),
        ],
        "related_articles": ["how-much-does-ai-cost-small-business", "indiana-in-ai-initiative-small-business"],
    },
    {
        "slug": "how-much-does-ai-cost-small-business",
        "title": "How Much Does AI Cost for a Small Business? | Walker IG",
        "desc": "What AI really costs a small business: the four levels of spending, the hidden costs most quotes leave out, and a simple way to estimate your return first.",
        "h1": "How much does AI cost for a small business? <em>A plain-English guide</em>",
        "lede": "Price ranges online are all over the place, and most come from companies selling AI. Here is how to think about the cost for your own business instead.",
        "card": "The four levels of AI spending, the hidden costs, and how to estimate your return.",
        "published": "2026-10-14",
        "modified": "2026-10-14",
        "service": "ai-integration",
        "sections": [
            ("The short answer", """
        <p>AI can cost almost nothing or it can cost a lot. What you pay depends far more on what you want it to do than on the size of your company. A team using an AI assistant for writing emails is in a completely different place than a business building a custom tool that reads every incoming order.</p>
        <p>The good news is that most small businesses do not need to start with the expensive option. It helps to think about AI spending in four levels.</p>"""),
            ("Level 1: Off-the-shelf AI tools", """
        <p>This is ChatGPT, Claude, Gemini, Microsoft Copilot, and similar tools, paid per person each month. It is the cheapest way to start, and it is great for writing, summarizing, and research.</p>
        <p>The catch is that each person uses it on their own. Nothing is connected to your systems, and results depend on who is typing. Business plans also matter here. Free personal accounts usually have weaker data protections than business versions, so check the settings before anyone pastes in customer information.</p>"""),
            ("Level 2: AI inside tools you already pay for", """
        <p>Many platforms you may already use, such as Microsoft 365, Google Workspace, and popular CRMs, now offer AI features. Sometimes they are included and sometimes they are a paid add-on per user.</p>
        <p>This is often the best value because your data is already there and your team already knows the software. Before you buy anything new, it is worth finding out what you are already paying for.</p>"""),
            ("Level 3: Custom automations with AI", """
        <p>This is where AI starts doing real work on its own. For example, a system that reads incoming PDFs and fills in your CRM, or one that sorts your inbox and drafts replies for a person to approve.</p>
        <p>Costs here usually come in two parts:</p>
        <ul>
          <li><strong>A one-time build.</strong> Someone designs the workflow, connects your tools, and tests it.</li>
          <li><strong>Small ongoing costs.</strong> Automation platform fees, hosting, and AI usage fees that go up and down with how much you use it.</li>
        </ul>
        <p>For most small businesses, this level is where the clearest return shows up, because it removes work instead of just speeding it up. Our <a href="/workflow-automation/">workflow automation</a> page has more examples.</p>"""),
            ("Level 4: Custom AI apps", """
        <p>A purpose-built tool, like a quoting assistant trained on your past jobs or a private assistant that answers questions from your own manuals. This is the biggest investment and should usually come after a smaller project has proven the value.</p>"""),
            ("The costs most quotes leave out", """
        <p>The price of the software is rarely the whole picture. Plan for these too:</p>
        <ul>
          <li><strong>Your team's time.</strong> Someone needs to explain the process, test the results, and learn the new way of working.</li>
          <li><strong>Data cleanup.</strong> AI, like any new system, works best when your information is organized. Messy files and duplicate records slow everything down.</li>
          <li><strong>Security setup.</strong> Access controls, business-grade accounts, and the right privacy settings.</li>
          <li><strong>Maintenance.</strong> Tools change. Someone has to keep things running and fix what breaks.</li>
          <li><strong>Usage fees.</strong> Some AI services charge by how much you use them. Ask how costs grow if your volume doubles.</li>
        </ul>"""),
            ("A simple way to estimate your return", """
        <p>You do not need a complicated model. Pick one task and answer three questions:</p>
        <ul>
          <li>How many hours a week does this task take, across everyone who does it?</li>
          <li>What does an hour of that person's time cost you, including wages and benefits?</li>
          <li>How much of the task could be automated or sped up?</li>
        </ul>
        <p>Multiply them together for a weekly savings estimate, then compare it to the cost of the fix. Here is an example with made-up numbers: a task that takes 10 hours a week, at $35 an hour, that is 60% automatable, is worth about $210 a week, or roughly $10,000 a year. If the fix costs less than that in its first year, it is worth a serious look. Use your own numbers, and include the soft benefits too, like faster replies to customers and fewer mistakes.</p>"""),
            ("How to keep costs down", """
        <ul>
          <li><strong>Start with one workflow.</strong> Prove the value before you expand.</li>
          <li><strong>Use what you already own.</strong> Check the AI features in your current software first.</li>
          <li><strong>Ask for a fixed scope.</strong> A clear price for a clear result beats an open-ended retainer.</li>
          <li><strong>Cut waste to fund it.</strong> Unused subscriptions and duplicate tools can often pay for a first project. See <a href="/cost-optimization/">cost optimization</a>.</li>
          <li><strong>Look for free local help.</strong> Indiana's <a href="/insights/indiana-in-ai-initiative-small-business/">IN AI initiative</a> offers workshops and a readiness assessment.</li>
        </ul>"""),
            ("AI is one option, not the only one", """
        <p>Sometimes the right answer is not AI at all. A simple automation, better use of software you already own, or cleaning up how information moves between your systems can deliver the same savings for less money and less risk. Start with the problem, then pick the tool. AI earns its place when the work involves reading, writing, or judgment that simpler automation cannot handle.</p>"""),
            ("Get a real number for your business", """
        <p>General ranges only go so far. The fastest way to get a real number is to talk through one specific problem. In a <a href="/contact/">free 30-minute consult</a>, we will look at what is slowing your team down, tell you whether AI, automation, or a simpler fix makes the most sense, and give you an honest idea of cost. Then, if you want, we build it, host it, and support it. See our <a href="/ai-integration/">AI integration</a> services for what that looks like.</p>"""),
        ],
        "faq": [
            ("Is ChatGPT enough for a small business?", "It is a good place to start for writing and research. It will not connect to your systems or run processes on its own. When you want AI to do work automatically, you need an automation or a custom tool."),
            ("Are there monthly costs after the build?", "Usually, yes, but they are often small. Expect platform or hosting fees and AI usage fees. Ask any provider to estimate these before you start."),
            ("Is AI worth it for a business with fewer than 20 people?", "Often, yes. Small teams feel time savings the most because every hour of busywork comes out of someone who has other jobs to do. Start with the task your team complains about most."),
        ],
        "related_articles": ["how-to-choose-an-ai-consultant-indianapolis", "indiana-in-ai-initiative-small-business"],
    },
    {
        "slug": "indiana-in-ai-initiative-small-business",
        "title": "Indiana IN AI Initiative: Small Business Guide | Walker IG",
        "desc": "What Indiana's IN AI initiative offers small businesses, what it does not, and how to use its workshops and readiness tools to start your first AI project.",
        "h1": "Indiana's IN AI initiative: <em>what small businesses should know</em>",
        "lede": "Indiana launched a statewide push to help employers adopt AI. Here is what it is, what it offers, and how a small business can actually use it.",
        "card": "What the state's AI program offers, what it does not, and how to use it.",
        "published": "2026-10-14",
        "modified": "2026-10-14",
        "service": "technology-strategy",
        "sections": [
            ("What IN AI is", """
        <p>IN AI is a statewide initiative to help Indiana employers put AI to work. Governor Mike Braun announced it at a press conference on April 28, 2026. It is led by the CEOs of the Indiana Corporate Partnership (CICP), working with the governor's administration. The stated goal is for Indiana to become the most AI-ready state in the nation, and state leaders have said they want to reach one million Hoosiers.</p>
        <p>The program is for employers of all sizes, from small businesses to large companies. Its online hub lives at <a href="https://www.cicpindiana.com/ai/" rel="noopener">cicpindiana.com/ai</a>. The shorter address, inaiready.com, sends you to the same place.</p>"""),
            ("What it offers", """
        <p>The IN AI hub is organized around a few simple steps. As of October 2026, it includes:</p>
        <ul>
          <li><strong>AI use cases</strong> showing practical ways businesses are using AI</li>
          <li><strong>An AI readiness assessment</strong> and an <strong>AI playbook</strong> for planning adoption</li>
          <li><strong>Roadshows and workshops</strong> held in person around the state</li>
          <li><strong>Peer learning groups</strong> where business leaders work through similar challenges together</li>
          <li><strong>Project intake and a partner directory</strong> for when you are ready to put AI to work</li>
          <li><strong>Team training</strong> to build day-to-day AI skills</li>
        </ul>
        <p>Google has also announced a series of workshops called Make AI Work for You for small and mid-sized Indiana businesses and startups, delivered with Ivy Tech Community College and TechPoint. The IN AI site lists those events too.</p>"""),
            ("What it is not", """
        <p>IN AI is not a grant program. When it launched, the governor did not commit state funding to it and said funding would depend on the state's cash flow and the economy. Think of it as education, guidance, and connections, not money for your project.</p>
        <p>Separately, the state's Community Collaboration Fund has awarded grants to organizations that run AI training for small businesses. Those funds go to the training providers, not directly to businesses. If you are counting on outside money, check with the <a href="https://iedc.in.gov/" rel="noopener">Indiana Economic Development Corporation</a> for current programs.</p>"""),
            ("How a small business can use it", """
        <p>The program is a useful starting point, especially if AI still feels abstract. Here is a practical way to use it:</p>
        <ul>
          <li><strong>Take the readiness assessment.</strong> It gives you a quick read on where you stand.</li>
          <li><strong>Go to a workshop or roadshow.</strong> Seeing real examples makes it much easier to spot opportunities in your own business.</li>
          <li><strong>Write down one problem.</strong> Pick the task that wastes the most time each week. One clear problem is worth more than a long wish list.</li>
          <li><strong>Find someone to build it.</strong> Workshops teach. They do not set up the tools, connect them to your systems, or keep them running. That is where an implementation partner comes in.</li>
        </ul>"""),
            ("Where we fit", """
        <p>Walker Intelligence Group is a technology consulting and implementation firm based in Indianapolis, and AI is part of what we do. We think IN AI is a good thing for Indiana businesses, and we are glad to see the state take AI seriously for small and mid-sized employers.</p>
        <p>Our job is the next step. Once you have an idea of where AI could help, we help you pick the right first project, whether that turns out to be AI, automation, or a simpler technology fix, then build it, host it, and support it. If you have been to an IN AI event and want help turning what you learned into something your team uses every day, <a href="/contact/">book a free 30-minute consult</a>. You can also read <a href="/insights/how-much-does-ai-cost-small-business/">what AI costs for a small business</a> or <a href="/insights/how-to-choose-an-ai-consultant-indianapolis/">how to choose an AI consultant</a>.</p>"""),
            ("Sources", """
        <ul>
          <li><a href="https://www.cicpindiana.com/ai/" rel="noopener">IN AI hub, Indiana Corporate Partnership</a></li>
          <li><a href="https://indianapublicradio.org/news/2026/04/in-ai-governor-unveils-artificial-intelligence-business-portal/" rel="noopener">Indiana Public Radio: IN AI, governor unveils artificial intelligence business portal (April 2026)</a></li>
          <li><a href="https://www.cicpindiana.com/?p=17961" rel="noopener">CICP: Google to offer AI readiness workshops for small and medium-sized businesses statewide</a></li>
          <li><a href="https://iedc.in.gov/events/news/details/2026/07/06/gov.-braun-strengthens-indiana-entrepreneurship-through-community-grants" rel="noopener">IEDC: Community Collaboration Fund awards (July 2026)</a></li>
        </ul>
        <p>Program details change. This article reflects what was published as of October 14, 2026. Check the IN AI hub for current events and offerings.</p>"""),
        ],
        "faq": [
            ("Does IN AI cost anything?", "The IN AI site does not list pricing for its resources. Check each workshop or event listing for details."),
            ("Is IN AI only for large companies?", "No. It is meant for Indiana employers of all sizes, and small businesses are a stated focus."),
            ("Will IN AI build an AI tool for my business?", "The program focuses on education, assessments, peer learning, and connecting businesses with partners. To get a tool built and running, you will work with an implementation partner."),
        ],
        "related_articles": ["how-much-does-ai-cost-small-business", "how-to-choose-an-ai-consultant-indianapolis"],
    },
]
ARTICLE_BY_SLUG = {a["slug"]: a for a in ARTICLES}


# ── SHARED PIECES ────────────────────────────────────────────────────────────
def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    return s.replace("<em>", "").replace("</em>", "")


def head(title, desc, path, schema, og_type="website", extra_meta=""):
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
  <meta property="og:type" content="{og_type}" />
{extra_meta}  <meta property="og:site_name" content="Walker Intelligence Group" />
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
    <span class="brand-top">Technology Consulting &amp; Implementation</span>
    <span class="brand-main">Walker <span>Intelligence Group</span></span>
  </a>
  <nav class="site-nav" aria-label="Main">
    <a href="/#services"{cur('services')}>Services</a>
    <a href="/insights/"{cur('insights')}>Insights</a>
    <a href="/about/"{cur('about')}>About</a>
    <a href="/contact/"{cur('contact')}>Contact</a>
{'' if current == 'contact' else '    <a class="btn" href="/contact/">Free consult</a>' + chr(10)}  </nav>
  <details class="menu">
    <summary>Menu</summary>
    <div class="menu-panel">
      <span class="menu-label">Services</span>
{svc_links}
      <span class="menu-label">Company</span>
      <a href="/insights/">Insights</a>
      <a href="/about/">About</a>
      <a href="/contact/">Contact</a>
      <a href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </div>
  </details>
</header>
"""


def footer_html():
    svc = "\n".join(f'          <li><a href="/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in SERVICES)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="footer-name" href="/">Walker <span>Intelligence Group</span></a>
        <p>Technology consulting &amp; implementation</p>
        <p class="footer-contact"><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><span aria-hidden="true">&middot;</span><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <nav aria-label="Services">
        <h4>Services</h4>
        <ul class="footer-two-col">
{svc}
        </ul>
      </nav>
      <nav aria-label="Company">
        <h4>Company</h4>
        <ul>
          <li><a href="/insights/">Insights</a></li>
          <li><a href="/about/">About</a></li>
          <li><a href="/contact/">Contact</a></li>
        </ul>
      </nav>
    </div>
    <div class="footer-base">
      <span>&copy; 2026 Walker Intelligence Group<span class="sep" aria-hidden="true">&middot;</span><a href="/privacy/">Privacy Policy</a></span>
    </div>
  </div>
</footer>
"""


def footer():
    return footer_html() + "</body>\n</html>\n"


def sync_homepage_footer():
    """The homepage is hand-written; keep its footer identical to the generated pages."""
    home = ROOT / "index.html"
    h = home.read_text()
    start, end = "<!-- SHARED-FOOTER:START -->", "<!-- SHARED-FOOTER:END -->"
    a, b = h.index(start) + len(start), h.index(end)
    home.write_text(h[:a] + "\n" + footer_html() + h[b:])
    print("synced footer into index.html")


def cta_band(heading="Let's talk about <em>your</em> business.",
             text="Tell us what is slowing your team down. In a free 30-minute call, we will point out where better technology can help and what it would take. No pressure and no jargon."):
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
    guides = [a for a in ARTICLES if a["service"] == s["slug"]]
    insights = "" if not guides else """  <section>
    <div class="wrap">
      <h2>Related guides</h2>
      <div class="grid">
""" + "\n".join(
        f'        <a class="card" href="/insights/{a["slug"]}/"><h3>{strip_tags(a["h1"])}</h3>'
        f'<p>{esc(a["card"])}</p><span class="more">Read &rarr;</span></a>' for a in guides) + """
      </div>
    </div>
  </section>
"""
    body = f"""{header('services')}
<main>
  <div class="wrap crumbs"><a href="/">Home</a> / <a href="/#services">Services</a> / {esc(s['name'])}</div>

  <section class="hero">
    <div class="wrap">
      <span class="eyebrow">{esc(s['name'])}</span>
      <h1>{s['h1']}</h1>
      <p class="lede">{esc(s['lede'])}</p>
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
{insights}</main>
"""
    write(path, head(s["title"], s["desc"], path, schema) + body + footer())


def about_page():
    path = "/about/"
    desc = ("Indianapolis technology consulting and implementation firm founded by Dustin Walker, a Purdue-trained "
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
      <span class="eyebrow">About</span>
      <h1>A partner who plans it <em>and builds it</em>.</h1>
      <p class="lede">Walker Intelligence Group is a technology consulting and implementation firm based in Indianapolis. We help organizations figure out where modern technology, automation, and AI fit, then we build, deploy, and support the solution.</p>
    </div>
  </section>

  <section>
    <div class="wrap prose">
      <h2>Meet the founder</h2>
      <p>Walker Intelligence Group was founded in 2026 by Dustin Walker, a technology leader with more than 25 years of experience implementing, administering, and leading technology for organizations. Over that career he has worked hands-on across many roles and many generations of technology, from running the systems businesses depend on every day to leading the teams and projects that put new ones in place.</p>
      <p>Dustin holds a degree in Computer and Information Technology from Purdue University. That combination of formal training and decades of real-world delivery is why WIG can both advise and build. He has seen plenty of technology waves come and go, and he knows the difference between hype and tools that actually change how a business runs.</p>
      <p>He started Walker Intelligence Group because he is passionate about helping small and medium-sized businesses see what is possible with technology and innovation, including AI. Large companies have whole departments for this. Most growing businesses do not. WIG gives them a senior, hands-on partner who explains things in plain English and then gets the work done.</p>
      <ul class="checks">
        <li>25+ years in technology implementation, administration, and leadership</li>
        <li>Degree in Computer and Information Technology, Purdue University</li>
        <li>Focused on small and mid-sized businesses</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>What we <em>believe</em></h2>
      <div class="grid">
        <div class="card"><h3>Plain English, no hype</h3><p>You should understand what you are buying and why. We explain things clearly and tell you when new technology is not the answer.</p></div>
        <div class="card"><h3>Build, don't just advise</h3><p>A plan only matters if it gets done. We build, launch, host, and support what we recommend.</p></div>
        <div class="card"><h3>Your data stays yours</h3><p>We choose tools and settings based on how sensitive your information is, and we keep it out of public AI training and third-party hands.</p></div>
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
    write(path, head("About Walker Intelligence Group | Indianapolis Technology Firm",
                     desc, path, schema) + body + footer())


def contact_page():
    path = "/contact/"
    desc = ("Book a free 30-minute consult with an Indianapolis technology consulting and implementation firm. "
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
        <span class="eyebrow">Free consult</span>
        <h1>Let's find where technology <em>pays off</em> for you.</h1>
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
    write(path, head("Free Technology Consult in Indianapolis | Contact Walker IG",
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


def long_date(iso):
    d = date.fromisoformat(iso)
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def read_minutes(a):
    text = " ".join(body for _, body in a["sections"]) + " ".join(q + " " + ans for q, ans in a["faq"])
    words = len(re.sub(r"<[^>]+>", " ", text).split())
    return max(1, round(words / 230))


def article_page(a):
    path = f"/insights/{a['slug']}/"
    url = SITE + path
    svc = BY_SLUG[a["service"]]
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "@id": f"{url}#article",
                "headline": strip_tags(a["h1"]),
                "description": a["desc"],
                "url": url,
                "mainEntityOfPage": url,
                "image": f"{SITE}/og-image.jpg",
                "datePublished": a["published"],
                "dateModified": a["modified"],
                "inLanguage": "en-US",
                "author": {"@id": f"{SITE}/#founder"},
                "publisher": PROVIDER,
                "isPartOf": {"@id": f"{SITE}/insights/#collection"},
                "about": {"@id": f"{SITE}/{svc['slug']}/#service"},
            },
            FOUNDER,
            breadcrumb_schema([("Home", "/"), ("Insights", "/insights/"), (strip_tags(a["h1"]), path)]),
        ],
    }
    meta = (f'  <meta property="article:published_time" content="{a["published"]}" />\n'
            f'  <meta property="article:modified_time" content="{a["modified"]}" />\n'
            f'  <meta property="article:author" content="Dustin Walker" />\n')
    sections = "\n".join(f"        <h2>{esc(h)}</h2>{body}" for h, body in a["sections"])
    faq = "\n".join(
        f"        <details><summary>{esc(q)}</summary><p>{esc(ans)}</p></details>" for q, ans in a["faq"])
    related = [
        f'        <a class="card" href="/{svc["slug"]}/"><span class="num">Service</span><h3>{esc(svc["name"])}</h3>'
        f'<p>{esc(svc["card"])}</p><span class="more">Learn more &rarr;</span></a>'
    ] + [
        f'        <a class="card" href="/insights/{r}/"><span class="num">Insight</span>'
        f'<h3>{strip_tags(ARTICLE_BY_SLUG[r]["h1"])}</h3><p>{esc(ARTICLE_BY_SLUG[r]["card"])}</p>'
        f'<span class="more">Read &rarr;</span></a>'
        for r in a["related_articles"]
    ]
    body = f"""{header('insights')}
<main>
  <div class="wrap crumbs"><a href="/">Home</a> / <a href="/insights/">Insights</a> / {strip_tags(a['h1'])}</div>

  <article>
    <section class="hero">
      <div class="wrap">
        <span class="eyebrow">Insights &middot; {esc(svc['name'])}</span>
        <h1 class="article-title">{a['h1']}</h1>
        <p class="lede">{esc(a['lede'])}</p>
        <p class="byline">By <a href="/about/">Dustin Walker</a> &middot; <time datetime="{a['published']}">{long_date(a['published'])}</time> &middot; {read_minutes(a)} min read</p>
      </div>
    </section>

    <section>
      <div class="wrap prose article-body">
{sections}
      </div>
    </section>

    <section>
      <div class="wrap">
        <h2>Common questions</h2>
        <div class="faq">
{faq}
        </div>
      </div>
    </section>

    <section>
      <div class="wrap prose author-box">
        <span class="eyebrow">About the author</span>
        <p><a href="/about/">Dustin Walker</a> founded Walker Intelligence Group, a technology consulting and implementation firm in Indianapolis. He has more than 25 years of experience in technology implementation, administration, and leadership, and a degree in Computer and Information Technology from Purdue University. He is passionate about helping small and medium-sized businesses put AI to work.</p>
      </div>
    </section>
  </article>

{cta_band()}
  <section>
    <div class="wrap">
      <h2>Keep reading</h2>
      <div class="grid">
{chr(10).join(related)}
      </div>
    </div>
  </section>
</main>
"""
    write(path, head(a["title"], a["desc"], path, schema, "article", meta) + body + footer())


def insights_index():
    path = "/insights/"
    url = SITE + path
    desc = ("Plain-English guides on technology, automation, and AI for Indianapolis small and mid-sized "
            "businesses, from Walker Intelligence Group.")
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "@id": f"{url}#collection",
                "url": url,
                "name": "Insights",
                "description": desc,
                "publisher": PROVIDER,
                "mainEntity": {
                    "@type": "ItemList",
                    "itemListElement": [
                        {"@type": "ListItem", "position": i + 1, "url": f"{url}{a['slug']}/",
                         "name": strip_tags(a["h1"])}
                        for i, a in enumerate(ARTICLES)
                    ],
                },
            },
            breadcrumb_schema([("Home", "/"), ("Insights", path)]),
        ],
    }
    cards = "\n".join(
        f'        <a class="card" href="/insights/{a["slug"]}/"><span class="num">{long_date(a["published"])} &middot; '
        f'{esc(BY_SLUG[a["service"]]["name"])}</span><h3>{strip_tags(a["h1"])}</h3><p>{esc(a["card"])}</p>'
        f'<span class="more">Read &rarr;</span></a>'
        for a in ARTICLES)
    body = f"""{header('insights')}
<main>
  <div class="wrap crumbs"><a href="/">Home</a> / Insights</div>

  <section class="hero">
    <div class="wrap">
      <span class="eyebrow">Insights</span>
      <h1>Practical technology, <em>in plain English</em>.</h1>
      <p class="lede">Short, honest guides for small and mid-sized businesses on technology, automation, and AI. What it costs, where it helps, and how to get started.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Latest guides</h2>
      <div class="grid">
{cards}
      </div>
    </div>
  </section>

{cta_band()}</main>
"""
    write(path, head("Insights: Technology & AI for Small Business | Walker IG",
                     desc, path, schema) + body + footer())


def sitemap():
    urls = ["/"] + [f"/{s['slug']}/" for s in SERVICES] + ["/about/", "/contact/", "/privacy/", "/insights/"]
    lastmod = {u: TODAY for u in urls}
    for a in ARTICLES:
        lastmod[f"/insights/{a['slug']}/"] = a["modified"]
    entries = "\n".join(
        f"  <url>\n    <loc>{SITE}{u}</loc>\n    <lastmod>{m}</lastmod>\n  </url>" for u, m in lastmod.items())
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
    for a in ARTICLES:
        article_page(a)
    insights_index()
    sync_homepage_footer()
    sitemap()
