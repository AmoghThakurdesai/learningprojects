# Write your code here :-)
import pyinputplus as pyip
print('Sandwich')
cost=0
breadcost=0
print('What bread do you want?')
bread=pyip.inputMenu(['wheat','white','sourdough'])
if bread=='wheat':
    breadcost=7
elif bread=='white':
    breadcost=8
elif bread=='sourdough':
    breadcost=9
cost+=breadcost

print('What protein type do you need?')
protein=pyip.inputMenu(['chicken','turkey','ham','tofu'])
proteincost=0
if protein=='chicken':
    proteincost=4
elif protein=='turkey':
    proteincost=4
elif protein=='ham':
    proteincost=4
elif protein=='tofu':
    proteincost=6
cost+=proteincost


cheeseYN=pyip.inputYesNo('Do you want cheese?')
if cheeseYN==('Yes' or 'yes' or 'y'):
    print('What type of cheese do you want?')
    cheese=pyip.inputMenu(['cheddar','Swiss','mozzarella'])
    cheesecost=0
    if cheese=='cheddar':
        cheesecost=2
    elif cheese=='Swiss':
        cheesecost=3
    elif cheese=='mozzarella':
        cheesecost=2
    cost+=cheesecost





print('How many sandwiches do you want?')
sandnum=pyip.inputInt(min=1)
totalcost=cost*sandnum
print('The cost of your sandwich is '+str(totalcost)+'$')
print(ecost)
