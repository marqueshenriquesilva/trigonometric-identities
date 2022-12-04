"""
Given the values of the adjacent side, opposite side and hypotenuse of a right triangle,
this application prints the values of its sine, cosine and tangent
Created by Marques Henrique Silva
"""


def trigonometry_relations(adjacent, opposite, hypotenuse):
    sin = (opposite/hypotenuse)
    cos = (adjacent/hypotenuse)
    tan = (opposite/adjacent)
    results = (sin, cos, tan)
    return results


def print_relations(results):
    print("Sin = %.2f" % results[0])
    print("Cos = %.2f" % results[1])
    print("Tan = %.2f" % results[2])


while (True):
    adjacent = int(input("Adjacent: "))
    opposite = int(input("Opposite: "))
    hypotenuse = int(input("Hypotenuse: "))

    results = trigonometry_relations(adjacent, opposite, hypotenuse)

    print_relations(results)
