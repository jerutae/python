num=5
ip=int(input('Enter the integer: '))
if num==ip:
    print('congrats, guess is crt')
elif num<ip:
    print('oops..its higher')
elif num>ip:
    print('oops..its lower')
else:
    print('oopsie..try again')
