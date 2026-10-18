from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from app.models.cohort_models import RetentionResponse, RetentionRow

BASE_DIR = Path(__file__).resolve().parents[2] / "product" / "frameworks" / "cohort"


def build_cohort_analysis() -> RetentionResponse:
    # 1. Generate sample transactional data
    np.random.seed(42)

    # Define the number of transactions and date range
    n_customers = 1000
    start_date = pd.to_datetime("2024-01-01")
    end_date = pd.to_datetime("2024-12-31")

    # Create random customer IDs, transaction dates, and sales amounts
    customer_ids = np.random.choice(range(1, 1001), n_customers)
    transaction_dates = pd.to_datetime(
        np.random.randint(start_date.value, end_date.value, n_customers, dtype=np.int64), unit='ns'
    )
    sales = np.random.randint(10, 1000, n_customers)

    # Create a DataFrame to store the generated data
    data = pd.DataFrame({
        "CustomerID": customer_ids,
        "TransactionDate": transaction_dates,
        "Sales": sales
    })

    # Save the generated data to a CSV file for reference
    file_path = BASE_DIR / "cohort_analysis_data.csv"
    data.to_csv(file_path, index=False)
    print(f"Sample data saved to: {file_path}")

    # 2. Perform cohort analysis
    # Add the "OrderMonth" column to represent the month of each transaction
    data["OrderMonth"] = data["TransactionDate"].dt.to_period("M")

    # Add the "CohortMonth" column to represent the first transaction month of each customer
    data["CohortMonth"] = data.groupby("CustomerID")["TransactionDate"].transform("min").dt.to_period("M")

    # Function to calculate the difference in months between OrderMonth and CohortMonth
    def get_months_difference(df):
        return (df["OrderMonth"].dt.year - df["CohortMonth"].dt.year) * 12 + (
            df["OrderMonth"].dt.month - df["CohortMonth"].dt.month
        )

    # Apply the function to calculate the CohortIndex (number of months since the first purchase)
    data["CohortIndex"] = get_months_difference(data)

    # Group data by CohortMonth and CohortIndex and count the unique customers
    cohort_data = data.groupby(["CohortMonth", "CohortIndex"])["CustomerID"].nunique().unstack(1)

    # Calculate retention rates by dividing the number of customers in each period by the size of the cohort
    cohort_sizes = cohort_data.iloc[:, 0]
    retention = cohort_data.divide(cohort_sizes, axis=0) * 100

    # Save the retention rates to a CSV file
    retention_file_path = BASE_DIR / "cohort_retention.csv"
    retention.to_csv(retention_file_path)
    print(f"Cohort retention data saved to: {retention_file_path}")

    # 3. Visualize the cohort analysis using a heatmap
    # Set up the plot
    plt.figure(figsize=(12, 8))
    plt.title("Cohort Analysis: Customer Retention (%)")  # Title for the heatmap

    # Create the heatmap with retention data
    sns.heatmap(retention, annot=True, fmt=".1f", cmap="coolwarm", cbar=True)

    # Label the axes
    plt.ylabel("Cohorts (First Purchase Month)")
    plt.xlabel("Cohort Period (Months Since First Purchase)")

    # Adjust layout and save the heatmap as a PNG image
    plt.tight_layout()
    plt.savefig(BASE_DIR / "cohort_retention_heatmap.png")
    plt.close()

    print("Cohort analysis heatmap saved as 'cohort_retention_heatmap.png'")

    # 4. Retention in JSON for the browser
    rows = [
        RetentionRow(
            cohort_month=str(cohort_month),
            retention=[None if pd.isna(v) else round(float(v), 2) for v in values],
        )
        for cohort_month, values in retention.iterrows()
    ]
    return RetentionResponse(count=len(rows), rows=rows)
