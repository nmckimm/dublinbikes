from flask import render_template, jsonify, json
from app import app
import os
import json
import sys
import re
from astropy.wcs.docstrings import lat




        
    
        
     #first is integer second is dict
    # if all else fails use re
    
@app.route('/', methods=['GET'])
def index():
    with app.open_resource('Dublin.json', 'r') as f:
        mydata = json.load(f)
        location = []
        name = []
        number = []
        address = []
        lat = []
        long = []
        j=0
        for i in mydata:
            number.append(mydata[j]['number'])
            name.append(mydata[j]['name'])
            address.append(mydata[j]['address'])
            lat.append(mydata[j]['latitude'])
            long.append(mydata[j]['longitude'])

            j+=1
        address = json.dumps(address).replace("\'", "\\'")
        name = json.dumps(name).replace("\'", "\\'")   
        number = json.dumps(number)
        lat = json.dumps(lat)
        long = json.dumps(long)    
    jsonObject()
    returnDict = {}
    returnDict['user'] = 'User123'
    returnDict['title'] = 'Dublin Bikes'
    return render_template("index.html", **returnDict, number=number, address=address, lat=lat, long=long)
@app.route('/jsonObject', methods=['GET'])
def jsonObject():
    with app.open_resource('Dublin.json', 'r') as f:
        mydata = json.load(f)
        
        location = []
        name = []
        number = []
        address = []
        lat = []
        long = []
        j=0
        for i in mydata:
            number.append(mydata[j]['number'])
            name.append(mydata[j]['name'])
            address.append(mydata[j]['address'])
            lat.append(mydata[j]['latitude'])
            long.append(mydata[j]['longitude'])
            j+=1
        address = json.dumps(address).replace("\'", "\\'")
        name = json.dumps(name).replace("\'", "\\'")
        number = json.dumps(number)
        print(type(lat))
        
        lat = json.dumps(lat)
        long = json.dumps(long)
        print(long[1])
        print(type(number))
    return number, address, lat, long
'''
def regex():
    re1='.*?'    # Non-greedy match on filler
    re2='((?:[a-z][a-z]+))'    # Word 1
    re3='.*?'    # Non-greedy match on filler
    re4='(\\d+)'    # Integer Number 1
    re5='.*?'    # Non-greedy match on filler
    re6='((?:[a-z][a-z]+))'    # Word 2
    re7='.*?'    # Non-greedy match on filler
    re8='(".*?")'    # Double Quote String 1
    re9='.*?'    # Non-greedy match on filler
    re10='((?:[a-z][a-z]+))'    # Word 3
    re11='.*?'    # Non-greedy match on filler
    re12='(".*?")'    # Double Quote String 2
    re13='.*?'    # Non-greedy match on filler
    re14='((?:[a-z][a-z]+))'    # Word 4
    re15='.*?'    # Non-greedy match on filler
    re16='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'    # Float 1
    re17='.*?'    # Non-greedy match on filler
    re18='((?:[a-z][a-z]+))'    # Word 5
    re19='.*?'    # Non-greedy match on filler
    re20='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'    # Float 2
    
    with app.open_resource('Dublin.json', 'r') as f:
        mydata = json.load(f)
    rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14+re15+re16+re17+re18+re19+re20,re.IGNORECASE|re.DOTALL)
    m = re.findall(rg, mydata)
    if m:
        word1=m.group(1)
        int1=m.group(2)
        word2=m.group(3)
        string1=m.group(4).replace("\"", "")
        word3=m.group(5)
        string2=m.group(6).replace("\"", "")
        word4=m.group(7)
        float1=m.group(8)
        word5=m.group(9)
        float2=m.group(10)
        print(word1, ' ', int1)'''
