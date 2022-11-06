name=input('what is your name?:')
age=input('How old are you?:')
city=input('which city do you live in?:')
love=input('what do you love doing?:')

string= "Your name is {} and you are {} years old.You live in {} and you love {}"
output = string.format(name,age,city,love)
print (output)
