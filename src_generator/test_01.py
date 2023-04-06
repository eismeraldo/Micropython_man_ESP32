
# from glbfunct import gen_file_names

# f = gen_file_names("DOIT")
# print(f.finalref)
# print(f.roh)

# with open(f.roh, "r", encoding= "utf-8") as infile, open(f.finalref, "w", encoding= "utf-8") as outfinal, \
# open(f.modlist, "w", encoding= "utf-8") as outmod, open(f.foundurls, "w", encoding= "utf-8") as outfound,  \
# open(f.unknowmods, "w", encoding= "utf-8") as outunknow, open(f.manurls, "w", encoding= "utf-8") as outmanurls :
#     for line in infile:
#         outfinal.write(line)
#         outmod.write(line)
#         outfound.write(line)
#         outunknow.write(line)
#         outmanurls.write(line)

# ===================================================================================================

# from gen_urls import UrlDb

# db = UrlDb()
# db.add("modn1", 1, "https:www")
# db.add("modn1", 1, "https:www2")
# db.add("modn1", 1, "https:www3")
# db.add("modn1", 2, "https:wwwa")
# db.add("modn1", 2, "https:wwwb")
# db.add("modn2", 1, "https:wwwx")
# db.add("modn2", 1, "https:wwwy")

# print(f'URL DB: {db.db}')
# print(f'Groups: {db.get_types("modn2")}')
# print(f'URLs modn1, Group 1: {db.get_urls("modn1", 1)}')

# ===================================================================================================
