from tkinter import *
#Create main app window
text_file = open("Text_file", "r")
text_input = text_file.read()
text_file.close()
lzw_app = Tk()
lzw_app.title("LZW Compression")
lzw_app.geometry("700x600")
Tag = []
def lzw_Compression(text):
    ascii_table = [('A', 65), ('B', 66), ('C', 67), ('D', 68), ('E', 69), ('F', 70), ('G', 71), ('H', 72),
                   ('I', 73), ('J', 74), ('K', 75), ('L', 76), ('M', 77), ('N', 78), ('O', 79),
                   ('P', 80), ('Q', 81), ('R', 82), ('S', 83), ('T', 84), ('U', 85), ('V', 86),
                   ('W', 87), ('X', 88), ('Y', 8), ('Z', 90)]
    ##Here is the start part of GUI for compression
    the_text = Label(lzw_app, text="The Original text : ", height=2, font=("Arial", 20))
    the_text.pack()
    text_to_compress = Label(lzw_app, text=text, height=2, font=("Arial", 15))
    text_to_compress.pack()
    origin_bits = len(text) * 8
    str_origin_bits = str(origin_bits) + " bits"
    total_bits_text = Label(lzw_app, text="Total bits of original text : ", height=2, font=("Arial", 20))
    total_bits_text.pack()
    total_bits = Label(lzw_app, text=str_origin_bits, height=2, font=("Arial", 15))
    total_bits.pack()
    ##Here is the end part of GUI compression
    ##Here is the start of compression
    sub_str = ""
    count = 0
    counter = 128
    i = 0
    while i < (len(text)):#ABAABA
        sub_str += text[i]
        for j in range(len(ascii_table)):
            if sub_str == ascii_table[j][0]:
                count = 1
                tag_value = ascii_table[j][1]
                break
            else:
                count = 0
        if count == 0:
            ascii_table.append((sub_str, counter))
            counter += 1
            sub_str = ""
        i += 1
        if len(sub_str) == 0:
            i = i - 1
            Tag.append(tag_value)
    if sub_str:
        for j in range(len(ascii_table)):
            if sub_str == ascii_table[j][0]:
                index = j
        Tag.append(ascii_table[index][1])
    ##Here is the end of compression
##Here compression calling
lzw_Compression(text_input)
##Here decompression start function
def lzw_decompression():
    dictionary_table = [('A', 65), ('B', 66), ('C', 67), ('D', 68), ('E', 69), ('F', 70), ('G', 71), ('H', 72),
                        ('I', 73), ('J', 74), ('K', 75), ('L', 76), ('M', 77), ('N', 78), ('O', 79),
                        ('P', 80), ('Q', 81), ('R', 82), ('S', 83), ('T', 84), ('U', 85), ('V', 86),
                        ('W', 87), ('X', 88), ('Y', 8), ('Z', 90)]
    original_text = []
    count = 0
    counter = 128
    for i in Tag:
        for j in range(len(dictionary_table)):
            if i == dictionary_table[j][1]:
                index = j
                break
            else:
                index = -1
        if count == 0:
            original_text.insert(count, dictionary_table[index][0])
            prv_str = dictionary_table[index][0]
            count += 1
        elif count > 0 and index >= 0:
            original_text.insert(count, dictionary_table[index][0])
            count += 1
            index_str = dictionary_table[index][0]
            dic_str = prv_str + index_str[0]
            dictionary_table.append((dic_str, counter))
            counter += 1
            prv_str = dictionary_table[index][0]
        elif index == -1:
            dic_str = prv_str + prv_str[0]
            dictionary_table.append((dic_str, counter))
            counter += 1
            original_text.insert(count, dic_str)
            prv_str = dic_str
            count += 1
    de_compress = ""
    for i in range(len(original_text)):
        de_compress += original_text[i]
    output_text = open("output_file", "w")
    output_text.write(de_compress)
    output_text.close()
    ##Here is the end of decompression part
    ##Here is the start part of GUI for decompression
    total_bit_compressed = len(Tag) * 8
    bits_total = str(total_bit_compressed) + " bits"
    the_text = Label(lzw_app, text="The compressed text : ", height=2, font=("Arial", 20))
    the_text.pack()
    the_decompressed_text = Label(lzw_app, text=de_compress, height=2, font=("Arial", 15))
    the_decompressed_text.pack()
    total_bits_text = Label(lzw_app, text="Total bits of compressed text : ", height=2, font=("Arial", 20))
    total_bits_text.pack()
    total_bits = Label(lzw_app, text=bits_total, height=2, font=("Arial", 15))
    total_bits.pack()
    the_text.pack()
    ##Here is the end part of GUI decompression
##Here decompression calling
lzw_decompression()
##Here end of the code
lzw_app.mainloop()



