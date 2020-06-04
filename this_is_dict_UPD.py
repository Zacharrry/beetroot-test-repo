stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
    "pumpkin": 1
   
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
     for p in prices: 
          print(prices.get("pumpkin", 0)

     sum = 0
     for i in stock: 
           sum += stock[i] * prices[i]
     return sum
   
     
  
# Driver Function 
dict = stock

print("Sum :", returnSum(dict)) 