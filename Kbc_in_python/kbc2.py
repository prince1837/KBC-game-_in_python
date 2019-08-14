# part 1
question=["Which animal is known as the ‘Ship of the Desert?","How many letters are there in the English alphabet?","What do you call the person who brings a letter to your home from post office?","How many consonants are there in the English alphabet?","Which country is Delhi located in?"]

# part 2
first_option=["cat","22","postman","27","USA"]
second_option=["camel","28","police","29","India"]
third_option=["cow","26","doctor","32","Switzerland"]
fourth_option=["bull","29","teacher","21","England"]

#part 3
all_options=[first_option,second_option,third_option,fourth_option]

#part 4
ans_key=[2,0,1,3]

# part 1 

# print (question[1])
# print (first_option[1])
# print (second_option[1])
# print (third_option[1])
# print (fourth_option[1])

# # part 3
# print (first_option[2])
# print (second_option[2])
# print (third_option[2])
# print(fourth_option[2])

# # part 4

question.pop()
first_option.pop()
second_option.pop()
third_option.pop()
fourth_option.pop()
#print (first_option)
#print (second_option)
#print (third_option)
#print (fourth_option)	
# part 5


# part 6
question.append("where is our campus? ")
first_option.append("Banlore")
second_option.append("Sighapur")
third_option.append("dharamsala")
fourth_option.append("lucknow")
print (len(question))

# part 7
option2=second_option[1]
print (option2)

# part 8
if option2 in third_option:
	print ("hai")
else:
	print ("nahi hai")
