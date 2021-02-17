import statistics

inp = input()
if len(inp) == 0:
    print('No Input!')
else:
    inp = list(map(float, inp.split()))
    print("Summation is", sum(inp))
    print("Maximum is", max(inp))
    print("Minimum is", min(inp))
    print("Arithmetic Mean is", statistics.mean(inp))
    print("Geometric mean is", statistics.geometric_mean(inp))
    print("Harmonic mean is", statistics.harmonic_mean(inp))
    print("Median is", statistics.median(inp))
    print("Low Median is", statistics.median_low(inp))
    print("High median is", statistics.median_high(inp))
    print("Median of the grouped data is", statistics.median(inp))
    print("Single mode is", statistics.mode(inp))
    print("Multiple modes is", statistics.multimode(inp))
