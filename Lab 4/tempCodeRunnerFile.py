theta = [i * 0.01 for i in range(int(2 * math.pi / 0.01))]
    x = [a * math.cos(t) + centerX for t in theta]
    y = [b * math.sin(t) + centerY for t in theta]