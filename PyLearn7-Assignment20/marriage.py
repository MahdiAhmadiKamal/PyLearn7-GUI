import random

boys = ['mohammad', 'sobhan', 'abdollah', 'kiya', 'mahdi', 'sajjad', 'homan', 'arman']
girls = ['mahtab', 'hane', 'harir', 'fateme', 'kiana', 'faezeh', 'minoo', 'mina', 'soghra']
marriage = []
while len(boys)>0:
    boy = boys[random.randint(0,len(boys)-1)]
    girl = girls[random.randint(0,len(girls)-1)]
    couple = {"boy":boy, "girl":girl}
    marriage.append(couple)
    boys.remove(boy)
    girls.remove(girl)

print(marriage)