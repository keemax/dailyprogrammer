name = input("what's your name\n")
age = input("how old are you?\n")
redditName = input("what's your reddit name?\n")

output = 'your name is {0}, you are {1} years old, and your username is {2}'.format(name, age, redditName)
print(output)

log = open('output.txt', 'a')
log.write(output + '\n')
log.close()