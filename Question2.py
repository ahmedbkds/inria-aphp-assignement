def detect_duplicates(df):
    df.replace(to_replace=[None], value='', inplace=True)
    df=df.loc[df.isna().sum(axis=1).groupby(df.patient_id).idxmin(),:]
    df=df.reset_index()
    del df['index']
    return df
    
