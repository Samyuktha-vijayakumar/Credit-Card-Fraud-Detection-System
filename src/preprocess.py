import pandas as pd

def preprocess_data(df):

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    numeric_df = df.select_dtypes(include=["number"])

    if "Class" in numeric_df.columns:
        numeric_df = numeric_df.drop("Class", axis=1)

    numeric_df = numeric_df.fillna(0)

    return numeric_df