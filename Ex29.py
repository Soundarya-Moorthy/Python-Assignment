def FirCharchange(str1):
 char=str1[0]
 str1=str1.replace(char,'$')
 str1=char+str1[1:]
 return str1
UserStr=input("Enter a string: ")
print("Modified string:",FirCharchange(UserStr))
