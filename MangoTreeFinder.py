def mangoTreeFinder(rows,colums,tree_number):
    if(tree_number<=rows or tree_number%colums==0 or tree_number%colums==1):
        return True
    return False
rows,colums,tree_number=map(int,input().split())
print(mangoTreeFinder(rows,colums,tree_number))
    