#==============================================================================================
# Die zu finalsierenden und die resultierenden Filenames sind:
#     - help_roh_DOIT.txt
#     - help_roh_S2-Mini.txt
#     - mp_referenz_final_DOIT.md
#     - mp_referenz_final_S2-Mini.md
#
# Als Input File wird das zuvor abgespeichert File 'hilfe_roh.txt' eingelesen und alle
# Zeilen zwischen "@@@DELETE START" und "@@@DELETE END" inklusive entfernt.
# Das Resultat befindet sich anschliessend im File 'hilfe_finish.txt'.
# Dieses File muss dann entsprechend umbenannt (csv oder md) werden.
#
# Programmaufruf in der DOS Shell:
#   - python finalizer.py           # default = d für doit
#   - python finalizer.py d         # DOIT
#   - python finalizer.py s2        # S2 Mini
#
#==============================================================================================

import sys
from datetime import datetime

import consts
from glbfunct import gen_board_names
from glbfunct import FileNames
from glbfunct import UrlDb



def skip_block(fin):
    while True:
        line = next(fin, None)
        if line.startswith(consts.MARK_BLOCK_TO_SKIP_END):
            break


def write_sorted_table(infile, outfile):
    mod_list = []
    line = infile.readline()
    while not line.startswith(consts.MARK_TABLE_END):
        mod = line.strip()
        mod_list.append(mod)
        line = infile.readline()
    mod_list.sort()

    # Anzahl der Spalten in der Tabelle
    num_columns = 6

    # Anzahl der Zeilen in der Tabelle berechnen
    num_rows = len(mod_list) // num_columns
    if len(mod_list) % num_columns != 0:
        num_rows += 1

    # Markdown-Tabelle erstellen
    table = "|"
    for i in range(num_columns):
        table += " | "
    table += "\n"
    table += "|"
    for i in range(num_columns):
        table += " --- |"
    table += "\n"

    # Markdown-Tabelle Zellen einfügen
    for i in range(num_rows):
        table += "|"
        for j in range(num_columns):
            index = i + j*num_rows
            if index < len(mod_list):
                pkg_elem = mod_list[index]
                colelem = " ["
                colelem += pkg_elem
                colelem += "](#"
                colelem += pkg_elem
                colelem += ")"
                table += f" {colelem} |"
            else:
                table += " |"
        table += "\n"
    # Tabelle ausgeben
    outfile.write(table)


def import_css(outfile):
    with open(filenames.scss, "r", encoding="utf-8") as infile:
        for line in infile:
            outfile.write(line)


def import_legend(outfile):
    outfile.write("\n## Legende: Links and Buttons\n")
    outfile.write("|     |     |\n")
    outfile.write("| --- | --- |\n")

    with open(filenames.legend, "r", encoding="utf-8") as infile:
        for ind, line in enumerate(infile, start=1):
            line = line.strip()
            if ind == 1:
                outfile.write("| [ein Link](#Overview) | " + line +" |\n")
                continue
            outfile.write(f'| <form ><button ><mark style="background: {consts.BACKGROUND_COLOR[str(ind)]};"><b>{consts.SHORT_NAMES[str(ind)]}</b></mark></button></form> | ' + line + "\n")


def overview(infile, outfile):
    outfile.write("--- \n")
    outfile.write(f"# Micropython Ref. `ESP32 {board_name}`\n")
    outfile.write("--- \n")

    import_css(outfile)

    now = datetime.now() # current date and time
    outfile.write(f'Generated: {now.strftime("%d.%m.%Y %H:%M:%S")}\n\n')

    import_legend(outfile)

    outfile.write('## Overview of all modules <span id="Overview"><span>\n')
    line = infile.readline().strip()
    while not line.startswith(consts.MARK_TABLE_START):
        line = infile.readline()
    write_sorted_table(infile, outfile)
    infile.readline() # Skip MARK_OVERVIEW_END


def gen_normal_button(typ, url):
    backcolor = consts.BACKGROUND_COLOR[typ]
    name = consts.SHORT_NAMES[typ]

    btn = f'<form action="{url}"  target="_blank">'
    btn += f'<button type="submit"><mark style="background: {backcolor};"><b>{name}</b></mark></button></form>'
    return btn


def gen_highlight_button(typ, url, value, serachstr):
    backcolor = consts.BACKGROUND_COLOR[typ]
    name = consts.SHORT_NAMES[typ]

    btn = f'<form action="{url}" method="get" target="_blank">'
    btn += f'<button type="submit"><mark style="background: {backcolor};"><b>{name}</b></mark></button>'
    btn += f'<input  type="hidden" name="{value}" value="{serachstr}" /> </form>'
    return btn


def write_buttons(outfile, modname) :
    outfile.write("\n")
    url_dict = {}
    for typ in urldb.get_types(modname):
        for url in urldb.get_urls(modname,typ):
            url_dict[url] = typ

    if len(url_dict) == 0:
        return

    for url in url_dict:
        outfile.write("|    ")
    outfile.write("|\n")

    for url in url_dict:
        outfile.write("| --- ")
    outfile.write("|\n")

    for url, typ in url_dict.items():
        quests = url.find("?")
        if quests == -1:
            outfile.write(f'| {gen_normal_button(typ, url)} ')
        else:
            names = url.split("?")
            url = names[0]
            keyval = names[1].strip()
            keyvals = keyval.split("=")
            outfile.write(f'| {gen_highlight_button(typ, url, keyvals[0], keyvals[1])} ')

    outfile.write("|\n\n")


def write_module(infile, outfile, line):
     # Module Kopf
    while not line.startswith(consts.MARK_MODULE_END):
        mod_name = line[len(consts.MARK_MODULE_START):].strip() # alles hinter dem Marker übernehmen
        outfile.write(f'# {mod_name} <span id="{mod_name}"></span>\n') # Titel

        write_buttons(outfile, mod_name)
        break

    #Module Körper
    line = next(infile, None).rstrip()
    while not line.startswith(consts.MARK_MODULE_END):
        if line.startswith(consts.MARK_BLOCK_TO_SKIP_START):
            skip_block(infile)
            line = infile.readline().rstrip()
            if not line:
                break
            continue
        if line.startswith(consts.MARK_SUBMDL_NOT_DEF):
            line = next(infile, None).rstrip()
            outfile.write(f'  * `{line}`\n')
        elif line.startswith(consts.MARK_SUBMDL_DEF):
            submod = line[len(consts.MARK_SUBMDL_DEF):].strip() # alles hinter dem Marker übernehmen
            line = next(infile, None).strip()
            outfile.write(f'  * [`{line}`](#{submod})\n')
        elif line.startswith(consts.MARK_NO_HELP):
            outfile.write("Hile in Micropython hat fehlgeschlagen\n\n")
        else:
            outfile.write(f'`{line}`\n')
        line = infile.readline().rstrip()
        if not line:
            break
    outfile.write('\n[--> Overview](#Overview)\n')



def write_submodule(infile, outfile, line):
    # Submodule Kopf
    while not line.startswith(consts.MARK_SUBMODULE_END):
        comp_mod_name = line[len(consts.MARK_SUBMODULE_START):].strip() # alles hinter dem Marker übernehmen
        names = comp_mod_name.split(".")
        outfile.write(f'## {names[0]} --> {names[1]} <span id="{comp_mod_name}"></span>\n')

        write_buttons(outfile, comp_mod_name)

        break

    # Submodule Körper
    line = next(infile, None).strip()
    while line.startswith(consts.MARK_LINE):
        aline = line[len(consts.MARK_LINE):].strip()
        outfile.write(f'  * `{aline}`\n')
        line = infile.readline().strip()
        if not line:
            break
    outfile.write(f'\n[--> {names[0]}](#{names[0]})\n')
    outfile.write('\n[--> Overview](#Overview)\n')


def main():

    with open(filenames.roh, "r", encoding="utf-8") as infile, open(filenames.finalref, "w", encoding="utf-8") as outfile:
        for line in infile:
            # if ">>> " not in line:
            if line.startswith(consts.MARK_BLOCK_TO_SKIP_START):
                skip_block(infile)
                continue
            if line.startswith(consts.MARK_OVERVIEW_START):
                overview(infile, outfile)
                continue
            if line.startswith(consts.MARK_MODULE_START) :
                write_module(infile, outfile, line)
                continue
            if line.startswith(consts.MARK_SUBMODULE_START) :
                write_submodule(infile, outfile, line)
                continue
            # outfile.write(line)

if __name__ == "__main__":
    board_name = gen_board_names(sys.argv)
    filenames = FileNames(board_name)
    urldb = UrlDb()
    urldb.load_urldb(filenames)

    main()


