import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def main():
    print("🦠 COVID-19 Global Data Tracker")
    print("="*40)

    # Load dataset
    file_path = "data/sample_covid.csv"
    if not os.path.exists(file_path):
        print(f"❌ Dataset not found at {file_path}")
        return

    try:
        df = pd.read_csv(file_path)
        print("✅ Dataset loaded successfully\n")
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return

    # Show first rows
    print("📊 First 5 Rows:")
    print(df.head(), "\n")

    # Dataset info
    print("📊 Dataset Info:")
    print(df.info(), "\n")

    # Missing values
    print("🔎 Missing Values:")
    print(df.isnull().sum(), "\n")

    # Handle missing values
    df = df.fillna(0)
    print("✅ Missing values handled\n")

    # Basic statistics
    print("📈 Descriptive Statistics:")
    print(df.describe(), "\n")

    # Grouping Example
    if "Country" in df.columns and "Confirmed" in df.columns:
        grouped = df.groupby("Country")["Confirmed"].mean()
        print("🌍 Average Confirmed Cases by Country:")
        print(grouped.head(), "\n")

    # Line Chart
    if "Date" in df.columns and "Confirmed" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        daily_cases = df.groupby("Date")["Confirmed"].sum()

        plt.figure(figsize=(10,5))
        plt.plot(daily_cases, label="Confirmed Cases", color="blue")
        plt.title("Daily Confirmed COVID-19 Cases Over Time")
        plt.xlabel("Date")
        plt.ylabel("Confirmed Cases")
        plt.legend()
        plt.show()

    # Bar Chart
    if "Country" in df.columns and "Confirmed" in df.columns:
        avg_cases = df.groupby("Country")["Confirmed"].mean().sort_values(ascending=False).head(10)

        plt.figure(figsize=(10,5))
        avg_cases.plot(kind="bar", color="orange")
        plt.title("Top 10 Countries - Average Confirmed Cases")
        plt.xlabel("Country")
        plt.ylabel("Average Confirmed Cases")
        plt.show()

    # Histogram
    if "Confirmed" in df.columns:
        plt.figure(figsize=(8,5))
        plt.hist(df["Confirmed"], bins=30, color="green", edgecolor="black")
        plt.title("Distribution of Confirmed Cases")
        plt.xlabel("Confirmed Cases")
        plt.ylabel("Frequency")
        plt.show()

    # Scatter Plot
    if "Confirmed" in df.columns and "Deaths" in df.columns:
        plt.figure(figsize=(8,5))
        plt.scatter(df["Confirmed"], df["Deaths"], alpha=0.5, color="red")
        plt.title("Confirmed Cases vs Deaths")
        plt.xlabel("Confirmed Cases")
        plt.ylabel("Deaths")
        plt.show()

    # Insights
    print("🔎 Insights:")
    print("- Daily confirmed cases reveal waves of infection.")
    print("- Some countries have significantly higher averages than others.")
    print("- The distribution of cases is highly skewed.")
    print("- Scatter plot shows correlation between confirmed cases and deaths.")

if __name__ == "__main__":
    main()
