# 💠 SkillSync — A Private Audit of Candidate & Role

**A lightweight, in-browser skill-gap assessment tool that compares a resume against a target job's requirements and tells you exactly what's missing.**

`Status: Prototype / Demo` · `Frontend: Streamlit + HTML/CSS/JS` · `Matching Engine: Client-side keyword scan` · `Persistence: None (session-only)`

---

## 🌟 1. What SkillSync Does

Job seekers and recruiters both face the same small, repetitive problem: **does this resume actually match this job description, and by how much?**

Manually re-reading a job post against a resume is slow, and generic "ATS score" tools are black boxes that don't say *which* skills are missing or *what to do* about it.

SkillSync solves the immediate version of this problem — a self-contained, single-page tool that:

1. Reads a plain-text resume
2. Reads a pasted job description or requirement list
3. Compares them against a known set of skill keywords
4. Shows what overlaps, what's missing, and links straight to a course for each gap

No servers, no sign-up, no data leaves the browser tab.

---

## 🧠 2. How the Assessment Works

Unlike a full ML pipeline, SkillSync is intentionally simple: **one client-side matching engine**, running entirely in JavaScript inside the Streamlit component — there is no backend, database, or model file.

```
┌─────────────────────────────┐
│   I. Candidate Profile       │   .txt resume, read via FileReader
└─────────────────────────────┘
              │
              ▼
┌─────────────────────────────┐
│  II. Target Requirements     │   pasted job description / text
└─────────────────────────────┘
              │
              ▼
┌───────────────────────────────────────────┐
│   Matching Engine (browser JS)             │
│   • Lower-cases both texts                 │
│   • Checks each keyword in a fixed skill   │
│     list against both texts                │
│   • Buckets each required skill as         │
│     "matched" or "gap"                     │
└───────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────┐
│   Findings                   │
│   • Match % (Venn overlap)   │
│   • Verified capabilities    │
│   • Capability gaps + links  │
└─────────────────────────────┘
```

**Current skill vocabulary** (hard-coded in `runInference()`):
`python, java, sql, machine learning, react, html, css, data structures, algorithms, aws, git`

> [!NOTE]
> This is a fixed keyword list, not an NLP model — it will not catch synonyms (e.g. "JS" vs "JavaScript") or infer skills from context. See [Roadmap](#-6-roadmap--known-limitations) for where this is headed.

---

## 💻 3. Feature Catalog

### 📄 Candidate & Requirement Intake
- Drag-and-drop **or** click-to-browse `.txt` resume upload, with live drag-over and "file received" states
- Free-text paste area for job descriptions or credential lists

### 🎯 Findings / Results
- **Venn diagram visualization** — two circles (Candidate ∩ Role) that animate together proportional to the match score, with the percentage rendered inside the overlap
- **Verified Capabilities** ledger — every matched skill, styled as a checked manifest line
- **Capability Gaps** ledger — every missing required skill, each with a one-click **"pursue ↗"** link to a relevant course search
- Live counts for total verified vs. gap skills

### 🎨 Interface
- Custom "audit dossier" visual identity (letterhead, wax-seal mark, hairline rules) rather than a generic dashboard template
- Entrance and reveal animations for the page, the gauge, and each result row, with `prefers-reduced-motion` support
- Fully responsive down to mobile widths
- Visible keyboard focus states throughout

---

## 🔧 4. Tech Stack

| Layer | Technology | Notes |
|---|---|---|
| App shell | Streamlit (Python) | Hosts the component and sets page config |
| UI / rendering | HTML + CSS embedded via `st.components.v1.html` | Single self-contained component |
| Matching logic | Vanilla JavaScript | Runs entirely client-side, no network calls |
| Fonts | Fraunces, Inter, JetBrains Mono | Loaded from Google Fonts CDN |
| Data storage | None | Nothing is persisted between runs or sessions |

---

## 🚀 5. Setup & Installation

### Prerequisites
- Python 3.9+
- `streamlit` installed (`pip install streamlit`)

### Run it

```bash
git clone <your-repo-url>
cd <your-repo-folder>
pip install streamlit
streamlit run skillsync_app.py
```

Streamlit will open the app automatically at `http://localhost:8501`.

> [!TIP]
> Because the matching engine runs entirely in the browser, there's no `.env` file, API key, or backend service to configure — it works the moment Streamlit boots.

---

## 🗺️ 6. Roadmap & Known Limitations

SkillSync is intentionally minimal today. Being upfront about the gaps:

- **Fixed skill list** — only the ~11 hard-coded keywords are ever checked; anything outside that list is invisible to the tool.
- **No synonym/semantic matching** — "ML" won't match "machine learning," and misspellings won't match at all.
- **`.txt` resumes only** — no PDF or DOCX parsing yet.
- **No persistence** — refreshing the page clears everything; there's no history or account system.

### Planned Next Steps
- Expand the skill taxonomy and allow a custom/uploaded skill list instead of a hard-coded one
- Add PDF/DOCX resume parsing
- Move from exact keyword matching to lightweight semantic similarity (synonyms, related terms)
- Optional save/export of a past assessment as a PDF report

---

Built as a fast, honest way to see exactly where a resume stands against a role — nothing more, nothing less.
