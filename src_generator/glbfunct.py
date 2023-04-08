
import os
import sys
from pathlib import Path
import consts


class FileNames :
    def __init__(self, board_name):
        root_folder = Path(__file__).parents[1]
        data_path = root_folder / "data/"
        gen_path = root_folder / "src_generator/"

        self.roh = self.constr_filename(data_path, 1, consts.FILE_PREFIX_ROH, board_name, consts.FILE_EXT_TXT)
        self.modlist = self.constr_filename(data_path, 2, consts.FILE_PREFIX_MOD_LIST_RAW, board_name, consts.FILE_EXT_TXT)
        self.foundurls = self.constr_filename(data_path, 3, consts.FILE_PREFIX_FOUND_URLS, board_name, consts.FILE_EXT_TXT)
        self.unknowmods = self.constr_filename(data_path, 4, consts.FILE_PREFIX_UNKNOWN_MODS, board_name, consts.FILE_EXT_TXT)
        self.manurls = self.constr_filename(data_path, 5, consts.FILE_PREFIX_MAN_FIXED_URLS, board_name, consts.FILE_EXT_TXT)
        self.finalref = self.constr_filename(data_path, "", consts.FILE_PREFIX_FINAL, board_name, consts.FILE_EXT_MD)

        self.scss = gen_path / consts.CSS_FILE_NAME
        self.legend = gen_path / consts.LEGEND_FILE_NAME


    def constr_filename(self, dpath, fnbr, fprefix, board, fext):
        nbr = ""
        if fnbr not in (0, ""):
            nbr = f'{fnbr:02d}' + "_"
        return dpath / (nbr + fprefix + "_" + board + fext)


    def print_root_folder(self):
        print(self.print_root_folder)


class UrlDb :
    db = {} # Key= Modulename, Value= List of Urls

    def add(self, modname, url):
        modnameturl = self.db.get(modname)
        if modnameturl is None :
            modnameturl = []
            self.db[modname] = modnameturl
        modnameturl.append(url.strip())

    def get_urls(self, modname):
        modnameturl = self.db.get(modname)
        if modnameturl is None :
            return []
        return modnameturl

    def print_all_urls(self):
        for mod, urls in sorted(self.db.items()):
            for url in sorted(urls):
                print(f"{mod}, {url}")


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
                url = symbols[1].strip()
                self.add(mod, url)

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
                self.add(mod, url)



def append_dada_dir():
    # Paralleles Verzeichnis hinzufügen.
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



