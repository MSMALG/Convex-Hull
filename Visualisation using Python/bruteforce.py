import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#side value function to determine the orientation
def side_value(a, b, c):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)


def brute_force_convex_hull(points):
    n = len(points)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):

            all_left = True
            all_right = True

            for k in range(n):
                if k == i or k == j:
                    continue

                s = side_value(points[i], points[j], points[k])

                if s < 0:
                    all_left = False
                if s > 0:
                    all_right = False

            if all_left or all_right:
                edges.append((points[i], points[j]))

    return edges


def visualize(points, edges):
    # Plot all points
    xs = [p.x for p in points]
    ys = [p.y for p in points]
    plt.scatter(xs, ys, label="Points")

    # Plot convex hull edges
    for a, b in edges:
        plt.plot([a.x, b.x], [a.y, b.y])

    plt.title("Brute Force Convex Hull")
    plt.xlabel("X")
    plt.ylabel("Y")
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

    edges = brute_force_convex_hull(points)

    print("\nConvex Hull Edges (Brute Force):")
    for a, b in edges:
        print(f"({a.x}, {a.y}) -> ({b.x}, {b.y})")

    visualize(points, edges)
