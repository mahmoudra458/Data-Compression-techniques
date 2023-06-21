import math
from tkinter import *
#Create main app window
Binary_app = Tk()
Binary_app.title("LZW Compression")
Binary_app.geometry("700x600")

def float_bin(number, k):
    b = ""
    for x in range(k):
        number = number * 2
        if number > 1:
            b = b + str(1)
            x = int(number)
            number = number - x
        elif number < 1:
            b = b + str(0)
        elif number == 1:
            b = b + str(1)
            break
    return b

def tag_encode(alpha, prob, chara_file, seq):
    char_info = []
    prob_range = 0.0
    #Here get low and upper the probability of each character in file
    for i in range(chara_file):
        low = prob_range
        prob_range = prob_range + prob[i]
        upper = prob_range
        char_info.append([alpha[i], low, upper])

    #Here start compress
    for i in range(len(seq) - 1):
        for j in range(len(char_info)):
            if seq[i] == char_info[j][0]:
                prob_low = char_info[j][1]
                prob_high = char_info[j][2]
                diff = prob_high - prob_low
                #Here to update scale
                for k in range(len(char_info)):
                    char_info[k][1] = prob_low
                    char_info[k][2] = prob[k] * diff + prob_low
                    prob_low = char_info[k][2]
                break
    low = 0
    high = 0
    for i in range(len(char_info)):
        if char_info[i][0] == seq[-1]:
            low = char_info[i][1]
            high = char_info[i][2]
    tag = (low + high) / 2
    the_text = Label(Binary_app, text="The Tag value for the sequence is : ", height=2, font=("Arial", 20))
    the_text.pack()
    text_to_compress = Label(Binary_app, text=str(tag), height=2, font=("Arial", 15))
    text_to_compress.pack()
    k = math.ceil(math.log((1 / (high - low)), 2) + 1)
    # convert floating point number to binary
    bin_code = float_bin(tag, k)
    the_text = Label(Binary_app, text="Binary code for the sequence is : ", height=2, font=("Arial", 20))
    the_text.pack()
    text = (str(seq) + " is " + str(bin_code))
    text_to_compress = Label(Binary_app, text=text, height=2, font=("Arial", 15))
    text_to_compress.pack()
    return [tag, N, alpha, prob]

def tag_decode(binary_seq):
    tag = binary_seq[0]
    N = binary_seq[1]
    alpha = binary_seq[2]
    prob = binary_seq[3]
    unity = []
    prob_range = 0.0
    seq = ""
    for i in range(N):
        l = prob_range
        prob_range = prob_range + prob[i]
        u = prob_range
        unity.append([alpha[i], l, u])
    for i in range(N + 1):
        for j in range(len(unity)):
            if unity[j][1] < tag < unity[j][2]:
                prob_low = unity[j][1]
                prob_high = unity[j][2]
                diff = prob_high - prob_low
                seq = seq + unity[j][0]
                for k in range(len(unity)):
                    unity[k][1] = prob_low
                    unity[k][2] = prob[k] * diff + prob_low
                    prob_low = unity[k][2]
                break
    the_text = Label(Binary_app, text="The sequence for tag : ", height=2, font=("Arial", 20))
    the_text.pack()
    text = (str(tag) + " is " + str(seq))
    text_to_compress = Label(Binary_app, text=text, height=2, font=("Arial", 15))
    text_to_compress.pack()
alphabet = []
probability = []
N = int(input("Enter number of letters in file: "))
for i in range(N):
    a = input("Enter the letter: ")
    p = float(input("Enter probability for " + a + ": "))
    alphabet.append(a)
    probability.append(p)
sequence = input("Enter the sequence to be encoded: ")
master = tag_encode(alphabet, probability, N, sequence)
tag_decode(master)
Binary_app.mainloop()