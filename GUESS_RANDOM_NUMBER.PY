import random as rand

target = rand.randint(1,10)

while True:
  guess_number=input('guess a target or Quit')
  if (guess_number=='Quit'):
    break

  guess_number = int(guess_number)
  if (guess_number==target):
    print('success... You guessed')
    break
  elif(guess_number<target):
    print('your number is small...guess bigger number')
  else:
    print('you number is too big ...guess smaller number')
print('game over...')