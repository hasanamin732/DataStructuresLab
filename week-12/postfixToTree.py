from tree import Tree

def postfixToTree(string:str):
    bucket=string.split(' ')
    stack=[]
    for b in bucket:
        if b.isalnum():
            stack.append(Tree(b))
        elif b in '*+/-':
            right=stack.pop()
            left=stack.pop()
            stack.append(Tree(b,Lchild=left,Rchild=right))
        else:
            raise ValueError("Invaid Expression")
    if stack:
        final_tree=stack.pop()
        return final_tree
    
print(postfixToTree("B B * A C 4 * * -"))
    
print(postfixToTree("91 95 + 15 + 19 + 4 *"))