import heapq
from tkinter import *
huffman = Tk()
huffman.title("Huffman coding")
huffman.geometry("1500x1500")
class huffmanCoding:
    def __init__(self):
        self.heap = []
        self.bin_codes = {}
        self.reverse_coding = {}
        self.padded_length = []
        self.frequency = {}

    class heapNode:
        def __init__(self, char, freq, left=None, right=None):
            self.char = char
            self.freq = freq
            self.left = left
            self.right = right

        def __lt__(self, other):
            return self.freq < other.freq

        def __eq__(self, other):
            if other is None:
                return False
            return self.freq == other.freq

    @staticmethod
    def frequency_table(self, text):
        # Here calc freq and return it
        for char in text:
            if not char in self.frequency:
                self.frequency[char] = 0
            self.frequency[char] += 1
        print(self.frequency)
        return self.frequency

    def heap_fun(self, frequency):
        # Here priority queue
        for key in frequency:
            node = self.heapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        # here build huffman tree
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged_node = self.heapNode(None, node1.freq + node2.freq)
            merged_node.left = node1
            merged_node.right = node2
            heapq.heappush(self.heap, merged_node)

    def code_left_right(self, node, current_code):
        if node is None:
            return
        if node.char is not None:
            self.bin_codes[node.char] = current_code
            self.reverse_coding[current_code] = node.char
        self.code_left_right(node.left, current_code + "0")
        self.code_left_right(node.right, current_code + "1")

    def make_bin_code(self):
        # here codes for each character
        root = heapq.heappop(self.heap)
        current_code = ""
        self.code_left_right(root, current_code)

    def get_encoded_text(self, text):
        # Here replace character with code and return
        encoded_text = ""
        for char in text:
            if len(self.bin_codes[char]) == 8:
                encoded_text += self.bin_codes[char]
            else:
                padded = 8 - len(self.bin_codes[char])
                for i in range(padded):
                    self.bin_codes[char] += "0"
                encoded_text += self.bin_codes[char]
            self.padded_length.append(padded)
        return encoded_text

    def get_total_bits(self):
        total_bits = 0
        for i in self.reverse_coding:
            for j in self.frequency:
                if j == self.reverse_coding[i]:
                    total_bits += len(i) * self.frequency[j]
        return total_bits
    def compress(self):
        with open("sequence_characters", 'r') as file, open("output_file", 'w') as output:
            text = file.read()
            text = text.rstrip()
            the_text = Label(huffman, text="The Original text : ", height=2, font=("Arial", 20))
            the_text.pack()
            text_to_compress = Label(huffman, text=text, height=2, font=("Arial", 15))
            text_to_compress.pack()
            freq = self.frequency_table(self, text)
            self.heap_fun(freq)
            self.merge_nodes()
            self.make_bin_code()
            encoded_text = self.get_encoded_text(text)
            output.write(encoded_text)
            str_bits = str(8 * len(text)) + " bits"
            the_text = Label(huffman, text="The total original bits : ", height=2, font=("Arial", 20))
            the_text.pack()
            text_to_compress = Label(huffman, text=str_bits, height=2, font=("Arial", 10))
            text_to_compress.pack()
            compressed_bits = str(self.get_total_bits()) + " bits"
            the_text = Label(huffman, text="The total compressed bits : ", height=2, font=("Arial", 20))
            the_text.pack()
            text_to_compress = Label(huffman, text=compressed_bits, height=2, font=("Arial", 10))
            text_to_compress.pack()
        file.close()
        output.close()

    @staticmethod
    def get_eight_bits(start, end, text_bits):
        return text_bits[start:end]

    def decompress(self):
        with open("output_file", "r") as read_file, open("original_string", "w") as out_file:
            binary_seq = read_file.read()
            original_str = ""
            i = 0
            count = 0
            text_binary = ""
            while i < (len(binary_seq)):
                eight_bits = self.get_eight_bits(i, i+8, binary_seq)
                padded_count = self.padded_length[count]
                count += 1
                eight_bits = eight_bits[0:8 - padded_count]
                if eight_bits in self.reverse_coding:
                    original_str += self.reverse_coding[eight_bits]
                    text_binary += eight_bits
                i += 8
            the_text = Label(huffman, text="The encoded bits : ", height=2, font=("Arial", 20))
            the_text.pack()
            text_to_compress = Label(huffman, text=text_binary, height=2, font=("Arial", 10))
            text_to_compress.pack()
            out_file.write(original_str)
        the_text = Label(huffman, text="The decompressed text : ", height=2, font=("Arial", 20))
        the_text.pack()
        text_to_compress = Label(huffman, text=original_str, height=2, font=("Arial", 15))
        text_to_compress.pack()
        read_file.close()
        out_file.close()
# Here is main calling
huff = huffmanCoding()
huff.compress()
huff.decompress()
huffman.mainloop()
