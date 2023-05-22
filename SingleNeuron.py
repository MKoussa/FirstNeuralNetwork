width = 4
inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

i = 0
output = 0
while i < width:
    output += inputs[i] * weights[i]
    i += 1

print(output + bias)
