size = 10
prices = [None]*size


def hash_function(item):
    return sum(ord(c) for c in item) % size

def insert(item,price):
    index = hash_function(item)
    prices[index] = price
    
def get(item):
    index = hash_function(item)
    return prices[index]



insert("apple",400)
insert("orange",600)
insert("banana",500)

print(get("apple"))
print(get("banana"))
print(get("orange"))