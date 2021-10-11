import random

score = 0
round = []
for x in range(1,21):
    number = random.randint(1,1000)
    round = ('this is round: {}'.format(x))
    print(round)
    for i in range(0,10):
        user = int(input('guess the number: '))
        if abs(user - number) <= 50 and abs(user - number) > 20:
            print('u are warm')
        if abs(user - number) <= 20:
            print('u are really warm')
        if user == number:
            score = score + 1
            print('Hurray')
            print(f"you guessed the right number, its {number}")
            print('your score so far ' + str(score) + ' points')
            break
        
    if user != number:
        print(f'your guessed the incorrect number, the correct number is: {number} ')
        print('your score so far is ' + str(score) + ' points')
    again = input('geuss another number? y/n ')
    if again == 'n' or again == 'N':
        break
print('your final score is ' + str(score) + ' points')