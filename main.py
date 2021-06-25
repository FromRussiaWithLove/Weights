def getWeight(weight,last):
    # weight - требуемый вес, last - вес последней добавленной гири
    for i in reversed(range(1, last+1)):
        if kratn[i] > 0 and i <= weight:
            # Перебираем гири разновеса от большей к меньшей. Если количество гирь данного веса
            # больше 0,а ее вес меньше требуемого веса, убираем ее из разновеса и
            # добавляем к набираемому весу
            kratn[i] =kratn[i] - 1
            sol[i] += 1
            # Оставшийся вес равен требуемому весу минус вес добавленной гири
            weightRemaining = weight-i
            # Если оставшийся вес - 0, решение найдено, выводим решение на экран
            if weightRemaining == 0:
                for j in range(1,10):
                    print(sol[j], end='\t')
                print('\n')
            else: # иначе продолжаем подбор
                getWeight(weightRemaining,i)
            # Выполняем возврат, убираем гирю из набираемого веса
            # и возвращаем в разновес
            sol[i] -= 1
            kratn[i] += 1

# Создаем разновес
kratn = [0,3,0,1,1,0,0,1,1,1]
# Создаем список для набираемого веса
sol = [0,0,0,0,0,0,0,0,0,0]
# Выводим шапку таблицы
print('1кг\t2кг\t3кг\t4кг\t5кг\t6кг\t7кг\t8кг\t9кг\t')
getWeight(9,9)
input('Для продолжения нажмите клавишу Enter')