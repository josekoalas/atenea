import random
random.random()
#[Out]# 0.8763212121081146
random.uniform(3,7)
#[Out]# 6.7044946442538595
random.randint(2,5)
#[Out]# 4
random.randrange(2,5,0.5)
random.randrange(2,5,1)
#[Out]# 4
l = list(range(2,15,2)
)
random.choice(l)
#[Out]# 4
random.sample(l,3)
#[Out]# [4, 2, 12]
get_ipython().system('clear ')
import numpy as np
np.random.random()
#[Out]# 0.22542655722629557
np.random.random([2,3])
#[Out]# array([[ 0.52313479,  0.22202441,  0.63614351],
#[Out]#        [ 0.82811067,  0.53084388,  0.41383688]])
#Entre 5 y 10
5 + 5 * np.random.random([2,3])
#[Out]# array([[ 5.49596957,  6.04077998,  5.38100704],
#[Out]#        [ 7.54275256,  5.00150035,  9.73468697]])
#Entero
np.round_(5 + 5 * np.random.random([2,3])
)
#[Out]# array([[  8.,  10.,   7.],
#[Out]#        [ 10.,  10.,   7.]])
np.random.rand(2,3)
#[Out]# array([[ 0.08090203,  0.16623449,  0.30152101],
#[Out]#        [ 0.79613928,  0.33474163,  0.03720274]])
np.random.permutation([1,2,3,4,5,6,7,8,9,0])
#[Out]# array([6, 5, 3, 7, 8, 0, 1, 4, 2, 9])
np.random.shuffle([1,2,3,4,5,6,7,8,9,0])
get_ipython().system('clear ')
import matplotlib as plt
import pylab #Version interactiva
pylab
#[Out]# <module 'pylab' from '/usr/lib/python3/dist-packages/pylab.py'>
#Simplemente carga matplotlib y numpy ? (Creo)
x = np.linspace(-np.pi, np.pi, 20)
x
#[Out]# array([-3.14159265, -2.81089869, -2.48020473, -2.14951076, -1.8188168 ,
#[Out]#        -1.48812284, -1.15742887, -0.82673491, -0.49604095, -0.16534698,
#[Out]#         0.16534698,  0.49604095,  0.82673491,  1.15742887,  1.48812284,
#[Out]#         1.8188168 ,  2.14951076,  2.48020473,  2.81089869,  3.14159265])
y = np.sin(x)
y
#[Out]# array([ -1.22464680e-16,  -3.24699469e-01,  -6.14212713e-01,
#[Out]#         -8.37166478e-01,  -9.69400266e-01,  -9.96584493e-01,
#[Out]#         -9.15773327e-01,  -7.35723911e-01,  -4.75947393e-01,
#[Out]#         -1.64594590e-01,   1.64594590e-01,   4.75947393e-01,
#[Out]#          7.35723911e-01,   9.15773327e-01,   9.96584493e-01,
#[Out]#          9.69400266e-01,   8.37166478e-01,   6.14212713e-01,
#[Out]#          3.24699469e-01,   1.22464680e-16])
plt.plot(x, y)
plot(x, y)
pylab.plot(x, y)
#[Out]# [<matplotlib.lines.Line2D at 0xb44c6a2c>]
pylab.show(False)
pylab.grid(True)
pylab.show(True)
import numpy as np
quit()
import numpy as np
import matplotlib as plt
x = linspace(-pi, pi, 30)
y = sin(x)
plot(x,y)
#[Out]# [<matplotlib.lines.Line2D at 0xb30f26ec>]
grid(True)
x = linspace(-2*pi, 2*pi, 60)
plot(x,y)
x = linspace(-2*pi, 2*pi, 60)
y = sin(x)
plot(x,y)
#[Out]# [<matplotlib.lines.Line2D at 0xb2a5ca0c>]
clf()
plot(x, y, 'rv:')
#[Out]# [<matplotlib.lines.Line2D at 0xb28ba14c>]
clf()
plot(x,y, 'ro--')
#[Out]# [<matplotlib.lines.Line2D at 0xb2a9ba2c>]
y2 = cos(x)
plot(x, y2, 'b*-'
)
#[Out]# [<matplotlib.lines.Line2D at 0xb2a6f68c>]
clf()
plot(x, y, color='red', linestyle=':', linewidth='5')
#[Out]# [<matplotlib.lines.Line2D at 0xb28f548c>]
clf()
plot(x, y, color='red', linestyle=':', linewidth='5')
#[Out]# [<matplotlib.lines.Line2D at 0xb28bb34c>]
x.min()
#[Out]# -6.2831853071795862
x.max()
#[Out]# 6.2831853071795862
xlim(x.min(), x.max())
#[Out]# (-6.2831853071795862, 6.2831853071795862)
ylim(-2,2)
#[Out]# (-2, 2)
xticks([-pi, -pi/2, 0, pi/2, pi])
#[Out]# ([<matplotlib.axis.XTick at 0xb2b1adcc>,
#[Out]#   <matplotlib.axis.XTick at 0xb28f57cc>,
#[Out]#   <matplotlib.axis.XTick at 0xb2a5d42c>,
#[Out]#   <matplotlib.axis.XTick at 0xb30d7f2c>,
#[Out]#   <matplotlib.axis.XTick at 0xb310534c>],
#[Out]#  <a list of 5 Text xticklabel objects>)
xticks([2*-pi, -pi, 0, pi, 2*pi])
#[Out]# ([<matplotlib.axis.XTick at 0xb2b1adcc>,
#[Out]#   <matplotlib.axis.XTick at 0xb28f57cc>,
#[Out]#   <matplotlib.axis.XTick at 0xb2a5d42c>,
#[Out]#   <matplotlib.axis.XTick at 0xb30d7f2c>,
#[Out]#   <matplotlib.axis.XTick at 0xb310534c>],
#[Out]#  <a list of 5 Text xticklabel objects>)
yticks([-1, 0, 1])
#[Out]# ([<matplotlib.axis.YTick at 0xb2ae95cc>,
#[Out]#   <matplotlib.axis.YTick at 0xb2ae76ec>,
#[Out]#   <matplotlib.axis.YTick at 0xb30d7fcc>],
#[Out]#  <a list of 3 Text yticklabel objects>)
grid(True)
xticks([2*-pi, -pi, 0, pi, 2*pi], ["])
xticks([2*-pi, -pi, 0, pi, 2*pi], ["-2Pi", "-Pi", "0", "Pi", "2Pi"])
#[Out]# ([<matplotlib.axis.XTick at 0xb2b1adcc>,
#[Out]#   <matplotlib.axis.XTick at 0xb28f57cc>,
#[Out]#   <matplotlib.axis.XTick at 0xb2a5d42c>,
#[Out]#   <matplotlib.axis.XTick at 0xb30d7f2c>,
#[Out]#   <matplotlib.axis.XTick at 0xb310534c>],
#[Out]#  <a list of 5 Text xticklabel objects>)
xticks([2*-pi, -pi, 0, pi, 2*pi], ["$-2\p$i", "-Pi", "0", "Pi", "2Pi"])
#[Out]# ([<matplotlib.axis.XTick at 0xb2b1adcc>,
#[Out]#   <matplotlib.axis.XTick at 0xb28f57cc>,
#[Out]#   <matplotlib.axis.XTick at 0xb2a5d42c>,
#[Out]#   <matplotlib.axis.XTick at 0xb30d7f2c>,
#[Out]#   <matplotlib.axis.XTick at 0xb310534c>],
#[Out]#  <a list of 5 Text xticklabel objects>)
xticks([2*-pi, -pi, 0, pi, 2*pi], ["$-2\pi", "-Pi", "0", "Pi", "2Pi"])
#[Out]# ([<matplotlib.axis.XTick at 0xb2b1adcc>,
#[Out]#   <matplotlib.axis.XTick at 0xb28f57cc>,
#[Out]#   <matplotlib.axis.XTick at 0xb2a5d42c>,
#[Out]#   <matplotlib.axis.XTick at 0xb30d7f2c>,
#[Out]#   <matplotlib.axis.XTick at 0xb310534c>],
#[Out]#  <a list of 5 Text xticklabel objects>)
xticks([2*-pi, -pi, 0, pi, 2*pi], ["$-2\pi$", "$-\pi$", "0", "Pi", "2Pi"])
#[Out]# ([<matplotlib.axis.XTick at 0xb2b1adcc>,
#[Out]#   <matplotlib.axis.XTick at 0xb28f57cc>,
#[Out]#   <matplotlib.axis.XTick at 0xb2a5d42c>,
#[Out]#   <matplotlib.axis.XTick at 0xb30d7f2c>,
#[Out]#   <matplotlib.axis.XTick at 0xb310534c>],
#[Out]#  <a list of 5 Text xticklabel objects>)
xticks([2*-pi, -pi, 0, pi, 2*pi], ["$-2\pi$", "$-\pi$", "0", "Pi", "2Pi"])
#[Out]# ([<matplotlib.axis.XTick at 0xb2b1adcc>,
#[Out]#   <matplotlib.axis.XTick at 0xb28f57cc>,
#[Out]#   <matplotlib.axis.XTick at 0xb2a5d42c>,
#[Out]#   <matplotlib.axis.XTick at 0xb30d7f2c>,
#[Out]#   <matplotlib.axis.XTick at 0xb310534c>],
#[Out]#  <a list of 5 Text xticklabel objects>)
clf()
get_ipython().system('clear ')
plot(x,y, 'bo--', label='cos(x))
plot(x,y, 'bo--', label='cos(x)')
#[Out]# [<matplotlib.lines.Line2D at 0xb304442c>]
plot(x,y2, 'gD-', label='sin(x)')
#[Out]# [<matplotlib.lines.Line2D at 0xb303e66c>]
legend()
#[Out]# <matplotlib.legend.Legend at 0xb2908b8c>
ylim(-2, 2)
#[Out]# (-2, 2)
grid(true)
grid(True)
