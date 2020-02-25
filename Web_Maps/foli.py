import folium
import pandas as pd
import io

def color_producer(elevation):
    if elevation<1000:
        return('green')
    elif 1000<=elevation<3000:
        return ('orange')
    else:
        return ('red')
#Using pandas
df= pd.read_csv('Volcanoes_USA.txt')
lon=list(df['LON'])
lat=list(df['LAT'])
elev=list(df['ELEV'])

#Using Folium
#tilesMaobox =' https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}'
map= folium.Map(location=[40.58, -99.09],zoom_start=3, tilesMaobox='Dark')

fgv= folium.FeatureGroup(name='Volcanoes')
# Here we will use a for loop that will create a zip() function and iterate len,lat and elev one by one
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.Marker(location=[lt, ln],popup=str(el)+ ' m', icon=folium.Icon(color=color_producer(el))))
# map --> Featuregroup ---> child

map.save('folium.html')

fgp= folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=io.open('world.json','r', encoding='utf-8-sig').read(),
                             style_function=lambda x:{'fillOpacity': 0.1,'fillColor':'green' if x['properties']['pop_est']<10000000
                             else 'orange' if 10000000 <= x['properties']['pop_est'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('MAP2.html')