Синхронная проверка:

Память:

![img.png](image/img.png)

Процессор:

![img_1.png](image/img_1.png)

Сеть:

![img_2.png](image/img_2.png)

Время работы: 1303764ms = 21,7 m

![img_3.png](image/img_3.png)

max_workers = 5

Память:

![img_4.png](image/img_4.png)

Процессор:

![img_5.png](image/img_5.png)

Сеть:

![img_6.png](image/img_6.png)

Время работы: 557925ms = 9,3 m

![img_7.png](image/img_7.png)

max_workers=10

Память:

![img_8.png](image/img_8.png)

Процессор:

![img_9.png](image/img_9.png)

Сеть:

![img_10.png](image/img_10.png)

Время работы: 391481ms = 6,5 m

![img_11.png](image/img_11.png)

max_workers=100

Память:

![img_12.png](image/img_12.png)

Процессор:

![img_13.png](image/img_13.png)

Сеть:

![img_14.png](image/img_14.png)

Время работы: 315087ms = 5,3 m

![img_15.png](image/img_15.png)

Вывод: Загрузка памяти не зависит от количества воркеров. При увеличении числа воркеров: загрузка проццесора - увеличивается, загрузка сети - увеличивается, время работы - уменьшается.

Генерируем монетки (6): 

Память:

![img_16.png](image/img_16.png)

Процессор:

![img_17.png](image/img_17.png)

Сеть:

![img_18.png](image/img_18.png)

Время работы: 373090ms = 6,2 m

![img_19.png](image/img_19.png)

max_workers = 2

Память:

![img_20.png](image/img_20.png)

Процессор:

![img_21.png](image/img_21.png)

Сеть:

![img_22.png](image/img_22.png)

Время работы: 566232ms = 9,4 m

![img_23.png](image/img_23.png)

max_workers = 4

Память:

![img_24.png](image/img_24.png)

Процессор:

![img_25.png](image/img_25.png)

Сеть:

![img_26.png](image/img_26.png)

Время работы: 419699ms = 7 m

![img_27.png](image/img_27.png)

max_workers = 5

Память:

![img_28.png](image/img_28.png)

Процессор:

![img_29.png](image/img_29.png)

Сеть:

![img_30.png](image/img_30.png)

Время работы: 546221ms = 9,1 m

![img_31.png](image/img_31.png)

max_workers = 10

Память:

![img_32.png](image/img_32.png)

Процессор:

![img_33.png](image/img_33.png)

Сеть:

![img_34.png](image/img_34.png)

Время работы: 590152ms = 9,8 m

![img_35.png](image/img_35.png)

max_workers = 100

Ошибка: 
![img_36.png](image/img_36.png)

Вывод: Загрузка памяти и сети не зависит от количества воркеров. При увеличении числа воркеров, загрузка процессора - увеличивается. Сильной зависимости времени работы программы от количества воркеров я не заметил, больше зависит от скорости нахождения монеток(везения).