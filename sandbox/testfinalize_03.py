#  
# Korrigierte Version von 2, die war inkorrekt, hat Zeilen verloren!
# Die Ausgabe muss die Zeilen 1,2,3...29 lückenlos aufweisen
#  

with open("testfinalize_03_in.txt", "r") as input_file, open("testfinalize_03_out.txt", "w") as output_file:
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
            # next(input_file, None)
            continue
        
        if has_val_from_line_before == True:
            line = val + " " + line
            has_val_from_line_before = False

        output_file.write(line)
