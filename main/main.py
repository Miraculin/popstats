import numpy as np
import pandas as pd
import mapplot as map

censusFilePath = "../dataset/census2018.csv"

def main():
    map.mapshow()
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
    census_iter=pd.read_csv(censusFilePath,dtype=dtypes,na_values=["...","x","F","..","E","r"],iterator=True,chunksize=1000)
    df=pd.concat([chunk[chunk['GEO_LEVEL'] < 3] for chunk in census_iter])
    print(df)
    
if __name__ == "__main__":
    main()
