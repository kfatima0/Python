##backslash n to start a new line and backslash t to insert a tab
splitString ="This string has been\nsplit over\nseveral\nlines"
print(splitString)

## using backslash t causes python to tab to the next stop before printing
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)
## backslash can also be used to escape special characters such as quotes and double quotes
print('The pet shop said "No, no, \'e\'s uh,...he\'s resting".') ## here  string is delimited with single quotes,
## so we have to escape any single quotes(first n end quote) that appear in string 
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".") 
##here we have delimited using double quotes, means the double quotes inside the string is escaped
      
print ("""The pet shop owner said \"No, no, 'e's uh,...he's resting\".""")
##while using triple quotes no need to escape any quotes inside the string . python knows that the string doesnt end ,
## until it finds those matching triple qutots at the end

anotherSplitString = """This string has been 
split 
over 
severl 
lines"""

print(anotherSplitString)


