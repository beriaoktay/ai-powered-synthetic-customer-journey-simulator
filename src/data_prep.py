import pandas as pd


def read_session_csv(path:str)->pd.DataFrame:
    df = pd.read_csv(path)
    if "ts" in df.columns:
        df["ts"]=pd.to_datetime(df["ts"])
    return df


def df_to_sessions(df:pd.DataFrame)->pd.DataFrame:
    needed_columns = {"session_id","action"}
    if not needed_columns.issubset(df.columns):
        raise ValueError("df must included needed columns")

    if "ts" in df.columns:
        df=df.sort_values(["session_id","ts"])
    else:
        df=df.sort_values(["session_id"])

    sessions=df.groupby("session_id")["action"].apply(list).tolist()

    return sessions


