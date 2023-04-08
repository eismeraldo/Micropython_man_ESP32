
from collections import namedtuple


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


URLS_OF_UNKNOWN_MODS_FILE_NAME = "urls_of_unknown_modules.txt"

CSS_FILE_NAME = "styles.scss"
LEGEND_FILE_NAME = "overview_legend.md"

FILE_EXT_TXT = ".txt"
FILE_EXT_MD = ".md"
FILE_PREFIX_ROH = "help_roh"
FILE_PREFIX_MOD_LIST_RAW = "modul_liste_raw"
FILE_PREFIX_FOUND_URLS = "found_urls"
FILE_PREFIX_UNKNOWN_MODS = "unknown_modules"
FILE_PREFIX_MAN_FIXED_URLS = "manual_fixed_urls"
FILE_PREFIX_FINAL = "mp_referenz_final"

URL_MP_REFERENZ =  "https://docs.micropython.org/en/latest/library/"
URL_MP_ESP32 =  "https://docs.micropython.org/en/latest/esp32/quickref.html"
URL_MP_EXTERN = "https://docs.python.org/3/library/exceptions.html"
URL_YOUTUBE = "https://www.youtube.com/watch"

URL_PRE_REF = "https://docs.micropython.org/en/"
URL_POST_REF = "/library/esp32.html"
URL_PRE_ESP32 = "https://docs.micropython.org/en/"
URL_POST_ESP32 = "/esp32/quickref.html"

URL_MP_ESP32_HL =  URL_MP_ESP32 + "?highlight="
URL_MP_EXTERN_HL = URL_MP_EXTERN + "?highlight="

url_pre_post = namedtuple("url_pre_post", ["is_regular", "link_typ", "pre", "post"])
url_pre_posts = []
url_pre_posts.append(url_pre_post(True, "2", URL_PRE_REF, URL_POST_REF))
url_pre_posts.append(url_pre_post(False, "3", URL_PRE_REF, URL_POST_REF))
url_pre_posts.append(url_pre_post(False, "4", URL_PRE_ESP32, URL_POST_ESP32))

url_info = namedtuple("url_info",["is_regular", "link_typ", "bg_color", "short_name", "url"])
url_infos = []
url_infos.append(url_info(True, "2", "SkyBlue", "MP Home", URL_MP_REFERENZ))
url_infos.append(url_info(False, "3", "Yellow", "MP Home highlight", URL_MP_REFERENZ))
url_infos.append(url_info(False, "4", "Yellow", "MP ESP32 highlight", URL_MP_ESP32))
url_infos.append(url_info(True, "5", "SkyBlue", "Extern", URL_MP_EXTERN))
url_infos.append(url_info(False, "6", "Yellow", "Extern highlight", URL_MP_EXTERN))
url_infos.append(url_info(False, "7", "Red", "YouTube", URL_YOUTUBE))


def find_urlinfo_by_link_typ(typ):
    styp = str(typ)
    for info in url_infos:
        if styp == info.link_typ:
            return info
    return None # Darf nicht vor kommen


def find_urlinfo_by_url(url):
    is_regular = not url.find("?") > 1
    if not is_regular:
        url = url.split("?")[0].strip()

    # Zuerst prüfen, ob die URL in eine bekannte Famile gehört
    for urlprepost in url_pre_posts:
        if url.startswith(urlprepost.pre) and url.endswith(urlprepost.post) and is_regular == urlprepost.is_regular:
            return find_urlinfo_by_link_typ(urlprepost.link_typ)

    # Nun die komplette URL prüfen
    for urlinfo in url_infos:
        if url.startswith(urlinfo.url) and is_regular == urlinfo.is_regular:
            return urlinfo
    if is_regular is True:
        return find_urlinfo_by_link_typ(5)
    return find_urlinfo_by_link_typ(6)
