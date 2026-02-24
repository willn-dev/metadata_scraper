
raw_data = []
parsed = []

with open('assets/juniper_butterfly.jpeg', 'rb') as f:
    byte_obj = f.read()

    length = len(byte_obj)

    for i, v in enumerate(byte_obj):

        if v == 255 and i < length -1: 

            raw_data.append((i, byte_obj[i + 1]))
            



for each in raw_data:
    if each[1] != 0:
        parsed.append(each)


print(parsed)