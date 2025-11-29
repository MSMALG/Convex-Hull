import math
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def cross(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

def dist(a, b):
    return (a.x - b.x)**2 + (a.y - b.y)**2


def graham_scan(points):
    n = len(points)
    if n < 3:
        return points

    #Find lowest point (pivot)
    points.sort(key=lambda p: (p.y, p.x))
    pivot = points[0]

    #Sort by polar angle around pivot
    points = [pivot] + sorted(points[1:], key=lambda p: (
        math.atan2(p.y - pivot.y, p.x - pivot.x), dist(p, pivot)
    ))

    #Build hull
    hull = [points[0], points[1]]
    for i in range(2, n):
        while len(hull) > 1 and cross(hull[-2], hull[-1], points[i]) <= 0:
            hull.pop()
        hull.append(points[i])

    return hull


def hull_edges(hull):
    edges = []
    for i in range(len(hull)):
        edges.append((hull[i], hull[(i+1) % len(hull)]))  
    return edges


def visualize(points, edges):
    # plot all points
    xs = [p.x for p in points]
    ys = [p.y for p in points]
    plt.scatter(xs, ys, label="Points")

    for e in edges:
        plt.plot([e[0].x, e[1].x], [e[0].y, e[1].y], 'r-')  

    plt.title("Graham Scan Convex Hull")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.show()

if __name__ == "__main__":
    n = int(input("Enter number of points: "))

    points = []
    print("Enter points (x y):")
    for _ in range(n):
        x, y = map(float, input().split())
        points.append(Point(x, y))

    hull = graham_scan(points)
    edges = hull_edges(hull)

    print("\nConvex Hull Edges (Graham Scan):")
    for e in edges:
        print(f"({e[0].x}, {e[0].y}) -> ({e[1].x}, {e[1].y})")

    visualize(points, edges)
