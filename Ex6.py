def Day(day_no):
 match day_no:
  case 1:
   return "Sunday"
  case 2:
   return "Monday"
  case 3:
   return "Tuesday"
  case 4:
   return "Wednesday"
  case 5:
   return "Thursday"
  case 6:
   return "Friday"
  case 7:
   return "Saturday"
  case _:
   return "Invalid Entry"
day_no = int(input("Enter a number (1-7): "))
print(Day(day_no))
