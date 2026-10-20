import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def generate_sample_data(n_customers=1000, seed=42):
    """Generate sample transactional data."""
    np.random.seed(seed)  # Set random seed for reproducibility

    # Define the number of transactions and date range
    start_date = pd.to_datetime("2024-01-01")
    end_date = pd.to_datetime("2024-12-31")

    # Create random customer IDs, transaction dates, and sales amounts
    customer_ids = np.random.choice(range(1, 1001), n_customers)
    transaction_dates = pd.to_datetime(np.random.randint(start_date.value, end_date.value, n_customers, dtype=np.int64), unit='ns')
    sales = np.random.randint(10, 1000, n_customers)

    # Create a DataFrame to store the generated data
    data = pd.DataFrame({
        "CustomerID": customer_ids,
        "TransactionDate": transaction_dates,
        "Sales": sales
    })

    return data


def save_sample_data(data, file_path="cohort_analysis_data.csv"):
    """Save the generated data to a CSV file for reference."""
    data.to_csv(file_path, index=False)
    print(f"Sample data saved to: {file_path}")


def add_cohort_columns(data):
    """Add OrderMonth and CohortMonth columns to the data."""
    # Add the "OrderMonth" column to represent the month of each transaction
    data["OrderMonth"] = data["TransactionDate"].dt.to_period("M")

    # Add the "CohortMonth" column to represent the first transaction month of each customer
    data["CohortMonth"] = data.groupby("CustomerID")["TransactionDate"].transform("min").dt.to_period("M")

    return data


def get_months_difference(df):
    """Calculate the difference in months between OrderMonth and CohortMonth."""
    return (df["OrderMonth"].dt.year - df["CohortMonth"].dt.year) * 12 + (df["OrderMonth"].dt.month - df["CohortMonth"].dt.month)


def add_cohort_index(data):
    """Add the CohortIndex column (number of months since the first purchase)."""
    data["CohortIndex"] = get_months_difference(data)
    return data


def calculate_cohort_data(data):
    """Group data by CohortMonth and CohortIndex and count unique customers."""
    return data.groupby(["CohortMonth", "CohortIndex"])["CustomerID"].nunique().unstack(1)


def calculate_retention(cohort_data):
    """Calculate retention rates as percentages of the cohort size."""
    cohort_sizes = cohort_data.iloc[:, 0]  # Get the size of each cohort (first column)
    return cohort_data.divide(cohort_sizes, axis=0) * 100  # Calculate retention as percentages


def save_retention(retention, file_path="temp/cohort_retention.csv"):
    """Save the retention rates to a CSV file."""
    retention.to_csv(file_path)
    print(f"Cohort retention data saved to: {file_path}")


def plot_retention_heatmap(retention, file_path="temp/cohort_retention_heatmap.png"):
    """Visualize the cohort analysis using a heatmap."""
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
    plt.savefig(file_path)
    plt.show()


def main():
    """Run the full cohort analysis pipeline."""
    # 1. Generate sample transactional data
    data = generate_sample_data(n_customers=1000)

    # Save the generated data to a CSV file for reference
    save_sample_data(data)

    # 2. Perform cohort analysis
    data = add_cohort_columns(data)

    # Apply the function to calculate the CohortIndex (number of months since the first purchase)
    data = add_cohort_index(data)

    # Group data by CohortMonth and CohortIndex and count the unique customers
    cohort_data = calculate_cohort_data(data)

    # Calculate retention rates by dividing the number of customers in each period by the size of the cohort
    retention = calculate_retention(cohort_data)

    # Save the retention rates to a CSV file
    save_retention(retention)

    # 3. Visualize the cohort analysis using a heatmap
    plot_retention_heatmap(retention)

    print("Cohort analysis heatmap saved as 'cohort_retention_heatmap.png'")


if __name__ == '__main__':
    main()
