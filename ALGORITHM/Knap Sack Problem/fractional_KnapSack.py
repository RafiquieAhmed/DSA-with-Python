def Fractional_Knapsack(items_wt, cost, Capacity):
    size= len(items_wt)
    
    items=[( cost[i], items_wt[i], cost[i]/items_wt[i]) for i in range(size)]
    
    for i in range(size):
        for j in range(i+1,size):
            if (items[i][2] < items[j][2]):
                items[i] , items[j]=items[j],items[i]
                
    
    profit= 0.0
    for cost , items_wt ,perkgprice in items:
        if(Capacity >=items_wt):
            Capacity =Capacity-items_wt
            profit = profit +  cost   
        else:
            profit =profit +perkgprice+Capacity
    
    print("Total Price =" ,profit)
    
cost= [24,21,12,10]   
items_wt=[7,3,4,5]
capacity=20
Fractional_Knapsack(items_wt,cost,capacity)       
            