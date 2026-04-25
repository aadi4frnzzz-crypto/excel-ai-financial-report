import pandas as pd
import numpy as np
from pathlib import Path


class DataAnalyzer:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.df = self._load()

    def _load(self) -> pd.DataFrame:
        suffix = self.file_path.suffix.lower()
        if suffix == ".csv":
            return pd.read_csv(self.file_path)
        elif suffix in [".xlsx", ".xls"]:
            return pd.read_excel(self.file_path)
        else:
            raise ValueError(f"Unsupported file type: {suffix}")

    def analyze(self) -> dict:
        df = self.df
        numeric_df = df.select_dtypes(include=[np.number])
        date_cols = [c for c in df.columns if "date" in c.lower() or "month" in c.lower() or "year" in c.lower()]

        # Auto-detect financial columns
        revenue_cols = [c for c in numeric_df.columns if any(k in c.lower() for k in ["revenue", "income", "sales", "earning"])]
        expense_cols = [c for c in numeric_df.columns if any(k in c.lower() for k in ["expense", "cost", "spend", "loss"])]
        profit_cols = [c for c in numeric_df.columns if any(k in c.lower() for k in ["profit", "margin", "net"])]

        stats = {
            "file_name": self.file_path.name,
            "row_count": len(df),
            "col_count": len(df.columns),
            "numeric_cols": len(numeric_df.columns),
            "columns": list(df.columns),
            "date_cols": date_cols,
            "revenue_cols": revenue_cols,
            "expense_cols": expense_cols,
            "profit_cols": profit_cols,
            "summary": numeric_df.describe().to_dict(),
            "totals": numeric_df.sum().to_dict(),
            "means": numeric_df.mean().to_dict(),
        }

        # KPI calculations
        if revenue_cols:
            stats["total_revenue"] = float(df[revenue_cols[0]].sum())
        if expense_cols:
            stats["total_expenses"] = float(df[expense_cols[0]].sum())
        if revenue_cols and expense_cols:
            stats["net_profit"] = stats.get("total_revenue", 0) - stats.get("total_expenses", 0)
            rev = stats.get("total_revenue", 0)
            stats["profit_margin"] = round((stats["net_profit"] / rev * 100), 2) if rev else 0

        return stats
