

def edits(r, t, m):
    for i in range(len(r) + 1):
        m[i][0] = i 
    for j in range(len(t) + 1):
        m[0][j] = j

    for i in range(1, len(r) + 1):
        for j in range(1, len(t) + 1):
            m[i][j] = min(
                        m[i][j-1]   + 1,
                        m[i-1][j]   + 1,
                        m[i-1][j-1] + (0 if r[i-1] == t[j-1] else 1)
                      )
    return m[-1][-1]

def wer(r, t):
    r = r.split()
    t = t.split()

    m = [[0 for x in range(len(t) + 1)] for y in range(len(r) + 1)]
    
    num_edits = edits(r, t, m)
    return num_edits/len(r)

def main():
    # Reference
    r = "Israeli officials are responsible for airport security"

    # Translation ouput
    t = "Israeli official responsible airport is security"
    print(wer(r, t))

if __name__=="__main__":
    main()