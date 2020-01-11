
from flask import Flask, request, jsonify
import requests
import json

code = 'syd2'
app = Flask(__name__)

url = 'https://newsapi.org/v2/top-headlines?sources={query}&apiKey=2f722a1876b34f38bfd0fe5558ee006a&q'

'''
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

'''

#https://RundownGroundedServers--five-nine.repl.co/syd2/news
@app.route("/syd2/news_source", methods=['POST'])
def news():
  #GET the query / what they want to here about
  args = request.get_json()
  query = args['params']['source']

  #Trigger the API with the REQUEST
  response = requests.get(url.format(query=query)).json()
  #GET the TITLE and AUTHOR from the response

  title = response['articles'][0]['title']
  author = response['articles'][0]['author']
  description = response['articles'][0]['description']
  image_url = response['articles'][0]['urlToImage']
  article_url = response['articles'][0]['url']
  time = response['articles'][0]['publishedAt']

  #ASSEMBLE the REPLY
  reply =  f'<p style="font-weight:bold;font-family:times new roman;font-size: 20px"><a href = "{article_url}">{title}</a></p> <p>{news} </p><p style="color:red;font-family:times new roman">Written by {author} </p> <p>{time}</p><p><img src="{image_url}" alt="" align="middle" style="width:800px"></p><p style = "font-family:times new roman">{description}</p>' 


  #GIVE the REPLY back to USER
  return jsonify({
    'author': 'News Bot',
    'text': reply,
  })

app.run(host='0.0.0.0')

#ROOM SETTINGS FOR BOT
#NEWS BOT
#What's happening with (?P<Trigger>.*)
#https://RundownGroundedServers--five-nine.repl.co/syd2/news
