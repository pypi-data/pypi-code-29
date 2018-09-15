from solid_toolbox.units import Point2d

_pascal_triangle = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
]

def inclusive_range(start, end):
    return range(start, end + 1)

def binomial(n, k):
    # Expand cache
    while n >= len(_pascal_triangle):
        s = len(_pascal_triangle)
        prev_row = _pascal_triangle[s - 1]
        next_row = [0 for _ in range(s + 1)]
        next_row[0] = 1
        for i in range(1, s):
            next_row[i] = prev_row[i - 1] + prev_row[i]
        next_row[s] = 1
        _pascal_triangle.append(next_row)
    return _pascal_triangle[n][k]

def bezier_curve(control_points, num_samples):
    def bezier(t):
        x_final = 0
        y_final = 0
        n = len(control_points) - 1
        for k, point in enumerate(control_points):
            fraction = binomial(n, k) * (1 - t)**(n - k) * t**k
            x_final += point.x * fraction
            y_final += point.y * fraction
        return Point2d(x_final, y_final)
    return [bezier(i / (num_samples - 1)) for i in range(num_samples)]
