# part 1
question=["Which animal is known as the ‘Ship of the Desert?(1000)","How many letters are there in the English alphabet?(2000)","What do you call the person who brings a letter to your home from post office?(3000)","How many consonants are there in the English alphabet? (5000)","Which country is Delhi located in?(10,000)"]

# part 2
first_option=["1.cat","1.22","1.postman","1.57","1.USA"]
second_option=["2.camel","2.28","2.police","2.29","2.India"]
third_option=["3.cow","3.26","3.doctor","3.32","3.Switzerland"]
fourth_option=["4.bull","4.29","4.teacher","4.22","4.England"]

#part 3
all_options=[first_option,second_option,third_option,fourth_option]

#part 4
ans_key=[2,3,1,4,2]
# part 1 
for i in range(len(question)):
	print (question[i], len(question[i]))
	print (first_option[i])
	print (second_option[i])
	print (third_option[i])
	print (fourth_option[i])
	user=int(input("Enter your answer "))	
	if user==ans_key[i]:
		print ("apka answer sahi hai  ")
	else:
		print ("sadly apka answer wrong hai  ")
		break
# part 3
# print (first_option[2])
# print (second_option[2])
# print (third_option[2])
# print(fourth_option[2])

# part 4

# question.pop()
# first_option.pop()
# second_option.pop()
# third_option.pop()
# fourth_option.pop()
# print (first_option)
# print (second_option)
# print (third_option)
# print (fourth_option)	
# part 5


# part 6

# question.append("where is our campus? ")
# first_option.append("Banlore")
# second_option.append("Sighapur")
# third_option.append("dharamsala")
# fourth_option.append("lucknow")
# print (len(question))

# # part 7
# option2=second_option[1]
# print (option2)

# # part 8
# print (" ")
# if option2 in third_option:
# 	print ("hai")
# else:
# 	print ("nahi hai")
# # 
# for i in question:
# 	print ( i)
# 	for i in first_option:
# 		print ( i)
# 	for i in second_option:
# 		print ( i)
# 	for i in third_option:
# 		print ( i)
# 	for i in fourth_option:
# 		print ( i)