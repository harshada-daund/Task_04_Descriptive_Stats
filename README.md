# Task 04 – Descriptive Statistics System

This project analyzes datasets related to the 2024 U.S. presidential election using three distinct approaches:
1. **Pure Python** 
2. **Pandas**  
3. **Polars**

The goal is to extract descriptive statistics and categorical insights for each dataset and compare methodologies.

---

## Datasets Used

You must manually download the following files and place them in the working directory.

📎 **Download**: [Google Drive Link](https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view)

- `2024_fb_ads_president_scored_anon.csv`
- `2024_fb_posts_president_scored_anon.csv`
- `2024_tw_posts_president_scored_anon.csv`

---

## Objective

All three scripts compute:

- Descriptive statistics: `count`, `mean`, `min`, `max`, `std`
- Top frequency values for first 3 columns
- Group-wise summaries:
  - Facebook Ads: `groupby(['page_id', 'ad_id'])`
  - Facebook Posts: `groupby('Type')`
  - Twitter Posts: `groupby('lang')`

---

## Project Structure

| File Name             | Purpose                                    |
|------------------------|--------------------------------------------|
| `pure_python_stats.py` | Uses built-in modules like `csv`, `math`   |
| `pandas_stats.py`      | Analysis using Pandas                      |
| `polars_stats.py`      | Analysis using Polars for speed            |

---

## Installation & Running

Install dependencies:

```bash
pip install pandas polars
```

Run any script using:

```bash
python pure_python_stats.py
python pandas_stats.py
python polars_stats.py
```

Each script will read the datasets and output grouped and overall statistics.

---


### Summary of Findings

#### **1. Facebook Ads**

* A small number of `page_id`s are linked to a large volume of ads, highlighting centralized campaign strategies.
* Grouped stats for `['page_id', 'ad_id']` show wide variation in numeric metrics like spend or impressions, indicating targeted and budget-variable advertising.

#### **2. Facebook Posts**

* One or two `Type` values (e.g., Photo, Link) dominate the content, suggesting preferred post formats.
* Grouped analysis by `Type` reveals substantial differences in average engagement, implying content type affects reach and interaction.

#### **3. Twitter Posts**

* Most tweets are in English (`'en'`), showing language-based audience targeting.
* Grouped statistics by `lang` show varying mean metrics like likes or retweets, suggesting language influences audience engagement.
