from flask import Flask, request, jsonify
import requests
import json
import random
app = Flask(__name__)
#KEY FOR GRACENOTE API: vwnyqh3p9tbkjdxps3enrsdy
#URL FOR GRACENOTE API: http://data.tmsapi.com/v1.1
#https://chat.ncss.cloud/
#http://developer.tmsapi.com/docs
url = 'https://tastedive.com/api/similar?q={movie}' 
code = 'syd2'

def store_url(key):
  return f'https://store.ncss.cloud{key}'

def store_get(key):
  url2 = store_url(key)
  r = requests.get(url2)
  if r.status_code == 404:
    return {}
  else:
    return r.json()

def store_set(key, value):
  url2 = store_url(key)
  r = requests.post(url2, json=value)

def store_delete(key):
  store_set(key, {'seen': []})#dont delete just reset FIX

#https://RundownGroundedServers--five-nine.repl.co/syd2/recommendation
@app.route("/syd2/recommendation", methods=['POST'])
def movie():
  #Get Movie
  args = request.get_json()
  moviename = args['params']['Movie']
  type_delete = args['params']['Type']
  #Get response from Simular Movie API
  response = requests.get(url.format(movie=moviename)).json()

  #List of Movies seen
  listofsimular = []

  #Get all 20 movies in List
  for i in range(20):
    listofsimular.append(response['Similar']['Results'][i]['Name'])

  #Get list of movies seen from API
  seen = store_get('/test/will')['seen']

  #CHECK if user has seen that movie before, if not, give that movie to them, and say     they've seen it.
  for name in listofsimular:
    if name not in seen:
      simular = name
      seen.append(simular)
      break

    #IF they have seen all the movies, Give them the top recommended one
    if listofsimular[19] == name:
      simular = listofsimular[0]

  #Add the movie they originally liked to seen
  if moviename not in seen:
    seen.append(moviename)

  #RESET list in storage API with all the new movies seen
  store_set('/test/will', {'seen':seen})

  #THING TO HELP ME CLEAR KEY
  if type_delete == 'delete':
    store_delete('/test/will')
    return jsonify({
    'author': 'Recommendation Bot',
    'text': 'Delete Successful',
    'room': 'test123412',
  })

  #SET REPLY for user
  reply = 'How about you try ' + simular

  #RETURN REPLY
  return jsonify({
    'author': 'Recommendation Bot',
    'text': reply,
    'room': 'test123412',
  })

app.run(host='0.0.0.0')

#BOT SETTINGS
#TESTBOT
#Recommend me a (?P<Type>.*) like (?P<Movie>.*)
#https://recommendations.wdavo.repl.co/syd2/recommendation
