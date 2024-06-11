import matplotlib.pyplot as plt 
import numpy as np

def plot_triangles(triangle1, triangle2, title):
    """Plot two triangles."""
    plt.figure()  # new figure create
    triangle1.append(triangle1[0])  # Connect last point to the first
    xs1, ys1 = zip(*triangle1)  # Extract x and y coordinates
    plt.plot(xs1, ys1, 'bo-', label='Original Triangle')  # Plot triangle1
    
    triangle2.append(triangle2[0])
    xs2, ys2 = zip(*triangle2)
    plt.plot(xs2, ys2, 'ro-', label='Transformed Triangle')  # Plot triangle2

    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True) # Add a grid
    plt.axis('equal') # aspect ratio equally set
    plt.legend()
    plt.show()

def translate(triangle, tx, ty):
    """Translate a triangle by (tx, ty)."""
    translated_triangle = [(point[0] + tx, point[1] + ty) for point in triangle]  # Translate each point by (tx, ty)
    return translated_triangle

def scale(triangle, sx, sy):
    """Scale a triangle by (sx, sy) factors."""
    scaled_triangle = [(point[0] * sx, point[1] * sy) for point in triangle]  # Scale each point by (sx, sy)
    return scaled_triangle

def rotate(triangle, angle):
    """Rotate a triangle by a given angle in degrees."""
    angle_rad = np.radians(angle)  # Convert angle to radians
    rotation_matrix = np.array([[np.cos(angle_rad), -np.sin(angle_rad)],  # Create a rotation matrix
                                [np.sin(angle_rad), np.cos(angle_rad)]])
    rotated_triangle = [(np.dot(rotation_matrix, np.array(point))) for point in triangle]  # Rotate each point by mul
    return rotated_triangle

#the vertices of the triangle
triangle = [(0, 0), (1, 0), (0.5, 1)]

# Translation
tx, ty = 1, 1  # Translation factors
translated_triangle = translate(triangle, tx, ty)

# Scaling
sx, sy = 2, 2  # Scaling factors
scaled_triangle = scale(triangle, sx, sy)

# Rotation
angle = 45  # Rotation angle
rotated_triangle = rotate(triangle, angle)

# Plot original and transformed triangles together
plot_triangles(triangle, translated_triangle, 'Original and Transformed Triangle (Translation)')
plot_triangles(triangle, scaled_triangle, 'Original and Transformed Triangle (Scaling)')
plot_triangles(triangle, rotated_triangle, 'Original and Transformed Triangle (Rotation)')