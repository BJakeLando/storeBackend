

# LISTS

from tokenize import Name


def list_1():
    print("list 1")

    colors = ["red", "green", "blue"]
    print(colors)
    print(type(colors))

    # add element
    colors.append("white")

    #count/ length

    print(len(colors))

    # delete
    #by index

    del colors[0]

    #by value
    colors.remove("white")

    #travel a list
    for x in colors:
        print(x)




def list_2():
    print (" list 2")
    nums = [12,34,-1,53,12,88,55,32,-123,9,1,78,1,-4,11,5,6,4,678,4,883,0, -13, 12, 92]

    # print all numbers that are lower than 0
    for n in nums:
        if n < 0:
            print(n)

    #print the sum of all numbers
    # count numbers grater than 50
    #  count numbers between 10-50

    total = 0
    count = 0
    between = 0

    for num in nums:
        total = total + num

        if num < 50:
            count += 1

        if num >=10 and num <=50:
            between += 1

        

    print (total)
    print ("There are " + str(count) + " greater than 50")
    print(between)


list_2()

# Dictionary: similar to objects in JS, keys are strings and values are anything

def dict_1():
    me = {
        "name": "Brandon",
        "last": "Landers",
        "age": "29",
        "hobbies": [],
        "address": {
            "streeet": "Baker",
            "num": "22B",
            "city": "London",
            "zip": "123"
        }
    }

    print(me)
    print(type(me))

    #add pairs
    me["preffered_color"]= "blue"

    #modify existing information
    me["age"]= 99

    #delete
    del me["hobbies"]

    print(me)
    

    #read

    name = me["name"]
    print(name)


    address = me["address"]
    print(address["street"] + "" + address["num"] + ", " + address["city"])


#start
dict_1()

# homwork: string formatting python (f string)