import pandas as pd

# Load data
df_raw = pd.read_pickle('subset_data.pkl')

# Find all occurrences of duplicate rows (including the first one)
all_duplicates = df_raw[df_raw.duplicated(keep=False)]

# Find duplicates in tripID
duplicates_tripID = df_raw[df_raw['TRIP_ID'].duplicated(keep=False)]

# Find duplicates in POLYLINE
duplicates_POLYLINE = df_raw[df_raw['POLYLINE'].duplicated(keep=False)]

# Find duplicates in taxiID and TIMESTAMP
duplicates_taxiID_TIMESTAMP = df_raw[df_raw.duplicated(subset=['TAXI_ID', 'TIMESTAMP'], keep=False)]


# check for data in wrong format
non_integer_entries = df_raw[~df_raw['TRIP_ID'].apply(lambda x: isinstance(x, int))]
non_integer_entries = df_raw[~df_raw['TAXI_ID'].apply(lambda x: isinstance(x, int))]
non_integer_entries = df_raw[~df_raw['TIMESTAMP'].apply(lambda x: isinstance(x, int))]
non_integer_entries = df_raw[~df_raw['MISSING_DATA'].apply(lambda x: isinstance(x, bool))]
non_integer_entries = df_raw[~df_raw['CALL_TYPE'].isin(['A', 'B', 'C'])]
non_integer_entries = df_raw[~df_raw['DAY_TYPE'].isin(['A', 'B', 'C'])]
non_integer_entries = df_raw[~df_raw['ORIGIN_CALL'].apply(lambda x: isinstance(x, float))]
non_integer_entries = df_raw[~df_raw['ORIGIN_STAND'].apply(lambda x: isinstance(x, float))]

non_integer_entries = df_raw[~df_raw['POLYLINE'].apply(lambda x: isinstance(x, str))]
polyline_records = df_raw[df_raw['POLYLINE'].apply(len) <= 25]

missing_data_rows = df_raw[df_raw[['TRIP_ID', 'CALL_TYPE', 'TAXI_ID', 'TIMESTAMP',
                                   'DAY_TYPE', 'MISSING_DATA', 'POLYLINE']].isna().any(axis=1)]