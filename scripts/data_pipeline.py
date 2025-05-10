# scripts/data_pipeline.py

import pandas as pd
import os
import os


def load_and_clean_data(file_path):
    # Load dataset
    df = pd.read_excel(file_path, sheet_name='Year 2010-2011')

    # Convert date column
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # Create TotalPrice column
    df['TotalPrice'] = df['Quantity'] * df['Price']

    # Drop null CustomerID and remove cancelled invoices
    df = df.dropna(subset=['Customer ID'])
    df = df[~df['Invoice'].astype(str).str.startswith('C')]

    return df

def save_clean_data(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_path = 'data/online_retail.xlsx'
    output_path = '../outputs/tables/cleaned_data.csv'

    df_cleaned = load_and_clean_data(input_path)
    save_clean_data(df_cleaned, output_path)
    print(f" Cleaned data saved to: {output_path}")
