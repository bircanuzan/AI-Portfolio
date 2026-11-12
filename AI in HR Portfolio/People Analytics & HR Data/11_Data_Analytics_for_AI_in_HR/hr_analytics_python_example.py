"""
AI in HR Analytics Lab - Python example
Synthetic data only. Purpose: demonstrate practical HR analytics workflow.
"""
import pandas as pd

df = pd.read_csv("synthetic_hr_data.csv")

# Data-quality checks
assert df["employee_id"].is_unique
assert df["performance_rating"].between(1, 5).all()
assert df["skill_level"].between(1, 5).all()

# Workforce KPIs
kpis = {
    "headcount": len(df),
    "exit_rate_pct": round(df["exit_12m"].mean() * 100, 1),
    "internal_mobility_pct": round(df["internal_move_12m"].mean() * 100, 1),
    "avg_time_to_fill_days": round(df["time_to_fill_days"].mean(), 1),
    "avg_learning_hours": round(df["learning_hours"].mean(), 1),
}

# Department analytics
department = (
    df.groupby("department")
      .agg(
          headcount=("employee_id", "count"),
          exits=("exit_12m", "sum"),
          avg_tenure=("tenure_years", "mean"),
          avg_performance=("performance_rating", "mean"),
          avg_learning_hours=("learning_hours", "mean"),
      )
      .reset_index()
)
department["exit_rate_pct"] = (department["exits"] / department["headcount"] * 100).round(1)

# Skills intelligence
skills = (
    df.groupby("primary_skill")
      .agg(
          employees=("employee_id", "count"),
          avg_skill_level=("skill_level", "mean"),
          below_proficiency=("skill_level", lambda s: (s < 3).sum()),
      )
      .reset_index()
      .sort_values("below_proficiency", ascending=False)
)

# Example AI-ready aggregate summary.
# Only aggregate, validated metrics should be sent to an approved enterprise LLM.
ai_context = {
    "kpis": kpis,
    "department_metrics": department.round(2).to_dict(orient="records"),
    "skills_metrics": skills.round(2).to_dict(orient="records"),
}
print(kpis)
