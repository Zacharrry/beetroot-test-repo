stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
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
      
     sum = 0
     for i in dict.values(): 
           sum = sum + i 
       
     return sum
  
# Driver Function 
dict = stock

print("Sum :", returnSum(dict)) 