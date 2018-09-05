import numpy as np
import pandas as pd
import mapplot as map
import datautils as dutil

censusFilePath = "../dataset/census2018.csv"
censusRowsPath = "../dataset/census2018rows.csv"

def main():
    #map.mapshow()
    #df = dutil.loadall(censusFilePath)
    df = dutil.load_section(censusFilePath,censusRowsPath,"British Columbia")
    print(df)

if __name__ == "__main__":
    main()
