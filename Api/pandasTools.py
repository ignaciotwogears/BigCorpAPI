import pandas as pd
import middleware
import tools

# it return the employees without manager
def getOrphanFrames(df):
    ids = df['id']
    orphans = df.query('manager not in @ids')['manager']
    ls = [p for p in orphans]
    ls = tools.formatLS(ls)
    ls = list(dict.fromkeys(ls))
    return ls

# Turns the list of dicts to a pandas dataframe
def formatDataframe(rawData):
    df = pd.DataFrame.from_dict(rawData)
    ls = getOrphanFrames(df)
    # While there exists employees without manager it will call to the employees service recursively until all the data is complete
    while(len(ls) > 0):
        pendingData = middleware.getEmployeesByIds(ls)
        pdFrame = pd.DataFrame.from_dict(pendingData)
        frames = [df, pdFrame]
        df = pd.concat(frames)
        ls = getOrphanFrames(df)
    return df
