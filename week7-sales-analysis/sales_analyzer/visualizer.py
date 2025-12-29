import matplotlib.pyplot as plt
import os

class Visualizer:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def plot_monthly_sales(self, monthly_sales):
        plt.figure(figsize=(10,5))
        monthly_sales.plot(marker='o')
        plt.title("Monthly Sales Trend")
        plt.xlabel("Month")
        plt.ylabel("Sales Amount")
        plt.grid(True)
        plt.savefig(f"{self.output_dir}/monthly_sales.png")
        plt.close()

    def plot_category_sales(self, category_sales):
        plt.figure(figsize=(8,5))
        category_sales.plot(kind='bar')
        plt.title("Sales by Category")
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/category_sales.png")
        plt.close()
