string = input("Please give me a string: ").strip()
if len(string) < 2:
  print("Empty string")
if len(string) == 2:
  print(f'{string + string}')
if len(string) > 2:
  print(f'{string[:2] + string[-2:]}')
