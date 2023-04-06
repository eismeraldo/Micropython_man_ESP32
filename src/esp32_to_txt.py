# -----------------------------------------------------------------------------------------------------------
# Aufgrund der help('modules') werden die Packages / Modules extrahiert, von jedem einzelen wiederum die help()
# Funktion aufgerufen und von jedem Package, sofern vorhanden, deren Modules mit help() extrahiert und gedruckt.
#  
# Die Ausgabe wird mit dem Python Skript filer.py bereinigt.
#  
# Anleitung
#     1) Thonny an den gewünschten ESP32 anschliessen
#     2) Dieses Skript in Thonny ausführen
#     3) Output von Thonny in die Text Datei hilfe_roh.txt kopieren und in das Verzeichnis src_filter speichern
#     4) Python Skript 'filer.py' im Verzeichnis src_filter ausführen 
#             python .\filter.py
#     5) das produzierte File hilfe_finish.md kann nun mit dem Browser geöffnet werden
#  
#  Erstell: am März 2023
#  Autor:   adrian.schnyder.ch@gmail.com
#  
# -----------------------------------------------------------------------------------------------------------

import uos, machine, uio as io, usys as sys


MARK_BLOCK_TO_SKIP_START = "@@@DELETE Start"
MARK_BLOCK_TO_SKIP_END = "@@@DELETE End"
MARK_OVERVIEW_START = "Ä1 Overview Start"
MARK_OVERVIEW_END = "Ä1 Overview End"
MARK_TABLE_START = "ä tbl Start"
MARK_TABLE_END = "ä tbl End"
MARK_MODULE_START = "Ä1 Module Start"
MARK_MODULE_END = "Ä1 Module End"
MARK_SUBMODULE_START = "Ä2 Submodule Start"
MARK_SUBMODULE_END = "Ä2 Submodule End"
MARK_LINE = "Ä3 line"
MARK_SUBMDL_DEF = "ä Submodule def "
MARK_SUBMDL_NOT_DEF = "ä Submodule notdef"
MARK_NO_HELP = "Ö1 no Help"


def printhelp():

    print(MARK_BLOCK_TO_SKIP_START)
    # Erstelle einen Puffer, um die Standardausgabe zu umleiten
    output_buffer = io.StringIO()
    uos.dupterm(output_buffer)
    # Hilfe ausgeben
    help('modules')
    # Die Standardausgabe wieder auf die Konsole umleiten
    uos.dupterm(None)
    print(MARK_BLOCK_TO_SKIP_END)

    # Die Hilfe in eine Variable speichern
    help_str = output_buffer.getvalue()
    pkg_list_raw = help_str.split()
    # Erstellt die Liste aller Pakages auf oberster Ebene
    pkg_list = []
    for pkg in pkg_list_raw:
        pkg = pkg.strip()
        if pkg is not "Plus":
            if pkg != "__main__" and pkg != "None" and pkg !=  "uasyncio/__init__" :
                pkg_list.append(pkg)
        else:
            break # Nach Plus kommt nichts verwörtbares
            
    pkg_list.sort()

    print(MARK_OVERVIEW_START)

    # Pakages drucken
    print(MARK_TABLE_START)
    for pkg in pkg_list :
        print(pkg)
    print(MARK_TABLE_END)

    print(MARK_OVERVIEW_END)

    return pkg_list


def print_package(pkg_name):

    # Module als Titel und ID schreiben
    print(MARK_MODULE_START, pkg_name)

    # Liste aller pkgs auf nächsten Ebene
    pkg_list = []

    if pkg_name != "webrepl" and pkg_name != "webrepl_setup" and pkg_name != "usys" :

        print(MARK_BLOCK_TO_SKIP_START)
        output_buffer = io.StringIO()
        uos.dupterm(output_buffer)
        try:
            pkg = __import__(pkg_name, globals(), locals(), [], 0)
            print(help(pkg))
        except:
            uos.dupterm(None)
            print("Fehler beim Laden von", pkg_name)
            return []

        uos.dupterm(None)
        help_str = output_buffer.getvalue()
        print(MARK_BLOCK_TO_SKIP_END)

        # Help String in Variable speichern
        mod_zeilen_raw = help_str.split("\n")

        # Zeile mit einem dieser Tokens wird in der nächsten Funktion weiter aufgedröselt
        tokens = [" -- <pkg ", " -- <class"]
        for zeile in mod_zeilen_raw:
            token_found = False
            modelname = ""
            zeile = zeile.strip()
            if zeile != "" and zeile != "None" :
                ind = zeile.find(tokens[0])
                if ind >= 0 :
                    token_found = True
                    modelname_raw = zeile[0:ind]
                    modelname = modelname_raw.strip()
                    pkg_list.append(modelname)
                else:
                    ind = zeile.find(tokens[1])
                    if ind >= 0 :
                        token_found = True
                        modelname_raw = zeile[0:ind]
                        modelname = modelname_raw.strip()
                        pkg_list.append(modelname)

                # Zeile und evt. Link erstellen
                if token_found is True :
                    print(MARK_SUBMDL_DEF, pkg_name, ".", modelname, sep='')
                    print(zeile)
                else :
                    print(MARK_SUBMDL_NOT_DEF)
                    print(zeile)
    else :
        print(MARK_NO_HELP)

    print(MARK_MODULE_END)

    # print("\n[--> Overview](#Overview)")
    return pkg_list


def print_module(pkg_name, mod_name):

    print(MARK_BLOCK_TO_SKIP_START)
    output_buffer = io.StringIO()
    uos.dupterm(output_buffer)

    try:
        pakg = __import__(pkg_name, globals(), locals(), [])
        mod = getattr(pakg, mod_name)
        print(help(mod))
    except:
        uos.dupterm(None)
        print("Fehler beim Laden von", pkg_name, "mod: ", mod_name)

    uos.dupterm(None)
    help_str = output_buffer.getvalue()
    print(MARK_BLOCK_TO_SKIP_END)
    
    # Hile in Variabel speichern
    mod_zeilen_raw = help_str.split("\n")

    # Erstellt die Liste aller Modules auf der nächsten Ebene
    pkg_list = []
    for zeile in mod_zeilen_raw:
            modelname = zeile.strip()
            if modelname != "" and modelname != "None" :
                pkg_list.append(modelname)
    pkg_list.sort()

    # Pakage, Model ausgeben
    print(MARK_SUBMODULE_START, pkg_name, ".", mod_name, sep='')
 
    #Liste der Models ausgeben
    for model in pkg_list:
        print(MARK_LINE, model)
        
    print(MARK_SUBMODULE_END)

    # print("\n[--> ", pkg_name, "](#", pkg_name, ")\n", sep='')
    # print("[--> Overview](#Overview)")


def main():
    pkg_list = printhelp()
    for pkg in pkg_list:
        mod_list = print_package(pkg)
        if len(mod_list) > 0:
            for mod in mod_list:
                print_module(pkg, mod)

if __name__ == "__main__":
    main()
