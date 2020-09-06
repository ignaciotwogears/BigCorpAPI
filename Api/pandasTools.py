import pandas as pd
import middleware
import tools

def getOrphanFrames(df):
    
    ids = df['id']
    orphans = df.query('manager not in @ids')['manager']
    ls = [p for p in orphans]
    ls = tools.formatLS(ls)
    ls = list(dict.fromkeys(ls))
    return ls


def formatDataframe(rawData):
    df = pd.DataFrame.from_dict(rawData)
    
    ls = getOrphanFrames(df)
    while(len(ls) >0):
        pendingData = middleware.getEmployeesByIds(ls)

        pdFrame = pd.DataFrame.from_dict(pendingData)
        frames = [df, pdFrame]
        df = pd.concat(frames)
        ls = getOrphanFrames(df)
    
    return df
