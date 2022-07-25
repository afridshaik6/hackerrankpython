cost_of_item = 20
d = 3
minimum = 6
wallet = 70
games_bought = 0
while cost_of_item > minimum:
    games_bought += 1
    wallet = wallet - cost_of_item
    cost_of_item = cost_of_item - d
    print(cost_of_item)


