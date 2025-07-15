# Import necessary libraries
import csv
import math
import os
from collections import defaultdict, Counter

# Dictionary specifying dataset file paths
DATASETS = {
    "Facebook Ads": "2024_fb_ads_president_scored_anon.csv",
    "Facebook Posts": "2024_fb_posts_president_scored_anon.csv",
    "Twitter Posts": "2024_tw_posts_president_scored_anon.csv"
}

# Function to check if value is numeric
def is_numeric(val):
    try:
        float(val)
        return True
    except:
        return False

# Load a dataset from CSV
def load_dataset(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader), reader.fieldnames

# Function to compute descriptive statistics for numeric columns
def compute_numeric(values):
    nums = [float(v) for v in values if is_numeric(v)]
    if not nums:
        return None
    mean = sum(nums) / len(nums)
    std = math.sqrt(sum((x - mean) ** 2 for x in nums) / len(nums))
    return {
        'count': len(nums),
        'mean': round(mean, 2),
        'min': min(nums),
        'max': max(nums),
        'std': round(std, 2)
    }

# Function to compute basic statistics for categorical columns
def compute_categorical(values):
    values = [v for v in values if v]
    counter = Counter(values)
    return {
        'count': len(values),
        'unique': len(counter),
        'top': counter.most_common(1)[0] if counter else None
    }


# Function to compute column-wise statistics
def get_stats(rows, headers):
    stats = {}
    for col in headers:
        values = [row[col] for row in rows]
        if all(is_numeric(v) or v == '' for v in values):
            stats[col] = compute_numeric(values)
        else:
            stats[col] = compute_categorical(values)
    return stats

# Group data by specific columns
def group_by(data, keys):
    grouped = defaultdict(list)
    for row in data:
        key = tuple(row[k] for k in keys)
        grouped[key].append(row)
    return grouped

# Display stats for top groups
def display_grouped_stats(grouped_data, headers, limit=3):
    for i, (key, rows) in enumerate(grouped_data.items()):
        if i >= limit:
            break
        print(f"\nGroup: {key}")
        stats = get_stats(rows, headers)
        for col, stat in stats.items():
            print(f"{col}: {stat}")

# Analyze a single dataset
def analyze_dataset(name, path):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    print(f"\n {name.upper()} ")
    rows, headers = load_dataset(path)

    print("\nOverall Descriptive Statistics:")
    stats = get_stats(rows, headers)
    for col, stat in stats.items():
        print(f"{col}: {stat}")

    print("\nTop Frequencies (first 3 columns):")
    for col in headers[:3]:
        values = [row[col] for row in rows]
        counter = Counter(values)
        print(f"{col}: {counter.most_common(1)}")

    # Conditional grouping logic
    if name == "Facebook Ads" and {'page_id', 'ad_id'}.issubset(headers):
        print("\nGrouped by ['page_id', 'ad_id']:")
        grouped = group_by(rows, ['page_id', 'ad_id'])
        display_grouped_stats(grouped, headers)

    elif name == "Facebook Posts" and "Type" in headers:
        print("\nGrouped by 'Type':")
        grouped = group_by(rows, ['Type'])
        display_grouped_stats(grouped, headers)

    elif name == "Twitter Posts" and "lang" in headers:
        print("\nGrouped by 'lang':")
        grouped = group_by(rows, ['lang'])
        display_grouped_stats(grouped, headers)

# Main execution block
if __name__ == "__main__":
    for dataset_name, file_path in DATASETS.items():
        analyze_dataset(dataset_name, file_path)
