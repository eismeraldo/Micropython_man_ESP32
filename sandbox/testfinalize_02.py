# Dieses Skript öffnet eine Eingabedatei namens "input.txt" und eine Ausgabedatei namens "output.txt". 
# Es geht davon aus, dass die Eingabedatei Zeilen enthält, die durch beginnende und endende Markierungen 
# markiert sind, die jeweils mit "@@@@" und "####" beginnen.
#
# Das Skript liest jede Zeile der Eingabedatei und überprüft, ob sie eine der Markierungen enthält. 
# Wenn die Zeile die beginnende Markierung enthält, wird der Block übersprungen. 
# Wenn die Zeile die endende Markierung enthält, wird der Block beendet. 
# Wenn der Block übersprungen wird, wird die nächste Zeile gelesen, ohne dass sie in die Ausgabedatei 
# geschrieben wird.
#  
# Wenn der Block nicht übersprungen wird, wird die Zeile getestet, ob sie mit der
# Markierung "aaaa" startet. 
# Ist dies der Fall, wird alles was sich hinter der Markierung befindet in eine Variable gespeichert und
# die nächste Zeile gelesen. Dieser neuen Zeile wird dann der Wert aus der Variablen vorangestellt und das
# Resultat in die Ausgabedatei geschrieben.
#  
# Ansonsten werden die Zeilen 1:1 in die Ausgabedatei übernommen


with open("testfinalize_02_in.txt", "r") as input_file, open("testfinalize_02_out.txt", "w") as output_file:
    skip_block = False
    has_val_from_line_before = False
    val = ""
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
        if line.startswith("aaaa") :
            has_val_from_line_before = True
            val = line[5:-1] # alles hinter aaaa in die val übernehmen
            next(input_file, None)
            continue
        
        if has_val_from_line_before == True:
            line = val + " " + line
            has_val_from_line_before = False

        output_file.write(line)
