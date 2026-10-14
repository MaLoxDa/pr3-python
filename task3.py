print("Проверка, пересекаются ли два отрезка")

print("Отрезок 1:")
x1 = float(input("  x1 = "))
y1 = float(input("  y1 = "))
x2 = float(input("  x2 = "))
y2 = float(input("  y2 = "))

print("Отрезок 2:")
x3 = float(input("  x3 = "))
y3 = float(input("  y3 = "))
x4 = float(input("  x4 = "))
y4 = float(input("  y4 = "))


def orientation(ax, ay, bx, by, cx, cy):
    value = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0


o1 = orientation(x1, y1, x2, y2, x3, y3)
o2 = orientation(x1, y1, x2, y2, x4, y4)
o3 = orientation(x3, y3, x4, y4, x1, y1)
o4 = orientation(x3, y3, x4, y4, x2, y2)

if o1 != o2 and o3 != o4:
    print("Отрезки пересекаются.")
elif o1 == 0 and o2 == 0:
    print("Отрезки лежат на одной прямой.")
else:
    print("Отрезки не пересекаются.")