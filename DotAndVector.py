a = [1, 2, 3]
b = [2, 3, 4]

i = 0
dot_product = 0
while i < len(a):
    dot_product += a[i] * b[i]
    i += 1

print(dot_product)
dot_product = 0
#Doing a zip(), for fun'n'knowledge
for a_vector, b_vector in zip(a, b):
    dot_product += a_vector * b_vector

print(dot_product)