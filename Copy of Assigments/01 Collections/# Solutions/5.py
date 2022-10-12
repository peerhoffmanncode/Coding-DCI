color_names = ['red', 'green', 'blue']
color_hex = ['#FF0000','#00FF00', '#0000FF']

colors = {}

def main():
  for i in range(len(color_names)):
  name = color_names[i]
  value = color_hex[i]

  colors[name] = value

  print(colors)

# Alternative solution using zip()
def alternative():
  colors = dict(zip(color_names, color_hex))
  print(colors)

if __name__ == '__main__':
  main()