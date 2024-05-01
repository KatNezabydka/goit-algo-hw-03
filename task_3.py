"""
Напишіть програму, яка виконує переміщення дисків з стрижня А на стрижень С, використовуючи стрижень В як допоміжний.
 Диски мають різний розмір і розміщені на початковому стрижні у порядку зменшення розміру зверху вниз.
"""


def move_disk(source, destination):
    disk = source.disks.pop()
    destination.disks.append(disk)
    print(f"Перемістити диск з {source.name} на {destination.name}: {disk}")


def hanoi_tower(n, source, auxiliary, destination):
    if n == 1:
        move_disk(source, destination)
    else:
        hanoi_tower(n - 1, source, destination, auxiliary)
        move_disk(source, destination)
        hanoi_tower(n - 1, auxiliary, source, destination)


class Tower:
    def __init__(self, name):
        self.name = name
        self.disks = []


n = int(input("Введіть кількість дисків: "))
source = Tower("A")
auxiliary = Tower("B")
destination = Tower("C")
source.disks = list(range(n, 0, -1))

print(f"Початковий стан: {vars(source)}")
hanoi_tower(n, source, auxiliary, destination)
print(f"Кінцевий стан: {vars(destination)}")
