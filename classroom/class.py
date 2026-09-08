#nums=[1, 2, 3, 4, 5]
#squares={n:n**2 for n in nums}
#print(squares)

#names=["rahul","sachin","anil"]
#temp={i:len(i) for i in names}
#print(temp)

nums=[1, 2, 3, 4, 5]
squares={
      n:n**2  
      if n%2==0 
      else n**3
      for n in nums
         }
print(squares)

#note;
#key -> n
#value -> n**2 if n is even
#loop -> for n in nums