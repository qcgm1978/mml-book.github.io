import re
class IntroMotiv(object):
    core = ('data', 'model', 'learning')
    foundations = {'Regression':( 'Vector Calculus', 'Linear Algebra'),
                     'dimensionality reduction & density estimation':('Probability & Distributions','Analytic Geometry'),
                    'Classification':('Optimization','Matrix Decomposition')}
    __paraphrase = '''A model is said to 'learn from data' if its per- formance on a given task improves after the data is taken into account. 
    The goal is to find good models that 'generalize well to yet unseen data', which we may care about in the future. 
    Learning can be understood as a way to automatically 'find patterns and structure in data' by optimizing the parameters of the model. '''
    mathematical_foundations = '''Understanding these principles can facilitate 'creating new machine learning solutions', 'understanding and debugging existing approaches', and 'learning about the inherent assumptions and limitations of the methodologies' we are working with.'''
    
    linear_algerba='The study of vectors and matrices '
    analytic_geometry='The construction of similarity and distances '
    matrix_decomposition='allow for an intuitive interpretation of the data and more efficient learning'
    probability_theory='Quantification of uncertainty  '
    vector_calculus=' gradients, optimization to find maxima/minima of functions'
    algorithm_senses={'predictors':'makes predictions based on input data','training':'adapts some internal parameters of the predictor'}
    vectors = '''a vector as an array of numbers (a 'computer science' view), a vector as an arrow with a direction and magnitude (a 'physics' view), and a vector as an object that obeys addition and scaling (a 'mathematical' view).'''
    strategies = {'Bottom-up': {
        'advantage': 'able to rely on their previously learned concepts',
        'downside':'forgotten'
    }, 'Top-down': {
        'advantage': 'interesting',
        'downside':'do not have any way of understanding'
    }}
    @property
    def process_generate(self):
        processes = re.findall(r"'(.+)'", self.__paraphrase)
        return processes
    @property
    def math_for(self):
        m=re.findall(r"'(.+?)'",self.mathematical_foundations)
        return m
    @property
    def vector_view(self):
        v = re.findall(r"'(.+?)'", self.vectors)
        return v