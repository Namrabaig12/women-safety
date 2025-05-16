import folium

def generate_heatmap(data):
    m = folium.Map(location=[lat, lon], zoom_start=15)
    folium.plugins.HeatMap(data).add_to(m)
    m.save('templates/map.html')
