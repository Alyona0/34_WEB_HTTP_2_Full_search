# определение уровня масштабирования для GeoObject Яндекс.Карт

def zoomСorner(upperCorner, lowerCorner):
# масштаб по крайним координатам геообъекта
# upperCorner - верхний правый угол список, текст
# lowerCorner - нижний левый угол список, текст
    east, north = upperCorner.split(" ")
    west, south = lowerCorner.split(" ")

    delta_lon = float(east) - float(west)
    delta_lat = float(north) - float(south)

    for step in  range(17, 0, -1):
        #  охват карты по долготе 360 град
        if (delta_lon * (2 ** step)) < 360:
            print((delta_lon * (2 ** step)), step)
            zoom_lon = step
            break

    for step in  range(17, 0, -1):
        #  охват карты по штроте 180 град
        if (delta_lat * (2 ** step)) < 180:
            print((delta_lat * (2 ** step)), step)
            zoom_lat = step
            break

    if zoom_lon < zoom_lat:
        return(str(zoom_lon))
    else:
        return(str(zoom_lat))

