class Node:
    """
    TThe node contains the left and right child and the data.
    """
    def __init__(self, data):
        """
        Constructor.
        """
        self.left = None
        self.right = None
        self.data= data

    def insert(self,data):
        """
        Inserting the node.
        Input: data
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data :
                if self.right is None:
                    self.right =Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    def printInterval(self, low, high):
        """
        Printing the nodes within the given interval
        Input: low - interval starting value
                high - intrval ending value
        Output: the nodes within the interval
        """
        if self.left and self.left.data >= low and self.left.data <=high:
            self.left.printInterval(low, high)
        elif self.left and self.left.right:
            if self.left.right.data >= low:
                self.left.right.printInterval(low, high)

        if self.data >= low and self.data <=high:
            print self.data,

        if self.right and self.right.data >= low and self.right.data <= high :
            self.right.printInterval(low, high)
        elif self.right and self.right.left:
            if self.right.left.data >= low:
                self.right.left.printInterval(low, high)

"""creating the tree"""
n1=Node(50)

"""populating"""
n1.insert(17)
n1.insert(72)
n1.insert(12)
n1.insert(23)
n1.insert(54)
n1.insert(76)
n1.insert(9)
n1.insert(14)
n1.insert(19)
n1.insert(67)

"""printing"""
n1.printInterval(23,68)
