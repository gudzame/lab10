import logging
logging.basicConfig(level=logging.INFO, filename="logger10.log",
                    format='%(levelname)s (%(asctime)s): %(message)s',
                    encoding='utf-8', force=True)
logger = logging.getLogger(__name__)
logger.info('Игра началась!')

import random
y = 0
while y == 0:
     N = input("Введите максимальное число ")
     k = input("Введите число попыток ")
     if (int(N) <= 0 or N.isdigit() == False) and (int(k) <= 0 or k.isdigit() == False):
          print("Некорректно введены данные, попробуйте ещё раз!")
          logger.info('Некорректно введены данные, попробуйте ещё раз!')
     else:
          N = int(N)
          k = int(k)
          logger.info(f"Максимальное число N: {N}")
          logger.info(f"Число попыток k: {k}")
          s = list(range(1, N + 1))
          x = random.choice(s)
          logger.info(f"Загаданное число: {x}")
          y = 1

q = 0
while q == 0:
     for i in range(k):
          n = input("Угадайте число ")
          if (int(n) <= 0 or n.isdigit() == False):
               print("Некорректно введены данные, попробуйте ещё раз!")
               logger.info('Некорректно введены данные, попробуйте ещё раз!')
          else:
               n = int(n)
               if n > x:
                    print("Загаданное число меньше!")
                    logger.info("Загаданное число меньше!")
               elif n < x:
                    print("Загаданное число больше!")
                    logger.info("Загаданное число больше!")
               else:
                    print("Вы угадали!")
                    logger.info("Вы угадали!")
                    break
               q = 1

if n != x:
     print("Попытки закончились!")
     logger.info("Попытки закончились!")
