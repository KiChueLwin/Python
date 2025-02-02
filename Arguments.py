# positional arguments and keywords arguments
# *args and **kwargs can be used to pass mutiple arguments

def add(*args):   # type is tuple
    result = 0
    for i in args:
        result += i
    return result
    
a = add(1,2,3,4,5)
print(a)

def concatnation(**kwargs):
    final_str = f"{kwargs['name']} is {kwargs['age']} years old and lives in {kwargs['city']} , {kwargs['country']}"
    return final_str  # return as dictionary type

output = concatnation(name= 'Ko Ko' , age = 23, city = 'Yangon' , country = 'Myanmar' )
print(output)  


# ordering 
# positional arguments
# multiple positional arguments
# mutiple keywords arguments

def my_function(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

my_function(1,2,3,4,5,6,7,8,name="Su Su ", age = '24')
