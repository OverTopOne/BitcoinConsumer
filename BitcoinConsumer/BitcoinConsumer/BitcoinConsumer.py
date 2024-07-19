import pandas as pd
import folium
from folium import Choropleth
from folium.features import GeoJson, GeoJsonTooltip


data = [
    ("United States", 3.2),
    ("Russia", 13.8),
    ("Canada", 24.1),
    ("Germany", 24.2),
    ("France", 28.7),
    ("United Kingdom", 42.2),
    ("Italy", 43.6),
    ("Australia", 55.6),
    ("Netherlands", 117.6),
    ("Czechia", 197.0)
]


countries = [item[0] for item in data]
percentages = [item[1] for item in data]

df = pd.DataFrame({
    'Country': countries,
    'Percentage': percentages
})


m = folium.Map(location=[20, 0], zoom_start=2, tiles='cartodb positron')


Choropleth(
    geo_data='https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json',
    data=df,
    columns=['Country', 'Percentage'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Energy Consumption Percentage'
).add_to(m)


GeoJson(
    'https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json',
    style_function=lambda x: {
        'fillOpacity': 0.0,  
        'color': 'black',
        'weight': 0.5
    },
    tooltip=GeoJsonTooltip(
        fields=['name'],
        aliases=['Country:'],
        localize=True,
        labels=True,
        sticky=True
    )
).add_to(m)


folium.TileLayer(
    tiles='https://{s}.tile.stamen.com/toner/{z}/{x}/{y}.png',
    attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.',
    name='Base Map'
).add_to(m)

folium.LayerControl().add_to(m)

m.save('energy_consumption_map.html')
