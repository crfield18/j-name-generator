import json
namesdb = open('../names-database/NameDatabases/NamesDatabases/first names/all.txt', 'r')
jnamesdb = {'j-names' : []}
jnames = []
lines = 0
for line in namesdb:
    lines += 1
    if line.startswith('J'):
        jnames.append(line.strip('\n'))
    else:
        pass
jnamesdb['j-names'] += jnames



with open("j-names.json", 'w') as db:
    json.dump(jnamesdb, db)


db1 = json.load(open('j-names.json', 'r'))["j-names"]
print(db1[7])