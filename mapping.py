import folium
import pandas
from pandas.io.parquet import to_parquet

data = pandas.read_csv("ClimbingGymsSingapore.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
type = list(data["TYPE"])
             
#create function for changing colour of markers dynamically
def colour_producer():
    if tp == "Boulder":
        return 'green'
    elif tp == "Mixed":        
        return 'purple'
    elif tp == "HighWall":
        return 'blue'
    elif tp == "Restricted":
        return 'red'
    else:
        return 'gray'

#add feature group for climbing gyms in Singapore
fgC = folium.FeatureGroup(name = "Climbing Gyms")
map = folium.Map(location=[1.3649142214739636, 103.8329729018762], zoom_start = 12, tiles = "Stamen Terrain")

for lt, ln, nm, tp in zip(lat, lon, name, type):
    fgC.add_child(folium.Marker(location=[lt, ln], popup=nm, icon = folium.Icon(color = colour_producer())))

#add feature group for world population
fgP = folium.FeatureGroup(name = "World Population")

#adding layers for boundary polygons according to population
fgP.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005'] <10000000 else 'blue' if 10000000<= x['properties']['POP2005'] <20000000 else 'red'}))



#adding feature groups into the map.
#map.add_child(folium.Marker(location = [], popup="GymName", icon=folium.Icon(color = 'green')))
map.add_child(fgC)
map.add_child(fgP)

#put layer control after the feature group is added into the map
map.add_child(folium.LayerControl())

map.save("ClimbingGymsSingapore.html")
