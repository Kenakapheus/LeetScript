import re, time, sys


#script = "12.34>tes=t<123#§10{>\n<%#>\n<#§(1##{>\n<#§)>\nt+2<{§}"


def exe(i, s = [], d = True):
    o = ""
    #replace = []
    p = 0
    l = []
    m = re.compile(r"(?P<A>(\d+)\.?\d*|\[[^]^[]*\])|(?P<B>##?)|(?P<C>§)|(?P<D>{)|(?P<E>})|(?P<F>\()|(?P<G>\))|(?P<H>%)|(?P<I>!)|(?P<J>~)|(?P<K>@)").search
    f = m(i)
    while f is not None:
        c = f.lastgroup
        v = f.group()
        p = f.end()
        if c == 'A':
            try:
                s += [float(v)]
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
            v1 = s.pop()
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
                if s[-1]:
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
        
        #time.sleep(1)
        #print(s, l, v)
        f = m(i, p)
    return o, s
    
#script = "5(!§{({!#§1##)}1##)"

#script = r"[World test][Hello \1\n][(?P<A>\w+)]~§"

script = "100({100%##[% complete!]#!#§1##0.25@)"

exe(script)


#\.|\(|\)|##