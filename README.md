# Задание №1

### С++
```С
bool isEvenDiv(uint64_t value) {
	return (value % 2) == 0;
}

bool isEvenLogicalAnd(uint64_t value) {
	return (value & 1) == 0;
}
```
### Python
```Python
def isEvenDiv(value):
    return value % 2 == 0


def isEvenLogicalAnd(value):
    return value & 1 == 0

```

После написания двух вариантов функций определения четности 
числа сначала на Python, а после на C++,
и последующего дизассемблирования было установлено, что
при использовании компилятора GCC с включенной оптимизацией
функции имеют одинаковые методы
![](https://github.com/k-toncha/Test_task/blob/master/GCC.PNG) 

следовательно, и работают они одинаковое количество времени. 

Однако при использовании MSVC и оптимизации /Od функция isEvenLogicalAnd 
работает быстрее: 

<p align="center">
  <img width="336" height="292" src="https://github.com/k-toncha/Test_task/blob/master/Time_test.PNG">
</p>

в этом можно убедиться так же, сравнив дизасемблированный код (функция isEvenLogicalAnd имеет больше методов).
![](https://github.com/k-toncha/Test_task/blob/master/GB_msvc.PNG) 

Таким образом, стоит отметить, что до момента выключения оптимизации функции работают относительно одинаково
по времени. После выключения всех оптимизаций, функция isEvenLogicalAnd быстрее.

# Задание №2 #

Написано две реализации циклического буфера FIFO:
- с помощью массива заданной длинны (class Mass_FIFO);
- с помощью связного циклического списка с заданным колличеством
элементов (Linked_List_FIFO).

Дополнительно приведено сравнение времени, затраченного для работы двух реализаций.
Варианты работают примерно одинакого.


# Задание №3 #

Предложен вариант быстрой сортировки слиянием. Это рекурсивный алгоритм, который постоянно разбивает список пополам. 
Если список пуст или состоит из одного элемента, 
то он отсортирован по определению (базовый случай). 
Если в списке больше, чем один элемент, мы разбиваем его 
и рекурсивно вызываем сортировку слиянием для каждой из половин. 
После того, как обе они уже отсортированы, выполняется основная 
операция, называемая слиянием. Слияние - это процесс комбинирования 
двух меньших сортированных списков в один новый, но тоже отсортированный.
<p align="center">
  <img width="658" height="355" src="https://github.com/k-toncha/Test_task/blob/master/MergeSort1.PNG">
</p>
<p align="center">
  <img width="471" height="375" src="https://github.com/k-toncha/Test_task/blob/master/MergeSort2.PNG">
</p>

