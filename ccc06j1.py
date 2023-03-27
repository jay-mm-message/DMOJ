menu_burger = int(input())
calories_burger = 0

menu_side = int(input())
calories_side = 0

menu_drink = int(input())
calories_drink = 0

menu_dessert = int(input())
calories_dessert = 0

if menu_burger == 1:
    calories_burger = calories_burger + 461
if menu_burger == 2:
    calories_burger = calories_burger + 431
if menu_burger == 3:
    calories_burger = calories_burger + 420
#print('calories_burger: %d' % calories_burger)
if menu_side == 1:
  calories_side = calories_side + 100
if menu_side == 2:
  calories_side = calories_side + 57
if menu_side == 3:
  calories_side = calories_side + 70
#print('calories_side: %d' % calories_side)
if menu_drink == 1:
  calories_drink = calories_drink + 130
if menu_drink == 2:
  calories_drink = calories_drink + 160
if menu_drink == 3:
  calories_drink = calories_drink + 118
#print('calories_drink: %d' % calories_drink)
if menu_dessert == 1:
  calories_dessert = calories_dessert + 167
if menu_dessert == 2:
  calories_dessert = calories_dessert + 266
if menu_dessert == 3:
  calories_dessert = calories_dessert + 75
#print('calories_dessert: %d' % calories_dessert)

calories_total = calories_burger + calories_side + calories_drink + calories_dessert
print("Your total Calorie count is %d." % calories_total)