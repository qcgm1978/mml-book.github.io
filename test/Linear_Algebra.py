import numpy as np
class Linear_Algebra(object):
    underlie='vector space'
    @property
    def vectors(self):
        vectors = {
         'properties': ('can be added together', 'multiplied by scalars', 'to produce another object of the same kind'),
         'objects': {
            'geometric': ('concrete'),
            'polynomial': ('concepts'),
            'Audio signals': float(),
            'Rn':(float(),)
         }
        }
        return vectors
    def getYByFunc(self,x,coefs):
        y=np.polyval(coefs,x)
        return y
    def linalgSolve(self,a,b):
        if len(np.array(a).shape) == 1:
            a=[a]
        return np.linalg.solve(a, b)
    def lstsq(self, a, b):
        return np.linalg.lstsq(a,b, rcond=None)