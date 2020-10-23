import re
import numpy as np
# Table of Abbreviations and Acronyms
Acronym = 'e.g. GMM i.e. i.i.d. MAP MLE ONB PCA PPCA REF SPD SVM'
Meaning = '''Exempli gratia(Latin: for example)
Gaussian mixture model
Id est(Latin: this means)
Independent, identically distributed 
Maximum a posteriori
Maximum likelihood estimation / estimator
Orthonormal basis
Principal component analysis
Probabilistic principal component analysis
Row-echelon form
Symmetric, positive definite
Support vector machine
'''
Symbol = '''a,b,c,α,β,γ
x,y,z 
A,B,C 
x⊤,A⊤
A−1
⟨x,y⟩
x⊤y
B = (b1,b2,b3) 
B = [b1,b2,b3] 
B = {b1,b2,b3} 
Z,N
R,C
Rn
∀x
∃x 
a:=b 
a=:b 
a∝b 
g◦f
⇐⇒
=⇒ 
A,C 
a∈A 
∅ 
A\B 
D
N
Im 
0m,n
1m,n
ei
dim 
rk(A) 
Im(Φ) 
ker(Φ) 
span[b1 ] 
tr(A) 
det(A) 
|·|
∥·∥
λ 
Eλ
x⊥y 
V
V⊥
􏰛Nn=1 xn 
􏰜Nn=1 xn
θ
∂f ∂x
df dx 
∇
f∗ = minx f(x)
x∗ ∈ arg minx f (x)
L
L
􏰁n􏰂 k
VX [x]
EX [x] 
CovX,Y [x, y] 
X ⊥ Y | Z 
X∼p
N􏰁μ, Σ􏰂 
Ber(μ) 
Bin(N, μ) 
Beta(α, β)'''
Typical_meaning = '''Scalars are lowercase
Vectors are bold lowercase
Matrices are bold uppercase
Transpose of a vector or matrix
Inverse of a matrix
Inner product of x and y
Dot product of x and y
(Ordered) tuple
Matrix of column vectors stacked horizontally
Set of vectors (unordered)
Integers and natural numbers, respectively
Real and complex numbers, respectively
n-dimensional vector space of real numbers
Universal quantifier: for all x
Existential quantifier: there exists x
aisdefinedasb
b is defined as a
a is proportional to b, i.e., a = constant · b
Function composition: “g after f ”
If and only if
Implies
Sets
aisanelementofsetA
Empty set
A without B: the set of elements in A but not in B
Number of dimensions; indexed by d = 1, . . . , D
Number of data points; indexed by n = 1,...,N
Identity matrix of size m × m
Matrix of zeros of size m × n
Matrixofonesofsizem×n
Standard/canonical vector (where i is the component that is 1) 
Dimensionality of vector space
Rank of matrix A
Image of linear mapping Φ
Kernel (null space) of a linear mapping Φ
Span (generating set) of b1
Trace of A
Determinant of A
Absolute value or determinant (depending on context)
Norm; Euclidean unless specified
Eigenvalue or Lagrange multiplier
Eigenspace corresponding to eigenvalue λ
Vectors x and y are orthogonal
Vector space
Orthogonal complement of vector space V 
Sumofthexn:x1 +...+xN 
Productofthexn:x1 ·...·xN
Parameter vector
Partial derivative of f with respect to x
Total derivative of f with respect to x
Gradient
The smallest function value of f
The value x∗ that minimizes f (note: arg min returns a set of values) 
Lagrangian
Negative log-likelihood
Binomial coefficient, n choose k
Variance of x with respect to the random variable X
Expectation of x with respect to the random variable X
Covariance between x and y.
X is conditionally independent of Y given Z
Random variable X is distributed according to p
Gaussian distribution with mean μ and covariance Σ
Bernoulli distribution with parameter μ
Binomial distribution with parameters N, μ
Beta distribution with parameters α, β'''


def get_mean(acro):
    l_acro = re.split(r'\s+', Acronym)
    l_meaning = re.split(r'\n', Meaning)
    ind = l_acro.index(acro)
    return l_meaning[ind]


def get_symbol_mean(sym):
    l_sym = np.array(re.split(r'\n', Symbol))
    l_meaning = re.split(r'\n', Typical_meaning)
    try:
        ind = [i for i,item in enumerate(l_sym) if item.strip()==sym][0]
    except IndexError:
        def f(x):
            l = x.split(',')
            return sym in l
        try:
            ind = indices(l_sym, f)[0]
        except IndexError:
            def f(x):
                return x[0] == sym[0] and len(x) == len(sym)
            try:
                ind = indices(l_sym, f)[0]
            except IndexError:
                def f(x):
                    return re.search(rf'{sym}', x)
                try:
                    ind = indices(l_sym, f)[0]
                except IndexError:
                    if re.search(r'\s', sym):
                        sym = re.sub(r'\s', '', sym)
                        return get_symbol_mean(sym)
                    else:
                        return 'not found'

    print(ind)
    return l_meaning[ind]
def indices(l,filtr=lambda x: bool(x)):
        return [i for i,x in enumerate(l) if filtr(x)]
