# Site Doctor — AI Web Accessibility & SEO Audit Agent

A Google ADK 2.0 agent that automatically audits websites for accessibility violations and SEO issues, proposes fixes, and generates compliance reports.

## What It Does

1. **Fetches** a website's HTML
2. **Analyzes** it for 6 common accessibility violations
3. **Routes** issues: auto-fixable vs. needs human review
4. **Human Approval** — you approve/reject proposed fixes
5. **Generates** corrected HTML snippets
6. **Evaluates** compliance score (before/after)
7. **Reports** findings in clean markdown

## Quick Start

### Requirements
- Python 3.10+
- `uv` package manager
- Google API Key (free Gemini API)

### Setup

```bash
# Clone and enter project
cd site-doctor

# Install dependencies
uv add google-adk httpx beautifulsoup4 rich python-dotenv reportlab

# Create .env with your API key
echo "GOOGLE_API_KEY=your_key_here" > .env

# Run the agent
uv run python agent.py
```

### Output

Generates:
- `site_doctor_report.md` (Markdown summary)
- `site_doctor_report.pdf` (Professional enterprise PDF report featuring metric cards, severity badges, preformatted wrapped code blocks, and dynamic page numbering)

## Architecture