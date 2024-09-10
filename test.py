from geometry_drawer import draw
from shapely import Point, LineString, Polygon

platno = draw.GeometryDrawer()

poligon1 = Polygon([(1,2),(3,4),(6,5),(4,2),(3,3),(1,2)])
poligon2 = Polygon([(4,6),(5,3),(10,5),(7,7),(4,6)])
linija1 = LineString([(3,7),(7,5),(7,2)])
linija2 = LineString([(1,4),(3,4),(6,5),(8,7)])
tocka1 = Point(5,4)
tocka2 = Point(4,3)
tocka3 = Point(2,5)


platno.crtaj_tocku(tocka1, "bs")
platno.crtaj_tocku(tocka2, "bs")
platno.crtaj_tocku(tocka3, "bs")
platno.crtaj_liniju(linija1, "r-")
platno.crtaj_liniju(linija2, "r-")
platno.crtaj_poligon(poligon1)
platno.crtaj_poligon(poligon2)

platno.show_plot()