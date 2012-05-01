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

This project is a loose port of the Spatial Econometrics for Matlab by James P. LeSage?.

spatial-econometrics but for Python not Matlab. The port is based on the matrix and vector datatypes in NumPy?, so you will need NumPy? to use these tools. Extensive documentation on NumPy? can be found here: numpy .
Also if you are new to NumPy? but famaliar with Matlab, this page may be helpful. http://www.scipy.org/NumPy_for_Matlab_Users

You can browse the source here: http://code.google.com/p/pyconometrics/source/browse/trunk/src/

This code is listed by module, however it is most convenient have all the functions listed in one module, when the library becomes larger it may help to bundle everything in a package instead of one module. One file can be accessed here: http://code.google.com/p/pyconometrics/source/browse/trunk/pyconometrics.py

The code currently has tested with Python 2.6, 2.7 ad 3.X support are coming as these have better floating point performance.

The performance of this code is slower than Matlab.
