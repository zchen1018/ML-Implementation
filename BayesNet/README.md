Naive Bayes is assuming conditional independence among features $X_i$ given $Y$, a simplified case of Bayesian Networks.

The Tree Augmented Network (TAN) algorithm

1. compute weight I(Xi, Xj| Y) for each possible edge
(Xi, Xj) between features
2. find maximum weight spanning tree (MST) for graph
over X1 … Xn by Prim's algorithm
3. assign edge directions in MST
4. construct a TAN model by adding node for Y and an
edge from Y to each Xi

Assignment Page: http://pages.cs.wisc.edu/~dpage/cs760/nb_tan.html

This implementation assumes data files are in the [ARFF](http://weka.wikispaces.com/ARFF+%28stable+version%29) format.