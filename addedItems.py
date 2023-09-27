# Write your code here :-)
def displayInventory(inventory):
    print('Inventory:')
    item_total=0
    for k,v in inventory.items():
        print(str(v)+' '+str(k),end='')
        print()
        item_total+=v
    print('Total number of items:'+ str(item_total))

def addToInventory(inventory,addedItems):
    for index,v in enumerate(addedItems):
        inventory.setdefault(v,0)
        inventory[v]+=1
    return inventory
inv={'gold coin':42,'rope':1}
dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby']
inv=addToInventory(inv,dragonLoot)
displayInventory(inv)
