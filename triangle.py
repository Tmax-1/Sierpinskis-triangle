import random
from math import sqrt
import matplotlib.pyplot as plt

def get_dimentions(side_length):
    p1 = (0, 0)
    p2 = (side_length, 0)
    p3 = (side_length/2, sqrt(3)*side_length/2)
    return p1, p2, p3


def start_point_in_triangle(vertices):
    (x1, y1), (x2, y2), (x3, y3) = vertices
    r1 = random.random()
    r2 = random.random()
    
    if r1 + r2 > 1:
        r1 = 1 - r1
        r2 = 1 - r2
    
    x = x1 + r1 * (x2 - x1) + r2 * (x3 - x1)
    y = y1 + r1 * (y2 - y1) + r2 * (y3 - y1)
    
    return (x, y)


def generate_random_points(vertices, num_points, start_point):
    (x1, y1), (x2, y2), (x3, y3) = vertices
    points = []
    current_point = start_point
    for _ in range(num_points):
        chosen_vertex = random.choice([ (x1, y1), (x2, y2), (x3, y3) ])
        current_point = ((current_point[0] + chosen_vertex[0]) / 2,
                         (current_point[1] + chosen_vertex[1]) / 2)
        points.append(current_point)
    return points

def plot_triangle_and_points(vertices, points):
    (x1, y1), (x2, y2), (x3, y3) = vertices
    triangle_x = [x1, x2, x3, x1]
    triangle_y = [y1, y2, y3, y1]
    plt.plot(triangle_x, triangle_y, 'b-')
    plt.scatter(*zip(*points), s=1, color='red')
    plt.axis('equal')
    plt.title("Sirpinski Triangle")
    #plt.scatter([side_length/2], [1.5], color='green', s=30, label='Special Point')
    plt.legend()
    plt.show()

    return

    

side_length = float(5.0)
num_points = 100
start_point = (0, 0)


side_length = float(input("Enter the side length of the equalateral triangle: "))
vertices = get_dimentions(side_length)
start_point = start_point_in_triangle(vertices)
#print(f"Vertices of the triangle: {vertices}")
#print(f"Random starting point inside the triangle: {start_point}")
num_points = int(input("Enter the number of random points to generate: "))
points = generate_random_points(vertices, num_points, start_point)
#print(f"Generated random points inside the triangle; {points}")
plot_triangle_and_points(vertices, points)



