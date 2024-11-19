import geopandas as gpd

shapefile = gpd.read_file(r"D:\Data\LUCAS\Lucas-2015\LUCAS2015_topsoildata_20200323\LUCAS_Topsoil_2015_20200323-shapefile\LUCAS_Topsoil_2015_20200323.shp")
shapefile.to_csv("data/output/lucas/shp.csv", index=False)
