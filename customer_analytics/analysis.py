import pandas as pd
from ydata_profiling import ProfileReport
from .config import REPORT_PATH

def generate_profile(df, report_name="profile_report.html"):
    profile = ProfileReport(df, title="Customer Purchases Profiling", explorative=True)
    report_file = REPORT_PATH / report_name
    profile.to_file(report_file)
    print(f"Profiling report generated at: {report_file}")

def log_basic_summary(df):
    print("Basic Data Summary:")
    print(df.describe(include="all"))
