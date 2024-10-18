name=input('enter your name\n')
import time    
timestamp = time.strftime('%H:%M:%S')
timestamp = int(time.strftime('%H'))
if(timestamp<=12 and timestamp>=00):
    print('good morning',name)
elif(timestamp<=17 and timestamp>=12):
    print('good afternoon')
elif(timestamp<=19 and timestamp>=17):
    print('good evening',name)
else:
    print('good night',name) 

print('welcome to KBC')    
questions=[
    ['Which language was used to make the game tetris','c','c++','java','python','a'],
    ['what was the first programming language','python','c++','c','java','c'],
    ['Which company is credited with creating the first commercially successful personal computer?','IBM','Apple','Microsoft','Windows','b'],
    ['In which year was first iphone released?','2009','2008','2003','2007','d'],
    ['what was the first apple product','macintosh','ipod','iphone','apple-1','d'],
    ['Which company is known for developing the worlds first microprocessor?','intel','IBM','Microsoft','none','a'],
    ['what was the first ever pc game?','spacewars','tetris','snake','marioo','a'],
    ['Where did Mark Zuckerberg study','Harvard','MIT','IIT','none','a'],
    ['Which company developed playstation','samsung','sony','apple','nokia','b'],
    ['what was Mark Zuckerberg\'s first website','facebook','omegle','facemash','instagram','c'],

]
levels=[200000,500000,700000,1000000,1200000,1600000,2000000,2300000,2600000,3000000]
money=0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"\n\nThe questions is. {question[0:5]}")
    print(f"a. {question[1]}          b. {question[2]} ")
    print(f"c. {question[3]}          d. {question[4]} ")
    reply =input("Enter your answer (a-d) or  q to quit:\n" )
    if (reply == 'q'):
        print('you take 0 rs')
        break
    if(reply == question[5]):
            print(f"Correct answer, you have won Rs. {levels[i]}")
            if(i == 3):
                money = 1000000
            elif(i == 6):
                money = 2000000
            elif(i == 9):
                money = 3000000
    else:
        print("Wrong answer!")
        break 

print('congrats',name,'you have won',money,'dollars')