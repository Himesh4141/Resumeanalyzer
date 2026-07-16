import streamlit as st

st.set_page_config(
    page_title="SkillSync // Audit Dossier",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .stApp { background: #0E1613 !important; }
    header, footer, [data-testid="stToolbar"] { display: none !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    iframe { border: none !important; }
    </style>
""", unsafe_allow_html=True)

premium_ui_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

    :root {
        --ink: #0E1613;
        --ink-2: #131C18;
        --line: rgba(239,231,216,0.14);
        --line-strong: rgba(239,231,216,0.24);
        --parchment: #EFE7D8;
        --muted: #96A197;
        --muted-dim: #5C665D;
        --brass: #C9A227;
        --brass-soft: rgba(201,162,39,0.13);
        --verified: #7FAE87;
        --verified-soft: rgba(127,174,135,0.12);
        --gap: #B06456;
        --gap-soft: rgba(176,100,86,0.12);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    html { background: var(--ink); }

    body {
        background: var(--ink);
        color: var(--parchment);
        font-family: 'Inter', sans-serif;
        padding: 56px 24px 80px;
        min-height: 100vh;
        position: relative;
    }

    /* fine paper grain */
    body::before {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        opacity: 0.05;
        z-index: 0;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
    }
    body::after {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        z-index: 0;
        background: radial-gradient(ellipse 1200px 700px at 50% -10%, rgba(201,162,39,0.05), transparent 60%);
    }

    .dossier {
        position: relative;
        z-index: 1;
        width: 100%;
        max-width: 860px;
        margin: 0 auto;
        border: 1px solid var(--line);
        border-radius: 2px;
        padding: 48px 56px 56px;
        background: linear-gradient(180deg, rgba(239,231,216,0.015), transparent 200px);
        opacity: 0;
        animation: pageIn 0.8s cubic-bezier(0.16,1,0.3,1) forwards;
    }
    @media (max-width: 640px) { .dossier { padding: 36px 22px 44px; } }

    /* ---------- Letterhead ---------- */
    .letterhead {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        padding-bottom: 28px;
        border-bottom: 1px solid var(--line-strong);
        margin-bottom: 34px;
    }
    .brand { display: flex; align-items: center; gap: 16px; }
    .seal { width: 46px; height: 46px; flex-shrink: 0; }
    .brand-name {
        font-family: 'Fraunces', serif;
        font-weight: 500;
        font-size: 1.7rem;
        letter-spacing: -0.01em;
    }
    .brand-sub {
        font-size: 0.78rem;
        color: var(--muted);
        font-style: italic;
        font-family: 'Fraunces', serif;
        margin-top: 3px;
    }
    .dossier-no {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.08em;
        color: var(--muted-dim);
        text-align: right;
        line-height: 1.6;
        white-space: nowrap;
        padding-top: 4px;
    }
    .dossier-no span { color: var(--brass); }

    /* ---------- Sections ---------- */
    .entry {
        padding: 26px 0;
        border-bottom: 1px solid var(--line);
    }
    .entry:first-of-type { padding-top: 0; }

    .entry-head {
        display: flex;
        align-items: baseline;
        gap: 12px;
        margin-bottom: 16px;
    }
    .numeral {
        font-family: 'Fraunces', serif;
        font-style: italic;
        font-size: 1.1rem;
        color: var(--brass);
        width: 26px;
    }
    .entry-title {
        font-family: 'Fraunces', serif;
        font-weight: 500;
        font-size: 1.15rem;
        letter-spacing: -0.01em;
    }
    .entry-hint {
        font-size: 0.78rem;
        color: var(--muted-dim);
        margin-left: auto;
    }

    input[type="file"] { display: none; }

    .attach-line {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 14px 18px;
        border: 1px dashed var(--line-strong);
        border-radius: 3px;
        cursor: pointer;
        transition: all 0.25s ease;
        font-size: 0.92rem;
        color: var(--muted);
    }
    .attach-line:hover, .attach-line.drag-over {
        border-color: var(--brass);
        background: var(--brass-soft);
        color: var(--parchment);
    }
    .attach-line.has-file {
        border-style: solid;
        border-color: var(--verified);
        background: var(--verified-soft);
        color: var(--parchment);
    }
    .attach-icon { font-size: 1rem; opacity: 0.85; }
    .attach-label { flex: 1; }
    .attach-meta { font-size: 0.72rem; color: var(--muted-dim); }

    textarea {
        width: 100%;
        background: transparent;
        border: none;
        border-bottom: 1px solid var(--line-strong);
        padding: 8px 2px 14px;
        color: var(--parchment);
        font-family: 'Inter', sans-serif;
        font-size: 0.94rem;
        line-height: 1.6;
        outline: none;
        resize: none;
        transition: border-color 0.25s ease;
    }
    textarea::placeholder { color: var(--muted-dim); font-style: italic; }
    textarea:focus { border-color: var(--brass); }

    /* ---------- Action ---------- */
    .action-row {
        display: flex;
        justify-content: flex-end;
        padding: 30px 0 6px;
    }
    .btn-audit {
        position: relative;
        background: transparent;
        border: 1px solid var(--brass);
        color: var(--brass);
        font-family: 'Fraunces', serif;
        font-style: italic;
        font-size: 0.98rem;
        padding: 12px 28px;
        border-radius: 3px;
        cursor: pointer;
        letter-spacing: 0.01em;
        transition: all 0.3s cubic-bezier(0.16,1,0.3,1);
        display: flex;
        align-items: center;
        gap: 10px;
        overflow: hidden;
    }
    .btn-audit::before {
        content: "";
        position: absolute;
        inset: 0;
        background: var(--brass);
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.35s cubic-bezier(0.16,1,0.3,1);
        z-index: -1;
    }
    .btn-audit:hover { color: var(--ink); }
    .btn-audit:hover::before { transform: scaleX(1); }
    .btn-audit .arrow { transition: transform 0.3s ease; }
    .btn-audit:hover .arrow { transform: translateX(4px); }
    .btn-audit.loading { pointer-events: none; opacity: 0.6; }
    .btn-audit .spinner {
        display: none;
        width: 12px; height: 12px;
        border: 1.5px solid rgba(201,162,39,0.3);
        border-top-color: var(--brass);
        border-radius: 50%;
        animation: spin 0.7s linear infinite;
    }
    .btn-audit.loading .spinner { display: inline-block; }

    /* ---------- Findings ---------- */
    .findings {
        display: none;
        margin-top: 36px;
        padding-top: 40px;
        border-top: 1px double var(--line-strong);
    }
    .findings.visible { display: block; animation: pageIn 0.7s cubic-bezier(0.16,1,0.3,1) forwards; }

    .findings-eyebrow {
        text-align: center;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--muted-dim);
        margin-bottom: 28px;
    }

    /* Venn */
    .venn-wrap {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 6px;
        margin-bottom: 40px;
    }
    .venn-svg { width: 100%; max-width: 380px; height: auto; }
    .venn-figA, .venn-figB {
        transition: transform 1.3s cubic-bezier(0.22,1,0.36,1);
    }
    .venn-label {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.62rem;
        letter-spacing: 0.06em;
        fill: var(--muted);
        text-transform: uppercase;
    }
    .venn-score {
        font-family: 'Fraunces', serif;
        font-weight: 600;
        font-size: 2.6rem;
        fill: var(--parchment);
    }
    .venn-caption {
        font-family: 'Fraunces', serif;
        font-style: italic;
        color: var(--muted);
        font-size: 0.95rem;
        margin-top: 2px;
    }

    /* Metric strip */
    .metric-strip {
        display: flex;
        justify-content: center;
        gap: 48px;
        padding: 18px 0 6px;
        margin-bottom: 8px;
    }
    .metric {
        text-align: center;
    }
    .metric .value {
        font-family: 'Fraunces', serif;
        font-weight: 600;
        font-size: 1.7rem;
    }
    .metric.match .value { color: var(--verified); }
    .metric.gap .value { color: var(--gap); }
    .metric .label {
        font-size: 0.68rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: var(--muted-dim);
        margin-top: 2px;
    }
    .metric-divider { width: 1px; background: var(--line); }

    /* Ledger lists */
    .ledger-row {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 40px;
        margin-top: 32px;
    }
    @media (max-width: 640px) { .ledger-row { grid-template-columns: 1fr; gap: 0; } }

    .ledger-col h4 {
        font-family: 'Fraunces', serif;
        font-weight: 500;
        font-size: 1rem;
        margin-bottom: 14px;
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        border-bottom: 1px solid var(--line);
        padding-bottom: 10px;
    }
    .ledger-count {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        color: var(--muted-dim);
    }
    .ledger-list { display: flex; flex-direction: column; }
    .ledger-item {
        display: flex;
        align-items: baseline;
        gap: 8px;
        padding: 9px 0;
        font-size: 0.9rem;
        opacity: 0;
        transform: translateY(4px);
        animation: itemIn 0.45s ease forwards;
    }
    .ledger-item .mark { font-size: 0.85rem; width: 14px; flex-shrink: 0; }
    .match .mark { color: var(--verified); }
    .gap .mark { color: var(--gap); }
    .ledger-item .name { text-transform: capitalize; }
    .leader {
        flex: 1;
        border-bottom: 1px dotted var(--line-strong);
        margin: 0 6px;
        transform: translateY(-4px);
    }
    .ledger-item .status {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.66rem;
        color: var(--muted-dim);
        letter-spacing: 0.03em;
    }
    .ledger-item a.status {
        color: var(--brass);
        text-decoration: none;
        border-bottom: 1px solid transparent;
        transition: border-color 0.2s ease;
    }
    .ledger-item a.status:hover { border-color: var(--brass); }
    .empty-note {
        font-size: 0.85rem;
        color: var(--muted-dim);
        font-style: italic;
        font-family: 'Fraunces', serif;
        padding: 6px 0;
    }

    @keyframes pageIn {
        from { opacity: 0; transform: translateY(16px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes itemIn {
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes spin { to { transform: rotate(360deg); } }

    @media (prefers-reduced-motion: reduce) {
        * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
    }

    :focus-visible { outline: 1px solid var(--brass); outline-offset: 3px; }
</style>
</head>
<body>

<div class="dossier">

    <div class="letterhead">
        <div class="brand">
            <svg class="seal" viewBox="0 0 48 48" fill="none">
                <circle cx="24" cy="24" r="22" stroke="#C9A227" stroke-width="1"/>
                <circle cx="24" cy="24" r="18" stroke="#C9A227" stroke-width="0.5" opacity="0.5"/>
                <circle cx="19" cy="24" r="10" stroke="#C9A227" stroke-width="1" fill="none"/>
                <circle cx="29" cy="24" r="10" stroke="#C9A227" stroke-width="1" fill="none"/>
            </svg>
            <div>
                <div class="brand-name">SkillSync</div>
                <div class="brand-sub">a private audit of candidate &amp; role</div>
            </div>
        </div>
        <div class="dossier-no">DOSSIER <span>N&deg;014</span><br>issued on review</div>
    </div>

    <div class="entry">
        <div class="entry-head">
            <span class="numeral">I.</span>
            <span class="entry-title">Candidate Profile</span>
            <span class="entry-hint">.txt only</span>
        </div>
        <input type="file" id="resume_upload" accept=".txt">
        <div class="attach-line" id="upload-zone">
            <span class="attach-icon">📎</span>
            <span class="attach-label" id="upload-text">Attach resume — drop file or click to browse</span>
            <span class="attach-meta" id="upload-meta"></span>
        </div>
    </div>

    <div class="entry">
        <div class="entry-head">
            <span class="numeral">II.</span>
            <span class="entry-title">Target Requirements</span>
        </div>
        <textarea id="job_text" rows="4" placeholder="Transcribe the job description or required credentials here..."></textarea>
    </div>

    <div class="action-row">
        <button class="btn-audit" id="run-btn" onclick="runInference()">
            <span class="spinner"></span>
            <span class="btn-label">Conduct the Audit</span>
            <span class="arrow">→</span>
        </button>
    </div>

    <div class="findings" id="results">
        <div class="findings-eyebrow">— Findings —</div>

        <div class="venn-wrap">
            <svg class="venn-svg" viewBox="0 0 380 200">
                <g class="venn-figA" id="venn-a">
                    <circle cx="150" cy="95" r="62" fill="#7FAE87" fill-opacity="0.45" style="mix-blend-mode:multiply;"/>
                    <text x="90" y="45" class="venn-label">CANDIDATE</text>
                </g>
                <g class="venn-figB" id="venn-b">
                    <circle cx="230" cy="95" r="62" fill="#C9A227" fill-opacity="0.45" style="mix-blend-mode:multiply;"/>
                    <text x="255" y="45" class="venn-label">ROLE</text>
                </g>
                <text x="190" y="102" text-anchor="middle" class="venn-score" id="venn-score">0%</text>
            </svg>
            <div class="venn-caption" id="venn-caption">synchronized</div>
        </div>

        <div class="metric-strip">
            <div class="metric match">
                <div class="value" id="val-match">0</div>
                <div class="label">Verified</div>
            </div>
            <div class="metric-divider"></div>
            <div class="metric gap">
                <div class="value" id="val-gaps">0</div>
                <div class="label">Gaps</div>
            </div>
        </div>

        <div class="ledger-row">
            <div class="ledger-col">
                <h4>Verified Capabilities <span class="ledger-count" id="match-count">0</span></h4>
                <div class="ledger-list" id="match-list"></div>
            </div>
            <div class="ledger-col">
                <h4>Capability Gaps <span class="ledger-count" id="gap-count">0</span></h4>
                <div class="ledger-list" id="gap-list"></div>
            </div>
        </div>
    </div>

</div>

<script>
    let fileContent = "";
    const uploadZone = document.getElementById('upload-zone');
    const uploadInput = document.getElementById('resume_upload');
    const uploadText = document.getElementById('upload-text');
    const uploadMeta = document.getElementById('upload-meta');

    uploadZone.addEventListener('click', () => uploadInput.click());
    ['dragover', 'dragenter'].forEach(evt => uploadZone.addEventListener(evt, (e) => {
        e.preventDefault(); uploadZone.classList.add('drag-over');
    }));
    ['dragleave', 'dragend'].forEach(evt => uploadZone.addEventListener(evt, () => uploadZone.classList.remove('drag-over')));
    uploadZone.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadZone.classList.remove('drag-over');
        const file = e.dataTransfer.files[0];
        if (file) handleFile(file);
    });
    uploadInput.addEventListener('change', (e) => { if (e.target.files[0]) handleFile(e.target.files[0]); });

    function handleFile(file) {
        uploadText.innerText = file.name;
        uploadMeta.innerText = "received";
        uploadZone.classList.add('has-file');
        const reader = new FileReader();
        reader.onload = (evt) => { fileContent = evt.target.result; };
        reader.readAsText(file);
    }

    function runInference() {
        const jobText = document.getElementById('job_text').value;
        const btn = document.getElementById('run-btn');
        if (!fileContent || !jobText) {
            alert("Please attach a resume and transcribe the target requirements first.");
            return;
        }
        btn.classList.add('loading');

        setTimeout(() => {
            btn.classList.remove('loading');
            const resume_lower = fileContent.toLowerCase();
            const job_lower = jobText.toLowerCase();
            const core_skills = ['python', 'java', 'sql', 'machine learning', 'react', 'html', 'css', 'data structures', 'algorithms', 'aws', 'git'];
            let matched = [], gaps = [];
            core_skills.forEach(skill => {
                if (job_lower.includes(skill)) {
                    if (resume_lower.includes(skill)) matched.push(skill);
                    else gaps.push(skill);
                }
            });
            const total = matched.length + gaps.length;
            const score = total > 0 ? Math.round((matched.length / total) * 100) : 0;

            document.getElementById('val-match').innerText = matched.length;
            document.getElementById('val-gaps').innerText = gaps.length;
            document.getElementById('venn-score').innerText = score + "%";

            const caption = document.getElementById('venn-caption');
            caption.innerText = score >= 80 ? "closely synchronized" : score >= 50 ? "partially synchronized" : score > 0 ? "loosely synchronized" : "not yet synchronized";

            // Move circles together proportional to score
            const maxShift = 34;
            const shift = (score / 100) * maxShift;
            document.getElementById('venn-a').style.transform = `translateX(${shift}px)`;
            document.getElementById('venn-b').style.transform = `translateX(-${shift}px)`;

            const matchList = document.getElementById('match-list');
            document.getElementById('match-count').innerText = matched.length;
            matchList.innerHTML = "";
            if (matched.length) {
                matched.forEach((skill, i) => {
                    const row = document.createElement('div');
                    row.className = 'ledger-item match';
                    row.style.animationDelay = (i * 0.07) + 's';
                    row.innerHTML = `<span class="mark">✓</span><span class="name">${skill}</span><span class="leader"></span><span class="status">confirmed</span>`;
                    matchList.appendChild(row);
                });
            } else {
                matchList.innerHTML = `<div class="empty-note">No overlapping capabilities on file.</div>`;
            }

            const gapList = document.getElementById('gap-list');
            document.getElementById('gap-count').innerText = gaps.length;
            gapList.innerHTML = "";
            if (gaps.length) {
                gaps.forEach((skill, i) => {
                    const row = document.createElement('div');
                    row.className = 'ledger-item gap';
                    row.style.animationDelay = (i * 0.07) + 's';
                    row.innerHTML = `<span class="mark">—</span><span class="name">${skill}</span><span class="leader"></span><a class="status" href="https://www.youtube.com/results?search_query=${encodeURIComponent(skill)}+course" target="_blank">pursue ↗</a>`;
                    gapList.appendChild(row);
                });
            } else {
                gapList.innerHTML = `<div class="empty-note">Every requirement accounted for.</div>`;
            }

            document.getElementById('results').classList.add('visible');
            document.getElementById('results').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }, 900);
    }
</script>
</body>
</html>
"""

st.components.v1.html(premium_ui_html, height=1100, scrolling=True)
