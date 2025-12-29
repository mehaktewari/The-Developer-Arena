import numpy as np

class DataCleaner:
    def __init__(self, df):
        self.df = df

    def clean(self):
        self.df.drop_duplicates(inplace=True)

        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            self.df[col].fillna(self.df[col].median(), inplace=True)

        categorical_cols = self.df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            self.df[col].fillna(self.df[col].mode()[0], inplace=True)

        return self.df
