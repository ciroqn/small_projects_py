# Visualing Data w/ matplotlib

To make use of matplotlib, it is imported.

The example below shows how a simple plot can be made using `days` as the x-values and `money_spent` as the y-values. The `plt.show()` is included to actually show the graph.

```py
days = [0, 1, 2, 3, 4, 5, 6]
money_spent = [10, 12, 12, 10, 14, 22, 24]

plt.plot(days, money_spent)

plt.show()
```

And showing two lines on the *same* plot requires specifying two `plt.plot(...)` commands like so:

```py
from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

# plot two lines on same plot
plt.plot(time, revenue)
plt.plot(time, costs)

plt.show()
```

## Styling

```py
# Line colours (either specify using words or HEX code) ------------------------------------
plt.plot(days, money_spent, color='blue')
plt.plot(days, money_spent_2, color='#AAAFHUS')

# Line styling ------------------------------------
# Dashed:
plt.plot(x_values, y_values, linestyle='--')
# Dotted:
plt.plot(x_values, y_values, linestyle=':')
# No line:
plt.plot(x_values, y_values, linestyle='')

# Marker styling ------------------------------------
# A circle:
plt.plot(x_values, y_values, marker='o')
# A square:
plt.plot(x_values, y_values, marker='s')
# A star:
plt.plot(x_values, y_values, marker='*')
```

An example:

```py
lt.plot(time, revenue, color="purple", linestyle='--')
plt.plot(time, costs, color="#82edc9", marker='s')

plt.show()
```
