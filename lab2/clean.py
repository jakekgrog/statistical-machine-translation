import sys

# Removes line pairs from source and target files whose 
# length is out of the len_min and len_max bounds
def clean(source, target, len_min, len_max):
    with open(source, 'r') as src, open(target, 'r') as trgt:
        s = src.readlines()
        t = trgt.readlines()
        inp, out = [], []
        for i, (sline, tline) in enumerate(zip(s, t)):
            tokens = sline.split()
            if len(tokens) <= len_max and len(tokens) >= len_min:
                inp.append(sline)
                out.append(tline)

    open(source, 'w').close()
    open(target, 'w').close()

    with open(source, 'w') as i, open(target, 'w') as o:
        i.write("".join(inp))
        o.write("".join(out))


if __name__=="__main__":
    iname, oname = sys.argv[1], sys.argv[2]
    print(iname, oname)
    clean(iname, oname, 3, 5)
    