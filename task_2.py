from pathlib import Path
import shutil
import argparse

"""
Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» за умови,
 що користувач повинен мати можливість вказати рівень рекурсії.
"""

import turtle


def draw_koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            draw_koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

window = turtle.Screen()
window.bgcolor("white")
snowflake_turtle = turtle.Turtle()
snowflake_turtle.color("blue")
snowflake_turtle.speed(0)
snowflake_turtle.penup()
snowflake_turtle.goto(-150, 90)
snowflake_turtle.pendown()

for _ in range(3):
    draw_koch_snowflake(snowflake_turtle, level, 300)
    snowflake_turtle.right(120)

window.mainloop()
