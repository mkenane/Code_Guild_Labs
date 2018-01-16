

place = input('Name a room/place in your house: ')
color = input('Insert Your least favorite color')
number = int(input('Insert a random large number'))
wildanimal = input('Give me A wild animal:')

xmas_tree_instructions = 'How to prepare your xmas tree: \n Go buy a tree, place it in your {0} Go buy xmas lights that are one single color, preferably {1}. You will need at least {2} lights. Now for the crowning touch to your festive masterpiece - an eye-catching Christmas tree topper, instead of a star, put a {3}. It’ll make your tree unique'.format(place, color, number, wildanimal)

print(xmas_tree_instructions)
