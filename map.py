import folium

map = folium.Map(location=[52.52, 13.40], zoom_start=6, tiles="Stamen Terrain") #berlin

# create a feature group of marker
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[52.1, 13.20], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
