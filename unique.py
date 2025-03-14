import pandas as pd

df = pd.read_csv("normalized_data.csv")
duplicates = pd.read_csv("grouped_duplicates.csv")

duplicate_dict = {}

for index, row in duplicates.iterrows():
    comp1 = row["Company_1"]
    comp2 = row["Company_2"]

    if comp1 in duplicate_dict:
        duplicate_dict[comp1].add(comp2)
    elif comp2 in duplicate_dict:
        duplicate_dict[comp2].add(comp1)
    else:
        duplicate_dict[comp1] = {comp2}

unique_companies = set()
for group in duplicate_dict.values():
    representative = min(group)
    unique_companies.add(representative)

df_filtered = df[df["company_name"].isin(unique_companies)]

df_filtered.to_csv("unique_companies.csv", index=False)

