
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

def name_args(**kwargs):
  for k in kwargs.keys():
    print(f"{k}:{kwargs[k]}")


def all_true(iterable):
  return all(iterable)


def one_true(iterable):
  return any(iterable)


def recursive_factorial(number):
  if number <= 1:
    return 1
  else:
    return number * recursive_factorial(number-1)


def recursive_deduplicate(string,i=0):
  if len(string) <= 1 or i == len(string)-1:
    return string
  else:
    if string[i] == string[i+1]:
      return recursive_deduplicate(string[0:i]+string[i+1:],i)
    else:
      return recursive_deduplicate(string,i+1)
      

def recursive_reverse(string, i=0):
  if len(string)==0:
    return ""
  elif i == len(string)-1:
    return string[0]
  else:
    return string[-1-i] + recursive_reverse(string, i+1)


def max_num(a,b,c):
  return max([a,b,c])


def mult_list(list):
  if len(list) == 0:
    return 0

  product = list[0]

  if len(list) > 1:
    for i in list[1:]:
      product = product * i

  return product
    

def rev_string(string):
  return string[::-1]


def num_within(num,min,max):
  return num in range(min,max+1)
     

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)

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

name_args(name="Ruby", species="dog",breed="Golden Retriever",age=4)

print(all_true([True,True]))
print(all_true((True, False)))

print(one_true([True,True]))
print(one_true([False, False]))
print(one_true((True, False)))

print(recursive_factorial(3))
print(recursive_factorial(6))

print(recursive_deduplicate("aaaa"))
print(recursive_deduplicate("aaba"))
print(recursive_deduplicate("apple"))
print(recursive_deduplicate(""))

print(recursive_reverse("aaaa"))
print(recursive_reverse("aaba"))
print(recursive_reverse("apple"))
print(recursive_reverse(""))

print(max_num(1,2,3))
print(max_num(100,50,1))
print(max_num(15,30,2))

print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([15]))

print(rev_string(""))
print(rev_string("apple"))

print(num_within(3,2,4))     
print(num_within(3,1,3))     
print(num_within(10,2,5))

