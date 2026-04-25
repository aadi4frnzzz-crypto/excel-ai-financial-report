import matplotlib
matplotlib.use("Agg")  # Non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import base64
from io import BytesIO

sns.set_theme(style="whitegrid", palette="muted")


class ChartGenerator:
    def __init__(self, df: pd.DataFrame, stats: dict):
        self.df = df
        self.stats = stats

    def _fig_to_base64(self, fig) -> str:
        buf = BytesIO()
        fig.savefig(buf, format="png", dpi=120, bbox_inches="tight")
        buf.seek(0)
        encoded = base64.b64encode(buf.read()).decode("utf-8")
        plt.close(fig)
        return encoded

    def revenue_expense_trend(self) -> str | None:
        rev_cols = self.stats.get("revenue_cols", [])
        exp_cols = self.stats.get("expense_cols", [])
        date_cols = self.stats.get("date_cols", [])

        if not (rev_cols and exp_cols):
            return None

        fig, ax = plt.subplots(figsize=(10, 5))
        x = self.df[date_cols[0]] if date_cols else range(len(self.df))
        ax.plot(x, self.df[rev_cols[0]], label="Revenue", marker="o", linewidth=2, color="#2ecc71")
        ax.plot(x, self.df[exp_cols[0]], label="Expenses", marker="s", linewidth=2, color="#e74c3c")
        ax.set_title("Revenue vs Expenses Trend", fontsize=14, fontweight="bold")
        ax.set_xlabel("Period")
        ax.set_ylabel("Amount (₹)")
        ax.legend()
        plt.xticks(rotation=45)
        return self._fig_to_base64(fig)

    def numeric_bar_chart(self) -> str:
        numeric_df = self.df.select_dtypes(include=[np.number])
        totals = numeric_df.sum().sort_values(ascending=False).head(8)

        fig, ax = plt.subplots(figsize=(10, 5))
        bars = ax.bar(totals.index, totals.values, color=sns.color_palette("muted", len(totals)))
        ax.set_title("Column Totals Overview", fontsize=14, fontweight="bold")
        ax.set_ylabel("Total Value")
        plt.xticks(rotation=30, ha="right")
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() * 1.01,
                    f"{bar.get_height():,.0f}", ha="center", va="bottom", fontsize=9)
        return self._fig_to_base64(fig)

    def profit_margin_gauge(self) -> str | None:
        margin = self.stats.get("profit_margin")
        if margin is None:
            return None

        fig, ax = plt.subplots(figsize=(6, 4))
        color = "#2ecc71" if margin >= 20 else "#f39c12" if margin >= 10 else "#e74c3c"
        ax.barh(["Profit Margin"], [margin], color=color, height=0.4)
        ax.barh(["Profit Margin"], [100 - margin], left=[margin], color="#ecf0f1", height=0.4)
        ax.set_xlim(0, 100)
        ax.set_title(f"Profit Margin: {margin}%", fontsize=14, fontweight="bold")
        ax.set_xlabel("Percentage (%)")
        ax.axvline(x=20, color="gray", linestyle="--", alpha=0.5, label="20% benchmark")
        ax.legend()
        return self._fig_to_base64(fig)

    def generate_all(self) -> dict:
        charts = {}
        trend = self.revenue_expense_trend()
        if trend:
            charts["trend"] = trend
        charts["bar"] = self.numeric_bar_chart()
        margin = self.profit_margin_gauge()
        if margin:
            charts["margin"] = margin
        return charts
