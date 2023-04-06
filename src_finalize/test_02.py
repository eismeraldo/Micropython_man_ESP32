
import sys

from glbfunct import gen_board_names
from glbfunct import FileNames
from glbfunct import UrlDb


def test_global_variable():
    urldb.print_all_urls()


def main():
    test_global_variable()


if __name__ == "__main__":
    board_name = gen_board_names(sys.argv)
    fnames = FileNames(board_name)
    urldb = UrlDb()
    urldb.load_urldb(fnames)
    main()

