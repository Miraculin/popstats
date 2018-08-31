import matplotlib.pyplot as plt
import seaborn as sb
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature
import shapely.geometry as sgeom

def canadamapplot():
        canadaNW=(85.138256,-125.251778)
        canadaSE=(32.822230, -55.231211)
        parallels=(49,77)
        can_central_longitude = -(91 + 52 / 60)
        projection=ccrs.LambertConformal(central_longitude=can_central_longitude,
                                                        standard_parallels=parallels)
        shpfilename = shpreader.natural_earth(resolution='50m',
                                            category='cultural',
                                            name='admin_0_countries')
        reader = shpreader.Reader(shpfilename)
        countries = reader.records()
        provfilename = shpreader.natural_earth(resolution='50m',
                                            category='cultural',
                                            name='admin_1_states_provinces')
        provreader = shpreader.Reader(provfilename)
        provinces = provreader.records()
        canadaprovs = []
        for province in provinces:
            if province.attributes["iso_a2"]=="CA":
                canadaprovs.append(province)
        provincebounds = cfeature.NaturalEarthFeature(
            category='cultural',
            name='admin_1_states_provinces_lines',
            scale='50m',
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
        ax.add_feature(land_10m)
        ax.add_feature(cfeature.LAKES, alpha=0.95)
        ax.add_feature(cfeature.BORDERS, linestyle='-',edgecolor='black')
        ax.add_feature(provincebounds,alpha=0.75, edgecolor='black')
        ax.coastlines()
        fig = ax.get_figure()
        cid=fig.canvas.mpl_connect('button_press_event',onclick)

def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
        ('double' if event.dblclick else 'single', event.button,
        event.x, event.y, event.xdata, event.ydata))

def mapshow():
    canadamapplot()
    plt.show()
