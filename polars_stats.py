# Import necessary libraries
import polars as pl
import os

# Dictionary specifying dataset file paths
DATASETS = {
    "Facebook Ads": "2024_fb_ads_president_scored_anon.csv",
    "Facebook Posts": "2024_fb_posts_president_scored_anon.csv",
    "Twitter Posts": "2024_tw_posts_president_scored_anon.csv"
}

# Function to display summary statistics for the first 3 groups
def display_grouped_stats(df, group_cols):
    try:
        # Identify numeric columns for aggregation
        numeric_cols = [col for col in df.columns if df[col].dtype in [pl.Float64, pl.Int64]]

        # Compute grouped aggregates for numeric fields
        grouped = df.group_by(group_cols).agg([
            pl.len().alias("count"),
            *[pl.mean(col).alias(f"mean_{col}") for col in numeric_cols],
            *[pl.min(col).alias(f"min_{col}") for col in numeric_cols],
            *[pl.max(col).alias(f"max_{col}") for col in numeric_cols],
            *[pl.std(col).alias(f"std_{col}") for col in numeric_cols]
        ])
        print(grouped.head(3))
    except Exception as e:
        print("Group statistics error:", e)

# Analyze a single dataset
def run(name, path):
    print(f"\n{name.upper()}")

    try:
        df = pl.read_csv(path)
    except Exception as e:
        print(f"Failed to read: {path}. Error: {e}")
        return

    # Overall statistics
    print("\nDescriptive Statistics:")
    print(df.describe().head(10))

    # Top frequencies in first 3 columns
    print("\nMost Frequent Values (first 3 columns):")
    for col in df.columns[:3]:
        try:
            counts = df.group_by(col).agg(pl.len().alias("count")).sort("count", descending=True).head(1)
            print(f"{col}:")
            print(counts)
        except Exception:
            print(f"{col}: Unable to compute frequency.")

    # Grouped statistics by dataset type
    if name == "Facebook Ads" and {"page_id", "ad_id"}.issubset(df.columns):
        print("\nGrouped by ['page_id', 'ad_id']:")
        display_grouped_stats(df, ["page_id", "ad_id"])

    elif name == "Facebook Posts" and "Type" in df.columns:
        print("\nGrouped by 'Type':")
        display_grouped_stats(df, ["Type"])

    elif name == "Twitter Posts" and "lang" in df.columns:
        print("\nGrouped by 'lang':")
        display_grouped_stats(df, ["lang"])

# Main execution block
if __name__ == "__main__":
    for name, path in DATASETS.items():
        if os.path.exists(path):
            run(name, path)
        else:
            print(f"Missing file: {path}")
