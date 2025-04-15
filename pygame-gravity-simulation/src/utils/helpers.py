def vector_add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def vector_subtract(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])

def vector_magnitude(v):
    return (v[0]**2 + v[1]**2) ** 0.5

def vector_normalize(v):
    magnitude = vector_magnitude(v)
    if magnitude == 0:
        return (0, 0)
    return (v[0] / magnitude, v[1] / magnitude)

def distance(point1, point2):
    return vector_magnitude(vector_subtract(point1, point2))