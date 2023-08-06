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

if __name__ == "__main__":
  generate_word_index()