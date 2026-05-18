import json
import os

def load_json_file(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def generate_resume_html():
    # 1. Load User's Data Safely
    resume = load_json_file("resume.json")
    if not resume:
        print("❌ Error: resume.json not found! Ensure it's in the same folder.")
        return

    # 2. Build a beautifully styled standalone HTML Resume
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{resume.get('name', 'Resume')} - Portfolio</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            line-height: 1.5;
            color: #333;
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
        }}
        .header {{
            text-align: center;
            border-bottom: 2px solid #222;
            padding-bottom: 15px;
            margin-bottom: 20px;
        }}
        .header h1 {{
            margin: 0 0 5px 0;
            font-size: 28px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .header p {{
            margin: 5px 0;
            font-size: 14px;
            color: #666;
        }}
        .section-title {{
            font-size: 18px;
            text-transform: uppercase;
            border-bottom: 1px solid #aaa;
            margin-top: 25px;
            margin-bottom: 10px;
            padding-bottom: 3px;
            font-weight: bold;
            color: #111;
        }}
        .entry {{
            margin-bottom: 15px;
        }}
        .entry-header {{
            display: flex;
            justify-content: space-between;
            font-weight: bold;
            font-size: 15px;
        }}
        .entry-sub {{
            font-style: italic;
            color: #555;
            margin-bottom: 5px;
        }}
        ul {{
            margin: 5px 0 0 0;
            padding-left: 20px;
            font-size: 14px;
        }}
        .skills-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }}
        .skills-table td {{
            padding: 4px 0;
            vertical-align: top;
        }}
        .skills-label {{
            font-weight: bold;
            width: 25%;
        }}
    </style>
</head>
<body>

    <div class="header">
        <h1>{resume.get('name', 'Your Name')}</h1>
        <p>📬 {resume.get('contact', {}).get('email', '')} | 💻 <a href="{resume.get('contact', {}).get('github', '#')}">{resume.get('contact', {}).get('github', '')}</a></p>
    </div>

    <div class="section-title">Focus & Summary</div>
    <div class="entry" style="font-size: 14px;">
        {resume.get('title', 'Software Developer')} focused on clean architecture, efficient data structures, and automation development.
    </div>

    <div class="section-title">🎓 Education</div>
"""

    # Add Education Entries dynamically
    for edu in resume.get('education', []):
        html += f"""
    <div class="entry">
        <div class="entry-header">
            <span>{edu.get('institution', '')}</span>
        </div>
        <div class="entry-sub">{edu.get('degree', '')}</div>
        {f'<ul><li>{edu.get("details", "")}</li></ul>' if "details" in edu else ''}
    </div>"""

    # Add Technical Skills Section
    html += """
    <div class="section-title">🛠️ Technical Skills</div>
    <table class="skills-table">"""
    
    skills = resume.get('skills', {})
    if 'languages' in skills:
        html += f"""
        <tr>
            <td class="skills-label">Languages:</td>
            <td>{', '.join(skills['languages'])}</td>
        </tr>"""
    if 'technologies' in skills:
        html += f"""
        <tr>
            <td class="skills-label">Tools & Frameworks:</td>
            <td>{', '.join(skills['technologies'])}</td>
        </tr>"""
        
    html += """
    </table>

    <div class="section-title">🚀 Projects</div>"""

    # Add Project Entries dynamically
    for proj in resume.get('projects', []):
        html += f"""
    <div class="entry">
        <div class="entry-header">
            <span>{proj.get('name', '')}</span>
            <span style="font-weight: normal; font-size: 13px; font-style: italic;">{proj.get('tech_stack', '')}</span>
        </div>
        <ul>
            <li>{proj.get('description', '')}</li>
        </ul>
    </div>"""

    html += """
</body>
</html>"""

    # 4. Output as a clean standalone resume file using modern encoding
    with open("resume.html", "w", encoding="utf-8") as f:
        f.write(html)
        
    print("🚀 Standalone 'resume.html' has been successfully compiled!")

if __name__ == "__main__":
    generate_resume_html()