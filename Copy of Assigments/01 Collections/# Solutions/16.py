data = {
  'key1': 1,
  'key2': 2,
  'key3': 3,
  'key4': 4,
  'key5': 5,
  'key6': 6,
}

def chunk(data, size):
  chunks = []
  chunk = {}
  for key, value in data.items():
      if len(chunk.keys()) < size:
          chunk.update({key: value})
      else:
          chunks.append(chunk)
          chunk = {key: value}
  chunks.append(chunk)
  return chunks

def main():
  print(chunk(data, 2))

if __name__ == '__main__':
  main()