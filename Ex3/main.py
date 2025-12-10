s1 = {"bob", "studies", "ensisa"}
s2 = {"ensisa", "located", "mulhouse"}
fail = []
ret = lambda x: [x]

def add_prefixe(x):
    x = f"http://sem.org#{x}"
    return x

def remove_prefixe(x):
    x = x.replace("http://sem.org#", "")
    # x = x.split("#")[1]
    return x

def f_ensemble(f, ensemble):
    return list(map(lambda x: f(x), ensemble))

def concat(t):
    r = []
    for e in t:
        r+= e
    return r

def filter(p, t):
    return concat(map(lambda e: ret(e) if p(e) else fail, t))

res = f_ensemble(add_prefixe, s1)
print(res)
res = f_ensemble(remove_prefixe, res)
print(res)

db = [['bob', 'studies', 'ensisa'], ['ensisa', 'located', 'mulhouse']]
print(filter(lambda x: x[0]=="bob", db))
print([x for x in db if x[0]=="bob"])