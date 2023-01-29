import sys
from Samples.geocoder import get_coordinates, get_nearest_object


def main():
    toponym_to_find = " ".join(sys.argv[1:])

    if toponym_to_find:
        lat, lon = get_coordinates(toponym_to_find)
        point = lat, lon
        kind = 'district'
        district = get_nearest_object(point, kind)
        print(district)
    else:
        print("No data")


if __name__ == '__main__':
    main()
