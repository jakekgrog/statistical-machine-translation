import numpy

def edits(r, t, m):
    # Dynamic Programming
    
    for i in range(len(r)+1):
        m[i][0] = i
    for j in range(len(t)+1):
        m[0][j] = j
    
    for i in range(1, len(r)+1):
        for j in range(1, len(t)+1):
            m[i][j] = min(
                        m[i-1][j]   + 1,
                        m[i][j-1]   + 1,
                        m[i-1][j-1] + (0 if r[i-1] == t[j-1] else 1)
                      )
    return m[-1][-1]

def wer(r, t):
    r_tokens = r.split()
    t_tokens = t.split()

    # Build matrix of 0's
    matrix = numpy.zeros((len(r_tokens) + 1) * (len(t_tokens) + 1))
    matrix = matrix.reshape((len(r_tokens) + 1, len(t_tokens) + 1))

    num_edits = edits(r_tokens, t_tokens, matrix)

    return num_edits / len(r_tokens)

def main():
    # Reference
    r = "Israeli officials are responsible for airport security"

    # Translation ouput
    t = "Israeli official responsible airport is security"

    print("WER score: " + "{:.4f}".format(float(wer(r, t))))

if __name__=="__main__":
    main()