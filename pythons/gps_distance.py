from math import radians, cos, sin, asin, sqrt

from geopy.distance import geodesic


# 计算两点间距离-m
def geodistance(lng1, lat1, lng2, lat2):
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    dis = 2 * asin(sqrt(a)) * 6371 * 1000
    return dis


def get_distance(lng1, lat1, lng2, lat2):
    return geodesic((lat1, lng1), (lat2, lng2)).m  # 计算两个坐标直线距离


if __name__ == '__main__':
    lat1, lon1 = (22.5995780, 113.973129)  # 深圳野生动物园(起点）
    lat2, lon2 = (22.6986848, 114.3311032)  # 深圳坪山站 (百度地图测距：38.3km)
    d1 = geodistance(lon1, lat1, lon2, lat2)
    d2 = get_distance(lon1, lat1, lon2, lat2)
    print(d1)
    print(d2)
