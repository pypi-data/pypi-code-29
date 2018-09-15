from solid import *
from solid.utils import *

def construct_polyhedron(faces):
    points = []
    unique_points = {}

    translated_faces = []
    for face in faces:
        translated_face = []
        for point in face:
            if not isinstance(point, tuple):
                point = tuple(point)
            if point not in unique_points:
                unique_points[point] = len(points)
                points.append(point)
            translated_face.append(unique_points[point])
        translated_faces.append(translated_face)
    return polyhedron(points=points, faces=translated_faces, convexity=10)

def construct_polygon(*paths):
    unique_points = {}
    points_listing = []
    path_indices = []
    for path in paths:
        point_indices = []
        for point in path:
            if point not in unique_points:
                unique_points[point] = len(unique_points)
                points_listing.append(point)
            point_indices.append(unique_points[point])
        path_indices.append(point_indices)
    return polygon(
        points=points_listing,
        paths=path_indices,
    )
