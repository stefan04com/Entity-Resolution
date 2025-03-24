# Company Entity Resolution

This project aims to preprocess and clean a dataset of companies, identify duplicates, and generate a final list of unique companies based on several fields (like company name, country, and region). The process includes data cleaning, fuzzy matching, and grouping duplicates to generate the most accurate list of unique companies.

## Steps

### 1. Data Normalization
The first step of the process involves loading the raw data from a `.parquet` file and normalizing it by performing the following operations:

- **Drop columns with too many missing values:** Columns with more than 5% missing values are removed.
- **Remove irrelevant columns:** Columns that contain information irrelevant for company identification are dropped (e.g., employee count, revenue, website stats).
- **Drop columns with too much specific information:** Columns that contain overly accurate data (e.g., addresses, latitude, and longitude) are also removed to avoid any unnecessary complexity.
- **Normalize text data:** All relevant text fields (company name, country, region) are converted to lowercase and stripped of extra whitespace to ensure consistency.

The cleaned data is then saved to a CSV file called `normalized_data.csv`.

### 2. Duplicate Detection
Once the data is cleaned, the next step is identifying possible duplicates in the dataset. This is done using the following approach:

- **Block-based grouping:** Companies are grouped based on the first three letters of their names, reducing the number of comparisons that need to be made.
- **Fuzzy matching:** For each pair of companies within the same group, a similarity score is calculated for the company name, country, and region using the `rapidfuzz` library.
- **Threshold for duplicates:** If the average similarity score between these fields exceeds 85%, the two companies are considered duplicates.

These duplicates are saved in a new CSV file called `grouped_duplicates.csv`.

### 3. Identifying Unique Companies
After detecting duplicates, the next step is to generate a final list of unique companies:

- **Group duplicates:** Duplicate companies are grouped together, and one representative is chosen for each group (the lexicographically smallest company name).
- **Filter unique companies:** The dataset is filtered to retain only these unique company representatives.
- **Save to CSV:** The final list of unique companies is saved in a file called `unique_companies.csv`.

## Requirements

To run the code, you need to install the following Python packages:

- `pandas`
- `rapidfuzz`
- `scikit-learn`

Install them using pip:

```bash
pip install pandas rapidfuzz scikit-learn
