# In this python file, only the definations for the magic functions and the basic operations
# for the question segments are provided. There may be the need to add new functions or overload 
# existing ones as per the question requirements.

import math

class Vector:
        
    def __init__(self, *args): 

        # if arg is an int(dimension)
        if isinstance(args[0], int): 
            self._coords = [0]*args[0]
        elif isinstance(args[0], list):
            self._coords = [0]*len(args[0])
            for i,val in enumerate(args[0]):
                self._coords[i] = val

    def __len__(self):
        # return the dimension of the vector
        return len(self._coords)

    def __getitem__(self, j):
        # return the jth coordinate of the vector
        return self._coords[j]

    def __setitem__(self, j, val):
        # set the jth coordinate of vector to val
        self._coords[j] = val
        return

    def __add__(self, other):
        # u + v
        try:
            assert len(self._coords) == len(other)
            sum = Vector(len(self._coords))
            for i in range(len(self._coords)):
                sum.__setitem__(i,self._coords[i] + other.__getitem__(i))
            return sum
        except:
            print("Can't add two vectors of unequal size...")
            
    def __eq__(self, other):
        # return True if vector has same coordinates as other
        for i,val in enumerate(self.__coords):
            if val != other.__getitem__(i):
                return False
        return True
    
    def __ne__(self, other):
        # return True if vector differs from other
        for i,val in enumerate(self.__coords):
            if val != other.__getitem__(i):
                return True
        return False
    
    def __str__(self):
        # return the string representation of a vector within <>
        s = "<"
        if len(self._coords)>0:
            s += str(self._coords[0])
            for i in range(1, len(self._coords)):
                s += ", " + str(self._coords[i])
        s += ">"
        return s

    def __sub__(self, other):
        # Soln for Qs. 2
        try:
            assert len(self._coords) == len(other)
            dif = Vector(len(self._coords))
            for i in range(len(self._coords)):
                dif.__setitem__(i,self._coords[i] - other.__getitem__(i))
            return dif
        except:
            print("Can't take difference of two vectors with unequal sizes...")

    def __neg__(self):
        # Soln for Qs. 3
        ans = Vector(len(self._coords))
        for val in self._coords:
            ans.__setitem__(i, -val)
        return ans
    
    def __rmul__(self, value):
        return (self * value) 
    
    def __mul__(self, other):
        # Soln for Qs. 4, 5 and 6
        if isinstance(other, int):
            product = Vector(len(self._coords))
            for i in range(len(self._coords)):
                product.__setitem__(i,self._coords[i] * other)
            return product

        if isinstance(other, list):
            product = 0
            try:
                assert len(other)==len(self._coords)
                for i,val in enumerate(self._coords):
                    product += val * other.__getitem__(i)
                return product 
            except:
                print("Two vectors must have same dimension for dot product...")
        


    
def main():
    v1 = Vector(5)
    v2 = Vector (7)
    v3 = Vector([1,2,3,4,5])

    print(v3*3)
    print(3*v3)

    # Add suitable print statements to display the results
    # of the different question segments


if __name__ == '__main__':
    main()