from waitress import serve 
from flask import Flask, render_template
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mplmg
 
 
app = Flask(__name__)
 
@app.route('/')
 
def index():
  url = ('https://newsapi.org/v2/top-headlines?'
     'country=us&'
     'apiKey=cb02ca0d9ec34365a50b751270559a41')
 
  response = requests.get(url)
 
  news = response.json()
  article_1 = news['articles'][0]
  output = ""
  output+= f"{article_1['title']}"
  output+= f"Written By: {article_1['author']}"
  output+= f"Posted on: {article_1['source']['name']}"
  output+= f"---\n{article_1['url']}---\n"
  output+= f"Description: {article_1['description']}"
  return output
 
if __name__ == '__main__':
  serve(app, host='0.0.0.0', port=8080)