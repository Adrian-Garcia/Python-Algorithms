myGlobalVar = 3009 

# not using function
def testOfGlobalVar():
	print("My myGlobalVar = ", myGlobalVar)

# this is totaly going to crash
def chanteGlobalVar(): 
	myGlobalVar += 1
	print("myGlobalVar = ", myGlobalVar)

# this is not going to crash, is the correct way of doing it
def changeGlobalVarAsParameter(myGlobalVar): 
	myGlobalVar += 1
	print("myGlobalVar = ", myGlobalVar)

# this is going to crash because copy is not available in an integer
def copyVarToChange(myGlobalVar):
	copiedVar = myGlobalVar.copy()
	copiedVar += 1
	print("copiedVar = ", copiedVar)

# this is the correct way of doing it
def equalVarToChange():
	equaledVar = myGlobalVar
	equaledVar += 1

	print("myGlobalVar = ", myGlobalVar)
	print("equaledVar = ", equaledVar)	

# testOfGlobalVar()
# changeGlobalVarAsParameter(myGlobalVar)
# copyVarToChange(myGlobalVar)
equalVarToChange()