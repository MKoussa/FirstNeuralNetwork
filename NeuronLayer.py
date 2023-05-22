inputs = [1.0, 2.0, 3.0, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
bias = [2.0, 3.0, 0.5]

#Whipped this up. Very C# of me I think
k = 0
output = []
while k < len(weights):
    math = 0
    i = 0
    while i < len(inputs):
        math += inputs[i] * weights[k][i]
        i += 1
    output.append(math + bias[k])
    k += 1

#Books method (zip() looks cool)
layer_outputs = []

for neuron_weights, neuron_bias in zip(weights, bias):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input * weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(output)
print(layer_outputs)