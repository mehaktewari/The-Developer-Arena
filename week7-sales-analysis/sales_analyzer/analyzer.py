import pandas as pd
import numpy as np

class SalesAnalyzer:
    def __init__(self, df):
        self.df = df

    def basic_stats(self):
        return {
            "total_sales": self.df['total_amount'].sum(),
            "average_order_value": self.df['total_amount'].mean(),
            "total_orders": len(self.df),
            "unique_customers": self.df['customer_id'].nunique()
        }

    def sales_by_category(self):
        return self.df.groupby('category')['total_amount'].sum().sort_values(ascending=False)

    def monthly_sales(self):
        self.df['month'] = self.df['order_date'].dt.to_period('M')
        monthly = self.df.groupby('month')['total_amount'].sum()
        growth = monthly.pct_change() * 100
        return monthly, growth

    def top_products(self, n=5):
        return self.df.groupby('product_name')['total_amount'].sum().sort_values(ascending=False).head(n)
