with open("expense_report.txt","r") as expense_report:
    expense_list = []
    for line in expense_report.readlines():
        expense_list.append(line)

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

strA = "DOUBLE:\nFirst number is "+doubleA+"\n"
strB = "Second number is "+doubleB+"\n"
productDouble = int(doubleA)*int(doubleB)
strC = "Product is "+str(productDouble)+"\n\n"
strD = "TRIPLE:\nFirst number is "+tripleA+"\n"
strE = "Second number is "+tripleB+"\n"
strF = "Second number is "+tripleC+"\n"
productTriple = int(tripleA)*int(tripleB)*int(tripleC)
strG = "Product is "+str(productTriple)+"\n"

print("aaaa")

with open("outtest.txt","w") as outfile:
    outfile.write(strA)
    outfile.write(strB)
    outfile.write(strC)
    outfile.write(strD)
    outfile.write(strE)
    outfile.write(strF)
    outfile.write(strG)
