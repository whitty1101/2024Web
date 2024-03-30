class Car:
    def __init__(self,color):
        self.color=color
        self.previous=None
        self.next=None
head=Car('red')
ptr=head
ptr.previous=None
ptr.next=None
new=Car('blue')
ptr.next=new
new.previous=ptr
ptr=new

def rtraverse(head):
    print('start right traverse')
    ptr=head
    while ptr!=None:
        print('The color of the car is {}.'.format(ptr.color))
        ptr=ptr.next
    print('Finish right traverse')
def ltraverse(head):
    print('Start left traverse')
    ptr=head
    while ptr.next!=None:
        ptr=ptr.next
    while ptr !=None:
        print('The color of the car is {}'.format(ptr.color))
        ptr=ptr.previous
    print('Finish left traverse')

rtraverse(head)
ltraverse(head)