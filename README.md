# 🦠 COVID-19 Global Data Tracker

A Python project that loads, cleans, analyzes, and visualizes COVID-19 data.  
It uses a public dataset (Our World in Data) when internet is available, and includes a small local sample so the project still runs offline.

---

## 🎯 Objectives
- Load and explore global COVID-19 data
- Clean missing/invalid values
- Compute basic statistics and grouped insights
- Visualize trends and comparisons with Matplotlib/Seaborn
- Provide reflections/insights from the analysis

---

## 🛠️ Tools & Libraries
- Python 3.x
- pandas — data loading/cleaning
- matplotlib — charts
- seaborn — nicer visuals
- jupyter — run the notebook

Install dependencies:
```bash
pip install -r requirements.txt

## ✅ How to Run

Save the file as covid19_tracker.py.

Make sure you have a dataset in data/sample_covid.csv.

Install dependencies:

pip install pandas matplotlib seaborn


Run the script:

python covid19_tracker.py

## 📊 What You’ll See

Head of the dataset, inferred dtypes, and missing-value checks

Cleaned data with sensible defaults for numeric columns

Basic statistics (mean/median/std)

Grouped means by country/location

Four visualizations:

Line chart — daily new cases over time (Kenya example)

Bar chart — top locations by average new cases

Histogram — distribution of daily new cases

Scatter plot — new cases vs new deaths

## 📌 Insights / Reflections (example)

Daily cases vary strongly by location; averages highlight persistent high-case regions.

Visual trends (line charts) reveal clear waves/peaks over time.

Cleaning (filling new_cases/new_deaths with 0) is essential to avoid chart distortions.

Grouping by location quickly surfaces comparative patterns.

## 📂 Repo Layout
COVID19_Global_Tracker/
├── README.md
├── requirements.txt
├── covid19_tracker.py
├── covid19_tracker.ipynb
└── data/
    └── sample_covid.csv
