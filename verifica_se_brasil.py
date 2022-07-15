from shapely.geometry import Point, Polygon


# saber se essa latitude e longitude está no Brasil


def area_contem_cliente(a, c):
    ponto = Point(c)
    poligono = Polygon(a)
    return poligono.contains(ponto)


cidade = (-15.7801, -47.9292)

brasil = [(-8.046177, -34.584961),
          (-20.784877, -40.737305),
          (-33.713374, -53.481445),
          (-30.285635, -57.612305),
          (-16.370743, -60.249023),
          (-7.436552, -73.696289),
          (4.403373, -64.907227),
          (4.228090, -51.547852)]

print(area_contem_cliente(brasil, cidade))
