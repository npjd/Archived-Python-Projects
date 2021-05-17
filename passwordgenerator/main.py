list = []
names = []
temp_names = []
phoneNo = ''
dob = input("Date of Birth(DDMMYYYY): ")
if len(dob) == 8:
    day = dob[:2]
    month = dob[2:4]
    year = dob[4:]
else:
    print("Ivalid entry")
    exit()

phoneNo = input("Enter phone no: ")


def ImportWordsList():
    names.append(input("First name: "))
    names.append(input("Last Name: "))
    print("\n")
    names.append(input("Partners name: "))
    names.append(input("Partners last name: "))
    names.append(input("Partners Nickname"))
    print("\n")
    names.append(input("Pets name: "))
    names.append(input("Company name: "))
    names.append(input("School's name: "))
    names.append(input("Childhood home street name: "))
    print("\n")
    print("Enter any other keywords")
    while True:
        inp = input("Input any keywords")
        if inp == '':
            break
        names.append(inp)
    while '' in names:
        names.remove('')


def permute(inp):
    n = len(inp)
    mx = 1 << n
    inp = inp.lower()

    for i in range(mx):
        combination = [k for k in inp]
        for j in range(n):
            if ((i >> j) & 1) == 1:
                combination[j] = inp[j].upper()

        temp = ""
        for i in combination:
            temp += i
        temp_names.append(temp)

def WordListCreator(list):
    for word in names:
        for i in range(0, len(word)+1):
            list.append(word[:i] + day + word[i:])
            list.append(word[:i] + month + word[i:])
            list.append(word[:i] + year + word[i:])
            if len(year) == 4:
                list.append(word[:i] + year[2:] + word[i:])
                list.append(word[:i] + phoneNo + word[i:])
    if phoneNo != '':
                list.append(phoneNo)

def WriteToFile(list):
    with open('wordlist.txt', 'w') as f:
        for item in list:
            f.write("%s\n" % item)

ImportWordsList()
for i in names:
    permute(i)
names= names+ temp_names
WordListCreator(list)
WriteToFile(list)

