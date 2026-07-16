SkillSync Engine
A high-fidelity, dark-mode resume parsing and skill-gap assessment platform. Built on top of Streamlit using a bespoke, minimalist HTML5/JS interface that mimics modern design patterns seen in production platforms like Linear and Vercel.

Architecture & Design Philosophy
Rather than relying on generic out-of-the-box component styling, this application injects a custom-tailored document fragment into the page, bypassing Streamlit’s standard UI blocks.

Bento Grid Layout: Clean, structured micro-cards prioritizing readability and spatial symmetry.

Luxury Micro-Interactions: Subtle hover states and zero-latency border transformations that activate contextually.

Asynchronous Shutter Loading: High-fidelity transition states built using CSS transitions for an interactive, responsive feel.

Features
Candidate Parser: Upload standard .txt resume files and capture raw credentials.

Requirement Profiler: Input target roles, framework specifications, or raw job descriptions.

Dynamic Skill-Mapping Matrix: Instantly compares standard technical skills to flag overlaps and missing modules.

Interactive Action Links: Auto-generates customized external upskilling paths for identified core gaps.

Technical Stack
Framework: Streamlit (Python 3.10+)

Runtime Component: Streamlit Custom HTML Component (v1)

UI Architecture: Custom HTML5, CSS3 Variables, ES6 JavaScript

Fonts: Inter & JetBrains Mono (Via Google Fonts API)

Quick Start
1. Prerequisites
Ensure you have Python installed on your system.

Bash
python --version
2. Installation
Clone the workspace and install the single dependency required to boot the Streamlit container:

Bash
pip install streamlit
3. Run the App
Execute the Streamlit runtime directly from your terminal:

Bash
streamlit run app.py
File Structure
Plaintext
├── app.py              # Main Streamlit driver file with UI injection
└── README.md           # Documentation & Architecture overview
