# CBS_HW_04_05
CBS_HW_04_05



## Завдання 1
Створіть функцію для обчислення факторіала числа. Запустіть декілька завдань, використовуючи Thread, і заміряйте швидкість їхнього виконання, а потім заміряйте швидкість обчислення, використовуючи той же набір завдань на ThreadPoolExecutor. Як приклади використовуйте останні значення, від мінімальних і до максимально можливих, щоб побачити приріст або втрату продуктивності.

## Завдання 2
Створіть три функції, одна з яких читає файл на диску із заданим ім'ям та перевіряє наявність рядка «Wow!». Якщо файлу немає, то засипає на 5 секунд, а потім знову продовжує пошук по файлу. Якщо файл є, то відкриває його і шукає рядок «Wow!». За наявності цього рядка закриває файл і генерує подію, а інша функція чекає на цю подію і у разі її виникнення виконує видалення цього файлу. Якщо рядки «Wow!» не було знайдено у файлі, то засипати на 5 секунд. Створіть файл руками та перевірте виконання програми.
