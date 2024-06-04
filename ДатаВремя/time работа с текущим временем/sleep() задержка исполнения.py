# Функция sleep()
# используется для добавления задержки в выполнении программы.
# Эта функция принимает в качестве аргумента количество секунд (secs)
# и добавляет задержку в выполнении программы на указанное количество секунд

# останавливает выполнение только текущего потока, а не всей программы

# import time
# print('Before the sleep statement')
# time.sleep(3)
# print('After the sleep statement')

# Аргумент secs может быть числом с плавающей точкой (float),
# для указания более точного времени приостановки

# import time
# print('Before the sleep statement')
# time.sleep(0.7)
# print('After the sleep statement')


# может потребоваться задержка на разное количество секунд.
# Сделать это можно следующим образом:
# import time
# for i in [0.7, 0.5, 1.0, 2.5, 3.3]:
#     print(f'Waiting for {i} seconds')
#     time.sleep(i)
# print('The end')