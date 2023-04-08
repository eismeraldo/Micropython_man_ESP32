#==============================================================================================
#
# Als Input dient die vom Board generierte Datei "01_help_roh_xx.txt".
# Welche Roh Datei verwendet werden soll, wird über das Command Argument bestimmt
#
# Programmaufruf in der DOS Shell:
#   - python gen_mod_urls.py           # default = d für DOIT
#   - python gen_mod_urls.py d         # DOIT
#   - python gen_mod_urls.py s2        # S2 Mini
#
#==============================================================================================

import sys
import requests

from glbfunct import gen_board_names
from glbfunct import FileNames
from glbfunct import UrlDb

import consts


def check_module_url_to_highlight(urlck, notion):
    try:
        response = requests.get(urlck, notion, timeout=5)
        if response.status_code == 200:
            treffer = [response.text.count(w) for w in [notion]]
            if treffer[0] > 0 :
                return True
        return False
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
    return False


def check_module_url(urlck):
    try:
        response = requests.get(urlck, timeout = 3)
        if response.status_code == 200:
            return True
        return False
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
    return False



def find_url(compmodname):
    print(compmodname)
# Return:
#   - found = True / False
#   - URL

    names_to_look_for = []
    compmodname = compmodname.strip()
    modname = ""
    submodname = ""

    if compmodname.find(".") > 0:
        names = compmodname.split(".")
        modname = names[0].strip()
        submodname = names[1].strip()
    else:
        modname = compmodname
        names_to_look_for.append(modname)

    #Versuche die Website ohne führendes "u" aufzurufen
    if modname.startswith("u") :
        names_to_look_for.append(modname[1:])

    #Versuche die Website mit dem ersten Teile von bspw. "uasyncio/core", also "uasyncio" aufzurufen
    modnames = modname.split("/")
    if  len(modnames) > 1:
        names_to_look_for.append(modnames[0])

    # Test auf die URL URL_MP_REFERENZ --------------------------------------------------
    # Testen, ob irgen einer der Name am Ende einer URL auf eine 200er Response kommt
    for name in names_to_look_for:
        urlck = (consts.URL_MP_REFERENZ + name + '.html').strip()
        if check_module_url(urlck):
            return True, urlck

    # Teste, ob das Submodule auf der Website vorkommt
    if modname == "builtins" and len(submodname) > 1:
        urlck = consts.URL_MP_REFERENZ + "builtins.html?highlight=" + submodname
        if check_module_url_to_highlight(urlck, submodname):
            return True, urlck

    # Teste, ob das Submodule auf der Website vorkommt
    if modname == "uio" and len(submodname) > 1:
        urlck = consts.URL_MP_REFERENZ + "io.html?highlight=" + submodname
        if check_module_url_to_highlight(urlck, submodname):
            return True, urlck

    sname = ""
    if len(submodname) > 1:
        sname = submodname
    else:
        sname = modname

    # Teste, ob das Module oder Submodule auf einer der folgenden Websiten vorkommt
    urlck = consts.URL_MP_ESP32_HL + sname
    if check_module_url_to_highlight(urlck, sname):
        return True, urlck

    # Teste, ob das Submodule auf der Website vorkommt und highlighten
    if modname == "builtins" and submodname.endswith("Error") :
        urlck = consts.URL_MP_EXTERN_HL + submodname
        if check_module_url_to_highlight(urlck, submodname):
            return True, urlck

    # URL nicht gefunden
    return False, None


def extract_modname_to_db( line):
    mod_name = line[len(consts.MARK_MODULE_START):].strip() # hinter dem Marker ist der Module Name
    moduledb.add(mod_name)


def extract_submodname_to_db(line):
    comp_mod_name = line[len(consts.MARK_SUBMODULE_START):].strip() # alles hinter dem Marker übernehmen
    moduledb.add(comp_mod_name)


def main(): #----------------------------------------------------------------------

    # Module Liste Raw generieren
    with open(filenames.roh, "r", encoding="utf-8") as input_file:
        for line in input_file:
            if line.startswith(consts.MARK_MODULE_START) :
                extract_modname_to_db(line)
                continue
            if line.startswith(consts.MARK_SUBMODULE_START) :
                extract_submodname_to_db(line)
                continue

    # Module Liste Raw schreiben
    with open(filenames.modlist, "w", encoding="utf-8") as outmod:
        for mod in sorted(moduledb):
            outmod.write(mod + "\n")

    # Aufgrund der Module Liste wird für jedes Modul eine gültige URL ermittelt
    # Module ohne gültige URL werden in die Unknown Modul Datei geschrieben
    with open(filenames.unknowmods, "w", encoding="utf-8") as outunknown:
        for mod in sorted(moduledb):
            found, url = find_url(mod)
            if found:
                urldb.add(mod, url)
            else:
                outunknown.write(mod + ", \n")

    # Jedes Modul mit entsprechender URL wird in die Datei Found URLs geschrieben
    with open(filenames.foundurls, "w", encoding="utf-8") as outfound:
        for mod, urls in sorted(urldb.db.items()):
            for url in urls:
                outfound.write(f"{mod}, {url}\n")



if __name__ == "__main__":
    board_name = gen_board_names(sys.argv)
    filenames = FileNames(board_name)
    urldb = UrlDb()
    moduledb = set() # Set

    main()
