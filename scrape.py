from exif_inf import exif_tag, data_type_len, data_type
import sys
import pathlib

# ----> 225 is flag for EXIF START <----###
def main():
    raw_data = [] #full data
    parsed = [] # list of indices containing exif values.
    byte_order = ''# is set to big or little endian

    path_image = file_select()

    with open(path_image, 'rb') as f:
        byte_obj = f.read()

        length = len(byte_obj)

        for i, v in enumerate(byte_obj):

            if v == 255 and i < length -1: 

                raw_data.append((i, byte_obj[i + 1]))
            

    for each in raw_data:
        if each[1] != 0:
            parsed.append(each)


    for each in parsed:
        if each[1] == 225:
            exif_start = each[0]
            break
    else:
        print("Image contains no EXIF data")
        exit()

            #BIG OR LITTLE ENDIAN DETERMINATION
    b_order = byte_obj[exif_start + 10: exif_start +12] # position of MM/II 2byte order marker.

    if b_order == b'MM':
        byte_order = 'big'
    elif b_order == b'II':
        byte_order = 'little'

    head_len = byte_obj[exif_start + 2: exif_start + 4] # Exif header 6 byte total. skipping first values and just reading len

    exif_len = int.from_bytes(head_len, byteorder=byte_order)
    exif_end = exif_start + exif_len
    tiff_start = exif_start + 10


    byte_stepper(exif_start, exif_end, byte_obj, byte_order, tiff_start)

#---------------------------------------------------------------------------------------------------------------------------------
def byte_stepper(start, end, byte_obj, byte_order, tiff_start):

    ifd_entry_amt = int.from_bytes((byte_obj[start + 18 : start + 20]), byteorder= byte_order)
    all_ifd_entries = byte_obj[start + 20: start + 20 + (ifd_entry_amt * 12)] # each ifd entry is 12 bytes long hence mult

    print(f"Image has {ifd_entry_amt} unique metadata entries.")


    #start parse IFD individually
    for i in range(0, len(all_ifd_entries), 12):
        single_ifd = all_ifd_entries[i:i + 12]


        tag_id = int.from_bytes(single_ifd[0:2], byteorder=byte_order)
        datatype = single_ifd[2:4] 
        value_count = single_ifd [4:8]
        val_or_ptr = single_ifd[8:12]
    
        if tag_id in exif_tag:
            datatype = int.from_bytes(single_ifd[2:4], byteorder=byte_order)
            value_count = int.from_bytes(single_ifd [4:8], byteorder= byte_order)
            val_or_ptr = int.from_bytes(single_ifd[8:12], byteorder= byte_order)

            if datatype in data_type_len:
                length_of_bytes = data_type_len[datatype]

            true_byte_len = value_count * length_of_bytes

            if true_byte_len > 4:
                ptr_value_start = (tiff_start + val_or_ptr)
                ptr_value_end = (ptr_value_start + true_byte_len)
            
                true_data = byte_obj[ptr_value_start:ptr_value_end]
                print(exif_tag[tag_id], end=' ')
                type_decode = which_type(datatype)
                final = decoding(true_data, datatype,)
                

                print(final)

            elif true_byte_len <= 4:
                true_data = val_or_ptr
                type_decode = which_type(datatype)
                final = decoding(true_data, datatype)

                if tag_id == 0x8825: #pointer for gps info
                    gps_parse(byte_obj, tiff_start, val_or_ptr, byte_order)


                print(exif_tag[tag_id], end=' ')
                print(final)

        else:
            print("not found")

#------------------------------------------------------------------------------

def file_select():
    try:
        file_loc = sys.argv[1]
    except IndexError:
        print("Must specify path to image. \n Usage: scrape.py (imagepath)")
        exit()


    extention = pathlib.Path(file_loc).suffix

    if extention != '.jpeg' and extention != '.jpg':
        print("This program is designed for analysing jpeg/jpg images only.")
        exit()

    return file_loc

#--------------------------------------------------------------------------------
def which_type(integer_for_type):
    type_key = data_type[integer_for_type]
    return type_key
    
#--------------------------------------------------------------------------------
def decoding(true_data, datatype):

    if datatype == 2 and isinstance(true_data, bytes):
        return true_data.decode('ascii')
    else:
        return true_data
        
#--------------------------------------------------------------------------------
def gps_parse(byte_obj, tiff_start, gps_ptr, byte_order):
    print('testing')
    start = tiff_start + gps_ptr
    gps_entry_amt = byte_obj[start: start + 2]

    print(int.from_bytes(gps_entry_amt, byteorder= byte_order))

    #TODO: Make gps parsing loop to loop thru the gps entry amount in the 12 byte steps as
    #previously done in byte_stepper func

if __name__ == ("__main__"):
    main()


#finishing where data is decoded and printed in func bytestepper