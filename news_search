from flask import Flask, request, jsonify
import requests
import json

code = 'syd2'
app = Flask(__name__)

key = 'ashroom'

url = 'https://newsapi.org/v2/top-headlines?country=au&apiKey=2f722a1876b34f38bfd0fe5558ee006a&q={query}'

def store_url(key):
  return f'https://store.ncss.cloud/{code}/{key}'

def store_get(key):
  url = store_url(key)
  r = request.get(key)
  r= request.get(url)
  if r.status_code == 404:
    return {}
  else:
    return r.get_json()

#https://RundownGroundedServers--five-nine.repl.co/syd2/news
@app.route("/syd2/news", methods=['POST'])
def news():
  #GET the query / what they want to here about
  args = request.get_json()
  query = args['params']['Trigger']

  #Trigger the API with the REQUEST
  response = requests.get(url.format(query=query)).json()
  #GET the TITLE and AUTHOR from the response
  title = response['articles'][0]['title']
  author = response['articles'][0]['author']
  earl = response['articles'][0]['url']

  #ASSEMBLE the REPLY
  reply =  f'From author {author}, {title}, {earl}' #REWORD

  #GIVE the REPLY back to USER
  return jsonify({
    'author': 'News Bot',
    'text': reply,
    'room': 'test1234123',
  })

app.run(host='0.0.0.0')

#ROOM SETTINGS FOR BOT
#NEWS BOT
#What's happening with (?P<Trigger>.*)
#https://RundownGroundedServers--five-nine.repl.co/syd2/news
