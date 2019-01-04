import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_maker(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"    

map = folium.Map(location=[38.58, -99.09],zoom_start=6, tiles="Mapbox Bright")
fg_volc = folium.FeatureGroup(name="Volcanoes")


for lt, ln, el in zip(lat, lon, elev):
    # fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(str(el)+" m",parse_html=True), icon=folium.Icon(color=color_maker(el))))
    fg_volc.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m", fill_color=color_maker(el), color = 'grey', fill=True,fill_opacity=0.7))

fg_pop = folium.FeatureGroup(name="Population")


fg_pop.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg_pop)
map.add_child(fg_volc)
map.add_child(folium.LayerControl())
 
map.save("Map1.html")


 
