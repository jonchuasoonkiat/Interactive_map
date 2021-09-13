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

fg = folium.FeatureGroup(name = "My Map")
map = folium.Map(location=[1.3649142214739636, 103.8329729018762], zoom_start = 12, tiles = "Stamen Terrain")

for lt, ln, nm, tp in zip(lat, lon, name, type):
    fg.add_child(folium.Marker(location=[lt, ln], popup=nm, icon = folium.Icon(color = colour_producer())))


#map.add_child(folium.Marker(location = [], popup="GymName", icon=folium.Icon(color = 'green')))
map.add_child(fg)
map.save("ClimbingGymsSingapore.html")
