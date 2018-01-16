from flask import Flask, jsonify, render_template, request
from recommendation import mark_by_time
from recommendation import recommend_location
from recommendation import mark_by_time2
from recommendation import mark_by_time3
from recommendation import recommend_location2
from recommendation import recommend_location3
from weather import return_weather
import sys

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/echo/', methods=['GET'])
def echo():
    #Get the keyword from request
    keyword = {"value":request.args.get('echovalue')}
    if keyword['value']=='0:00-2:00':
        time=0
    elif keyword['value']=='2:00-4:00':
        time=2
    elif keyword['value']=='4:00-6:00':
        time=4
    elif keyword['value']=='6:00-8:00':
        time=6
    elif keyword['value']=='8:00-10:00':
        time=8
    elif keyword['value']=='10:00-12:00':
        time=10
    elif keyword['value']=='12:00-14:00':
        time=12
    elif keyword['value']=='14:00-16:00':
        time=14
    elif keyword['value']=='16:00-18:00':
        time=16
    elif keyword['value']=='18:00-20:00':
        time=18
    elif keyword['value']=='20:00-22:00':
        time=20
    elif keyword['value']=='22:00-24:00':
        time=22
    model={"value":request.args.get('model')}
    if model['value']=='green':

    #Connect to Elastic Search
    #es=es_conn()
    #Use parse_location to get the corresponding location of the keyword
    #resp = parse_location(es,keyword["value"])
        h=mark_by_time(time)
        s=h[0]
        length=h[1]+1
        return jsonify(length=200,data=s)
    if model['value']=='yellow':
        h=mark_by_time2(time)
        s=h[0]
        length=h[1]+1
        return jsonify(length=200,data=s)
    if model['value']=='uber':
        h=mark_by_time3(time)
        s=h[0]
        length=h[1]+1
        return jsonify(length=200,data=s)

@application.route('/getDetails/', methods=['GET'])
def getDetails():
    #Get the tweet id form the request
    location1 = {"value1":request.args.get('location1')}
    location2 = {"value1":request.args.get('location2')}
    keyword = {"value":request.args.get('value')}
    lat=location1['value1']
    lon=location2['value1']
    if keyword['value']=='0:00-2:00':
        time=0
    elif keyword['value']=='2:00-4:00':
        time=2
    elif keyword['value']=='4:00-6:00':
        time=4
    elif keyword['value']=='6:00-8:00':
        time=6
    elif keyword['value']=='8:00-10:00':
        time=8
    elif keyword['value']=='10:00-12:00':
        time=10
    elif keyword['value']=='12:00-14:00':
        time=12
    elif keyword['value']=='14:00-16:00':
        time=14
    elif keyword['value']=='16:00-18:00':
        time=16
    elif keyword['value']=='18:00-20:00':
        time=18
    elif keyword['value']=='20:00-22:00':
        time=20
    elif keyword['value']=='22:00-24:00':
        time=22
    lat=float(lat)
    lon=float(lon)
    model={"value":request.args.get('model')}
    if model['value']=='green':
        h=recommend_location(time,lat,lon)
        s=h[0]
        length=h[1]
        weather=return_weather(s)
    #Connect to Elastic Search
    #es=es_conn()
    #Return the tweet information using parse_id
    #return parse_id(es,twid["value"])
        return jsonify(length=1,data=s,weather=weather)
    if model['value']=='yellow':
        h=recommend_location2(time,lat,lon)
        s=h[0]
        length=h[1]
        weather=return_weather(s)
    #Connect to Elastic Search
    #es=es_conn()
    #Return the tweet information using parse_id
    #return parse_id(es,twid["value"])
        return jsonify(length=1,data=s)
    if model['value']=='uber':
        h=recommend_location3(time,lat,lon)
        s=h[0]
        length=h[1]
        weather=return_weather(s)
    #Connect to Elastic Search
    #es=es_conn()
    #Return the tweet information using parse_id
    #return parse_id(es,twid["value"])
        return jsonify(length=1,data=s,weather=weather)


if __name__ == '__main__':
    application.run(port=8080, debug=True)