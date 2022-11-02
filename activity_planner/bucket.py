
class Bucket:
    def __init__(self, items = []):
        self.items = items

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self.items[key] = value
    
    def __delitem__(self, key):
        return self.items.pop(key)

    def add(self, item, position=-1):
        if position == -1:
            self.items.append(item)
        else:
            self.items.insert(position, item)

    def __iter__(self):
        for item in self.items:
            yield item
    
    @property
    def size(self):
        return len(self.items)

def keep(should_keep, old_list):
    new_list = old_list

    index = 0
    while index < len(new_list):
        if not should_keep(new_list[index]):
            new_list.pop(index)
        else:
            index += 1

    return new_list

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


