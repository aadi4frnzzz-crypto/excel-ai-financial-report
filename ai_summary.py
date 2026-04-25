import os
from openai import OpenAI


class AISummary:
    def __init__(self, stats: dict):
        self.stats = stats
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate(self) -> str:
        stats = self.stats
        prompt = f"""You are a financial analyst. Analyze this data summary and give a concise 3-4 sentence business insight:

File: {stats.get('file_name')}
Rows: {stats.get('row_count')}
Total Revenue: {stats.get('total_revenue', 'N/A')}
Total Expenses: {stats.get('total_expenses', 'N/A')}
Net Profit: {stats.get('net_profit', 'N/A')}
Profit Margin: {stats.get('profit_margin', 'N/A')}%
Column Totals: {stats.get('totals', {})}

Provide actionable insights, flag any red flags, and suggest 1 improvement."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300,
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"AI summary unavailable: {str(e)}"
