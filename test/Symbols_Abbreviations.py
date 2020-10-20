import re
# Table of Abbreviations and Acronyms
Acronym='e.g. GMM i.e. i.i.d. MAP MLE ONB PCA PPCA REF SPD SVM'
Meaning='''Exempli gratia(Latin: for example)
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
def get_mean(acro):
    l_acro = re.split(r'\s+', Acronym)
    l_meaning = re.split(r'\n', Meaning)
    ind = l_acro.index( acro)
    return l_meaning[ind]