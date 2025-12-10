#GARRONE-GABRIEL
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
