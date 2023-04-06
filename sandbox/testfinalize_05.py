#  
# Argument beim Start des Programmes mitgeben. Aufgrund dessen wird das entsprechende Input und Output
# File benutzt.
# 
# Argumente:
#     d oder D (default): doit, die Filenamen sind: 
#         testfinalize_05_in_doit.txt und testfinalize_05_out_doit.txt
#     s2 und alles andere: 
#         testfinalize_05_in_s2.txt und testfinalize_05_out_s2.txt
# 

import sys

def skip_block(fin):
    while True:
        line = next(fin, None)
        if line.startswith("####"):
            break

def replace_module(fin, fout, line):
    val = line[5:-1] # alles hinter aaaa in die val übernehmen
    line = next(fin, None)
    line = val + " " + line
    fout.write(line)

def main():
    in_file_name = ""
    out_file_name = ""
    filename_ext = ".txt"
    in_file_name_1 = "testfinalize_05_in_"
    out_file_name_1 = "testfinalize_05_out_"
    filename_suffix_doit = "doit"
    filename_suffix_s2 = "s2"

    modell = "D"
    if len(sys.argv) >= 2:
        modell = sys.argv[1]
        modell = modell.upper()

    print(modell)
    if  modell.startswith("D") :
        in_file_name = in_file_name_1 + filename_suffix_doit + filename_ext
        out_file_name = out_file_name_1 + filename_suffix_doit + filename_ext
    else :
        in_file_name = in_file_name_1 + filename_suffix_s2 + filename_ext
        out_file_name = out_file_name_1 + filename_suffix_s2 + filename_ext

    
    with open(in_file_name, "r", encoding="utf-8") as input_file, open(out_file_name, "w", encoding="utf-8") as output_file:
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
