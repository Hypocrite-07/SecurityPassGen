#Dependencies
import time
import string
import random
import os
clear = lambda: os.system('clear')

clear();

#Password Generation Process
char_set = string.ascii_uppercase + string.digits



#Colors For Text
def red(text):
    print("\033[31m {}" .format(text))
def orange(text):
    print("\033[33m {}" .format(text))
def blue(text):
    print("\033[34m {}" .format(text))
def white(text):
    print("\033[37m {}" .format(text))
def green(text):
    print("\033[32m {}" .format(text))

#Info Text At The Beginning
blue('SecurityPassGen\n\n\n');
time.sleep(1)
orange("You want HARD PASS? I'M WILL DO IT!\n");
time.sleep(1)







def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	print ''.join(random.choice(chars) for _ in range(size))

#Main Menu
def main():
	secret='QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm1234567890'
#These characters consist of passwords.
#You can change.

#Remove '#' for a harder password
	#secret='QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm1234567890!@#$%^&*()_-+=~{[}]:;"'<,>.\?/'

	green('SPG Menu')
	green('1 - Generate pass')
	green('2 - About')
	red('99 - Exit')
	green('')
	a = input(' Choose number: ')
	if a == int('1'):
		size = input(" How long?: ")
		much = input(" How much?: ")
		clear();
		time.sleep(1)
		much=much-1
		rd = id_generator(size, secret)
		for rd in range(much):
			id_generator(size, secret)
			#green('\n\n\nPasswords were saved in: SPG.txt')
			#I wanted to make passwords stored in a file, but I don't know how to do it
		red('\nWARN! You must save passwords otherwise they will disappear.\nWARN! You must save passwords otherwise they will disappear.\nWARN! You must save passwords otherwise they will disappear.')
		red('99 - To back')
		green('')
		input('Choose number: ');
		clear();
		main();
	elif a == int('2'):
		time.sleep(0.5)
		blue('It app writed by Hypocrite-07\n');
		time.sleep(0.5)
		blue('VK: https://vk.com/seventhhypocrite')
		time.sleep(0.5)
		blue('Telegram: @Hypocrite07')
		time.sleep(0.5)
		blue('Gmail: seventhhypocrite@gmail.com\n\n')
		time.sleep(0.5)
		red('99 - To back')
		green('')
		input('Choose number: ');
		time.sleep(0.5)
		clear();
		time.sleep(0.5)
		main()
	elif a == int('99'):
		exit();
	else:
		red('Unknow command')
		time.sleep(2)
		main()

def info():
	clear()
	blue('This app is written by Hypocrite-07\n');
	blue('VK: https://vk.com/seventhhypocrite')
	blue('Telegram: @Hypocrite07')
	red('Gmail: seventhhypocrite@gmail.com\n\n')



info()

main()
