
import sys

import consts
from glbfunct import gen_board_names
from glbfunct import FileNames
from glbfunct import UrlDb


def main():
    urls =[
        # "https://docs.micropython.org/en/latest/library/_thread.html", # 2
        #    "https://docs.micropython.org/en/latest/library/?highlight=array", # 3
        #    "https://docs.micropython.org/en/latest/esp32/quickref.html?highlight=apa106", # 4
        #    "https://docs.python.org/3/library/exceptions.html", # 5
        #    "https://docs.python.org/3/library/exceptions.html?highlight=ArithmeticError", # 6
        #    "https://www.youtube.com/watch?v=CX5-dAmOxRc", # 7
        #    "https://docs.micropython.org/en/latest/library/builtins.html",
        #    "https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/nvs_flash.html",
        #    "https://docs.micropython.org/en/latest/library/esp32.html?highlight=Partition",
        #    "https://docs.micropython.org/en/v1.19/library/esp32.html?highlight=NVS",
        #    "https://docs.micropython.org/en/v1.19/library/esp32.html",
           "https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/nvs_flash.html"]
    for url in urls:
        urlinfo = consts.find_urlinfo_by_url(url)
        print(urlinfo.link_typ)


if __name__ == "__main__":
    board_name = gen_board_names(sys.argv)
    fnames = FileNames(board_name)
    urldb = UrlDb()
    urldb.load_urldb(fnames)
    main()

