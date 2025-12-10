#GARRONE-GABRIEL
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