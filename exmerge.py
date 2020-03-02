#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import click


def exmerge(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Merge two dataframes where:
    1) first datafraim contains numbers
    2) second datafraim contains some kind of voc with non-unique values
    3) you need to keep total numeric sum from first dataframe
    For example, first dataframe may contain sale-out data by cities
    and second one may contain list of employees and cities.
    And one city can be covered by more than one employee
    --------------------------------------------------
    In this case usual join or merge
    will duplicate your numeric data from 1-st df
    To avoid it exmerge will divide all numeric fields 
    by number of duplicate lines created by merge
    """
    numeric_dtypes = ["float32", "int32", "float64", "int64", "int", "float"]
    other_dtypes = ["object", "category", "datetime"]

    df1 = df1.reset_index().drop(["index"], axis=1)
    df = pd.merge(df1.reset_index(), df2, how="left")
    counts = pd.value_counts(df["index"].values).to_frame().reset_index()
    counts.columns = ["index", "count"]
    df = pd.merge(df, counts, how="left", on="index")
    df_text = df.select_dtypes(other_dtypes)
    df_numbers = (
        df.select_dtypes(numeric_dtypes)
        .div(df["count"], axis=0)
        .drop(["count", "index"], axis=1)
    )
    df_result = pd.merge(df_text, df_numbers, left_index=True, right_index=True)
    return df_result
