from pandas import read_excel
import numpy as np
import folium
from branca.element import Figure


df = read_excel('data/식당 좌표.xlsx')




df=df.filter(['식당명','위도','경도','링크'])





print(df)


map_osm = folium.Map(location=[37.5570377, 126.9841211], zoom_start=12.2 ,max_zoom=17,min_zoom=12)




list_latitude=[]
list_longitude=[]
list_link=[]

for i, v in enumerate(df['위도']):
    
    list_latitude.append(v)
for i, v in enumerate(df['경도']):
    
    list_longitude.append(v)
for i, v in enumerate(df['링크']):
    
    list_link.append(v)
    
#print(list_latitude)
#print(list_longitude)
print('2.지도에 마커 추가')
list_resName=[]
for i in df.index:
    list_resName.append(df['식당명'][i])
print(list_resName)

url='<iframe width="290" height="290" src="res_info/res_info1.html">'

for i in df.index:
    marker = folium.Marker([list_latitude[i], list_longitude[i]],tooltip=list_resName[i],popup=list_link[i] ,icon=folium.Icon(color='red', icon='star'))
    marker.add_to(map_osm)
	








map_osm.save('../식당.html')