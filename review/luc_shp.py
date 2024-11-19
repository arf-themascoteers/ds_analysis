import geopandas as gpd

shapefile = gpd.read_file(r"../data/original/lucas/LUCAS_Topsoil_2015_20200323-shapefile/LUCAS_Topsoil_2015_20200323.shp")
shapefile.to_csv("../data/original/lucas/lucas_shp.csv", index=False)
