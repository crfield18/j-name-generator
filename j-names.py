import json
namesdb = open('../names-database/NameDatabases/NamesDatabases/first names/all.txt', 'r')
jnamesdb = {'j-names' : []}
jnames = []
lines = 0

# Open list of first names from names-database
for line in namesdb:
    lines += 1
    # Add all J names to list
    if line.startswith('J'):
        jnames.append(line.strip('\n'))
    else:
        pass
# Add J names list to jnames database    
jnamesdb['j-names'] += jnames

# Dump J names to j-names.json
with open("j-names.json", 'w') as db:
    json.dump(jnamesdb, db)
