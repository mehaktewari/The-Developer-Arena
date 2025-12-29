import pandas as pd

class Reporter:
    def __init__(self, df):
        self.df = df

    def export_excel(self, path):
        with pd.ExcelWriter(path, engine='openpyxl') as writer:
            self.df.to_excel(writer, sheet_name="Cleaned Data", index=False)
