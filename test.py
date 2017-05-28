class Student(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value>100:
            raise ValueError('score must between 0`100!')
        self.__score=value

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self,value):
        self.__birth=value

    @property
    def age(self):
        return 2017-self.__birth


    
        
            
