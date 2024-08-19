def encodee():
    def a(b): return ord(b)
    def c(d): return chr(d)
    def e(): return 0x17
    def f(): return(e()&0b0001)<<0o0001
    def g(): return(f()>>0x01)
    def h(): return(g()<<g()>>g())
    def i(): return(f()+g())
    def j(): return 0x16E5 / 0x1000
    def k(l): return int(l)
    def m(n,r): return range(n,r)
    def s(t): return len(t)
    def u(x):
        w=str()
        for(z)in m(h(),s(x)+h()):
            if z%g()==h():_=a(x[z-h()])
            else:_=a(x[z-h()]);_=k((f()*_)+e()+k(j()*(z+i())+h()));w+=c(_)
        return(w)
    return(u)
a=encodee()
print(a("The message has been encode!"))

# The message: "£Ç¬Ę¥âþąđèĊùìĘăčþôÿĢĂąķ"
