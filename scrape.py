from exif_inf import exif_tag


# ----> 225 is flag for EXIF START <----###
def main():
    raw_data = [] #full data
    parsed = [] # list of indices containing exif values.
    byte_order = ''# is set to big or little endian


    with open('assets/juniper_butterfly.jpeg', 'rb') as f:
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

            #BIG OR LITTLE ENDIAN DETERMINATION
            b_order = byte_obj[exif_start + 10: exif_start +12] # position of MM/II 2byte order marker.

            if b_order == b'MM':
                byte_order = 'big'
            elif b_order == b'II':
                byte_order = 'little'

            head_len = byte_obj[exif_start + 2: exif_start + 4] # Exif header 6 byte total. skipping first values and just reading len

            exif_len = int.from_bytes(head_len, byteorder=byte_order)
            exif_end = exif_start + exif_len


    byte_stepper(exif_start, exif_end, byte_obj, byte_order)
#temp checks
#print(byte_obj[exif_start:exif_end])
#print("\n")
#print(exif_len)
#print(byte_order)



def byte_stepper(start, end, byte_obj, byte_order):

    ifd_entry_amt = int.from_bytes((byte_obj[start + 18 : start + 20]), byteorder= byte_order)
    all_ifd_entries = byte_obj[start + 20: start + 20 + (ifd_entry_amt * 12)] # each ifd entry is 12 bytes long hence mult

    # gets each ifd entry individually
    #RESUME HERE NEED TO COMPARE WITH TABLE SEE MIDORI BYTE STEPPER ENTRY

    for i in range(0, len(all_ifd_entries), 12):
        single_ifd = all_ifd_entries[i:i + 12]
        print(single_ifd)
        print("\n")

    #CYCLE THRU ENTRY AND COMPARE TO IFD STRUCTURE AND GO 2, 2, 4, 4,

if __name__ == ("__main__"):
    main()
