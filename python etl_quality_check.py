# Project: Enterprise Data Quality & ETL Monitor Dashboard
# Author: Aakash Srivastava
# Tools: Python (Pandas, smtplib), Power BI, SQL (Simulated with CSV)

import pandas as pd
import numpy as np
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import warnings
warnings.filterwarnings('ignore')

# Step 1: Load the ETL Data (Simulated CSV)
def load_data(file_path):
    try:
        df = pd.read_csv(file_path, parse_dates=['start_time', 'end_time'])
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Step 2: Basic Data Quality Checks
def check_data_quality(df):
    quality_report = {}

    quality_report['total_rows'] = len(df)
    quality_report['null_percent'] = df.isnull().mean() * 100
    quality_report['duplicate_count'] = df.duplicated().sum()

    # Delay in job runs (in minutes)
    df['delay_minutes'] = (df['end_time'] - df['start_time']).dt.total_seconds() / 60
    quality_report['avg_delay_minutes'] = df['delay_minutes'].mean()

    print("Data quality check complete.")
    return df, quality_report

# Step 3: Simple Alert Function if Nulls > 5%
def check_and_alert(quality_report, email_recipient):
    alert_triggered = False
    null_columns = quality_report['null_percent'][quality_report['null_percent'] > 5]

    if not null_columns.empty:
        alert_triggered = True
        message = f"Warning: High null values detected in columns:\n{null_columns.to_string()}"
        send_email_alert(message, email_recipient)
    else:
        print("No major null values detected.")

    return alert_triggered

# Step 4: Send Email (Console Simulated)
def send_email_alert(message, recipient):
    print("\n[EMAIL SENT SIMULATION]")
    print(f"To: {recipient}\nSubject: ETL Data Quality Alert\nMessage:\n{message}\n")
    # You can use smtplib for real emails (Gmail SMTP, etc.)

# Step 5: Export Clean Data for Power BI Dashboard
def export_clean_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Clean data exported to {output_path}")

# Run the full process
def run_etl_quality_pipeline():
    file_path = 'data/etl_sample_data.csv'  # Add your CSV path here
    email = 'data.team76@gmail.com'  # Simulated email

    df = load_data(file_path)
    if df is not None:
        df, report = check_data_quality(df)
        alert = check_and_alert(report, email)
        export_clean_data(df, 'data/etl_clean_output.csv')
        print("\nFinal Quality Report:")
        print(report)

if __name__ == "__main__":
    run_etl_quality_pipeline()
