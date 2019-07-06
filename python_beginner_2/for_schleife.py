users = ["Anton", "Bertha", "Caesar", "Detlef", "Emil"]


print(users)

i = 0
while i < len(users):
    users[i] = users[i] + "!!!"
    i += 1
    
print("*" * 5)