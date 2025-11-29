#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

struct Point {
    double x, y;
};

// Cross product
double cross(const Point& O, const Point& A, const Point& B) {
    return (A.x - O.x) * (B.y - O.y) - (A.y - O.y) * (B.x - O.x);
}

// Distance (for sorting collinear points)
double dist(const Point& a, const Point& b) {
    return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}

vector<Point> grahamScan(vector<Point>& points) {
    int n = points.size();
    if (n < 3) return points;

    // 1. Find the lowest point
    swap(points[0], *min_element(points.begin(), points.end(), [](const Point& a, const Point& b) {
        return (a.y < b.y) || (a.y == b.y && a.x < b.x);
    }));
    Point pivot = points[0];

    // 2. Sort by polar angle w.r.t pivot
    sort(points.begin() + 1, points.end(), [pivot](const Point& a, const Point& b) {
        double c = cross(pivot, a, b);
        if (c == 0)
            return dist(pivot, a) < dist(pivot, b);
        return c > 0;
    });

    // 3. Build the hull
    vector<Point> hull = { points[0], points[1] };
    for (int i = 2; i < n; i++) {
        while (hull.size() > 1 && cross(hull[hull.size() - 2], hull.back(), points[i]) <= 0)
            hull.pop_back();
        hull.push_back(points[i]);
    }

    return hull;
}

int main() {
    int n;
    cout << "Enter number of points: ";
    cin >> n;

    vector<Point> points(n);
    cout << "Enter points (x y):\n";

    for (int i = 0; i < n; i++) {
        cin >> points[i].x >> points[i].y;
    }

    vector<Point> hull = grahamScan(points);

    cout << "\nConvex Hull Points:\n";
    for (auto& p : hull) {
        cout << "(" << p.x << ", " << p.y << ")\n";
    }
    return 0;
}
