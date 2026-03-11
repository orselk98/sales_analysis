# E-Commerce Sales Analysis

A data analysis project exploring 3,500 e-commerce transactions from January 2022 to December 2024. Built with Python, Pandas, NumPy, Matplotlib, and Seaborn.

## Key Findings

- **Total Sales:** $10.67M across 3,500 transactions
- **Top Category:** Electronics at $5.3M, followed by Accessories at $4.2M
- **Profit Margin:** Consistent ~17% across all categories and regions
- **Growth:** Sales grew 16% from 2022 to 2023, then declined 4% in 2024
- **Regional Balance:** All four regions (East, North, South, West) perform similarly

## Project Structure

```
SALES_ANALYSIS/
├── Data/
│   ├── raw/                  # Original dataset from Kaggle
│   └── processed/            # Cleaned and transformed data
├── Notebooks/
│   └── analysis.py           # Exploratory data analysis
├── Scripts/
│   ├── download_data.py      # Dataset download and setup
│   └── report.py             # Automated PDF report generation
├── Output/                   # Charts and generated reports
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/orselk98/sales_analysis.git
cd sales_analysis
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download the dataset:
```bash
python Scripts/download_data.py
```

## Usage

Run the exploratory analysis:
```bash
python Notebooks/analysis.py
```

Generate the PDF report:
```bash
python Scripts/report.py
```

The report will be saved to `Output/sales_analysis_report.pdf`.

## Analysis Includes

- **Data Inspection:** Shape, types, missing values, summary statistics
- **Category Analysis:** Sales, profit, and margin breakdown by product category
- **Regional Analysis:** Performance comparison across East, North, South, and West
- **Time Trends:** Monthly and yearly sales patterns over 3 years
- **Profitability:** Profit margin analysis with high/low margin classification
- **Visualizations:** Bar charts, line charts, heatmaps, and multi-chart dashboards

## Technologies

- **pandas** — data manipulation and analysis
- **numpy** — numerical operations and conditional logic
- **matplotlib** — charts and visualizations
- **seaborn** — heatmaps and statistical graphics
- **reportlab** — automated PDF report generation
- **kagglehub** — dataset download from Kaggle

## Dataset

Source: [E-Commerce Sales Data](https://www.kaggle.com/datasets/uzmaakhtar/ecommerce-sales-data) on Kaggle

| Column | Description |
|--------|-------------|
| Order Date | Transaction date (2022–2024) |
| Product Name | Item purchased |
| Category | Accessories, Electronics, or Office |
| Region | East, North, South, or West |
| Quantity | Units purchased (1–9) |
| Sales | Transaction revenue |
| Profit | Transaction profit |