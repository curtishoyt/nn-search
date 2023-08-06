import json

def generate_search_results():
  """Generates the search results file."""

  with open("search_results.json", "w") as f:
    json.dump([
        {
          "id": 1,
          "title": "The Cat in the Hat",
          "url": "https://www.goodreads.com/book/show/14349.The_Cat_in_the_Hat",
          "score": 0.9
        },
        {
          "id": 2,
          "title": "Green Eggs and Ham",
          "url": "https://www.goodreads.com/book/show/198.Green_Eggs_and_Ham",
          "score": 0.8
        },
        {
          "id": 3,
          "title": "The Very Hungry Caterpillar",
          "url": "https://www.goodreads.com/book/show/2145.The_Very_Hungry_Caterpillar",
          "score": 0.7
        },
        {
          "id": 4,
          "title": "Where the Wild Things Are",
          "url": "https://www.goodreads.com/book/show/2485.Where_the_Wild_Things_Are",
          "score": 0.6
        },
        {
          "id": 5,
          "title": "Charlotte's Web",
          "url": "https://www.goodreads.com/book/show/150.Charlotte_s_Web",
          "score": 0.5
        },
    ], f)

if __name__ == "__main__":
  generate_search_results()