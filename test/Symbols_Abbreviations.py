import re
import numpy as np
from test.Constants_Sym_Abbre import Acronym, Meaning, Symbol, Typical_meaning
class Handle_Sym_Abbre(object):
    Acronym, Meaning, Symbol, Typical_meaning=Acronym, Meaning, Symbol, Typical_meaning
    l_sym = np.array(re.split(r'\n', Symbol))
    def __init__(self):
        self.rules = [None] * len(self.l_sym)
    def get_rule(self, ind,s):
        v=re.search(r'(\w).*?\,.*?([+-·/]).*([+-·/])',s).group
        self.rules[ind] = {v(1): 'Vecotors',
        'neutral_element': '0 = [0, . . . , 0]⊤',
        'inner_operation':'{0} called vector addition'.format(v(2)),
        'outer_operation':'{0} multiplication by scalars'.format(v(3))
        }
        return self.rules[ind]
    def get_mean(self,acro):
        l_acro = re.split(r'\s+', Acronym)
        l_meaning = re.split(r'\n', Meaning)
        ind = l_acro.index(acro)
        return l_meaning[ind]
    def get_sym_properties(self, s):
        meaning=self.get_symbol_meaning(s)
        rules = self.get_rule(self.ind, s)
        print(rules)
        return {'meaning':meaning,**rules}
    def get_symbol_meaning(self,sym):
        l_meaning = re.split(r'\n', Typical_meaning)
        def is_set_ops(x):
            return re.fullmatch(rf'{x}',sym,re.IGNORECASE)
        def f0(x):
            return x.strip() == sym
        def f1(x):
            l = x.split(',')
            return sym in l
        def f2(x):
            # x=x.strip()
            return x[0] == sym[0] and len(x) == len(sym)
        def f3(x):
            return re.search(rf'{sym}', x)
        def f4(x):
            return x[0] == sym[0] and x[-1] == sym[-1]
        l = [is_set_ops,f0, f1, f2, f3,f4]
        ind=None
        for i in range(len(l)):
            l1 = self.indices(self.l_sym, l[i])
            if len(l1):
                ind = l1[0]
                break
        if ind is None:
            if re.search(r'\s', sym):
                sym = re.sub(r'\s', '', sym)
                return self.get_symbol_mean(sym)
            else:
                return 'not found'
        self.ind=ind
        meaning=l_meaning[ind]
        print(ind,meaning)
        return meaning
    def indices(self,l,filtr=lambda x: bool(x)):
        return [i for i,x in enumerate(l) if (filtr(x) if callable(filtr) else exec(filtr))]
