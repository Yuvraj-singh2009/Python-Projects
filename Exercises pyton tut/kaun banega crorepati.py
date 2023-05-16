print("welcome to kaun banega crorepati(kbc)")
question_list = ["what is 1 + 1", "what is 2+2", "what is 3+3","what is 4+4"]
option_1 = ['a.1','a.2', 'a.4', 'a.6']
option_2 = ['b.2','b.4', 'b.5','b.7']
option_3 = ['c.3', 'c.5', 'c.6', 'c.8']
option_4 = ['d.5','d.6', 'd.8', 'd.0']

correct = 0
answer=['b','b','c','c']
prize= [0,100,1000,10000,20000]
a=0
# for i in range(0, len(question_list)):
while a<len(question_list):
    print(question_list[a])
    print(option_1[a])
    print(option_2[a])
    print(option_3[a])
    print(option_4[a])
    user = input("enter your answer:")
    if user==answer[a]:
        print("Congrats! Aapka answer sahi hai",prize[a])
        correct += 1
    
    else:
        print("your answer is wrong",prize[0])
        break
    a = a+1

a = sum(prize,)
print("total money you won in this game",a)
    
                


