#nested loop = a loop wiht another loopp (outer, inner) 
#                 outher 
#                       inner 
#can have while inside for, vise versa, while in while or for in for 

# for x in range(3):
#     for y in range(1,10):
#         print(y, end='')
# #be sure the counters are diuffrent variablees 
#     print()
#     #this makes a blank line 

rows = int(input('input number oof rows'))
columns = int(input('input number oof columns'))
symbol = input('enter a symbol to use')

for x in range(rows):
    for y in range(columns):
        print(symbol, end='')
    print()
