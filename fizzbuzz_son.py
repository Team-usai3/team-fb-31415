#for i in range(1, 1+15):
#    if i % 3 == 0 or i % 5 ==0:
#        print('fizz'*(i%3==0) + 'buzz'*(i%5==0))
#    else:
#        print(i)
print(['fizzbuzz' if i % 15 ==0 else 'fizz' if i % 3 ==0 else 'buzz' if i % 5 == 0 else i for i in range(1,15+1)])
