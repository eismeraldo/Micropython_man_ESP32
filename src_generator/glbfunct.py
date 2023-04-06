
import os
import sys
from pathlib import Path
import consts


class FileNames :
    def __init__(self, board_name):
        root_folder = Path(__file__).parents[1]
        data_path = root_folder / "data/"

        ext_txt = ".txt"
        ext_md = ".md"
        prefix_roh = "help_roh"
        prefix_mod_list_raw = "modul_liste_raw"
        prefix_found_urls = "found_urls"
        prefix_unknown_mods = "unknown_modules"
        prefix_man_urls = "manual_fixed_urls"
        prefix_final = "mp_referenz_final"

        CSS_FILE_NAME = "styles.scss"
        LEGEND_FILE_NAME = "overview_legend.md"

        self.roh = self.constr_filename(data_path, 1, prefix_roh, board_name, ext_txt)
        self.modlist = self.constr_filename(data_path, 2, prefix_mod_list_raw, board_name, ext_txt)
        self.foundurls = self.constr_filename(data_path, 3, prefix_found_urls, board_name, ext_txt)
        self.unknowmods = self.constr_filename(data_path, 4, prefix_unknown_mods, board_name, ext_txt)
        self.manurls = self.constr_filename(data_path, 5, prefix_man_urls, board_name, ext_txt)
        self.finalref = self.constr_filename(data_path, "", prefix_final, board_name, ext_md)

        data_path = root_folder / "src_finalize/"
        self.scss = data_path / CSS_FILE_NAME
        self.legend = data_path / LEGEND_FILE_NAME


    def constr_filename(self, dpath, fnbr, fprefix, board, fext):
        nbr = ""
        if fnbr not in (0, ""):
            nbr = f'{fnbr:02d}' + "_"
        return dpath / (nbr + fprefix + "_" + board + fext)


class UrlDb :
    db = {} # Key= Modulename, Value= Dictionary --> Key= Type, Value= List of Urls

    def add(self, modname, tp, url):
        modnametype = self.db.get(modname)
        if modnametype is None :
            modnametype = {}
            self.db[modname] = modnametype
        urltype = modnametype.get(tp)
        if urltype is None:
            urltype = []
            modnametype[tp] = urltype
        urltype.append(url.strip())

    def get_types(self, modname):
        modnametype = self.db.get(modname)
        if modnametype is None :
            return []
        result = []
        for tp in modnametype:
            result.append(tp)
        return result

    def get_urls(self, modname, tp):
        modnametype = self.db.get(modname)
        if modnametype is None :
            return []
        result = []
        for url in modnametype[tp]:
            result.append(url)
        return result

    def print_all_urls(self):
        for mod, types in sorted(self.db.items()):
            for tp, urls in sorted(types.items()):
                for url in urls:
                    print(f"{mod}, {tp}, {url}")


    def load_urldb(self, fnames):
        # URLs aus der Datei Found URLs einlesen und in die UrlDb übernehmen
        with open(fnames.foundurls, "r", encoding="utf-8") as inurls:
            for line in inurls:
                line = line.strip()
                foundsep = line.find(", ")
                if foundsep < 0:
                    continue
                symbols = line.split(",")
                if len(symbols) < 2:
                    continue
                mod = symbols[0].strip()
                typ = symbols[1].strip()
                url = symbols[2].strip()
                self.add(mod, typ, url)

        # URLs aus der Datei Manual Defined URLs laden
        with open(fnames.manurls, "r", encoding="utf-8") as inurls:
            for line in inurls:
                line = line.strip()
                foundsep = line.find(", ")
                if foundsep < 0:
                    continue
                symbols = line.split(",")
                if len(symbols) < 2:
                    continue
                mod = symbols[0].strip()
                url = symbols[1].strip()
                isyoutube = url.find("https://www.youtube.com")
                if isyoutube == -1:
                    self.add(mod, str(consts.LINK_TYP_MP_EXTERN), url)
                else:
                    self.add(mod, str(consts.LINK_TYP_YOUTUBE), url)



def append_dada_dir():
    # Paralleles Verzeichnis hinzufügen. Der pylint versteht dies nicht, funktioniert aber trotzdem
    script_dir = os.path.dirname( __file__ )
    mymodule_dir = os.path.join( script_dir, '..', 'data' )
    sys.path.append( mymodule_dir )


def gen_board_names(args):
    model_name = ""
    if len(args) >= 2:
        model_name = args[1]
    else:
        model_name = "D"

    model_name = model_name.upper()

    if  model_name.startswith("D") :
        board_name = "DOIT"
    else:
        board_name = "S2-Mini"
    return board_name



