# Merge bitcoin_price.csv with dataset_merged.csv by matching dates

import pandas as pd

# Load merged dataset
df_merged = pd.read_csv("data/dataset_merged.csv", parse_dates=["date"], index_col="date")

# Load bitcoin price dataset
df_price = pd.read_csv("data/bitcoin_price.csv", parse_dates=["Date"])
df_price = df_price.rename(columns={"Date": "date", "BTC - Price": "btc_price"})
df_price = df_price.set_index("date")

# Trim price data to match merged dataset dates
df_price_trimmed = df_price.loc[df_merged.index.min():df_merged.index.max()]

# Merge price column into merged dataset
df_final = df_merged.join(df_price_trimmed, how="left")

# Export to new file
df_final.to_csv("data/dataset_merged_with_price.csv", index=True, encoding="utf-8", float_format="%.2f")