db = [['bob', 'studies', 'ensisa'], ['ensisa', 'located', 'mulhouse']]

db += [[x[0], "rdf:type", "Person"] for x in db if x[1] == "studies"]
db += [[x[0], "rdf:type", "Ecole"] for x in db if x[1] == "located"]

print(db)