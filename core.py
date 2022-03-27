from sys import stdin
import math
from copy import deepcopy
class Matrix():
    def __init__(self, list_of_lists=None):
        if list_of_lists:
            self.data = deepcopy(list_of_lists)
        else:
            self.data = [[]]
        
    def __str__(self):
        return '\n'.join(' '.join(map(str, row))
                         for row in self.data)
    def __getitem__(self, idx):
        return self.data[idx]

    def __repr__(self):
         return 'Matrix(' + self.data.__repr__() + ')'
    
    def __del__(self):
        del self.data
        
    def __eq__(self, other):
        return self.data == other.data
    
    def getrow(self,indx):
        return Matrix([self.data[indx]])
    
    def getcolumn(self,indx):
        l = [[0] for i in range(self.shape()[1])]
        for i in range(len(l)):
            l[i][0] = self.data[i][indx]
        return Matrix(l)
    
    def setcolumn(self,col,indx):
        for i in range(len(self.data[indx])):
            self.data[i][indx] =  col.data[i][0]
    
    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                summa = other[i][j] + self.data[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.data):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)
    def __sub__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                sub = self.data[i][j] - other[i][j]
                numbers.append(sub)
                if len(numbers) == len(self.data):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)
    
    def fromfile(self,inputfile):
        self.data = []
        with open(inputfile,'r') as f:
            for line in f:
                if len(list(map(int,line.split()))) != 0:
                    self.data.append(list(map(int,line.split())))
        return self
    
    def tofile(self,outputfile,mode):
         with open(outputfile,mode) as f:
            for line in self.data:
                f.write(' '.join(list(map(str,line))) + '\n')
    
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[other * x for x in y] for y in self.data]
            return Matrix(result)
        if self.shape()[1] != other.shape()[0]:
            raise ValueError('Incorrect dimension')
        l = []
        for _ in range(len(self.data)):
            l.append(len(other.data[0])*[0])
        for i in range(len(l)):
            for j in range(len(l[0])):
                for k in range(len(other.data)):
                    l[i][j] += self.data[i][k]*other.data[k][j]
        return Matrix(l)
    
    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[x / other for x in y] for y in self.data]
            return Matrix(result)
    
    def __rtruediv__(self, other):
        return self.__div__(other)

    def norm(self):
        answer = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                answer += self.data[i][j]**2
        return math.sqrt(answer)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def T(self):
        l = []
        for _ in range(len(self.data[0])):
            l.append(len(self.data)*[0])
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                l[j][i] = self.data[i][j]
        return Matrix(l)
    
    def gram_sch(self):
        l = []
        for _ in range(len(a.data)):
            l.append(len(a.data[0])*[0])
        b = Matrix(l)
        for i in range(b.shape()[0]):
            b.setcolumn(a.getcolumn(i),i)
            for j in range(i):
                tmp = proj(a.getcolumn(i).T(),b.getcolumn(j).T())
                b.setcolumn((a.getcolumn(i) - tmp.T()).T(),i)
        for i in range(b.shape()[0]):
            b.setcolumn(b.getcolumn(i)/(b.getcolumn(i).norm()),i)
        return b

    def shape(self):
        return (len(self.data), len(self.data[0]))
def proj(a,b):
    if (a.shape()[0] != 1) or (a.shape() != b.shape()):
        raise 
    ab = (a*b.T()).data[0][0]
    bb = (b*b.T()).data[0][0]
    answer = (ab/bb)*b
    return answer