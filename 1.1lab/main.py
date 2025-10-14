#ВАРИАНТ 15 , ЗАДАНИЕ 4 (https://ege.sdamgia.ru/problem?id=99595)
c = 0 #счетчик вариантов
for c1 in range(1,7): # очки первого кубика
    for c2 in range(1,7):#очки второго кубика
        if c1+c2 == 5:#сумма очков равна 5
            c+=1
print(c)
