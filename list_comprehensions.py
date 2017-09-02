#coding=UTF-8

s = [x*2 for x in range(0, 10)]
print(s)

s2 = [x*2 for x in range(0, 10) if x % 2 == 0]
print(s2)

s3 = [w.capitalize() for w in ['um', 'dois', 'três']]
print(s3)

s4 = [[w.capitalize(), w.upper(), len(w)] for w in ['um', 'dois', 'três']]
print(s4)

s5 = [(w.capitalize(), w.upper(), len(w)) for w in ['um', 'dois', 'três']]
print(s5)
