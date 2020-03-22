# 1. print name five times
# 2. print name five times but start with 1. not 0. 
# 3. using a for loop - add numbers from 0 to 100

# 1. print name five times
for x in range(5):
	print(str(x) + '. My name is Singh!')
print('-------------*********-------------\n')

# 2. print name five times but start with 1. not 0.
for x in range(5):
	print(str(x+1) + '. My name is Singh!')
print('-------------*********-------------\n')

# 3. using a for loop - add numbers from 0 to 100
total = 0
for num in range(101):
  total = total + num; 
print('The sum from all number form 0 to 100 is: ' + str(total))
print('-------------*********-------------\n')