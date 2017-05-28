class Student(object):
    def __init__(self,name):
        self.name=name
    def __getattr__(self,attr):
        if attr=='score':
            return 99
##*******************************************
        
    def __str__(self):
        return 'Student object (name: %s)' % self.__name
    __repr__=__str__
    


class Fib(object):
    def __init__(self):
        self.a,self.b=0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>10000:
            raise StopIteration()
        return self.a
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a

        if isinstance(n,slice):
            start = n.start
            stop=n.stop
            step=n.step
            if start is None:
                start=0
            if step is None:
                step=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start and (x-start)%(step+1)==0:
                    L.append(a)
                a,b=b,a+b

            return L
    
