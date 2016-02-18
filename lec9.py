import sys

try:
    this_number = int(sys.argv[1])
except ValueError:
    print("Gib integer pls.")
    sys.exit()
except IndexError:
    print("Gib more integer pls.")
    sys.exit()
except:
    print("Gib arguments pls.")
    sys.exit()

#if len(sys.argv) <2 :
#   print("Gib arguments pls.")
#   sys.exit()

search_number = int(sys.argv[1])

print (search_number)

my_list = [0,1,2,3]

print("Looking for " + str(search_number) + " in " + str(my_list))
look_in_list(this_number, my_list)

if search_number in my_list :
    print("Bitch u guessed it")
elif 8 in my_list :
    print("8 is in there lol")
else :
    print("lolno")  

msg = "u was right" if search_number in my_list else "pls stop of the ask."

print(msg)

count = 0
attention_span = 10

while count < search_number:
    print("ur number was " + str(count))
    if count > attention_span:
        print("I'm done, sweaty. :)")
        break
    count = count+1
print("Your number was actually " + str(count))

for count2 in range(attention_span):
    if (count2%2 == 0):
        continue
    print("an odd number is " + str(count2))

my_other_list = ["Ken", "Jared", "Hannah", "Dane", "Zach"]

for name in my_other_list:
    print(name + " is my friend")

sub_list = []

for number in my_list:
    sub_list.append(number*number)

print(sub_list)

square_list = [ number*number for number in my_list ]

print(square_list)

dict_of_squares = {number : number*number for number in my_list }

print(dict_of_squares)

dict_of_even_squares = {number:number*number for number in my_list if number%2 ==0}

my_file = open('lec9.py')

for line in my_file:
    print ("my_file contains: " + line.strip('\n'))

def look_in_list(search_number, my_list):
    if find_number in search_list :
        print("It there")
    elif 8 in search_list :
        print("It not but 8 is")
    else :
        print("It not")

