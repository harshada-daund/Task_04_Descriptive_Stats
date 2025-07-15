# Import necessary libraries
import pandas as pd
import os

# Dictionary specifying dataset file paths
DATASETS = {
    "Facebook Ads": "2024_fb_ads_president_scored_anon.csv",
    "Facebook Posts": "2024_fb_posts_president_scored_anon.csv",
    "Twitter Posts": "2024_tw_posts_president_scored_anon.csv"
}

# Function to display statistics for the first 3 groups only
def display_grouped_stats(grouped):
    try:
        for i, (group_name, group_df) in enumerate(grouped):
            if i >= 3:
                break
            print(f"\nGroup: {group_name}")
            print(group_df.describe(include='all').transpose())
    except Exception as e:
        print("Error computing grouped statistics:", e)

# Function to process and summarize each dataset
def run(name, path):
    print(f"\n{name.upper()}")

    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(f"Unable to load file: {path}. Reason: {e}")
        return

    # Display overall descriptive statistics
    print("\nOverall Descriptive Statistics:")
    print(df.describe(include='all').transpose())

    # Display most frequent value for the first three columns
    print("\nTop Frequencies (first 3 columns):")
    for col in df.columns[:3]:
        value_counts = df[col].value_counts(dropna=False)
        if not value_counts.empty:
            print(f"{col}: {value_counts.head(1).to_dict()}")

    # Conditional grouping and grouped statistics
    if name == "Facebook Ads" and {'page_id', 'ad_id'}.issubset(df.columns):
        print("\nGrouped by ['page_id', 'ad_id']:")
        grouped = df.groupby(['page_id', 'ad_id'])
        display_grouped_stats(grouped)

    elif name == "Facebook Posts" and "Type" in df.columns:
        print("\nGrouped by 'Type':")
        grouped = df.groupby('Type')
        display_grouped_stats(grouped)

    elif name == "Twitter Posts" and "lang" in df.columns:
        print("\nGrouped by 'lang':")
        grouped = df.groupby('lang')
        display_grouped_stats(grouped)

# Main execution block
if __name__ == "__main__":
    for name, path in DATASETS.items():
        if os.path.exists(path):
            run(name, path)
        else:
            print(f"File not found: {path}")
