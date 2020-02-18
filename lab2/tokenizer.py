import sys
import string

# Tokenize an input file and write to tokenized.txt
def tokenize(fname):
    punctuation = string.punctuation.replace(" ", "")
    with open(fname, 'r') as f, open("tokenized.txt", 'a') as output:
        for line in f.readlines():
            formatted = ""
            for i, char in enumerate(line):
                if char in punctuation:
                    formatted = formatted + " " + char + " "
                else:
                    formatted = formatted + char
                print(formatted)
            output.write(formatted.strip())

if __name__=="__main__":
    fname = sys.argv[1]
    tokenize(fname)