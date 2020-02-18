from ngram import compute_ngrams
from functools import reduce

# Calculate BLEU score of candidate translation using a single reference sentence.
def sentence_bleu(trans, ref, n):
    precisions = []

    trans_ngrams = compute_ngrams(4, trans)
    reference_ngrams = compute_ngrams(4, ref)

    i = 1
    while i <= n:
        
        num_igrams = len(trans_ngrams[i-1])
        ref_igrams = reference_ngrams[i-1]
        trans_igrams = trans_ngrams[i-1]

        num_clipped_igrams = 0
        for tgram in trans_igrams:
            for rgram in ref_igrams:
                if tgram == rgram:
                    num_clipped_igrams += 1
        precisions.append(num_clipped_igrams/num_igrams)
        i += 1
    
    n_precision = (reduce((lambda x, y: x * y), precisions))**(1/n)
    brevity_penalty = min(1, len(trans_ngrams[0])/len(reference_ngrams[0]))
    
    return brevity_penalty*n_precision

# Calculate BLEU score of candidate translation for using multiple reference sentences.
def sentence_bleu_2(trans, refs, n):
    precisions = []
    for ref in refs:
        precisions.append(sentence_bleu(trans, ref, n))

    return max(precisions)
    
def main():
    trans = "The gunman was shot dead by police ."
    ref = "The gunman was shot dead by the police ."
    print("BLEU score: " + str(sentence_bleu(trans, ref, 4))) # 0.6801

    trans = "The gunman was shot dead by police ."
    refs = [
        "The gunman was shot to death by the police .",
        "The gunman was shot to death by the police .",
        "Police killed the gunman .",
        "The gunman was shot dead by the police ."
    ]
    
    print("BLEU score: " + str(sentence_bleu_2(trans, refs, 4))) # 0.6801


if __name__ == "__main__":
    main()
    