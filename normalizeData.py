import pandas as pd
# Read the data from the parquet file into a pandas dataframe
df = pd.read_parquet("veridion_entity_resolution_challenge.snappy.parquet")

# Drop columns with more than 5% missing values
threshold = 0.95
df = df.loc[:, df.isna().mean() < threshold]

# Drop columns with information that may be different from the multyple systems
df.drop(columns=["employee_count_type", "employee_count", "revenue_type", "revenue"], inplace=True)
df.drop(columns=["inbound_links_count", "website_number_of_pages"], inplace=True)

# Drop columns without relevant information to identify a company
df.drop(columns=["website_language_code", "domains", "lnk_year_founded"], inplace=True)
df.drop(columns=["short_description", "long_description"], inplace=True)

# Drop columns with duped information
df.drop(columns=["primary_email", "website_url", "primary_phone"], inplace=True)

# Drop columns with too accurate information
df.drop(columns=["main_address_raw_text", "main_longitude", "main_latitude", ], inplace=True)

# Normalize the columns
df["company_name"] = df["company_name"].str.lower()
df["main_country"] = df["main_country"].str.lower()
df["main_region"] = df["main_region"].str.lower()
df["company_name"] = df["company_name"].str.strip()
df["main_country"] = df["main_country"].str.strip()
df["main_region"] = df["main_region"].str.strip()

df.to_csv("normalized_data.csv", index=False)