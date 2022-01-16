import time
# lines 3 to 16 are the introduction
print('Good morning, afternoon or evening!')
time.sleep(2.5)
print('My name is Faisal. This is a password generator made in Python.')
time.sleep(2.5)
print('I used a few tutorials to start, but I did the rest myself.')
time.sleep(3.5)
print('This was made for a technology fair, and I thought this would be a helpful project to make.')
time.sleep(3.5)
print('With the rising amount of time we spend on the internet and on sites that require personal information, our passwords need to be stronger than ever.')
time.sleep(3.5)
print('This password generator will give you 4 types of passwords: Weak, Moderate, Strong, and Extremely Strong.')
time.sleep(4.5)
print('These are the tutorials I used while making this project, in link form. \nThe first video I used was https://youtu.be/iyOeJALTVUw. \nThe second video I used was https://youtu.be/nrvpnZ0GeOk. \nThe third and final video I used was https://youtu.be/NMKuf12mJu4. \nEnjoy!')
print('                                                  ')
import random
time.sleep(3)
# line 20 is the length of your password
length = input("How long do you want your password to be? (Use numbers)")
print('                                                    ')
# lines 23 to 28 is the code for creating the weak password
password = ''
lowercase = 'abcdefghijklmnopqrstuvwxyz'
for i in range(int(length)):
  randChar = random.choice(lowercase)
  password = password + randChar
print('Weak Password: ' + password)

# lines 31 to 36 is the code for creating the moderate password
password2 = ''
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(int(length)):
  randChar = random.choice(lowercase + uppercase)
  password2 = password2 + randChar
print('Moderate Password: ' + password2)

# lines 39 to 44 is the code for creating the strong password
password3 = ''
numbers = '0123456789'
for i in range(int(length)):
  randChar = random.choice(lowercase + uppercase + numbers)
  password3 = password3 + randChar
print('Strong Password: ' + password3)

# lines 47 to 54 is the code for creating the extremely strong password
password4 = ''
symbols = "`-=[]\;',./~!@#$%^&*()_+{}|:'<>?"
for i in range(int(length)):
  randChar = random.choice(lowercase + uppercase + numbers + symbols)
  password4 = password4 + randChar
print('Extremely Strong Password: ' + password4)
print('                                                 ')
print('I hope you liked my password generator! Thank you for trying it out!')
time.sleep(5)

# everything from line 57 to 65 is my username generator
print("\n\n Now, This is a username generator written in Python. As a follow-up to my previous Python program, the password generator that came before this, I developed this program. After all,there is no point in having a password without a username! \nYour username is what you input. Hope you enjoy it!")
print('                                        ')
animal = input('What is your favorite animal? ')
color = input('What is your favorite color? ')
num = input('What is your favorite number? ')
username =  color + animal + num  
print('Here is your username😂: ' + username)
print('                                                                     ')
time.sleep(2.5)
print('                                                                     ')
# this is my weak or strong password checker
UserPassword = input('\n\n Now, This is a Weak or Strong password checker. What password do you want me to check? ')
UserPasswordLength = len(UserPassword)
PasswordIsLower = UserPassword.islower()
PasswordIsUpper = UserPassword.isupper()
if PasswordIsLower == UserPassword.islower() and UserPasswordLength < 10:
		print(UserPassword + ' is a weak password.')
 
if PasswordIsLower != UserPassword.islower() and PasswordIsUpper != UserPassword.isupper() and UserPasswordLength > 10:
		print(UserPassword + ' is an good password.')
print('                                                                   ')
# everything else is my feedback section
feedback = input('\n\nHello again! Before you leave, please give some feedback on my project! \n\nUse "Great!", "Good.", "Okay.", "Not good.", and "Terrible!". DO NOT put quotation marks, and use the EXACT spelling, capitalization, and punctuation. Thank you! ')
if feedback == 'Great!': 
  print('Thank you for your feedback! Bye!')
if feedback == 'Good.':
  print('Thank you for your feedback! Please fill out this form here ---> ( https://docs.google.com/forms/d/e/1FAIpQLSdovMOoETRHetyds86ifjExlX4ACDAxLR7sO6UJAuRnNd7NSw/viewform?vc=0&c=0&w=1&flr=0 ) to give me your feedback. Thanks again!')
if feedback == 'Okay.':
    print('Thank you for your feedback! Please fill out this form here ---> ( https://docs.google.com/forms/d/e/1FAIpQLSdovMOoETRHetyds86ifjExlX4ACDAxLR7sO6UJAuRnNd7NSw/viewform?vc=0&c=0&w=1&flr=0 ) to give me your feedback. Thanks again!')
if feedback == 'Not good.':
    print('Thank you for your feedback! Please fill out this form here ---> ( https://docs.google.com/forms/d/e/1FAIpQLSdovMOoETRHetyds86ifjExlX4ACDAxLR7sO6UJAuRnNd7NSw/viewform?vc=0&c=0&w=1&flr=0 ) to give me your feedback. Thanks again!')
if feedback == 'Terrible!':
    print('Thank you for your feedback! Please fill out this form here ---> ( https://docs.google.com/forms/d/e/1FAIpQLSdovMOoETRHetyds86ifjExlX4ACDAxLR7sO6UJAuRnNd7NSw/viewform?vc=0&c=0&w=1&flr=0 ) to give me your feedback. Thanks again!')