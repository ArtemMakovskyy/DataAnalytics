import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.pyplot as plt


def generate_sample_data(n_customers=1000, n_transactions=5000, seed=42):
    """Generate sample transaction data."""
    np.random.seed(seed)

    # Generate customer IDs
    customer_ids = [f'CUST_{i:04d}' for i in range(n_customers)]

    # Generate random transactions
    data = {
        'customer_id': np.random.choice(customer_ids, n_transactions),
        'transaction_date': [(datetime(2024, 1, 1) - timedelta(days=np.random.randint(0, 365))) for _ in range(n_transactions)],
        'transaction_amount': np.random.normal(100, 30, n_transactions).round(2)
    }

    # Create DataFrame
    df = pd.DataFrame(data)
    df = df[df['transaction_amount'] > 0]  # Remove negative amounts

    return df


def calculate_rfm(df, analysis_date):
    """Calculate RFM metrics for each customer."""

    # Calculate RFM metrics
    rfm = df.groupby('customer_id').agg({
        'transaction_date': lambda x: (analysis_date - x.max()).days,  # Recency
        'transaction_id': 'count',  # Frequency
        'transaction_amount': 'sum'  # Monetary
    }).reset_index()

    # Rename columns
    rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']

    # Create R, F, and M quartiles
    rfm['R'] = pd.qcut(rfm['recency'], q=4, labels=[4, 3, 2, 1])
    rfm['F'] = pd.qcut(rfm['frequency'], q=4, labels=[1, 2, 3, 4])
    rfm['M'] = pd.qcut(rfm['monetary'], q=4, labels=[1, 2, 3, 4])

    # Calculate RFM Score
    rfm['rfm_score'] = rfm['R'].astype(str) + rfm['F'].astype(str) + rfm['M'].astype(str)

    # Calculate RFM Value
    rfm['rfm_value'] = rfm[['R', 'F', 'M']].mean(axis=1)

    return rfm


def segment_customers(value):
    """Assign a segment label based on the RFM value."""
    if value >= 3.5:
        return 'Best Customers'
    elif value >= 2.5:
        return 'Loyal Customers'
    elif value >= 1.5:
        return 'Average Customers'
    else:
        return 'Lost Customers'


def add_segments(rfm_results):
    """Add customer segment labels to the RFM table."""
    rfm_results['customer_segment'] = rfm_results['rfm_value'].apply(segment_customers)
    return rfm_results


def print_summary(rfm_results):
    """Print summary statistics and a sample of the RFM table."""
    print("\nRFM Analysis Summary:")
    print("-" * 50)
    print("\nCustomer Segments Distribution:")
    print(rfm_results['customer_segment'].value_counts())
    print("\nRFM Metrics Summary Statistics:")
    print(rfm_results[['recency', 'frequency', 'monetary']].describe())

    # Sample of the final RFM table
    print("\nSample RFM Results (First 10 customers):")
    print(rfm_results.head(10).to_string())


def plot_segments(rfm_results):
    """Visualize the distribution of customer segments."""
    plt.figure(figsize=(10, 6))
    sns.countplot(data=rfm_results, x='customer_segment')
    plt.title('Distribution of Customer Segments')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    """Run the full RFM analysis pipeline."""
    # Set analysis date
    analysis_date = datetime(2024, 1, 1)

    # Generate sample data
    df = generate_sample_data(n_customers=1000, n_transactions=5000)

    # Add transaction IDs
    df['transaction_id'] = range(len(df))

    # Calculate RFM
    rfm_results = calculate_rfm(df, analysis_date)

    # Add segment labels
    rfm_results = add_segments(rfm_results)

    # Print summary statistics
    print_summary(rfm_results)

    # Create segment visualization
    plot_segments(rfm_results)


if __name__ == '__main__':
    main()
