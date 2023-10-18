
def hello():
    print("Hello, user!") 

def pack(a,b,c):
    return [a,b,c]

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My lunchbox is empty!")
    else:
      for i in range(len(my_list)):
          if i == 0:
              print(f"First I eat {my_list[0]}")
          else:
              print(f"Next I eat {my_list[i]}")

def arb_args(*args):
    for a in args:
        print(a)

def inner_func(x,y):
    def add():
        return x+y
    def subtract():
        return x-y
    print(add()+subtract())

def lunch_lady(name, lunch="Mystery Meat"):
    print(name, lunch)

def sum_n_product(x,y):
    return x+y,x*y

alias_arb_args = arb_args

def arb_mean(*args):
    if len(args) == 0:
        print("No arguments provided")
    else:
        print(sum(args) / len(args))

def arb_longest_string(*args):
    characters_long = 0
    longest_string = ""
    for a in args:
        if len(a) > characters_long:
            characters_long = len(a)
            longest_string = a
    return longest_string




hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])
arb_args(1,2,3)
inner_func(4,9)
lunch_lady("zack","chocolate")
lunch_lady("dave")
print(sum_n_product(6,7))
alias_arb_args(4,3,2)
arb_mean(4,5,6,1,2,3)
print(arb_longest_string("a", "ab", "abc", "abcd"))

