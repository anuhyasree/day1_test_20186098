'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    """ frequence"""
    string = string.strip()
    regex = re.compile('[^a-z A-Z 0-9]')
    string = regex.sub('', string)
    # print(string)
    # string = string.strip()
    sequence = string.split(' ')
    freq = {}
    for i_i in sequence:
        freq[i_i] = freq.get(i_i, 0) + 1
    return freq
def main():
    """main"""
    string_len = ''
    num_lines = int(input())
    for i in range(num_lines):
        i += 1
        string_len += input()
        string_len += ' '
    print(tokenize(string_len))

if __name__ == '__main__':
    main()
