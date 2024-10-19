from datetime import datetime
cur=datetime.now()
print(cur)
format_1=cur.strftime("%Y-%m-%d %H:%M:%S")
print(format_1)

format_2=cur.strftime("%m %d %Y")
print(format_2)

format_3=cur.strftime("%a %d %Y")
print(format_3)

format_4=cur.strftime("%Y-%m-%d %H:%M:%S %p")
print(format_4)

format_5=cur.strftime("%a-%b-%d %H:%M:%S %Z %Y")
print(format_5)

format_6=cur.strftime()