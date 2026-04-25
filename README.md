# 🤖 Excel AI Financial Report Generator

> **Day 3 Build** | Notion Idea: *Automate Excel using AI and build financial reports*

Auto-analyze any Excel/CSV file and generate a professional financial summary report with charts — powered by Python, Pandas, Matplotlib, and OpenAI.

---

## 🚀 Features

- 📊 Auto-detects numeric columns (revenue, expenses, profit, etc.)
- 📈 Generates bar + line charts automatically
- 🤖 AI summary of key financial insights via OpenAI GPT
- 📄 Outputs a clean HTML report
- 💡 Works with any CSV or XLSX file — zero config

---

## 📦 Stack

| Layer | Tool |
|---|---|
| Data | Pandas, openpyxl |
| Charts | Matplotlib, Seaborn |
| AI Summary | OpenAI GPT-4o-mini |
| Report | Jinja2 HTML template |
| CLI | argparse |

---

## ⚡ Quick Start

```bash
# 1. Clone
git clone https://github.com/aadi4frnzzz-crypto/excel-ai-financial-report
cd excel-ai-financial-report

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your OpenAI key
export OPENAI_API_KEY=your_key_here

# 4. Run on your file
python main.py --file data/sample_financials.csv --output report.html

# 5. Open report
open report.html
```

---

## 📁 Project Structure

```
excel-ai-financial-report/
├── main.py              # CLI entry point
├── analyzer.py          # Data analysis engine
├── chart_generator.py   # Chart generation
├── ai_summary.py        # OpenAI GPT summary
├── report_builder.py    # HTML report builder
├── templates/
│   └── report.html      # Jinja2 report template
├── data/
│   └── sample_financials.csv  # Sample data
├── requirements.txt
└── README.md
```

---

## 📊 Sample Output

The generated report includes:
- **KPI cards** — Total Revenue, Total Expenses, Net Profit, Profit Margin
- **Monthly trend chart** — Revenue vs Expenses line chart
- **Category breakdown** — Bar chart by department/category
- **AI Insight paragraph** — GPT-generated plain-English analysis

---

## 🗺️ Roadmap

- [ ] PDF export (WeasyPrint)
- [ ] Multi-sheet Excel support
- [ ] Streamlit web UI
- [ ] Scheduled email delivery
- [ ] TradingView data integration

---

*Built from Notion idea vault → [aadi4frnzzz-crypto](https://github.com/aadi4frnzzz-crypto)*
