stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
<<<<<<< HEAD
    "pumpkin": 1
=======
    "pumpkin": 0
>>>>>>> c346a9290efbb02d0c1b9e2b83173ab83561b889
   
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
<<<<<<< HEAD
     for p in prices: 
          print(prices.get("pumpkin", 0)

=======
      
     #y = prices.get("pumpkin", "0")
     #print(y)
>>>>>>> c346a9290efbb02d0c1b9e2b83173ab83561b889
     sum = 0
     for i in stock: 
           sum += stock[i] * prices[i]
     return sum
<<<<<<< HEAD
   
=======
>>>>>>> c346a9290efbb02d0c1b9e2b83173ab83561b889
     
  
# Driver Function 
dict = prices

print("Sum :", returnSum(dict)) 