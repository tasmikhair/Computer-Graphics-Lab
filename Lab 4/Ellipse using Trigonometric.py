import math
import matplotlib.pyplot as plt

def drawEllipse(a, b, centerX, centerY):
    theta = [i * 0.01 for i in range(int(2 * math.pi / 0.01))]
    x = [a * math.cos(t) + centerX for t in theta]
    y = [b * math.sin(t) + centerY for t in theta]
    
    plt.figure()
    plt.plot(x, y, color='purple', linewidth=2)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Ellipse')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Define parameters of the ellipse
centerX = 332  # X-coordinate of the center
centerY = 132  # Y-coordinate of the center
a = 132        # Horizontal radius
b = 62         # Vertical radius

# Call the drawEllipse function with the parameters
drawEllipse(a, b, centerX, centerY)