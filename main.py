import random
from replit import clear
from game_data import data
from art import vs, logo

# print(data[0]["name"])
def generate_random_number():
    """ Generate Random Number """
    count = 0
    for celeb in data:
      count += 1
    random_number = random.randint(0,count-1)
    return random_number


def select_celeb():
    """ This Function Prevents Randomly Picking Same Celebrity """
    person_a = generate_random_number()
    person_b = generate_random_number()
    if person_a == person_b:
        select_celeb()
    else:
        return [person_a, person_b]

def compare(item_a, item_b):
    compare_a = int(data[item_a]['follower_count'])
    compare_b = int(data[item_b]['follower_count'])
    if compare_a > compare_b:
        return 1
    elif compare_a < compare_b:
        return 0

game_end = False

while not game_end:
  celeb_a = select_celeb()[0]
  celeb_b = select_celeb()[1]

  print(logo)

  print(f"Compare A: {data[celeb_a]['name']}, a {data[celeb_a]['description']}, from {data[celeb_a]['country']}")
  print(vs)
  print(f"Compare B: {data[celeb_b]['name']}, a {data[celeb_b]['description']}, from {data[celeb_b]['country']}")

  #print(compare(item_a = celeb_a, item_b = celeb_b))
  answer = input("\n\nWho has more followers? Type 'a' and 'b': ").lower()

  re_value = int(compare(item_a = celeb_a, item_b = celeb_b))

  if answer == "a" and re_value == 1:
      print(f"Answer is correct! {data[celeb_a]['name']} has more follower!")
      clear()
  elif answer == "b" and re_value == 0:
      print(f"Answer is correct! {data[celeb_b]['name']} has more follower!")
      clear()
  else:
      print("Game Over!")
      game_end = True