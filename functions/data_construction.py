import json

import pandas as pd


# Function to save pandas dataframe as a list with dictionaries for each record, so that it can be stored as JSON in dcc.Store
def save_df_into_store(df):
    df = df.to_json(orient='split')

    return df


# Function which loads data from dcc.Store and converts list of records into a pandas dataframe
def load_df_from_store(store_df):
    df = store_df

    if isinstance(df, list):
        df = pd.DataFrame(df)
    elif isinstance(df, str):
        df = pd.read_json(df, orient='split')

    return df


# Construct options with different label options
def construct_options(df, value_column, label_columns, sort_column, concat_separator):
    df = load_df_from_store(store_df=df)

    # Create column list with value and sort columns
    column_list = [value_column, sort_column]

    # Add label columns to column list and remove duplicates from column list
    [column_list.append(column) for column in label_columns]
    column_list = list(set(column_list))

    # Sort ascending, but descending in case of boolean
    sort_ascending = True
    if df.dtypes[sort_column] == 'bool':
        sort_ascending = False

    # Sort dataframe according to sort column
    df = df[column_list].sort_values(by=[sort_column], ascending=sort_ascending).drop_duplicates()

    # Save value column to dataframe in a new column named value
    df['value'] = df[value_column]

    if df.dtypes['value'] == 'bool':
        df['value'] = df['value'].astype(int)

    # Convert and concatenate label columns to strings and save them to the dataframe in a new column named label
    df[label_columns] = df[label_columns].astype(str)
    df['label'] = df[label_columns].values.tolist()
    df['label'] = df['label'].apply(concat_separator.join)

    # Keep only the label and value columns
    df = df[['label', 'value']]

    # Convert dataframe to records dictionary and save these as options
    options = df.to_dict('records')

    return options
