from numpy.linalg import *
from numpy import *

def rl(x, y):
  N = len(x)
  sx = sum(x)
  sy = sum(y)
  sx2 = sum(x**2)
  sy2 = sum(y**2)
  sxy = sum(x*y)

  d = N * sx2 - sx ** 2
  b = (N * sxy - sx * sy) / d
  a = (sx2 * sy - sx * sxy) / d

  s = sqrt(sum(y - a - b * x) ** 2 / (N - 2))
  sa = s * sqrt(sx2 / d)
  sb = s * sqrt(N / d)

  r = (N * sxy - sx * sy) / sqrt(d * (N * sum(y ** 2) - sy ** 2))

  return [a, b, sa, sb, r]



def rlp(x, y, sy):
    N = len(x)
    w = float(1) / sy ** 2
    sw = sum(w)
    swy = sum(w*y)
    swx2 = sum(w*x**2)
    swx = sum(w*x)
    swxy = sum(w*x*y)

    d = det(array([[sw, swx], [swx, swx2]]))
    a = (swy * swx2 - swx * swxy) / d
    b = (sw * swxy - swx * swy) / d

    sa = sqrt(swx2 / d)
    sb = sqrt(sw / d)

    r = (sw * swxy - swx * swy) / sqrt(d * (sw * sum(w * y ** 2) - swy ** 2))

    return [a, b, sa, sb, r]
