"""
Given the values of the adjacent side, opposite side and hypotenuse of a right triangle,
this application prints the values of its sine, cosine and tangent
Created by Marques Henrique Silva
"""

import math as math


def enter_triangle():
    # user enter values of the right triangle sides into a list
    adjacent = float(input("Adjacent: "))
    opposite = float(input("Opposite: "))
    hypotenuse = float(input("Hypotenuse: "))
    triangle_sides = [adjacent, opposite, hypotenuse]
    return triangle_sides


def pythagoras(triangle_sides):
    # calculates missing side of right triangle
    adjacent = triangle_sides[0]
    opposite = triangle_sides[1]
    hypotenuse = triangle_sides[2]

    if (adjacent == 0):
        adjacent = math.sqrt((hypotenuse**2) - (opposite**2))
        triangle_sides[0] = adjacent

    elif (opposite == 0):
        opposite = math.sqrt((hypotenuse**2) - (adjacent**2))
        triangle_sides[1] = opposite

    elif (hypotenuse == 0):
        hypotenuse = math.sqrt((adjacent**2) + (opposite**2))
        triangle_sides[2] = hypotenuse


def trigonometry_identities(triangle_sides):
    # calculates right triangle identities
    adjacent = triangle_sides[0]
    opposite = triangle_sides[1]
    hypotenuse = triangle_sides[2]

    sin = (opposite/hypotenuse)
    cos = (adjacent/hypotenuse)
    tan = (opposite/adjacent)
    results = (sin, cos, tan)
    return results


def print_identities(results, triangle_sides):
    # print all results
    print("Adjacent = %.2f" % triangle_sides[0])
    print("Opposite = %.2f" % triangle_sides[1])
    print("Hypotenuse = %.2f" % triangle_sides[2])

    print("Sin = %.2f" % results[0])
    print("Cos = %.2f" % results[1])
    print("Tan = %.2f" % results[2])


continue_menu = True


while (continue_menu):
    triangle_sides = enter_triangle()
    pythagoras_size = pythagoras(triangle_sides)
    results = trigonometry_identities(triangle_sides)
    print_identities(results, triangle_sides)
