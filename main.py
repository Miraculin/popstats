import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature

def main():
    canadaNW=(85.138256,-125.251778)
    canadaSE=(32.822230, -55.231211)
    parallels=(49,77)
    can_central_longitude = -(91 + 52 / 60)
    projection=ccrs.LambertConformal(central_longitude=can_central_longitude,
                                                    standard_parallels=parallels)
    censusFilePath = "dataset/census2018.csv"
    sb.set(style = 'darkgrid')
    #census = pd.read_csv(censusFilePath)
    #print(census)
    shpfilename = shpreader.natural_earth(resolution='110m',
                                        category='cultural',
                                        name='admin_0_countries')
    reader = shpreader.Reader(shpfilename)
    countries = reader.records()
    provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='10m',
        facecolor='none')
    land_10m = cfeature.NaturalEarthFeature(
        category='physical',
        name='land',
        scale='10m',
        facecolor='none')
    ax = plt.axes(projection =projection)
    ax.set_extent((canadaNW[1],canadaSE[1],canadaNW[0],canadaSE[0]))
    ax.stock_img()
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.LAKES, alpha=0.95)
    ax.add_feature(cfeature.BORDERS, linestyle='-',edgecolor='black')
    ax.add_feature(provinces,alpha=0.75, edgecolor='black')
    ax.coastlines()
    ax.plot(np.random.rand(10))
    fig = ax.get_figure()
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

if __name__ == "__main__":
    main()
