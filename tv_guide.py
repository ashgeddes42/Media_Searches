import random
from flask import Flask, jsonify
import requests

app = Flask('app')



print(response.text)
times = ['16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', ]

# link the program with a random time in the list
@app.route('/program_times', methods=['POST'])
def list_movies_and_shows():
  time_1 = random.choice(times) #random time taken from list times
  message = {
    'author': 'time_provider',
    'text': f'This will be on at {time_1} today',
  }
  return jsonify(message)


#use api and randomly respond with 3 programs "playing" at that time
@app.route('/programs_at_given_time', methods=['POST'])
def list_movies_and_shows():
  url = "http://www.omdbapi.com/?apikey=f3bb8028&"
  print(response)
  program_1 = random.choice() #random time taken from API
  program_2 = random.choice()
  program_3 = random.choice()
   message = {
    'author': 'program_provider',
    'text': f'The following programs will be on at that time: {program_1}, {program_2}, {program_3}',
  }
  return jsonify(message)



app.run(host='0.0.0.0')


''' '00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00', '04:30', '05:00', '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '23:00', '23:30' '''
'''
