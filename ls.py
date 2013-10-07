import re, time, sys
def e(i):
    c=[r"(\d+),?\d*|\[[^]^[]*\]","##?","§","{","}",r"\(",r"\)","%","!","~","@",r"\<",r"\>",r"\.\.?"]
    m = re.compile("|".join("(?P<%s>%s)"%(chr(65+p),c[p])for p in range(0,len(c)))).search
    p,l,f,s = 0,[],m(i),[]
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
            sys.stdout.write(str(s.pop()))
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
        f = m(i, p)