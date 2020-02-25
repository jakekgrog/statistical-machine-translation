from itertools import permutations 
import numpy 

def edits(r, t):

    m = numpy.zeros((len(r) + 1) * (len(t) + 1))
    m = m.reshape((len(r) + 1, len(t) + 1))
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

def ter(r, h):
    
    minEditDistance = edits(r, h)
    shifts = [list(shift) for shift in list(permutations(h))]
    print(shifts)
    for hp in shifts:
        ed = edits(r, hp)
        if ed < minEditDistance:
            minEditDistance = ed
    return minEditDistance


def main():
    r = "SAUDI ARABIA denied THIS WEEK information published in the AMERICAN new york times"
    t = "THIS WEEK THE SAUDIS denied information published in the new york times"
    r_tokens = r.split()
    t_tokens = t.split()

    print(ter(r_tokens, t_tokens))

if __name__=="__main__":
    main()