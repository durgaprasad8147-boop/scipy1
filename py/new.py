#  this is my first scipy code
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).data)

from scipy import constants
print(constants.pi)
# #SciPy Tutorial
# .sciPy is a scientific computation library that uses NumPy underneath.
# .SciPy is a scientific computation library that uses NumPy underneath.
# .It provides more utility functions for optimization, stats and signal processing.
# .SciPy was created by NumPy's creator Travis Olliphant.
# #Scipy intallation
# .C:\Users\Your Name>pip install scipy

# #Import SciPy
# .from scipy import "module"
# . from scipy import "constants"

# #SciPy Constants
# .As SciPy is more focused on scientific implementations, it provides many built-in scientific constants.These constants can be helpful when you are working with Data Science.
# #Constant Units:
# A list of all units under the constants module 
# Example:
from scipy import constants

print(constants.pi)
#
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).data)

# Unit Categories
"""The units are placed under these categories:

.Metric
.Binary
.Mass
.Angle
.Time
.Length
.Pressure
.Volume
.Speed
.Temperature
.Energy
.Power
.Force"""

"""" #Metric (SI) Prefixes:
*Return the specified unit in meter (e.g. centi returns 0.01)
Example:
from scipy import constants

print(constants.yotta)    #1e+24
print(constants.zetta)    #1e+21
print(constants.exa)      #1e+18
print(constants.peta)     #1000000000000000.0
print(constants.tera)     #1000000000000.0
print(constants.giga)     #1000000000.0

# #Binary Prefixes:
*Return the specified unit in bytes (e.g. kibi returns 1024)
Example:
from scipy import constants

print(constants.kibi)    #1024
print(constants.mebi)    #1048576
print(constants.gibi)    #1073741824
print(constants.tebi)    #1099511627776
print(constants.pebi)    #1125899906842624
print(constants.exbi)    #1152921504606846976
print(constants.zebi)    #1180591620717411303424
print(constants.yobi)    #1208925819614629174706176


# #Mass Units:
*Return the specified unit in kilograms (e.g. gram returns 0.001)
Example:
from scipy import constants
print(constants.gram)    #0.001
print(constants.kilogram)    #1.0


# #Angle Units:
*Return the specified unit in radians (e.g. degree returns 0.017453292
Example:
from scipy import constants
print(constants.degree)    #0.017453292519943295
print(constants.radian)    #1.0
print(constants.arcmin)    #0.0002908882086657216
print(constants.arcsec)    #4.84813681109536e-06

# #Time Units:
*Return the specified unit in seconds (e.g. minute returns 60)
Example:
from scipy import constants
print(constants.minute)    #60.0
print(constants.hour)    #3600.0
print(constants.day)    #86400.0


# #Length Units:
*Return the specified unit in meters (e.g. inch returns 0.0254)
Example:
from scipy import constants
print(constants.inch)    #0.0254
print(constants.feet)    #0.3048
print(constants.yard)    #0.9144
print(constants.mile)    #1609.344

# #Pressure Units:
*Return the specified unit in pascals (e.g. atmosphere returns 101325)

Example:
from scipy import constants
print(constants.atmosphere)    #101325.0
print(constants.bar)    #100000.0
print(constants.torr)    #133.32236842105263


# #Volume Units:
*Return the specified unit in cubic meters (e.g. liter returns 0.001)

Example:
from scipy import constants
print(constants.liter)    #0.001
print(constants.gallon)    #0.003785411784
print(constants.fluid_ounce)    #2.95735295625e-05

# #Speed Units:
*Return the specified unit in meters per second (e.g. knot returns 0.514
Example:
from scipy import constants
print(constants.knot)    #0.5144444444444445


# #Temperature Units:
*Return the specified unit in kelvin (e.g. celsius returns 273.15
Example:
from scipy import constants
print(constants.celsius)    #273.15
print(constants.fahrenheit)    #255.37222222222223

# #Energy Units:
*Return the specified unit in joules (e.g. calorie returns 4.184)

Example:
from scipy import constants
print(constants.calorie)    #4.184
print(constants.electron_volt)    #1.602176634e-19

# #Power Units:
*Return the specified unit in watts (e.g. horsepower returns 745.699871582

Example:
from scipy import constants
print(constants.horsepower)    #745.6998715822701

# #Force Units:
*Return the specified unit in newtons (e.g. dyne returns 1e-05)

Example:
from scipy import constants
print(constants.dyne)    #1e-05
print(constants.pound_force)    #4.4482216152605"""


# #SciPy Optimization
# SciPy provides a module called optimize to perform optimization tasks.
# It provides several optimization algorithms to minimize or maximize objective functions.
# The optimize module can be used for linear programming, nonlinear programming, and curve fitting.

# #Minimizing a Function:
# function, in this context, represents a curve, curves have high points and low points.
# High points are called maxima.
# Low points are called minima.

# #SciPy Sparse Data:
# Sparse data is data that has mostly unused elements (elements that don't carry any information ).
# It can be an array like this one:

# Example:[1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0]

# .Sparse Data: is a data set where most of the item values are zero.
# .Dense Array: is the opposite of a sparse array: most of the values are not zero.

# SciPy has a module, scipy.sparse that provides functions to deal with sparse data.
# There are primarily two types of sparse matrices that we use:
# CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.
# CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products
# We will use the CSR matrix in this tutorial.

# #CSR Matrix
# We can create CSR matrix by passing an arrray into function scipy.sparse.csr_matrix().

#Create a CSR matrix from an array:
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

print(csr_matrix(arr))

# #Sparse Matrix Methods:
# .Viewing stored "data (not the zero items)" with the data property:
# .Counting nonzeros with the "count_nonzero()" method:
# .Removing zero-entries from the matrix with the "eliminate_zeros()" method:
# .Eliminating duplicate entries with the "sum_duplicates()" method:
# .Converting from csr to csc with the tocsc() method:

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).data)
print(csr_matrix(arr).count_nonzero())
print(csr_matrix(arr).eliminate_zeros())
print(csr_matrix(arr).sum_duplicates())
print(csr_matrix(arr).tocsc())
print(csr_matrix(arr).todense())
print(csr_matrix(arr).toarray())
print(csr_matrix(arr).transpose())
print(csr_matrix(arr).getrow(1))
print(csr_matrix(arr).getcol(2))
print(csr_matrix(arr).reshape(1, 9))



# SciPy Graphs:
# .Graphs are an essential data structure.
# .SciPy provides us with the module scipy.sparse.csgraph for working with such data structures.

# #Adjacency Matrix:
# .Adjacency matrix is a nxn matrix where n is the number of elements in a graph.
# .And the values represents the connection between the elements.

# Connected Components:
# Find all of the connected components with the "connected_components()" method.

"""import numpy as np
from scipy.sparse.csgraph import
connected_components
from scipy.sparse import csr_matrix

arr = np.array([[0, 1, 0],[1, 0, 1],[0, 1, 0]])
newarr = csr_matrix(arr)
print(connected_components(newarr))"""

# #Dijkstra's Algorithm:
# .Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph

import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(dijkstra(newarr, return_predecessors=True, indices=0))

# #Floyd Warshall:
# Use the floyd_warshall() method to find shortest path between all pairs of elements.

# print(floyd_warshall(newarr, return_predecessors=True, indices=0))


# #Bellman Ford:
# .The bellman_ford() method can also find the shortest path between all pairs of elements, but this method can handle negative weights as well.

import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix

arr = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(bellman_ford(newarr, return_predecessors=True, indices=0))


# #Depth First Order:
# .The depth_first_order() method returns a depth first traversal from a node.

import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(depth_first_order(newarr, 1))

# #Breadth First Order:
# .The breadth_first_order() method returns a breadth first traversal from a node.
import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(breadth_first_order(newarr, 1))


# #SciPy Spatial Data:
# .Spatial data refers to data that is represented in a geometric space.
# .E.g. points on a coordinate system.
# .E.g. finding if a point is inside a boundary or not


# #Triangulation:
# .A Triangulation of a polygon is to divide the polygon into multiple triangles with which we can compute an area of the polygon.
# .One method to generate these triangulations through points is the Delaunay() Triangulation.

import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

plt.show()


# # #Convex Hull:
# .A Convex Hull is the smallest convex polygon that can contain all the points in a given set of points.
# .Use the "ConvexHull()" method to create a Convex Hull.
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')

plt.show()

# #SciPy Interpolation:
# .Interpolation is a method for generating points between given points.
# .For example: for points 1 and 2, we may interpolate and find points 1.33 and 1.66.

# .SciPy provides us with a module called scipy.interpolate which has many functions to deal with interpolation:

# #1D Interpolation:
# .The function interp1d() is used to interpolate a distribution with 1 variable.
# .It takes x and y points and returns a callable function that can be called with new x and returns corresponding y.
#F.or given xs and ys interpolate values from 2.1, 2.2... to 2.9:

from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)


# #SciPy Statistical Significance Tests:
# .In statistics, statistical significance means that the result that was produced has a reason behind it, it was not produced randomly, or by chance.

# .Hypothesis in Statistics:

# .Null Hypothesis:

# .Alternate Hypothesis:

'''Example:

For an assessment of a student we would take:

"student is worse than average" - as a null hypothesis, and:

"student is better than average" - as an alternate hypothesis.'''

# #One tailed test
# .When our hypothesis is testing for one side of the value only, it is called "one tailed test".

'''Example:

For the null hypothesis:

"the mean is equal to k", we can have alternate hypothesis:

"the mean is less than k", or:

"the mean is greater than k"'''

# Two tailed test
# .When our hypothesis is testing for both side of the values.

'''Example:

For the null hypothesis:

"the mean is equal to k", we can have alternate hypothesis:

"the mean is not equal to k"

In this case the mean is less than, or greater than k, and both sides are to be checked.'''

# Alpha value
# .Alpha value is the level of significance.

'''Example:

How close to extremes the data must be for null hypothesis to be rejected.

It is usually taken as 0.01, 0.05, or 0.1.'''


# #P value
# .P value tells how close to extreme the data actually is.

'''P value and alpha values are compared to establish the statistical significance.

If p value <= alpha we reject the null hypothesis and say that the data is statistically significant. otherwise we accept the null hypothesis.'''

