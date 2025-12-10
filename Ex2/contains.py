def includeEnsemble(text, ensemble):
    if text in ensemble:
        return True
    return False

def union(s1, s2):
    # uni = []
    # seen = []
    # for text in (s1 | s2):
    #     if text in seen:
    #         continue
    #     seen.append(text)
    #     uni.append(text)
    # return uni
    return list(difference(list(s1), list(s2))) + list(s2)

def intersection(s1, s2):
    intersection = []
    for text in s1:
        if includeEnsemble(text, s2):
            intersection.append(text)
    return intersection

def difference(s1, s2):
    diff = []
    for text in s1:
        if not includeEnsemble(text, s2):
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