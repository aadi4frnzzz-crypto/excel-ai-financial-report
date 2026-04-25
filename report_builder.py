from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import datetime


class ReportBuilder:
    def __init__(self, stats: dict, charts: dict, ai_insight: str):
        self.stats = stats
        self.charts = charts
        self.ai_insight = ai_insight

    def build(self, output_path: str):
        template_dir = Path(__file__).parent / "templates"
        env = Environment(loader=FileSystemLoader(str(template_dir)))
        template = env.get_template("report.html")

        html = template.render(
            stats=self.stats,
            charts=self.charts,
            ai_insight=self.ai_insight,
            generated_at=datetime.datetime.now().strftime("%B %d, %Y %I:%M %p"),
        )

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)
