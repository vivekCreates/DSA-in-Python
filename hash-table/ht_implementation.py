class Hash_table:
    def __init__(self,size=10):
        self.size = size
        self.arr = [[] for _ in range(self.size)]
        
    def hash_function(self,key):
        return sum(ord(c) for c in key) % self.size
    
    def insert(self,key,value):
        index = self.hash_function(key)
        chain = self.arr[index]
        
        for i, (k,v) in enumerate(chain):
            if k == key:
                chain[i] = (key,value)
                return
            
        chain.append((key,value))
        
    def search(self,key):
        index = self.hash_function(key)
        chain = self.arr[index]
        
        for i,(k,v) in  enumerate(chain):
            if k == key:
                return f"Found {k} at {v}"
        return "Not found"
    
    def get(self,key):
        index = self.hash_function(key)
        chain = self.arr[index]
        
        for i,(k,v) in enumerate(chain):
            if k == key:
                return v
        return None
          
    def delete(self,key):
        index = self.hash_function(key)
        chain = self.arr[index]
        
        for i,(k,v) in enumerate(chain):
            if k == key:
                del chain[i]
                return True
        return False
    
    def print_hash_table(self):
        for i in range(self.size):
            print(self.arr[i])
            

ht = Hash_table()

ht.insert("apple",100)
ht.insert("apricot",400)
ht.insert("apricot",500)
ht.insert("banana",200)
ht.insert("cherry",300)


print(ht.delete("cherry"))
print(ht.get("cherry"))

ht.print_hash_table()
            
        