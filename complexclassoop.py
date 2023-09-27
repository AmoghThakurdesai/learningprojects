class Complex:
    def __init__(self,real=0,img=0):
        self.real=real
        self.img=img

    def display(self):
        print(f'{self.real}+{self.img}i')

    def add(self, comp2):
        ans=Complex()
        ans.real=self.real + comp2.real
        ans.img=self.img + comp2.img
        return ans


a=Complex(2,8)
b=Complex(5,5)
c=a.add(b)
c.display()