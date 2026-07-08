import pandas as pd


# Load datasets

df1 = pd.read_csv(
    "one.csv",
    encoding="ISO-8859-1"
)

df2 = pd.read_csv(
    "two.csv",
    encoding="ISO-8859-1"
)


# Combine datasets

retail = pd.concat(
    [df1, df2],
    ignore_index=True
)


# Remove duplicate records

retail = retail.drop_duplicates()


# Clean text columns

retail["Description"] = (
    retail["Description"]
    .str.strip()
)


retail["Country"] = (
    retail["Country"]
    .str.strip()
)


# Convert data types

# Invoice contains values like C536379 (returns),
# so keep as string
retail["Invoice"] = (
    retail["Invoice"]
    .astype(str)
)


# Product codes can contain letters
retail["StockCode"] = (
    retail["StockCode"]
    .astype(str)
)


# Quantity should be integer
retail["Quantity"] = pd.to_numeric(
    retail["Quantity"],
    errors="coerce"
)


# Date conversion
retail["InvoiceDate"] = pd.to_datetime(
    retail["InvoiceDate"],
    errors="coerce"
)


# Price should be decimal
retail["Price"] = pd.to_numeric(
    retail["Price"],
    errors="coerce"
)


# Customer ID can contain missing values,
# so use nullable integer
retail["Customer ID"] = pd.to_numeric(
    retail["Customer ID"],
    errors="coerce"
).astype("Int64")


# Remove rows where critical fields are missing

retail = retail.dropna(
    subset=[
        "Invoice",
        "StockCode",
        "Description",
        "Quantity",
        "InvoiceDate",
        "Price"
    ]
)


# Remove invalid values

# Remove rows with zero or negative quantity
retail = retail[
    retail["Quantity"] > 0
]


# Remove rows with zero or negative price
retail = retail[
    retail["Price"] > 0
]


# Check final dataset

print(retail.info())

print(retail.head())


# Save cleaned dataset

retail.to_csv(
    "RetailTransaction.csv",
    index=False
)