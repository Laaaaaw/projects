import random

n = 5

times = 10000

m = n*6-n+1
chances = [0] * m

X = [] * m

for i in range(len(chances)):
    X[i] = str(n-1)


def throw(n):
  result = 0
  for i in range(n):
    result += random.randint(1,6)
  chances[result-n] += 1

for i in range(times):
  throw(n)

from bokeh.io import push_notebook, output_notebook, show
from bokeh.plotting import figure
output_notebook()

p = figure(x_range = X, title = 'Throwing dices many times')
p.line(X, chances, line_width = 3, color='blue')


output_notebook()
show(p)