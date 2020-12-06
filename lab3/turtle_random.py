import turtle as t
import random

t.shape('turtle')
t.speed(20)


move_list = [t.left, t.right, t.forward, t.back]



while 1 == 1 :
    b = random.randint(0, 3)
    a = random.randint(5, 20)
    move_list[b](a)



