import json
import difflib
import colorama
import sympy


with open('data.json', 'r') as f:
  data = f.read()

answer = json.loads(data)


class Colors:
    def __init__(self):
        self.colors = ['BLACK', 'BLUE', 'CYAN', 'GREEN', 'MAGENTA', 'RED', 'WHITE', 'YELLOW']
        self.codes = {color: getattr(colorama.Fore, color) for color in self.colors}

    def __getattr__(self, name):
        if name.upper() in self.codes:
            return self.codes[name.upper()]
        else:
            return ''

color = Colors()


def check(question):
  similarKey = difflib.get_close_matches(question, answer.keys())

  if similarKey:
    similarKey = similarKey[0]
    if similarKey:
        return answer[similarKey]
  else:
    return "I need more context."


def main():
  user = input(color.red + "[Question]> ")
  try:
      result = sympy.sympify(user).evalf()
      print(int(result))
      
  except:
      if check(user):
          print(color.cyan + f"[Scylla]> {check(user)}")


  
while True:
  main()