#!/usr/bin/python3

import sys, statistics
from collections import Counter

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)

def decrement(c):
    tmp = ""
    for i in range(len(c)):
        new = ((ord(c[i])-65) - 1) % 26
        tmp = tmp + alphabet[new]
    return tmp

def decode(cipher, key_list, key_len):
    acc = ""
    for i in range(len(cipher)):
        acc = acc + alphabet[(((ord(cipher[i])-65) - key_list[i % key_len]) % 26)]
    return acc

if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    #CTL-D to break stdin
    cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()

    #################################################################
    # Your code to determine the key and decrypt the ciphertext here
    list = []
    pop_var_list = []
    table = [[],[],[],[],[],[],[],[],[],[],[],[]]
    temp = 0
        #loop to determine key length based on pop_var function
    for i in range(2, 14):
        for j in range(0, i):
            list2 = [cipher[j::i], pop_var(cipher[j::i])]
            list.append(list2)
            temp = temp + list2[1]
        pop_var_list.append(temp/i)
        table[i-2].append(list)
        list = []
        temp = 0
    key_len = pop_var_list.index(max(pop_var_list)) + 2



    pop_list = []
    sublist = []
    accumulator = 0
        #cai-squared calculator
    for z in range(0, len(table[key_len - 2][0])):
        for u in range(26):
            yee = Counter(table[key_len - 2][0][z][0])
            for w in range(26):
                accumulator += ((yee[alphabet[w]] - (letter_freqs[alphabet[w]] * len(table[key_len - 2][0][z][0])))**2)/(letter_freqs[alphabet[w]] * len(table[key_len - 2][0][z][0]))
            sublist.append(accumulator)
            accumulator = 0
            table[key_len - 2][0][z][0] = decrement(table[key_len - 2][0][z][0])
        pop_list.append(sublist)
        sublist = []



    chi_sq_lst = []
        #determining the minimum chi-squared
    for b in range(len(table[key_len - 2][0])):
        chi_sq_lst.append(pop_list[b].index(min(pop_list[b])))



    decoded_cipher = decode(cipher, chi_sq_lst, key_len)
    print(decoded_cipher)