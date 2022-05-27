
def hello(name,age):
    year=2022-age
   
  
    return(f"Hello {name},you're were born in {year}")
    
def my_country(country="Sweden",student="Shirleen"):
    return(f"Hello {student} you are from {country}")

def greet_multiple(*names):
    for name in names:
        print(f"Hello {name}")
    
#    Write a function that accepts any number of intergers and returns the sum of all of them

def add_int(*int):
    n=0
    for num in int:
        n+=num
        print(n)

    
    
def multiply(*int):
    ans=1
    for num in int:
        ans*=num
        return(ans)

def greet(**kwargs):
    keys=kwargs.keys()

    if "country" in keys:
      print(f"Hello {kwargs['name']} you are from {kwargs['country']}")

    elif "age" in keys:
      year=2022-kwargs["age"]
    print(f"Hello {kwargs['name']} you were born in {year}")
   
        
  
def sum_and_greet(*args,**kwargs):
   
    sum=0
    for num in args:
        sum+=num
    keys=kwargs.keys()

    if "name" in keys:
     print(f"Hello {kwargs['name']} the answer is {sum}")

    # elif "country" in keys:
    #     print(f"Hello you are from {kwargs['countrur favourite food is ['food']")y']} and the answer is {sum}")
   

    elif not keys:
        print(f"Hello anonymous the answer is {sum}")




def sum(*args):
    num=0
    for nums in args:
        num+=nums
    return(num)



def say_hi(*args):
    return(f"Hello ['name'] and you are from ['country'] and your favourite food is ['food']")