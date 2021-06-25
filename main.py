def getWeight(weight,last,kratn,sol):
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
                getWeight(weightRemaining,i, kratn, sol)
            # Выполняем возврат, убираем гирю из набираемого веса
            # и возвращаем в разновес
            sol[i] -= 1
            kratn[i] += 1

def main():
    # Создаем разновес
    kratn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1,10):
        kratn[i] = int(input('Введите количество гирь весом', i, 'кг'))
    weight = int(input('Введите вес, который необходимо набрать'))
    sol = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Выводим шапку таблицы
    print('1кг\t2кг\t3кг\t4кг\t5кг\t6кг\t7кг\t8кг\t9кг\t')
    getWeight(weight, 9, kratn, sol)
    input('Для продолжения нажмите клавишу Enter...')

main()