import parenthesisclosure
import matplotlib.pyplot as plt


# a = parenthesisclosure.NodeTree(0)
#
# print(a.closure_probability() * 100)

depths = []
probabilities = []

# differences = []

max_depth = 22

closure = 0
# previous_closure = 0

for i in range(0, max_depth, 2):
    depths.append(i)
    a = parenthesisclosure.NodeTree(i)
    # previous_closure = closure
    closure = a.closure_probability() * 100

    # differences.append(closure - previous_closure)
    # print(closure - previous_closure)
    probabilities.append(closure)

plt.plot(depths, probabilities)
plt.axis([0, max_depth, 0, 100])
# plt.plot(differences)
plt.show()
