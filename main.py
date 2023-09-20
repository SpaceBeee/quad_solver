import math

def quad_solver(a, b, c):
    if type(a) != float or type(b) != float or type(c) != float:
        raise TypeError("This should be a float")

    p_roots = []

    if ((b ** 2) - (4 * a * c)) > 0:
        p_roots.append(((-b) + (math.sqrt((b ** 2) - (4 * a * c)))) / (2 * a))
        p_roots.append(((-b) - (math.sqrt((b ** 2) - (4 * a * c)))) / (2 * a))

    elif ((b ** 2) - (4 * a * c)) == 0:
        p_roots.append((-b) / (2 * a))

    else:
        raise Exception("there are no real roots")

    return p_roots


while True:
    try:
        a = float(input("enter the first coefficient"))
        b = float(input("enter the second coefficient"))
        c = float(input("enter the third  coefficient"))
        roots = quad_solver(a, b, c)
        break
    except ValueError:
        print("input has to be a float or integer")


for root in roots:
    print(root)