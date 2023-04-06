#==============================================================================================
#
# Als Input dient die vom Board generierte Datei "help_roh_DOIT.txt" oder "help_roh_S2-Mini.txt".
# Welche Roh Datei verwendet werden soll, wird über das Command Argument bestimmt
#
# Programmaufruf in der DOS Shell:
#   - python finalizer.py           # default = d für doit
#   - python finalizer.py d         # DOIT
#   - python finalizer.py s2        # S2 Mini
#
#==============================================================================================

import sys
import requests

from glbfunct import gen_board_names
from glbfunct import FileNames
from glbfunct import UrlDb

import consts


URL_MP_REFERENZ = "https://docs.micropython.org/en/latest/library/"
URL_MP_ESP32_HL = "https://docs.micropython.org/en/latest/esp32/quickref.html?highlight="
URL_MP_EXTERN_HL =  "https://docs.python.org/3/library/exceptions.html?highlight="




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
#   - Type = LINK_TYP_MP_HOME, LINK_TYP_MP_ESP32, LINK_TYP_MP_EXTERN
#   - URL

    modname = ""
    submodname = ""
    is_sub_modname = False
    compmodname = compmodname.strip()

    if compmodname.find(".") > 0:
        is_sub_modname = True
        names = compmodname.split(".")
        modname = names[0].strip()
        submodname = names[1].strip()
    else:
        modname = compmodname
        submodname = ""

    # URL des Modules und evt. Submodule
    urlck = URL_MP_REFERENZ + compmodname + ".html"
    if check_module_url(urlck):
        return True, consts.LINK_TYP_MP_HOME, urlck

    # URL von Submodule
    if is_sub_modname:
        urlck = URL_MP_REFERENZ + submodname + ".html"
        if check_module_url(urlck):
            return True, consts.LINK_TYP_MP_HOME, urlck

    #Versuche die Website ohne führendes "u" aufzurufen
    if not is_sub_modname and modname.startswith("u") :
        striped_modname = modname[1:]
        urlck = URL_MP_REFERENZ + striped_modname + ".html"
        if check_module_url(urlck):
            return True, consts.LINK_TYP_MP_HOME, urlck

    #Versuche die Website mit dem ersten Teile von bspw. "uasyncio/core", also "uasyncio" aufzurufen
    modnames = modname.split("/")
    if  len(modnames) > 1:
        urlck = URL_MP_REFERENZ + modnames[0] + ".html"
        if check_module_url(urlck):
            return True, consts.LINK_TYP_MP_HOME, urlck

    # Teste, ob das Submodule auf der Website vorkommt
    if modname == "builtins" and is_sub_modname :
        urlck = URL_MP_REFERENZ + "builtins.html?highlight=" + submodname
        if check_module_url_to_highlight(urlck, submodname):
            return True, consts.LINK_TYP_MP_HOME_HL, urlck

    # Teste, ob das Submodule auf der Website vorkommt
    if modname == "uio" and is_sub_modname :
        urlck = URL_MP_REFERENZ + "io.html?highlight=" + submodname
        if check_module_url_to_highlight(urlck, submodname):
            return True, consts.LINK_TYP_MP_HOME_HL, urlck

    # Teste, ob das Module oder Submodule auf der Website vorkommt und highlighten
    sname = ""
    if is_sub_modname:
        sname = submodname
    else:
        sname = modname
    urlck = URL_MP_ESP32_HL + sname
    if check_module_url_to_highlight(urlck, sname):
        return True, consts.LINK_TYP_MP_ESP32_HL, urlck

    # Teste, ob das Submodule auf der Website vorkommt und highlighten
    if modname == "builtins" and submodname.endswith("Error") :
        urlck = URL_MP_EXTERN_HL + submodname
        if check_module_url_to_highlight(urlck, submodname):
            return True, consts.LINK_TYP_MP_EXTERN_HL, urlck

    # URL nicht gefunden
    return False, None, None


def extract_module(outfile, line):
    mod_name = line[len(consts.MARK_MODULE_START):].strip() # hinter dem Marker ist der Module Name
    outfile.write(mod_name + "\n")
    moduledb.add(mod_name)


def extract_submodule(outfile, line):
    comp_mod_name = line[len(consts.MARK_SUBMODULE_START):].strip() # alles hinter dem Marker übernehmen
    outfile.write(comp_mod_name + "\n")
    moduledb.add(comp_mod_name)


def main():

# Module Liste Raw generieren
    with open(filenames.roh, "r", encoding="utf-8") as input_file, open(filenames.modlist, "w", encoding="utf-8") as outmod  :
        for line in input_file:
            if line.startswith(consts.MARK_MODULE_START) :
                extract_module( outmod, line)
                continue
            if line.startswith(consts.MARK_SUBMODULE_START) :
                extract_submodule(outmod, line)
                continue

    # Aufgrund der Module Liste wird für jedes Modul eine gültige URL ermittelt
    # Module ohne gültige URL werden in die Unknown Modul Datei geschrieben
    with open(filenames.unknowmods, "w", encoding="utf-8") as outunknown:
        for mod in sorted(moduledb):
            found, typ, url = find_url(mod)
            if found:
                urldb.add(mod, typ, url)
            else:
                outunknown.write(mod + "\n")

    # Jedes Modul mit entsprechender URL wird in die Datei Found URLs geschrieben
    with open(filenames.foundurls, "w", encoding="utf-8") as outfound:
        for mod, types in urldb.db.items():
            for typ in types:
                urls = urldb.get_urls(mod, typ)
                for url in urls:
                    outfound.write(f"{mod}, {typ}, {url}\n")



if __name__ == "__main__":
    board_name = gen_board_names(sys.argv)
    filenames = FileNames(board_name)
    urldb = UrlDb()
    urldb.load_urldb(filenames)
    moduledb = set() # Set

    main()



