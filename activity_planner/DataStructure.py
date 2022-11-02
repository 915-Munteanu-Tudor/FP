class DataStructure:
    def __init__(self,items = []):
        self.data = []
        for a in items:
            self.data.append(a)
        self.size = len(self.data)-1

    def __setitem__(self, key, value):
        if key == (self.size + 1):
            self.size += 1
            self.data.append(value)
        elif key <= self.size:
            self.data[key] = value
        else:
            raise IndexError

    def __getitem__(self, item):
        return self.data[item]

    def append(self,item):
        self.__setitem__(self.size+1, item)

    def pop(self,index):
        self.size -= 1
        return self.data.pop(index)

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current<=self.size:
            self.current += 1
            return self.__getitem__(self.current-1)
        else:
            raise StopIteration

    def __len__(self):
        return self.size+1

    def remove(self,item):
        for i in self.data:
            if item is i:
                self.data.remove(i)
                self.size -=1

    def clear(self):
        self.data = []
        self.size = -1

def gnome_sort( arr, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index +1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index = index - 1

def filter(l, condition_function):
    result = DataStructure()
    for i in l:
        if condition_function(i) is True:
            result.append(i)
    return result

