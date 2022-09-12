#Developer: Odimayo Taiye
#This program test if a graph with a adjancency matrix is eulerian graph
"""
    The test makes use of the below theorem.
    Theorem:
        A simple connected graph on n vertices is Eulerian if and only if the degree of every vertex is  
        congruent to 0 mod2 (Divisible by 2).
"""

#This function test if a matrix is associated to a simple graph
def SimpleGraphTest(m):
    simple = True
    sqr = True
    mult = False
    lop = False
    try:

        for i in range(len(m)):
            if m[i][i] != 0:
                lop = True
            for j in range(len(m)):
                if (0 > m[i][j]) or (m[i][j] >= 2):
                    mult = True
            if len(m[i]) != len(m):
                sqr = False
        if sqr:
            if not lop:
                if not mult:
                    trans = [[m[j][i] for j in range(len(m))] for i in range(len(m))]
                    if trans == m:
                        return "Adjacency Matrix For Simple Graph"
                    else:
                        return "Adjacency Matrix Not For Simple Graph"
                else:
                    return "Graph Contains Multiple Edges Not Simple"
            else:
                return "Graph Contains a loop"
    except:
        return "Invalid Input"
def EulerianGraphTest(m):
    n = []
    eulerian = True
    print(len(m))
    try:
        if SimpleGraphTest(m) == "Adjacency Matrix For Simple Graph":
            for i in range(len(m)):
                n.append(sum(m[i]))
        else:
            return "Adjancency matrix not for simple graph "
        for i in range(len(n)):
            if n[i]%2 != 0:
                eulerian = False
                break
        if eulerian:
            return "Eulerian Graph"
        else:
            return "Non Eulerian Graph"
    except:
        return "Invalid Input"