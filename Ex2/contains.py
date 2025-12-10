def includeEnsemble(text, ensemble):
    if text in ensemble:
        return True
    return False

def union(s1, s2):
    uni = []
    seen = []
    for text in (s1 | s2):
        if text in seen:
            continue
        seen.append(text)
        uni.append(text)
    return uni


def compare():
    intersection = []
    diff = []
    for text in s1:
        if includeEnsemble(text, s2):
            intersection.append(text)
        else:
            diff.append(text)
    # uni = list(set(s1).union(s2))
    uni = union(s1, s2)
    print(intersection)
    print(diff)
    print(uni)

ensemble = {"salut", "ça", "va"}
s1 = {"bob", "studies", "ensisa"}
s2 = {"ensisa", "located", "mulhouse"}

print(includeEnsemble("salut", ensemble))
compare()