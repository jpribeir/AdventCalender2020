#open file and list inputs
with open("../input_files/expense_report.txt","r") as expense_report:
    expense_list = []
    for line in expense_report.readlines():
        expense_list.append(line)

#3 nested loops check for sum of 2 and 3 inputs and break when done
checkDouble = False
checkTriple = False
for numA,expenseA in enumerate(expense_list):
    for numB,expenseB in enumerate(expense_list):
        if checkDouble == False:
            sumDouble = int(expenseA) + int(expenseB)
            if (numA != numB) and (sumDouble == 2020):
                doubleA = expenseA
                doubleB = expenseB
                checkDouble = True
        if checkTriple == False:
            for numC,expenseC in enumerate(expense_list):
                sumTriple = int(expenseA) + int(expenseB) + int(expenseC)
                if (numA != numB) and (numC != numB) and (numA != numC) and (sumTriple == 2020):
                    tripleA = expenseA
                    tripleB = expenseB
                    tripleC = expenseC
                    checkTriple = True
                    break
        if (checkDouble == True) and (checkTriple == True): break
    if (checkDouble == True) and (checkTriple == True): break

#output answers to file
strout = []
strout.append("DOUBLE:\nFirst number is "+doubleA+"\n")
strout.append("Second number is "+doubleB+"\n")
productDouble = int(doubleA)*int(doubleB)
strout.append("Product is "+str(productDouble)+"\n\n")
strout.append("TRIPLE:\nFirst number is "+tripleA+"\n")
strout.append("Second number is "+tripleB+"\n")
strout.append("Second number is "+tripleC+"\n")
productTriple = int(tripleA)*int(tripleB)*int(tripleC)
strout.append("Product is "+str(productTriple)+"\n")

with open("outtest.txt","w") as outfile:
    for outline in strout: outfile.write(outline)
