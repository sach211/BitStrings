def noOfStrings( n ): #The number of bit strings of bit size n is the (n + 2)th Fibonacci number 
	a1, a2 = 1, 0  #Setting intial values
	for num in range( n + 1 ):
		temp = a1
		a1, a2 = a1 + a2, temp 
		#Calculating the (num + 2)th Fibonacci number, and using that along with the previous to calculate the next
	return (a1 % (1000000007))

t = raw_input()
for turns in range( int(t) ):
	n = raw_input()
	print noOfStrings( int(n) ) 
