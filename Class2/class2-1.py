#自訂一個類別(class)
class Car:
    def __init__(self, color):
        self.color=color
        self.next=None
        #initiate the first element of the linked list
#traverse the linked list
def traverse(head):
    ptr=head
    while True:
        print('the car color is {}'.format(ptr.color))
        if ptr.next==head:
            break
        ptr=ptr.next
    print('finsh traverse!!')
head=Car('red')
ptr=head
ptr.next=None
#Add next element into linked list
new_data=Car('blue')
ptr.next=new_data
new_data.next=head
ptr=new_data
#新結點插入第一個新節點之前，成為環串列的首節點
new=Car('black')
new.next=head

ptr=head
while ptr.next !=head:
    ptr=ptr.next
ptr.next=new
head=new
#新節點插入單向串鍊在中間
new=Car("pink")
ptr=head
while ptr.color!= "red":
    ptr=ptr.next
new.next=ptr.next
ptr.next=new

ptr=head
while ptr.next !=head:
    ptr=ptr.next
head=head.next
ptr.next=head

ptr=head
while ptr.next.color!="pink":
   ptr= ptr.next
ptr.next=ptr.next.next

traverse(head)