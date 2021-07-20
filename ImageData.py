from PIL import Image
from PIL.ExifTags import TAGS
import exifread
import re

import json

def read():
    with open('IMG_1956.HEIC', 'rb') as f:
        try:
            contents = exifread.process_file(f)
            for key in contents:
                if key == "GPS GPSLongitude":
                    print("经度: ", contents[key], contents['GPS GPSLatitudeRef'])
                    print("纬度: ", contents['GPS GPSLatitude'], contents['GPS GPSLongitudeRef'])
                    print("高度基准: ", contents['GPS GPSAltitudeRef'])
                    print("海拔高度: ", contents['GPS GPSAltitude'])
                if re.match('Image Make', key):
                    print('品牌信息: ', contents[key])
                if re.match('Image Model', key):
                    print('具体型号: ', contents[key])
                if re.match('Image DateTime', key):
                    print('拍摄时间: ', contents[key])
                if re.match('EXIF ExifImageWidth', key):
                    print('照片尺寸: ', contents[key], '*', contents['EXIF ExifImageLength'])
                if re.match('Image ImageDescription', key):
                    print('图像描述: ', contents[key])

            print("-" * 100)
            exif_dict = exifread.process_file(f)
            for key in exif_dict:
                print("%s: %s" % (key, exif_dict[key]))

            print('拍摄时间：', exif_dict['EXIF DateTimeOriginal'])
            print('照相机制造商：', exif_dict['Image Make'])
            print('照相机型号：', exif_dict['Image Model'])
            print('照片尺寸：', exif_dict['EXIF ExifImageWidth'], exif_dict['EXIF ExifImageLength'])

            # 经度
            lon_ref = exif_dict["GPS GPSLongitudeRef"].printable
            lon = exif_dict["GPS GPSLongitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
            lon = float(lon[0]) + float(lon[1]) / 60 + float(lon[2]) / float(lon[3]) / 3600
            if lon_ref != "E":
                lon = lon * (-1)

            # 纬度
            lat_ref = exif_dict["GPS GPSLatitudeRef"].printable
            lat = exif_dict["GPS GPSLatitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
            lat = float(lat[0]) + float(lat[1]) / 60 + float(lat[2]) / float(lat[3]) / 3600
            if lat_ref != "N":
                lat = lat * (-1)
            print('照片的经纬度：', (lat, lon))

        except Exception as e:
            print("error: ", e)

def get_exif_data(fname):
    """Get embedded EXIF data from image file."""
    ret = {}
    try:
        img = Image.open(fname)
        if hasattr( img, '_getexif' ):
            exifinfo = img._getexif()
            if exifinfo != None:
                for tag, value in exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
    except IOError:
        print('IOERROR ' + fname)
    return ret
if __name__ == '__main__':
    fileName = "1 (36).jpg"
    # exif = get_exif_data(fileName)
    # print(exif)

    read()