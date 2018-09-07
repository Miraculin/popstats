import numpy as np
import pandas as pd
import mapplot as map
import datautils as dutil
import matplotlib.pyplot as plt
import os.path

datapath = "../dataset/"
censusFilePath = os.path.join(datapath, "census2018.csv")
censusRowsPath = os.path.join(datapath,"rows.csv")

def main():
    #df = dutil.loadall(censusFilePath)
    df = dutil.loadprovinces(censusFilePath,censusRowsPath)
    plot = map.CanadaMapPlot(df)
    plot.plot()
    plt.show()
    print(df)

if __name__ == "__main__":
    main()
