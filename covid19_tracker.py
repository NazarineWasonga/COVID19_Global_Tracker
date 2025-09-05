"""
COVID-19 Global Data Tracker
Loads COVID-19 data (live OWID if available; otherwise local sample),
cleans it, prints stats, and shows 4 visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

OWID_URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
LOCAL_SAMPLE = "data/sample_covid.csv"

def load_data():
    # Try live dataset first (internet); fallback to local sample
    usecols = ["date", "location", "new_cases", "new_deaths"]
    parse_dates = ["date"]
    try:
        print("Attempting to load live OWID dataset...")
        df = pd.read_csv(OWID_URL, usecols=usecols, parse_dates=parse_dates)
        print("✅ Loaded live dataset.\n")
        return df
    except Exception as e:
        print(f"⚠ Live dataset unavailable ({e}). Falling back to local sample.")
        df = pd.read_csv(LOCAL_SAMPLE, parse_dates=parse_dates)
        print("✅ Loaded local sample.\n")
        return df

def explore(df: pd.DataFrame):
    print("First 5 rows:")
    print(df.head(), "\n")

    print("Dtypes:")
    print(df.dtypes, "\n")

    print("Missing values per column:")
    print(df.isna().sum(), "\n")

def clean(df: pd.DataFrame) -> pd.DataFrame:
    # Ensure essential columns exist
    for col in ["date", "location", "new_cases", "new_deaths"]:
        if col not in df.columns:
            raise ValueError(f"Required column missing: {col}")

    # Drop rows missing date or location; fill numeric NaNs with 0
    df = df.dropna(subset=["date", "location"]).copy()
    for col in ["new_cases", "new_deaths"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Keep only non-negative values for cases/deaths
    for col in ["new_cases", "new_deaths"]:
        df.loc[df[col] < 0, col] = 0

    return df

def analyze(df: pd.DataFrame):
    print("Basic statistics:\n")
    print(df[["new_cases", "new_deaths"]].describe(), "\n")

    by_loc = df.groupby("location", as_index=True)[["new_cases"]].mean().sort_values("new_cases", ascending=False)
    print("Average new cases by location (top 10):")
    print(by_loc.head(10), "\n")
    return by_loc

def visualize(df: pd.DataFrame, by_loc: pd.DataFrame):
    sns.set(style="whitegrid")

    # Filter a single country for the line chart (Kenya if present, else first location)
    if "Kenya" in df["location"].unique():
        loc = "Kenya"
    else:
        loc = df["location"].iloc[0]

    country = df[df["location"] == loc].sort_values("date")

    # 1) Line chart — new cases over time
    plt.figure(figsize=(9, 5))
    plt.plot(country["date"], country["new_cases"], label=f"New cases - {loc}")
    plt.title(f"Daily New COVID-19 Cases Over Time — {loc}")
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # 2) Bar chart — top 5 locations by average new cases
    top5 = by_loc.head(5).iloc[::-1]  # reverse for nicer horizontal bar
    plt.figure(figsize=(9, 5))
    plt.barh(top5.index, top5["new_cases"])
    plt.title("Top 5 Locations by Average Daily New Cases")
    plt.xlabel("Average New Cases")
    plt.ylabel("Location")
    plt.tight_layout()
    plt.show()

    # 3) Histogram — distribution of daily new cases (all data)
    plt.figure(figsize=(9, 5))
    plt.hist(df["new_cases"], bins=30, edgecolor="black")
    plt.title("Distribution of Daily New COVID-19 Cases (All Locations)")
    plt.xlabel("New Cases")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # 4) Scatter — new cases vs new deaths
    plt.figure(figsize=(9, 5))
    sns.scatterplot(x="new_cases", y="new_deaths", data=df.sample(min(len(df), 5000), random_state=42))
    plt.title("New Cases vs New Deaths")
    plt.xlabel("New Cases")
    plt.ylabel("New Deaths")
    plt.tight_layout()
    plt.show()

def main():
    df = load_data()
    explore(df)
    df = clean(df)
    by_loc = analyze(df)
    visualize(df, by_loc)

if __name__ == "__main__":
    main()
