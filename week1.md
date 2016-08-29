Michael Muehlbradt  
mimu0324  
mimu0324@colorado.edu  
Week 1  
  
Exercise 2.2: For an _N x N_ symmetric adjacency matrix A, describe an algorithm to find the connected components.  
  
We start by initializing an empty array. For each row in the adjacency matrix we find the connected components, and iterate over the array to find a match. If no match is found we append the connected components. If we do find a match we take the union of matches from the array and the row in the adjacency matrix. We then remove components that matched (to prevent duplicates) and append the connected components from the union to the array. This should leave us with an array of connected components.

