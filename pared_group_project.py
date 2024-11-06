#Emily Wawrzyniak Yao Hua He 

#problem 1##########################################################################################
score  = int(input('Enter a list of student scores, One by One:(Negative number to quit): '))
#Prompts the user to begin entering the scores 
totalExc = 0
totalGood = 0
totalPass = 0 
totalFail = 0
#sets the total values for the grades 

while not score < 0 :
    score = int(input(" Student score: ")) # again it asks for the student's score 
    if score >= 90 or score >= 100: # if the score is greater than 90 or greater than 100, print excellent and add one to the total excellent grade 
        print("Excellent")
        totalExc = totalExc + 1
    elif score >=70 and score < 90:# if the score is greater than or equal to 70 or less than 90, print Good and add one to the total good grade 
        print("Good")
        totalGood = totalGood + 1
    elif score >= 50 and score < 70:# if the score is greater than or equal to 50 and less than 70, print pass and add a score to total pass grade 
        print('Pass')
        totalPass = totalPass + 1
    else:# anything that is less than 50 will be considered a fail and add to the total number of fails 
        print('Fail')
        totalFail =totalFail + 1 
#each time a score is inputted, it adds a count to the variable until a negative number is entered 
print(f'Total Excellent:{totalExc}')
print(f'Total Good:{totalGood}')
print(f'Total Pass:{totalPass}')
print(f'Total Fail:{totalFail}')
#this collects and prints the total number of the grades 


#problem 2##########################################################################################
startingNum = int(input('Input a starting Number'))
endingNum = int(input('Input an ending Number'))
#asks number for starting and ending 

specialEven = [9]
specialOdd = [12]
#these are 2 numbers that are not avalible under the conditions presented, so they will not interfere with the list while being able to be a place holder

for x in range (startingNum, endingNum):
    if x >= 10 and x%2 == 0:
        #this checks to make sure the number is bpoth more then 10 and even 
        specialEven.append(x)
    elif x <= 20 and x%2 == 1:
        #this checsks to see if the number is less then 20 and odd 
        specialOdd.append(x)

specialEven.remove(9)
specialOdd.remove(12)
#This removes the place holder values so they are not counted in the list of special ordds or specail evens 
print(f"You have {len(specialEven)} special even numbers and they are {specialEven}")
print(f'You have {len(specialOdd)} special odds and they are {specialOdd}')
#These print out the amount of special versions of these numbers and what numbers they are. 
