team = 'New England Patriots'
print(team[0])

print(len(team))

print(team[len(team)-1])
last = team[-1]
print(last)

prefixes = 'JKLMNOPQ'
for letter in prefixes:
    if letter == 'O' or letter == 'Q' :
        suffix = 'uack'
    else:
        suffix = 'ack'
    print (letter + suffix)
