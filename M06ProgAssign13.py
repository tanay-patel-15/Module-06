# 13.1

from datetime import datetime

today = datetime.today().strftime("%Y-%m-%d")

with  open("today.txt", "w") as file:
  file.write(str(today))
  
print("Today's date has been written to the 'today.txt' file.")


# 13.2

with open("today.txt", "r") as file:
    today_string = file.read()

# 13.3
    
todaydate = datetime.strptime(today_string, "%Y-%m-%d")

print("Parsed date:", todaydate)
