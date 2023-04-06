#  
# Aufbauend auf dem testfinalize_03.py wird der Code in Funktionen strukturiert, die 
# Funktionalität bleibt jedoch die selbe
#  

def skip_block(fin):
    while True:
        line = next(fin, None)
        if line.startswith("####"):
            break

def replace_module(fin, fout, line):
    val = line[5:-1] # alles hinter aaaa in die val übernehmen
    print(val, line)
    line = next(fin, None)
    line = val + " " + line
    fout.write(line)

def main():
    with open("testfinalize_04_in.txt", "r") as input_file, open("testfinalize_04_out.txt", "w") as output_file:
        for line in input_file:
            # Wenn die Zeile die beginnende Markierung enthält, wird der Block übersprungen.
            if line.startswith("@@@@"):
                skip_block(input_file)
                continue
            if line.startswith("aaaa") :
                replace_module(input_file, output_file, line)
                continue
            output_file.write(line)


if __name__ == "__main__":
    main()
