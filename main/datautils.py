import pandas as pd
import numpy as np
import itertools as it

def loadall(fp):
    """load the entire csv"""
    dtypes={
    "CENSUS_YEAR": np.int64,
    "GEO_CODE (POR)":np.int64,
    "GEO_LEVEL":np.int64,
    "GEO_NAME" : str,
    "GNR" : np.float64,
    "GNR_LF": np.float64,
    "DATA_QUALITY_FLAG":np.int64,
    "CSD_TYPE_NAME":str,
    "ALT_GEO_CODE":np.int64,
    "DIM: Profile of Census Divisions/Census Subdivisions (2247)":str,
    "Member ID: Profile of Census Divisions/Census Subdivisions (2247)": np.int64,
    "Notes: Profile of Census Divisions/Census Subdivisions (2247)" : str,
    "Dim: Sex (3): Member ID: [1]: Total - Sex" :np.float64,
    "Dim: Sex (3): Member ID: [2]: Male" : np.float64,
    "Dim: Sex (3): Member ID: [3]: Female" : np.float64,
    }
    cols = ["DIM: Profile of Census Divisions/Census Subdivisions (2247)",
            'GEO_CODE (POR)', 'GEO_LEVEL', 'GEO_NAME', 'GNR', 'DATA_QUALITY_FLAG',
            "Member ID: Profile of Census Divisions/Census Subdivisions (2247)",
            "Dim: Sex (3): Member ID: [1]: Total - Sex","Dim: Sex (3): Member ID: [2]: Male",
            "Dim: Sex (3): Member ID: [3]: Female"]
    census_iter=pd.read_csv(fp,dtype=dtypes,usecols=cols,na_values=["...","x","F","..","E","r"],iterator=True,chunksize=1000)
    df=pd.concat([chunk[chunk['GEO_LEVEL'] < 2] for chunk in census_iter])
    return df

def load_section(fp, rowfile,geoname):
    """load a section of a csv file based on a geoname and row file"""
    dtypes={
    "CENSUS_YEAR": np.int64,
    "GEO_CODE (POR)":np.int64,
    "GEO_LEVEL":np.int64,
    "GEO_NAME" : str,
    "GNR" : np.float64,
    "GNR_LF": np.float64,
    "DATA_QUALITY_FLAG":np.int64,
    "CSD_TYPE_NAME":str,
    "ALT_GEO_CODE":np.int64,
    "DIM: Profile of Census Divisions/Census Subdivisions (2247)":str,
    "Member ID: Profile of Census Divisions/Census Subdivisions (2247)": np.int64,
    "Notes: Profile of Census Divisions/Census Subdivisions (2247)" : str,
    "Dim: Sex (3): Member ID: [1]: Total - Sex" :np.float64,
    "Dim: Sex (3): Member ID: [2]: Male" : np.float64,
    "Dim: Sex (3): Member ID: [3]: Female" : np.float64,
    }
    cols = ['GEO_CODE (POR)', 'GEO_LEVEL', 'GEO_NAME', 'GNR', 'DATA_QUALITY_FLAG',
            "DIM: Profile of Census Divisions/Census Subdivisions (2247)",
            "Member ID: Profile of Census Divisions/Census Subdivisions (2247)",
            "Dim: Sex (3): Member ID: [1]: Total - Sex","Dim: Sex (3): Member ID: [2]: Male",
            "Dim: Sex (3): Member ID: [3]: Female"]
    rowdtype = {
    "Geo Code": np.int64,
    "Geo Name": str,
    "Line Number": np.int64,
    }
    row_table = pd.read_csv(rowfile, dtype=rowdtype)
    line = row_table[row_table['Geo Name'] == geoname].iloc[0]["Line Number"]
    census_iter=pd.read_csv(fp,dtype=dtypes,usecols=cols,na_values=["...","x","F","..","E","r"],iterator=True,chunksize=1000,skiprows=range(1,line-1))
    df = pd.concat(validchunk(census_iter, geoname))
    return df

def validchunk(chunks, geoname):
    """chunk generator with a geoname mask"""
    for chunk in chunks:
        mask = chunk['GEO_NAME'] == geoname
        if mask.all():
            yield chunk
        else:
            yield chunk.loc[mask]
            break

def loadprovinces(fp, rowfile):
    """loads census data for all the provinces in Canada into a dataframe"""
    provinces = ["British Columbia", "Alberta", "Saskatchewan", "Manitoba",
    "Ontario", "Quebec", "Nova Scotia","Prince Edward Island", "New Brunswick",
    "Newfoundland and Labrador","Northwest Territories", "Yukon", "Nunavut"]
    frames = []
    for p in provinces:
        frames.append(load_section(fp,rowfile, p))
    return pd.concat(frames)
