#GARRONE-GABRIEL
#I
def load():
    txt = open("data.csv").read()
    return txt

def save(txt):
    newfile = "dataSave.csv"
    with open(newfile, 'w') as f:
        for line in txt:
            f.write(line)

def csv_join(csv):
    joined_txt = "\n".join(map(lambda x: ",".join(x), csv))
    return joined_txt

def csv_split(txt):
    return map(lambda x: x.split(","), txt.split("\n"))

txt = load()
csv = csv_split(txt)
save(txt)
csv_joined = csv_join(csv)

print(txt)
print(csv_joined)


#II
import os

def includeEnsemble(text, ensemble):
    if text in ensemble:
        return True
    return False

def union(ens1, ens2):
    # uni = []
    # seen = []
    # for text in (s1 | s2):
    #     if text in seen:
    #         continue
    #     seen.append(text)
    #     uni.append(text)
    # return uni
    return list(difference(list(ens1), list(ens2))) + list(ens2)

def intersection(ens1, ens2):
    intersection = []
    for text in ens1:
        if includeEnsemble(text, ens2):
            intersection.append(text)
    return intersection

def difference(ens1, ens2):
    diff = []
    for text in ens1:
        if not includeEnsemble(text, ens2):
            diff.append(text)
    return diff

def compare():
    # intersection = []
    # diff = []
    # for text in s1:
    #     if includeEnsemble(text, s2):
    #         intersection.append(text)
    #     else:
    #         diff.append(text)
    # uni = list(set(s1).union(s2))
    inter = intersection(s1, s2)
    diff = difference(s1, s2)
    uni = union(s1, s2)
    print(inter)
    print(diff)
    print(uni)

ensemble = {"salut", "ça", "va"}
s1 = {"bob", "studies", "ensisa"}
s2 = {"ensisa", "located", "mulhouse"}

print(includeEnsemble("salut", ensemble))
compare()

s3 = {"bob", "etudie", "à", "l", "ensisa"}
s4 = {"à", "le", "la", "les", "l", "at", "the", "is"}
print(difference(s3, s4))

with open(os.path.join(os.path.dirname(__file__),"data.txt"), "r") as f:
    txt = f.read()
    txt = txt.split(".")
    resulting_sentences = []
    for sentence in txt:
        if sentence:
            sentence = sentence.split(' ')
            print(sentence)
            sentence = difference(sentence, s4)
            resulting_sentences.append(sentence)
    print(resulting_sentences)



#III
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

#7.
print( [x[0] for x in db if x[1] == "studies"])


#IV
db = [['bob', 'studies', 'ensisa'], ['ensisa', 'located', 'mulhouse']]

db += [[x[1], "rdf:domain", "Person"] for x in db if x[0] == "bob"]
db += [[x[1], "rdf:range", "School"] for x in db if x[2] == "ensisa"]
db += [[x[1], "rdf:domain", "ensisa"] for x in db if x[0] == "ensisa"]
db += [[x[1], "rdf:range", "School"] for x in db if x[2] == "mulhouse"]
db += [[x[0], "rdf:type", "Person"] for x in db if x[1] == "studies"]
db += [[x[0], "rdf:type", "School"] for x in db if x[1] == "located"]
db += [[x[1], "rdf:type", "owl:ObjectProperty"] for x in db if x[2] == "ensisa" and x[0] == "bob"]
db += [[x[0], "rdf:type", "owl:NamedIndividual"] for x in db if x[2] == "Person"]
db += [[x[2], "rdf:type", "owl:Class"] for x in db if x[0] == "studies" and x[1] == "rdf:domain"]

print(db)