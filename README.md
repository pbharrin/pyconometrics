pyconometrics
=============

Python Econometrics toolbox, requires NumPy

Install:
>sudo python setup.py install

This is a collection of Python Econometrics functions.

least squares
cointegration testing
difference operator
detrending
A number of utility functions as well.
----

This project is a loose port of the Spatial Econometrics for Matlab by James P. LeSage's spatial-econometrics but for Python not Matlab. The port is based on the matrix and vector datatypes in NumPy?, so you will need NumPy? to use these tools. Extensive documentation on NumPy? can be found here: numpy .
Also if you are new to NumPy? but famaliar with Matlab, this page may be helpful. http://www.scipy.org/NumPy_for_Matlab_Users

The code currently has tested with Python 2.6, and 2.7 with Numpy 1.6.0.   

The performance of this code is slower than Matlab.

example:
```python
>>> from pyconometrics import *
>>> from numpy import *
>>> x = matrix(random.random(9))
>>> y = matrix(random.random(9))
>>> cadf(x.H, y.H, 0, 1)
{'adf': -4.7107624192958664, 'alpha': -0.84577780823522175, 'nlag': 1, 'crit': matrix([[-4.02456, -3.40397, -3.08903, -0.99877, -0.63826,  0.09294]]), 'nvar': 1}
```
