import pandas as pd
from rapidfuzz import fuzz
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import DBSCAN

df = pd.read_csv("normalized_data.csv")

df['block_key'] = df['company_name'].str[:3]
groups = df.groupby('block_key')

def find_duplicates(group):
    duplicates = []
    n = len(group)
    for i in range(n):
        for j in range(i + 1, n):
            name_sim = fuzz.token_sort_ratio(group.iloc[i]["company_name"], group.iloc[j]["company_name"])
            country_sim = fuzz.token_sort_ratio(group.iloc[i]["main_country"], group.iloc[j]["main_country"])
            region_sim = fuzz.token_sort_ratio(group.iloc[i]["main_region"], group.iloc[j]["main_region"])
            avg_sim = (name_sim + country_sim + region_sim) / 3
            if avg_sim > 85:
                duplicates.append((group.iloc[i]["company_name"], group.iloc[j]["company_name"]))
    return duplicates

all_duplicates = []
for _, group in groups:
    all_duplicates.extend(find_duplicates(group))

df_duplicates = pd.DataFrame(all_duplicates, columns=["Company_1", "Company_2"])
df_duplicates.to_csv("grouped_duplicates.csv", index=False)

