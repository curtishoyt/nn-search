import json
import requests
import tensorflow as tf
import numpy as np
from flask import Flask, request

word_index = {}
max_len = 100

import json

def generate_word_index():
  """Generates the word index file."""

  # Create an empty dictionary to store the word index.
  word_index = {}

  # Iterate over the search results.
  with open("search_results.json") as f:
    search_results = json.load(f)

    for result in search_results:
      # Iterate over the words in the title.
      for word in result['title'].split():
        # Add the word to the word index if it is not already there.
        if word not in word_index:
          word_index[word] = len(word_index)

  # Save the word index to the file.
  with open("word_index.json", "w") as f:
    json.dump(word_index, f)

def get_results(query):
  """Gets the results from the database."""

  # Get the search results from the database.
  with open("search_results.json") as f:
    search_results = json.load(f)

  return search_results

def generate_embeddings(text):
  """Generates embeddings for the given text."""

  embeddings = {}

  for word in text.split():
    if word in word_index:
      embeddings[word] = tf.keras.models.Embedding(
          len(word_index), 128, input_length=max_len
      ).predict(np.array([word_index[word]]))[0]
    else:
      embeddings[word] = np.zeros(128)

  return embeddings

app = Flask(__name__)

@app.route('/', methods=['GET'])
def api_get():
  """Handles GET requests."""

  # Get the request object from Flask.
  requestFFFF = request

  if requestFFFF.method != 'GET':
    return {'error': 'Method not supported'}, 405

  query = requestFFFF.args.get('query')

  if query is None:
    return {'error': 'No query provided'}, 400

  results = get_results(query)

  if len(results) == 0:
    return {'error': 'No results found'}, 404

  return {'results': results}, 200

def main():
  generate_word_index()
  app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
  main()