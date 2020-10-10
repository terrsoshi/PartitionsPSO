# PartitionsPSO
Achieve maximum number of partitions in a given area using Particle Swarm Optimisation

## Running the algorithm
Put all .py files in the same directory, and run main.py using a Python IDE.
It is recommended to run this algorithm on Python IDEs that supports the integration of matplotlib such as Spyder.

## Problem Description
In this problem, we are required to split an area into partitions with identical dimensions such that the maximum number of partitions can be achieved in the given area by applying the Particle Swarm Optimization (PSO) algorith. The problem lies within the constraints set. For instance, the minimum value of m and n is predetermined and the values of x and y are fixed. Therefore, by applying the Particle Swarm Optimization (PSO) algorithm to this problem, we would be able to find the maximum number of identical partitions that the box can be split into as well as the best partition size (m & n) that gives us this result.

## Problem Formulation
x = 9, y = 3
minimum m = 2/5x. minimum n = 2/11y

To formulate this problem, we have set the area dimensions as x = 9 and y =3. In addition, the minimum values of m and n which represents the partitions' size are determined as 2/5x and 2/11y respectively. These variables can be edited to formulate a similar problem with different area sizes and minimum partition sizes.

The codes are split into 3 files: main.py, particle.py, and functions.py for better readability.

## Built On/With
Built On - Python
Built With - Spyder
