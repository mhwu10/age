driving = input('Have you driven?')
if driving != 'yes' and driving != 'no':
    print('Only two answers: yes/no')
    raise SystemExit

age = input('what is your age?')
age = float(age)

if driving == 'yes':
    if age >= 18:
        print('you have passed the exam')
    else:
        print('why can you drive?')
elif driving == 'no':
    if age >= 18:
        print('good, you can go for a exam')
    else:
        print('you need to wait for the exame until you are 18')
else:
    print('please answer yes/no')