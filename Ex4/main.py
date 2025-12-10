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