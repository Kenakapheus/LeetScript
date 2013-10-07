import re, time, sys

def exe(i, s = [], d = True, debug = False):
    c=[r"(\d+),?\d*|\[[^]^[]*\]","##?","§","{","}",r"\(",r"\)","%","!","~","@",r"\<",r"\>",r"\.\.?"]
    m = re.compile("|".join("(?P<%s>%s)"%(chr(65+p),c[p])for p in range(0,len(c)))).search
    t,o,p,l,f = 0,"",0,[],m(i)
    while f is not None:
        c,v,p = f.lastgroup,f.group(),f.end()
        if c == 'A':
            try:
                s += [float(v.replace(',', '.'))]
            except ValueError:
                s += [v.strip('[]')]
        elif c == 'B':
            v2 = s.pop()
            v1 = s.pop()
            if len(v) == 1:
                try:
                    s += [v1 + v2]
                except TypeError:
                    s += [str(v1) + str(v2)]
            else:
                s += [v1 - v2]
        elif c == 'C':
            v1 = str(s.pop())
            if d:
                sys.stdout.write(v1)
            o += v1
        elif c == 'D':
            s += [s[-1]]
        elif c == 'E':
            del s[-1]
        elif c == 'F':
            l += [p]
        elif c == 'G':
            if l:
                v1 = l.pop()
                if s and s[-1]:
                    p = v1 - 1
        elif c == 'H':
            v1 = s.pop()
            v2 = s.pop()
            s += [v1] + [v2]
        elif c == 'I':
            s += ["\n"]
        elif c == 'J':
            s += [re.sub(str(s.pop()), str(s.pop()), str(s.pop()))]
        elif c == 'K':
            time.sleep(s.pop())
        elif c == 'L':
            for v1 in str(s.pop()):
                s += [ord(v1)]
        elif c == 'M':
            s += chr(int(s.pop()))
        elif c == 'N':
            v2 = s.pop()
            v1 = s.pop()
            if len(v) == 1:
                s += [v1 * v2]
            else:
                s += [v1 / v2]
        if debug:
            print(s)
        t += 1
        f = m(i, p)
    return o, s, t
    
#script = "5(!§{({!#§1##)}1##)"

#script = r"[World test][Hello \1\n][(?P<A>\w+)]~§"

#script = "100({100%##[% \U63;omplete!]#!#§1##0.25@)[Done!]§"

script = "0[Tokn`chmfoqhu`sdehkdrsnFnnfkd9]<1#>%(1#>%#%)}§!§9({10%##10.0[$bnlokdsd ]<1#>%(1#>%#%)}#!#§1##0,25@)0[Cnmd ]<1#>%(1#>%#%)}§"

#script = "0[Cnmd ]<1##>%(1##>%#%)}§"

o, s, t = exe(script)

#print(t)