# sortierte Liste mit 50 Einträgen erstellen
my_list = [i for i in range(50)]
my_list.sort()

# Anzahl der Spalten in der Tabelle
num_columns = 6

# Anzahl der Zeilen in der Tabelle berechnen
num_rows = len(my_list) // num_columns
if len(my_list) % num_columns != 0:
    num_rows += 1

# Markdown-Tabelle erstellen
table = "|"
for i in range(num_columns):
    table += " Spalte {} |".format(i+1)
table += "\n"
table += "|"
for i in range(num_columns):
    table += " --- |"
table += "\n"

for i in range(num_rows):
    table += "|"
    for j in range(num_columns):
        index = i + j*num_rows
        if index < len(my_list):
            table += " {} |".format(my_list[index])
        else:
            table += " |"
    table += "\n"

# Tabelle ausgeben
print(table)
