"""


Given n points on a 2D plane where points[i] = [xi, yi],
 Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending
infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are
 not considered included in the area.

 Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.



Example 2:

Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3


"""
from isort.wrap_modes import vertical


def width(list1 : list[list[int]]):

    vertical  = sorted([x[0] for x in list1])
    x  = 0

    for index, y in enumerate(vertical):

        if index == len(vertical) - 1:
             return x

        elif vertical[index + 1] - vertical[index] > x:
             x = vertical[index + 1] - vertical[index]



print(width([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
