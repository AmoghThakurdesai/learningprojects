import time
def calcProd():
    #caculate the product of thr first 10000 numbers
    product =1
    for i in range(1,10000):
        product*=i
    return product
startTime=time.time()
prod=calcProd()
endTime=time.time()
print(f'The result is {len(str(prod))} digits long.')
print(f'Took {endTime-startTime} seconds to calculate')