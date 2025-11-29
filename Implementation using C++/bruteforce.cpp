#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

struct Point {
    double x, y;
};

double sideValue(const Point& a, const Point& b, const Point& c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

vector<pair<Point, Point>> BruteForceConvexHull(const vector<Point>& points) {
    int n = points.size();
    vector<pair<Point, Point>> edges;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            bool allLeft = true, allRight = true;
            for (int k = 0; k < n; k++) {
                if (k == i || k == j) continue;
                double s = sideValue(points[i], points[j], points[k]);
                if (s < 0) allLeft = false;
                if (s > 0) allRight = false;
                if (!allLeft && !allRight) break;
            }
            if (allLeft || allRight)  
                edges.push_back({points[i], points[j]});
        }
    }
    return edges;
}

int main() {
    int n;
    cout << "Enter number of points: ";
    cin >> n;

    vector<Point> points(n);
    cout << "Enter the points (x y):\n";
    for (int i = 0; i < n; i++)
        cin >> points[i].x >> points[i].y;

    auto hullEdges = BruteForceConvexHull(points);

    cout << "\nConvex Hull Edges (Brute Force):\n";
    for (auto& e : hullEdges)
        cout << "(" << e.first.x << ", " << e.first.y << ") -> ("
             << e.second.x << ", " << e.second.y << ")\n";

    return 0; 
}
