'''
My self Akshay, My project  domain is Sports Management, My Register number is 2347206, I am currently in year 2023'''

#count the frequency
sportsmanagement = "My self Akshay, My project  domain is sports Management, My Register number is 2347206, I am currently in year 2023, sports sports"
sports_case  = sportsmanagement
word_count = 'Sports'
frquency = sportsmanagement.split()
count = 0
for word in frquency:
    if word == word_count.lower():
        count += 1
print('number of times word has repeated is: ',count)
    

#Data Type

def data_type(details):
    data_type = []
    for value in details:
        data_type.append(type(value))
    return data_type
sports_lst = ['akshay', 132, 12.2]
result = data_type(sports_lst)
print(result)



#count the number of character, digits and symbols
string = input("Enter a sting: ")
alphabets = 0
digits = 0
symbols = 0


for i in range(len(string)):
    if (string[i].isalpha()):
        alphabets += 1
    elif (string[i].isdigit()):
        digits+=1
    else:
        symbols+=1
print("number of alphabets are: ",alphabets)
print('number of digits are: ',digits)
print("number of special characters are: ",symbols)


#----------------------------------------------------------
'''SETS and TUPLES'''

domain = {101, 22.2, 'akshay', 's'}

print(domain.pop())#removes the last item from the sets
print(domain)

domain.remove(22.2)# removes element 22.2 from set if it does not exist then it throws an error
print(domain.discard(102))#removes element 101 from set if it does not exist then there is no error
print(domain)
cl = domain.clear()#clears the whole set
print(cl)

#adding to sets
domain.add(31)
print(domain)
attributes = set()
attributes.add('players')
attributes.add('coach')
attributes.add('team name')
print(attributes)# printing the attributes


#sorting attributes
print("Before sorting: ",list(attributes))
sorted_domain = sorted(attributes, reverse=True)#using sorted function to sort the elements
print("After sorting:",list(sorted_domain))


#packing and unpacking 
tuples = (101, 'akshay', 'MCA')
(register, name, course) = tuples
print(register)#unpacking an element from the packed set


#count characters
domain_characters = ('p','r','o','g','r','a','m','s','s','s')
char_count = {}
for char in domain_characters:
    char_count[char] = char_count.get(char, 0) + 1

for char, count in char_count.items():
    print(char, count)


#slicing
domain_name = ('Sports Management')
print(domain_name[:])
print(domain_name[-1])
print(domain_name[0:6])
print(domain_name[::-1])


