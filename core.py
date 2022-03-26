import sys
class Matrix():
    def __init__(self):
        self.data = []
    def fromfile(self,inputfile):
        self.data = []
        with open(inputfile,'r') as f:
            for line in f:
                if len(list(map(int,line.split()))) != 0:
                    self.data.append(list(map(int,line.split())))
        return self
    def tofile(self,outputfile,ty):
         with open(outputfile,ty) as f:
            for line in self.data:
                f.write(' '.join(list(map(str,line))) + '\n')
    def fromlist(self,l):
        self.data = l
        return self
    def T(self):
        l = []
        for _ in range(len(self.data[0])):
            l.append(len(self.data)*[0])
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                l[j][i] = self.data[i][j]
        return Matrix().fromlist(l)
    def dot(self,b):
        l = []
        for _ in range(len(self.data)):
            l.append(len(b.data[0])*[0][:])
        for i in range(len(l)):
            for j in range(len(l[0])):
                for k in range(len(b.data[0])):
                    l[i][j] += self.data[i][k]*b.data[k][j]
        return Matrix().fromlist(l)
    def show(self,file=sys.stdout):
        print(self.data,file=file)
