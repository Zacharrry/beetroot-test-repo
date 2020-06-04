stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
    "pumpkin": 0
   
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
#total = {
    #"stock": stock,
    #"prices": prices
#}
def returnSum(dict): 
      
     #y = prices.get("pumpkin", "0")
     #print(y)
     sum = 0
     for i in stock: 
           sum += stock[i] * prices[i]
     return sum
     
  
# Driver Function 
dict = prices

print("Sum :", returnSum(dict)) 