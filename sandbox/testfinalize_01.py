# Dieses Skript öffnet eine Eingabedatei namens "input.txt" und eine Ausgabedatei namens "output.txt". 
# Es geht davon aus, dass die Eingabedatei Zeilen enthält, die durch beginnende und endende Markierungen 
# markiert sind, die jeweils mit "@@@@" und "####" beginnen.
#
# Das Skript liest jede Zeile der Eingabedatei und überprüft, ob sie eine der Markierungen enthält. 
# Wenn die Zeile die beginnende Markierung enthält, wird der Block übersprungen. 
# Wenn die Zeile die endende Markierung enthält, wird der Block beendet. 
# Wenn der Block übersprungen wird, wird die nächste Zeile gelesen, ohne dass sie in die Ausgabedatei 
# geschrieben wird. Wenn der Block nicht übersprungen wird, wird die Zeile verarbeitet und in die 
# Ausgabedatei geschrieben.

# In diesem Beispiel wird die Zeile verändert, wenn sie das 
# Wort "foo" enthält, indem das Wort durch "bar" ersetzt wird. 
# Sie können dies entsprechend Ihren Anforderungen anpassen.


with open("testfinalize_01_in.txt", "r") as input_file, open("testfinalize_01_out.txt", "w") as output_file:
    skip_block = False
    for line in input_file:
        # Wenn die Zeile die beginnende Markierung enthält, wird der Block übersprungen.
        if line.startswith("@@@@"):
            skip_block = True
            continue
        # Wenn die Zeile die endende Markierung enthält, wird der Block beendet.
        if line.startswith("####"):
            skip_block = False
            continue
        # Wenn der Block übersprungen wird, wird die nächste Zeile gelesen.
        if skip_block:
            continue
        # Sonst wird die Zeile verarbeitet und in die Ausgabedatei geschrieben.
        if "foo" in line:
            line = line.replace("foo", "bar")
        output_file.write(line)
