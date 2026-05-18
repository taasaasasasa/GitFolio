# GitFolio: Automated Resume Compiler 🚀

An open-source, automated resume pipeline that dynamically compiles a clean, beautifully styled standalone HTML portfolio document directly from a single structured `resume.json` dataset. 

This repository leverages a built-in Python compilation engine coupled with GitHub Actions automation to instantly rebuild and update your public-facing resume file the exact second you push modifications to your structured data.

---

## 🛠️ System Architecture

* **Data Layer (`resume.json`):** A strict schema-compliant JSON file housing cleanly isolated resume blocks (Education, Skills, Projects, and Professional Summaries).
* **Compilation Engine (`build_resume.py`):** A lightweight local Python automation script featuring multi-platform universal `UTF-8` charmap encoding to natively support clean web formatting and system emojis.
* **Automation Workflow (`.github/workflows/generate.yml`):** A cloud-hosted CI/CD pipeline triggered exclusively on modifications to your source data. It fires up an ephemeral runner, builds the workspace environment, runs the compilation engine, and automatically commits the resulting production document.

---

## 💻 Local Installation & Usage

To run the pipeline locally and preview document modifications dynamically on your machine:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/your-github-username/gitfolio.git](https://github.com/your-github-username/gitfolio.git)
   cd gitfolio