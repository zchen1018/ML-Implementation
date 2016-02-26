The Tree Augmented Network (TAN) algorithm

1. compute weight I(Xi, Xj| Y) for each possible edge
(Xi, Xj) between features
2. find maximum weight spanning tree (MST) for graph
over X1 … Xn by Prim's algorithm
3. assign edge directions in MST
4. construct a TAN model by adding node for Y and an
edge from Y to each Xi