import time

#***************************************************#

#Ex. 1

def isEvenDiv(value):

    return value % 2 == 0


def isEvenLogicalAnd(value):
    return value & 1 == 0


#***************************************************#

#Ex. 2

class Mass_FIFO:
    def __init__(self, max_length):
        self.mass = [None] * max_length
        self.max_length = max_length
        self.count = 0  # кол-во записей
        self.ptr_push = 0  # указатель на запись в буфер
        self.ptr_pop = 0  # указатель на чтение из буфера

    def push(self, value):
        self.mass[self.ptr_push] = value
        

        if self.ptr_push + 1 >= self.max_length:  # перевод указателя записи на начало, если уже записан последний элемент
            self.ptr_push = 0
        else:
            self.ptr_push = self.ptr_push + 1

        if self.count >= self.max_length:  # перевод указателя чтения из буфера на начало, если уже записан последний элемент
            self.ptr_pop = self.ptr_push
        else:
            self.count += 1
    def pop(self):

        if self.count == 0:  # если в буфер ничего не записано
            return None

        else:
            temp = self.ptr_pop
            if self.ptr_pop + 1 >= self.max_length:
                self.ptr_pop = 0
                del_val = self.mass[temp]
                self.mass[temp] = None
                return del_val

            else:
                self.ptr_pop = self.ptr_pop + 1
                del_val = self.mass[temp]
                self.mass[temp] = None
                return del_val

    def print_list(self):
        print(self.mass)


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Linked_List_FIFO():
    def __init__(self, max_length):
        self.max_length = max_length
        self.head = Node()
        self.count = 0  # кол-во операций записи в буфер
        self.ptr_push = 0
        self.ptr_pop = 0
        
        for i in range(0, max_length-1):
            if i == 0:
                New_Node = Node()
                self.head.next = New_Node
                New_Node.next = self.head

            else:
                New_Node = Node()
                New_Node.next = self.head.next
                self.head.next = New_Node


    def push(self, value):
        if self.count == 0:  # если не было записей в буфер
            self.head.value = value
            
            self.count += 1
            self.ptr_push = self.head
            self.ptr_pop = self.head
        else:
            self.ptr_push.next.value = value
            self.ptr_push = self.ptr_push.next

            if self.count >= self.max_length:
                self.ptr_pop = self.ptr_pop.next
            else:
                self.count += 1 
        
    
    def pop(self):

        if self.count == 0:
            return None
        
        del_val = self.ptr_pop.value
        self.ptr_pop.value = None
        self.ptr_pop = self.ptr_pop.next
        self.count -= 1
        return del_val

    def print_list(self):
        temp = self.head
        for k in range(self.max_length):
            print("{}\t".format(temp.value), end="")
            temp = temp.next
        print()

#***************************************************#

#Ex. 3


import operator

def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


if __name__ == "__main__":

    start1 = time.time()

    for k in range(10000000):
        isEvenDiv(4)

    end1 = time.time()
    print("TIME TO isEvenDiv", end1-start1)

    start2 = time.time()

    for k in range(10000000):
        isEvenLogicalAnd(4)

    end2 = time.time()
    print("TIME TO isEvenLogicalEnd", end2 - start2)


    ListNode = Linked_List_FIFO(50)
    start3 = time.time()

    for i in range(10000000):
        ListNode.push(i)

    end3 = time.time()
    print("TIME TO Linked_List_FIFO:", end3-start3)

    Mass = Mass_FIFO(50)
    start4 = time.time()

    for j in range(10000000):
        Mass.push(j)

    end4 = time.time()
    print("TIME TO Mass_FIFO:", end4-start4)

