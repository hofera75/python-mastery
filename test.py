from pprint import pprint

def func(a):
    a = a+ "asd"

def finc1(a):
    a.append("asd")

b = "ddd"
func(b)
print(b)

c = ["a", "b"]
finc1(c)
pprint(c)