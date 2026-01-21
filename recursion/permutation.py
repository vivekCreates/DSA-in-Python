
def printStr(st,res):
    if st == "":
        print(res,end='\n')
        return
    
    for i in range(len(st)):
        ch = st[i]
        left = st[0:i]
        right = st[i+1:]
        rem = left+right
        
        printStr(rem,res+ch)
        



def permutation(st):
    return printStr(st,"")

permutation("abc")
