##################################
########## QUESTION 1 ############
##################################
def readFile(filename):
    sentences = []
    with open(filename) as f:
        for line in f.readlines():
            sentences.append(line.strip())
    return sentences
    
def wordCounts(sentences):
    counts = {}
    for line in sentences:
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    return counts

def countTokens(sentences):
    count = 0
    for line in sentences:
        count += len(line.split())
    return count

def frequency(sentences):
    numTokens = countTokens(sentences)
    counts = wordCounts(sentences)
    frequencies = {}
    for k, v in counts.items():
        frequencies[k] = v / numTokens
    return frequencies

##################################
########## QUESTION 2 ############
##################################

def unigramProbability(sentence, corpusFilename):
    sentences = readFile(corpusFilename)
    frequencyDict = frequency(sentences)
    
    words = sentence.split()
    probability = 1.0
    for word in words:
        probability *= frequencyDict[word]
    return probability

##################################
########## QUESTION 3 ############
##################################

def ngrams(n, sentence):
    words = sentence.split()
    ngrams = []

    i, j = 0, n
    while (j < len(words) + 1):
        ngrams.append(" ".join(words[i:j]))
        i, j = i + 1, j + 1 
    return ngrams

def getBigramsCorpus(sentences):
    refBigrams = []
    for s in sentences:
        bigrams = ngrams(2, s)
        refBigrams = refBigrams + bigrams
    return refBigrams

def bigramProbability(sentence, filename):
    sentences = readFile(filename)

    refBigrams = getBigramsCorpus(sentences)
    sentenceBigrams = ngrams(2, sentence)

    bigramProbability = 1.0
    for sb in sentenceBigrams:
        bigramCount = refBigrams.count(sb)
        totalCount = 0
        for rb in refBigrams:
            if sb.split()[0] == rb.split()[0]:
                totalCount += 1
        bigramProbability *= bigramCount / totalCount
    return bigramProbability

##################################
########## QUESTION 4 ############
##################################

def getVocabCount(sentences):
    vocab = set()
    for s in sentences:
        words = s.split()
        for word in words:
            vocab.add(word)
    return len(vocab)

def bigramProbabilitySmoothing(sentence, filename):
    sentences = readFile(filename)

    refBigrams = getBigramsCorpus(sentences)
    sentenceBigrams = ngrams(2, sentence)
    vocabCount = getVocabCount(sentences)

    bigramProbability = 1.0
    for sb in sentenceBigrams:
        bigramCount = refBigrams.count(sb)
        totalCount = 0
        for rb in refBigrams:
            if sb.split()[0] == rb.split()[0]:
                totalCount += 1
        bigramProbability *= (bigramCount + 1) / (totalCount + vocabCount)
    return bigramProbability

def main():
    
    #######################
    ### QUESTION 1 TEST ###
    #######################

    filename = "corpus1.txt"

    sentences = readFile(filename)
    print(frequency(sentences))
    # {'with': 0.1111111111111111, 'mat': 0.1111111111111111, 'sat': 0.1111111111111111,
    #  'on': 0.1111111111111111, 'the': 0.2222222222222222, 'cat': 0.2222222222222222, 
    #  'a': 0.1111111111111111}

    #######################
    ### QUESTION 2 TEST ###
    #######################

    sentence = "a cat sat on the mat"
    print(unigramProbability(sentence, filename))
    # = 7.526705692635681e-06

    #######################
    ### QUESTION 3 TEST ###
    #######################

    filename = "corpus.txt"
    sentence = "the cat sat on the mat"
    print(bigramProbability(sentence, filename))
    # = 0.005580357142857142

    #######################
    ### QUESTION 4 TEST ###
    #######################

    filename = "corpus.txt"
    sentence = "<s> a cat sat on the car </s>"
    print(bigramProbabilitySmoothing(sentence, filename))
    # = 3.001704539363424e-05

    sentence = "<s> a cat sat on the mat </s>"
    print(bigramProbabilitySmoothing(sentence, filename))
    # = 0.00014094960445706513

if __name__=="__main__":
    main()