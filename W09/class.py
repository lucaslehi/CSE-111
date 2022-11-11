name_list = []
age_list = []

while True:
    name = input("Please, enter your name (q to quit): ")
    if name == 'q':
        break
    #name_list.append(name)
    age = input("Please, enter your age: ")
    name_list.append({name: age})

#print(name)
text_file = open("out.txt", "w")
text_file.write(str(name_list))
text_file.close()

for name in name_list:
    print(name)