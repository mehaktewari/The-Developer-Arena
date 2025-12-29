from sales_analyzer.data_loader import DataLoader
from sales_analyzer.data_cleaner import DataCleaner
from sales_analyzer.analyzer import SalesAnalyzer
from sales_analyzer.visualizer import Visualizer
from sales_analyzer.reporter import Reporter

DATA_PATH = "data/raw/sales_data.csv"

loader = DataLoader(DATA_PATH)
df = loader.load_csv()

cleaner = DataCleaner(df)
df_clean = cleaner.clean()

analyzer = SalesAnalyzer(df_clean)
stats = analyzer.basic_stats()
monthly, growth = analyzer.monthly_sales()
category_sales = analyzer.sales_by_category()

print("\n📊 SALES DATA ANALYSIS REPORT")
print("="*35)
for k, v in stats.items():
    print(f"{k}: {v}")

viz = Visualizer()
viz.plot_monthly_sales(monthly)
viz.plot_category_sales(category_sales)

report = Reporter(df_clean)
report.export_excel("data/reports/sales_report.xlsx")

print("\n✅ Analysis Completed Successfully!")
