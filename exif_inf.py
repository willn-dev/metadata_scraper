exif_tag = {

    0x010d: 'Document Name:',
    0x010e: 'Image Description',
    0x0131: 'Software:',
    0x0132: 'Modify Date:',
    0x013b: 'Artist:',
    0x013c: 'Host Computer:',
    0x8825:'GPS INFO POINTER',
    0x9003: 'Date/Time Original:',
    0x9213: 'Revision History:',
    0xa430: 'Device Owner Name:',
    0xa431: 'Camera Serial Num:',
    0xa432: 'Lens Info:',
    0xa433: 'Lens Make:',
    0xa434: 'Lens Model:',
    0xa435: 'Lens Serial Num:',
    0xa436: 'Image Title:',
    0xa437: 'Photographer',
    0xa438: 'Editor:',
    0x838f: 'Battery Level:',
    # Camera settings/hardware.
    0x829a: 'Exposure Time:',
    0x82a6: 'MD Scale Pixel:',
    0x8649: 'Photoshop Settings',
    0x8827: 'ISO'

}

data_type_len = {
# this is to reference the data type of the value, and the corresponding number of
#bytes which each value takes up. 

    1: 1, # BYTE
    2: 1, # ASCII
    3: 2, #UINT16
    4: 4, #UINT32
    5: 8, # RATIONAL - Two longs for numerator/ denominator
    6: 1,
    7: 1,
    8: 2,
    9: 4,
    10: 8,
    11: 4,
    12: 8,

}

data_type = {
    1: 'byte',
    2: 'ascii',
    3: int,
    4: int,
    5: int,
    6: int,
    7: int,
    8: int,
    9: int,
    10: int,
    11: int,
    12: int,

}

gps_inf = {
    0x0000:	'GPSVersionID: ',
    0x0001:	'GPSLatitudeRef: ',
    0x0002:	'GPSLatitude: ',
    0x0003:	'GPSLongitudeRef: ',
    0x0004:	'GPSLongitude: ',
    0x0005:	'GPSAltitudeRef: ',
    0x0006:	'GPSAltitude: ',
    0x0007:	'GPSTimeStamp: ',
    0x0008:	'GPSSatellites',
    0x0009:	'GPSStatus',
    0x000a:	'GPSMeasureMode',
    0x000b:	'GPSDOP',
    0x000c:	'GPSSpeedRef',
    0x000d:	'GPSSpeed',
    0x000e:	'GPSTrackRef',
    0x000f:	'GPSTrack',
    0x0010:	'GPSImgDirectionRef',
    0x0011:	'GPSImgDirection',
    0x0012:	'GPSMapDatum',
    0x0013:	'GPSDestLatitudeRef',
    0x0014:	'GPSDestLatitude',
    0x0015:	'GPSDestLongitudeRef',
    0x0016:	'GPSDestLongitude',
    0x0017:	'GPSDestBearingRef',
    0x0018:	'GPSDestBearing',
    0x0019:	'GPSDestDistanceRef',
    0x001a:	'GPSDestDistance',
    0x001b:	'GPSProcessingMethod',
    0x001c:	'GPSAreaInformation',
    0x001d:	'GPSDateStamp',
    0x001e:	'GPSDifferential',
    0x001f:	'GPSHPositioningError',
}