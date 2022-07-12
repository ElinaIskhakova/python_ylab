from functools import wraps
from time import sleep

def repeat_function(call_count=1, start_sleep_time=1.0,
             factor=3, border_sleep_time=10):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Количество запусков' ,call_count)
            print('Начало работы')
            sleep_time = start_sleep_time
            for counter in range(call_count):
                func_result = func(*args, **kwargs)
                if sleep_time < border_sleep_time:
                    sleep_time *= 2 ** factor
                    if sleep_time >= border_sleep_time:
                        sleep_time = border_sleep_time
                print(f'Запуск номер {counter+1}. Ожидание:'
                      f' {sleep_time} секунд. Результат '
                      f'декорируемой функций = {func_result}')
                sleep(sleep_time)
            print('Конец работы')
        return wrapper
    return decorator


@repeat_function(2, 1, 3, 10)
def function(number: int):
    return number+1

print(function(10))