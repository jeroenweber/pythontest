#item representation of a dict
string = [('limited', 1), ('all', 16), ('concept', 1), ('secondly', 1)]

d = dict(string)
#dict representation from item representation
print(d)

#create new dict from item representation with loop
my_dict = {}
for k, v in string:
  my_dict[k] = v
print(my_dict)

my_dict.update([('third',3)])
print(my_dict)

invoer = eval(input("geef value: "))

for k,v in my_dict.items():
    if v == invoer:
        print("key: " + str(k))