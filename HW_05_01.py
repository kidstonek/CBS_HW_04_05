'''
Завдання 1
Створіть функцію для обчислення факторіала числа. Запустіть декілька завдань, використовуючи Thread,
і заміряйте швидкість їхнього виконання, а потім заміряйте швидкість обчислення, використовуючи той же
набір завдань на ThreadPoolExecutor. Як приклади використовуйте останні значення, від мінімальних і до
максимально можливих, щоб побачити приріст або втрату продуктивності.
'''
from concurrent.futures import ThreadPoolExecutor
import threading
import time


def factorial(digit: int) -> float:
    factorial_result = 1
    for number in range(1, digit+1):
        factorial_result *= number
    return factorial_result


def main():
    start_time = time.time()
    thread1 = threading.Thread(target=factorial, args=[1000,])
    thread1.start()
    # print(time.time() - start_time)
    # start_time = time.time()
    thread2 = threading.Thread(target=factorial, args=[1000,])
    thread2.start()
    print(time.time() - start_time)

    start_time = time.time()
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(factorial, 1000) for i in range(2)]
    print(time.time() - start_time)


if __name__ == '__main__':
    main()
