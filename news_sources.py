from flask import Flask, request, jsonify
import requests
import json

code = 'syd2'
app = Flask(__name__)

url = 'https://newsapi.org/v2/top-headlines?sources={query}&apiKey=2f722a1876b34f38bfd0fe5558ee006a&q'


#https://RundownGroundedServers--five-nine.repl.co/syd2/news
@app.route("/syd-2/news_source", methods=['POST'])
def news():
  #GET the query / what they want to here about
  args = request.get_json()
  query = args['params']['source']

  #Trigger the API with the REQUEST
  response = requests.get(url.format(query=query)).json()
  #GET the TITLE and AUTHOR from the response
  print(response)
  title = response['articles'][0]['title']
  author = response['articles'][0]['author']
  description = response['articles'][0]['description']
  image_url = response['articles'][0]['urlToImage']
  article_url = response['articles'][0]['url']
  time = response['articles'][0]['publishedAt']
  date = time[:10]
  date = date.replace('-','/')

  #ASSEMBLE the REPLY
  reply =  f'<p style="font-weight:bold;font-family:times new roman;font-size: 20px"><a href = "{article_url}">{title}</a></p> <p>{news} </p><p style="color:red;font-family:times new roman">Written by {author} </p> <p> Posted on {date}</p><p><img src="{image_url}" alt="" align="middle" style="width:800px"></p><p style = "font-family:times new roman">{description}</p>' 


  #GIVE the REPLY back to USER
  return jsonify({
    'author': 'Alfred',
    'text': reply,
  })

app.run(host='0.0.0.0')

#ROOM SETTINGS FOR BOT
#NEWS BOT
#What's happening with (?P<Trigger>.*)
#https://RundownGroundedServers--five-nine.repl.co/syd2/news
