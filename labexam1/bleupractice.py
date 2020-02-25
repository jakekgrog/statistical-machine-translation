def compute_ngrams(s, n):
    ngrams = []
    tokens=s.split()
    i, k = 0, n
    while k < len(tokens) + 1:
        ngrams.append(tokens[i:k])
        i, k = i + 1, k + 1
    return ngrams

def bleu(h, r, n):
    return min(1, bp(h, r)) * precision(h, r, n)

def precision_comments(h, r, n):
    # Initialize count_clipped to 0 for 1 to 4

    # for i in 1..4
        # compute h_ngram for i
        # compute ngrams for i foreach reference

        # foreach h_gram in h_ngram
            # initialize ref_counts of keys 1..len(r)

            # foreach r_i, r_igram in r_ngrams
                # foreach r_gram in r_igram
                    # if r_gram == h_gram
                        # ref_count[r_i] += 1
            # count_clipped[i] += max(ref_counts.values())
        # i += 1

    # n_precision = 1
    # foreach k, v in count_clipped.items()
        # count = compute_ngrams(h, k)
        # n_precision *= v / len(count)

    # return n_precision ** (1/n) 
    pass

def precision(h, r, n):
    count_clipped = {}
    for x in range(1, n+1): count_clipped[x] = 0

    for i in range(1, n+1):
        h_ngrams = compute_ngrams(h, i)
        r_ngrams = [compute_ngrams(ref, i) for ref in r]

        for h_gram in h_ngrams:
            ref_counts = {}
            for x in range(len(r)): ref_counts[x] = 0

            for r_i, r_igrams in enumerate(r_ngrams):
                for r_gram in r_igrams:
                    if r_gram == h_gram:
                        ref_counts[r_i] += 1
            count_clipped[i] += max(ref_counts.values())
    
    n_precision = 1
    for k, v in count_clipped.items():
        count = len(compute_ngrams(h, k))
        n_precision *= v / count
    
    return n_precision ** (1/n)

def bp(h, r):
    outputlength = len(compute_ngrams(h, 1))
    r_unigrams = [compute_ngrams(ref, 1) for ref in r]

    closest = r_unigrams[0]
    diff = abs(outputlength-len(r_unigrams[0]))
    for gram in r_unigrams:
        if abs(outputlength-len(gram)) < diff:
            closest = gram
            diff = outputlength-len(gram)
    return outputlength/len(closest)

def main():
    n = 4
    h = "The gunman was shot dead by police ."
    #print(compute_ngrams(h, 4))
    r = ["The gunman was shot to death by the police .", "The gunman was shot to death by the police .", "Police killed the gunman .", "The gunman was shot dead by the police ."]
    print(bleu(h, r, n))


if __name__=="__main__":
    main()