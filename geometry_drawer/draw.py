import matplotlib.pyplot as plt
from shapely.geometry import Polygon, LineString, Point


class GeometryDrawer(object):
    """docstring for ClassName"""
    def __init__(self):
        self.setup_plot()

    def crtaj_tocku(self, geom, style="rs"):
        x_lista, y_lista = geom.xy
        plt.plot(x_lista, y_lista, style)

    def crtaj_liniju(self, geom, style="b-"):
        x_lista, y_lista = geom.xy
        plt.plot(x_lista, y_lista, style)

    def crtaj_poligon(self, geom, fill="y", plot="k-"):
        x_lista, y_lista = geom.exterior.xy
        plt.fill(x_lista, y_lista, fill)
        plt.plot(x_lista, y_lista, plot)
        
    def setup_plot(self):
        self.fig = plt.figure(figsize=(6, 6), dpi=180)
        self.ax = self.fig.add_subplot(111)

    def show_plot(self):
        plt.show()