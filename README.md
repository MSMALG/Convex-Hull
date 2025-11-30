# Algorithms Analysis and Design - CS315 Project 
## Convex Hulls
## This project was researched and developed by:
- Muzna Safieldin
- Bedor Alharbi
- Raghad Mesleh  
- Mayar Shihab  
- Malath Alharbi
## Project Details 
### The study of Convex Hulls is a foundational concpet of Geometrical Analysis and other mathematical fields. 
In this project, we discussed how you can find a convex hull "the smallest convex polygon that contains all given points" using two approaches:
- Brute Force
- Graham Scan
We also built a prototype simulation tool using Unity Game Engine. The tool allows users to spawn points with mouse clicks and then
select an algorithm to form a convex hull from the dataset.
### Observations
Our findings confirmed our studies:
- With the increase of points **_Brute Force_** becomes unreliable and slower.
- On the other hand, **_Graham Scan_** proved to be stable, faster and more reliable with generating convex hulls.  
  *In some cases, Brute Force was noticed to be slightly faster when the number of points where very few*.

Try the Simulation Tool here: [Convex Hull Simulator](https://msmalg.github.io/ConvexHullSimulator/)    
**Colours Used in Simulation:**    
Brute Force
| Colour  | 	Representation |
| ------------- | ------------- |
| White Dot    | Input point |
| Red Line | This edge fails → not hull |
| Green Line | This edge passes → hull edge |
| Purple Line | Final convex hull |  

Graham Scan
| Colour  | 	Representation |
| ------------- | ------------- |
|Yellow Dot | Starting pivot point |
| White Dot    | Input point |
|Cyan Line | Polar angle line being tested |
| Red Line | Right turn → reject point |
| Green Line | Left turn → accept point |
| Purple Line | Final convex hull |  

## Refrences 
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms (3rd ed.). MIT Press, Chapter 33, pp. 1030- 1036
- (https://www.geeksforgeeks.org/dsa/convex-hull-using-graham-scan/)
- (https://www.geeksforgeeks.org/dsa/convex-hull-algorithm/)
- (https://semisignal.com/brute-force-convex-hull-construction/)
- (https://www.cs.jhu.edu/~misha/Fall05/09.13.05.pdf)
- (https://www.cs.ucr.edu/~eldawy/19SCS133/slides/CS133-04-ConvexHull.pdf)




