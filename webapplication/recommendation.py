import pandas as pd
def mark_by_time(time):
    t=""
    if time==0:
        t="00-01"
    elif time==2:
        t="02-03"
    elif time==4:
        t="04-05"
    elif time==6:
        t="06-07"
    elif time==8:
        t="08-09"
    elif time==10:
        t="10-11"
    elif time==12:
        t="12-13"
    elif time==14:
        t="14-15"
    elif time==16:
        t="16-17"
    elif time==18:
        t="18-19"
    elif time==20:
        t="20-21"
    elif time==22:
        t="22-23"
    add="/your root/webapplication/bd/"+t+".csv"
    gdata = pd.read_csv(add)
    geolong=pd.DataFrame(gdata['Pickup_longitude'])
    geolat=pd.DataFrame(gdata['Pickup_latitude'])
    geo = pd.DataFrame(gdata, columns = ['Pickup_longitude','Pickup_latitude'])
    s=[]
    i=0
    for index, row in gdata.iterrows():
        temp={}
        temp['long']=row['Pickup_longitude']
        temp['lat']=row['Pickup_latitude']
        s.append(temp)
        i=i+1
    data=[s,i]
    return data
    #d=mark_by_time(0)
	#print(d)
from math import sin, cos, sqrt, atan2, radians

def recommend_location(time,lat,lon):
    t=""
    if time==0:
        t="00-01"
    elif time==2:
        t="02-03"
    elif time==4:
        t="04-05"
    elif time==6:
        t="06-07"
    elif time==8:
        t="08-09"
    elif time==10:
        t="10-11"
    elif time==12:
        t="12-13"
    elif time==14:
        t="14-15"
    elif time==16:
        t="16-17"
    elif time==18:
        t="18-19"
    elif time==20:
        t="20-21"
    elif time==22:
        t="22-23"
    add="/your root/webapplication/bd/"+t+".csv"
    gdata = pd.read_csv(add)
    geolong=pd.DataFrame(gdata['Pickup_longitude'])
    geolat=pd.DataFrame(gdata['Pickup_latitude'])
    geo = pd.DataFrame(gdata, columns = ['Pickup_longitude','Pickup_latitude'])
    d=[]
    i=0
    for index, row in gdata.iterrows():
        temp={}
        temp['long']=row['Pickup_longitude']
        temp['lat']=row['Pickup_latitude']
        d.append(temp)
        i=i+1
        
    m=100000
    R=6373.0
    lat1=radians(lat)
    lon1=radians(lon)
    for i in range (200):
        lat2_rec=d[i]['lat']
        lon2_rec=d[i]['long']       
        lat2=radians(d[i]['lat'])
        lon2=radians(d[i]['long'])   
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        #print(distance)
        if distance!=0 and distance<m:
            lat_result=lat2_rec
            lon_result=lon2_rec
            m=distance
            
    result={}
    result['lat']=lat_result
    result['long']=lon_result
    data=[result,1]
    #print("Result:", m, "km")
    #print("Recommended Spot:",result)
    #recommend_location(40.57543182,-73.98291779)
    return data

def mark_by_time3(time):
    t=""
    if time==0:
        t="00-01"
    elif time==2:
        t="02-03"
    elif time==4:
        t="04-05"
    elif time==6:
        t="06-07"
    elif time==8:
        t="08-09"
    elif time==10:
        t="10-11"
    elif time==12:
        t="12-13"
    elif time==14:
        t="14-15"
    elif time==16:
        t="16-17"
    elif time==18:
        t="18-19"
    elif time==20:
        t="20-21"
    elif time==22:
        t="22-23"
    add="/your root/webapplication/bduber/"+t+"_u"+".csv"
    gdata = pd.read_csv(add)
    geolong=pd.DataFrame(gdata['Lon'])
    geolat=pd.DataFrame(gdata['Lat'])
    geo = pd.DataFrame(gdata, columns = ['Lon','Lat'])
    s=[]
    i=0
    for index, row in gdata.iterrows():
        temp={}
        temp['long']=row['Lon']
        temp['lat']=row['Lat']
        s.append(temp)
        i=i+1
    data=[s,i]
    return data
    #d=mark_by_time(0)
    #print(d)
from math import sin, cos, sqrt, atan2, radians

def recommend_location3(time,lat,lon):
    t=""
    if time==0:
        t="00-01"
    elif time==2:
        t="02-03"
    elif time==4:
        t="04-05"
    elif time==6:
        t="06-07"
    elif time==8:
        t="08-09"
    elif time==10:
        t="10-11"
    elif time==12:
        t="12-13"
    elif time==14:
        t="14-15"
    elif time==16:
        t="16-17"
    elif time==18:
        t="18-19"
    elif time==20:
        t="20-21"
    elif time==22:
        t="22-23"
    add="/your root/webapplication/bduber/"+t+"_u"+".csv"
    gdata = pd.read_csv(add)
    geolong=pd.DataFrame(gdata['Lon'])
    geolat=pd.DataFrame(gdata['Lat'])
    geo = pd.DataFrame(gdata, columns = ['Lon','Lat'])
    d=[]
    i=0
    for index, row in gdata.iterrows():
        temp={}
        temp['long']=row['Lon']
        temp['lat']=row['Lat']
        d.append(temp)
        i=i+1
        
    m=100000
    R=6373.0
    lat1=radians(lat)
    lon1=radians(lon)
    for i in range (200):
        lat2_rec=d[i]['lat']
        lon2_rec=d[i]['long']       
        lat2=radians(d[i]['lat'])
        lon2=radians(d[i]['long'])   
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        #print(distance)
        if distance!=0 and distance<m:
            lat_result=lat2_rec
            lon_result=lon2_rec
            m=distance
            
    result={}
    result['lat']=lat_result
    result['long']=lon_result
    data=[result,1]
    #print("Result:", m, "km")
    #print("Recommended Spot:",result)
    #recommend_location(40.57543182,-73.98291779)
    return data 

def mark_by_time2(time):
    t=""
    if time==0:
        t="00-01"
    elif time==2:
        t="02-03"
    elif time==4:
        t="04-05"
    elif time==6:
        t="06-07"
    elif time==8:
        t="08-09"
    elif time==10:
        t="10-11"
    elif time==12:
        t="12-13"
    elif time==14:
        t="14-15"
    elif time==16:
        t="16-17"
    elif time==18:
        t="18-19"
    elif time==20:
        t="20-21"
    elif time==22:
        t="22-23"
    add="/your root/webapplication/"+t+"_y"+".csv"
    gdata = pd.read_csv(add)
    geolong=pd.DataFrame(gdata['pickup_longitude'])
    geolat=pd.DataFrame(gdata['pickup_latitude'])
    geo = pd.DataFrame(gdata, columns = ['pickup_longitude','pickup_latitude'])
    s=[]
    i=0
    for index, row in gdata.iterrows():
        temp={}
        temp['long']=row['pickup_longitude']
        temp['lat']=row['pickup_latitude']
        s.append(temp)
        i=i+1
    data=[s,i]
    return data
    #d=mark_by_time(0)
    #print(d)
from math import sin, cos, sqrt, atan2, radians

def recommend_location2(time,lat,lon):
    t=""
    if time==0:
        t="00-01"
    elif time==2:
        t="02-03"
    elif time==4:
        t="04-05"
    elif time==6:
        t="06-07"
    elif time==8:
        t="08-09"
    elif time==10:
        t="10-11"
    elif time==12:
        t="12-13"
    elif time==14:
        t="14-15"
    elif time==16:
        t="16-17"
    elif time==18:
        t="18-19"
    elif time==20:
        t="20-21"
    elif time==22:
        t="22-23"
    add="/your root/webapplication/bdyellow/"+t+"_y"+".csv"
    gdata = pd.read_csv(add)
    geolong=pd.DataFrame(gdata['pickup_longitude'])
    geolat=pd.DataFrame(gdata['pickup_latitude'])
    geo = pd.DataFrame(gdata, columns = ['pickup_longitude','pickup_latitude'])
    d=[]
    i=0
    for index, row in gdata.iterrows():
        temp={}
        temp['long']=row['pickup_longitude']
        temp['lat']=row['pickup_latitude']
        d.append(temp)
        i=i+1
        
    m=100000
    R=6373.0
    lat1=radians(lat)
    lon1=radians(lon)
    for i in range (200):
        lat2_rec=d[i]['lat']
        lon2_rec=d[i]['long']       
        lat2=radians(d[i]['lat'])
        lon2=radians(d[i]['long'])   
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        #print(distance)
        if distance!=0 and distance<m:
            lat_result=lat2_rec
            lon_result=lon2_rec
            m=distance
            
    result={}
    result['lat']=lat_result
    result['long']=lon_result
    data=[result,1]
    #print("Result:", m, "km")
    #print("Recommended Spot:",result)
    #recommend_location(40.57543182,-73.98291779)
    return data  