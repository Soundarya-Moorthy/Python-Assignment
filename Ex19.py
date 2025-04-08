def calTax(income):
 if income<=250000:
  tax=0
 elif income>250000 and income<=500000:
  tax=income*0.05
 elif income>500000 and income<=1000000:
  tax=income*0.20
 else:
  tax=income*0.30
 return tax

def main():
 income=float(input("Enter the annual income: "))
 taxAmt=calTax(income)
 print("Income tax amount is:",taxAmt)

main()
