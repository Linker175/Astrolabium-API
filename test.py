day_name=[]
for day_number in range(1,181):
    day_name.append(str(day_number)) 

day_columns={}
for day_number in day_name:
    day_columns[day_number]=7

print(day_columns)