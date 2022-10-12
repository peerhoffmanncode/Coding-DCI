def snake_case(input_dict):
  output_dict = {}
  for key, value in input_dict.items():
    words = key.split(' ')
    snake_case_key = '_'.join(words)
    snake_case_key = snake_case_key.lower()

    output_dict[snake_case_key] = value

  return output_dict

address = {
  'Company name': 'Digital Career Institute',
  'Street': 'Vulkanstrasse',
  'House Number': 1,
  'City': 'Berlin'
}

movie = {
  'Movie name': 'James Bond 007: Skyfall',
  'Director': 'Sam Mendes',
  'Production Year': 2012,
  'Duration in minutes': 143,
  'Production countries': ['US', 'UK']
}

def main():
  print(snake_case(address))
  print(snake_case(movie))

if __name__ == '__main__':
  main()