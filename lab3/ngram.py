# Compute n-grams for a given sentence
def compute_ngrams(n, s):
    ngrams = []
    words = s.split()
    
    i, j = 0, 0
    while i < n:
        igram = []

        k = i + 1
        while k < len(words) + 1:
            igram.append(words[j:k])
            j += 1
            k += 1
        
        ngrams.append(igram)
        j = 0
        i += 1
    
    return ngrams
        

def main():
    s = "cat sat on the mat"
    ngrams = compute_ngrams(4, s)
    for igram in ngrams:
        print(igram)


if __name__ == "__main__":
    main()