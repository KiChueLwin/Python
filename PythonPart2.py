# Tuple packing 
students_marks = 200, 560, 435 # without brackets # order structure # Tuple is imutable as they cannot substitute value like list
print(type(students_marks))


# Tuple unpacking 
studentone_mark, studenttwo_mark, studentthree_mark = students_marks
print(f"Student one's mark is {studentone_mark}")
print(f"Student two's mark is {studenttwo_mark}")
print(f"Student three's mark is {studentthree_mark}")

# Packing
person = ("Ki", 21, "Cloud Engineer")

# Unpacking
name, age, job = person

print(name)  # Output: Ki
print(age)   # Output: 21
print(job)   # Output: Cloud Engineer



#immutable but it ca create new tuple with previous ones
tuple1 = 2,3,4
tuple2 = 2,4,4
tuple3 = tuple1 + tuple2
print(tuple3)



# Dictionary 
books = ()  # This is tuple
pens = []  # This is list
People = {} # This is dictionary

# Dictionary                   # unorder data strure: have to call key instead od index
Records = {"Mg Mg": 2,
           "Aung Aung": 4,     # This is how declare dictionary with key : value pair 
           "Lin Lin" : 6,
           "Lin Lin": 8}       # if you put the same key twice, it will output the last one ignoring the first one 
print(Records)
 


 # creating dictionary with dict() constructor 
phone_number = dict()
phone_number["Aung Aung"] = 9865544
phone_number["Mg Mg"] = 8766422
phone_number["Min Min"] = 625432               # adding value in blank dictionary
print(type(phone_number))
print(phone_number)



 
 # Nested Dictionary 
 # Can write list <== list, list <== dict, dict <== list, dict <== dict
books_record = [
    {                                        # list <== dict
        "Author" : 'U Mya', 
        "Name" : 'Data structure',
        "Date" : '2004'
                                                
    },

    {
        "Author" : 'U La',
        "Name" : 'Python',
        "Date" : '2001'
    }
  
 ]
print(books_record[0]["Name"])
print(books_record[1]["Date"])




# dict <== dict
books_history = {"Chit Oo Nyo" :{"read_book": "Data Science"}}
print(books_history["Chit Oo Nyo"])
books_history["Chit Oo Nyo"] = {"unread_book" : "Java"}
print(books_history["Chit Oo Nyo"])

books_history = {"Chit Oo Nyo": {"read_book": "Data Science"}}

# Update instead of overwrite
books_history["Chit Oo Nyo"].update({"unread_book": "Java"})

print(books_history["Chit Oo Nyo"])


# adding 
books_history ["U naing"] = {"read_book" : "Script writing "}
print(books_history)

# remove 
del(books_history["U naing"])
print(books_history)


# Checking key exsitance using "in" keyword (return with boolean)
print("Chit Oo Nyo" in books_history )
print(" U Paing" in books_history)
