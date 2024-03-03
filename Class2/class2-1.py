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
traverse(head)