

Stock = {
    "A" : 6,
    "B" : 5,
    #"C" : 4
}
Price = {
    "A" : 1,
    "B" : 9
}
#Price.get("C", 0)

def returnSum(dict): 
     
     
     sum = 0
     for i in Stock: 
           sum += Stock[i] * Price[i]
     return sum
     
  
# Driver Function 
dict = Price

print("Sum :", returnSum(dict)) 



