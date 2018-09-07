import matplotlib.pyplot as plt
import seaborn as sb
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature
import shapely.geometry as sgeom
import datautils as dutil

profile = "DIM: Profile of Census Divisions/Census Subdivisions (2247)"
class CanadaMapPlot:
    canadaNW=(85.138256,-125.251778)
    canadaSE=(32.822230, -55.231211)
    parallels=(49,77)
    can_central_longitude = -(91 + 52 / 60)
    projection=ccrs.LambertConformal(central_longitude=can_central_longitude,
                                                standard_parallels=parallels)
    provinces = None
    def __init__(self,df):
        self.df = df
        self.provinces=getprovinces("CA")
        self.ax = None
        self.press = None
        self.cid=None

    def onclick(self,event):
        """On click, produce a pop up with population stats of the clicked
        province"""
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
            ('double' if event.dblclick else 'single', event.button,
            event.x, event.y, event.xdata, event.ydata))
        #for row in self.df[self.df[profile] == "Population, 2016"]
        print(self.df[self.df[profile] == "Population, 2016"]["Dim: Sex (3): Member ID: [1]: Total - Sex"])

    def plot(self):
        """Create a GeoAxes instance focused on Canada""""
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
        self.ax = plt.axes(projection=self.projection)
        self.ax.set_extent((self.canadaNW[1],self.canadaSE[1],self.canadaNW[0],self.canadaSE[0]))
        self.ax.stock_img()
        self.ax.add_feature(cfeature.OCEAN)
        self.ax.add_feature(land_10m)
        self.ax.add_feature(cfeature.LAKES, alpha=0.95)
        self.ax.add_feature(cfeature.BORDERS, linestyle='-',edgecolor='black')
        self.ax.add_feature(provincebounds,alpha=0.75, edgecolor='black')
        self.ax.coastlines()
        self.fig = self.ax.get_figure()
        self.cid = self.fig.canvas.mpl_connect('button_press_event',self.onclick)


def getprovinces(country):
    """get province/state divisions of a country by iso_a2 code"""
    provfilename = shpreader.natural_earth(resolution='50m',
                                        category='cultural',
                                        name='admin_1_states_provinces')
    provreader = shpreader.Reader(provfilename)
    provinces = provreader.records()
    ret = []
    for province in provinces:
        if province.attributes["iso_a2"]==country:
            ret.append(province)
    return ret

# def mapshow():
#     map = CanadaMapPlot()
#     map.plot()
#     plt.show()
