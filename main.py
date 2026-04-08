# 1-m
h = input("Hujjat topshirdingizmi? ")
s = input("Suhbatdan o'tingizmi? ")
t = input("Testdan o'tingizmi? ")

if h == "Ha" and s == "Ha" and t == "Ha":
    print("Siz ishga qabul qilindingiz!")

elif h == "Yoq" and s == "Ha" and t == "Ha":
    print("Avvalo hujjatlaringizni topshiring.")

elif h == "Ha" and s == "Yoq" and t == "Ha":
    print("Suhbatdan o‘tmagansiz.")

elif h == "Ha" and s == "Ha" and t == "Yoq":
    print("Test natijalari yetarli emas.")

else:
    print("Jarayon davom etmoqda.")

# 2-m
i = input("Jumla kirit: ")

text = ""
for a in i.split():
    text += a[0]

print(text)


# 3-m
royxat = [4, 7, 2, 5, 1, 10]
print(royxat)

yangi = []

for i in range(len(royxat)):
    yangi.append(i * royxat[i])

print(yangi)


# 4-m
words = ["dasturlash", "kitob", "shunday", "kompyuter", "ilm", "maktab"]

b = ""
i = ""

for w in words:
    if len(w) > len(b):
        i = b
        b = w
    elif len(w) > len(i):
        i = w

print("1-chi:", b)
print("2-chi:", i)



# 5-m
matn = input("So‘z kiriting: ")

for i, harf in enumerate(matn, 1):
    print(i, "-", harf)


# 6-m
ism = input("Matn kirit: ")

if len(ism) <= 2:
    print(ism)
else:
    print(ism[0] + "X" * len(ism[1:-1]) + ism[-1])


#7-m
t = ('a', 'b', 'c', 'd')
print(t)

res = tuple(enumerate(t))
print(res)


# 8-m
i = ("apple", "banana", "ok")
print(i)


r = tuple(a[::-1] for a in i )
print(r)


# 9-m
d = {"a": "1", "b": "2"}
y= {}

for k, v in d.items():
    y[v] = k

print(y)



# 10-m
k = input("Hayvon kirit: ")

d = {"it": "vov", "mushuk": "miyov", "sigir": "muu"}

if k in d:
    print(d[k])
else:
    print("Bunday hayvon bazada yo‘q")


# 11-m
d = int(input("Ball kirit: "))

def ball(a):
    if 100 >= a >= 90:
        print("A")
    elif 89 >= a >= 70:
        print("B")
    elif 69 >= a >= 50:
        print("C")
    else:
        print("D")

ball(d)


# 12-m
i = input("Ism kirit: ")

def uzunlik(a):
    if i in a:
       if len(a) <= 3:
           print("Juda qisqa")
       elif  5 >= len(a) > 3:
           print("normal")
       elif len(a) >= 6:
           print("uzun")


uzunlik(i)


# 13-m
a = input("1-so‘z: ")
b = input("2-so‘z: ")

i = (lambda x, y: (x + y)[::-1])(a, b)

print(i)


# 14-m
m = int(input("Daqiqa kirit: "))

s = lambda a: a * 60

print(s(m))


#  15-m
yosh = int(input("Yosh kiriting: "))

f = lambda x: "ruxsat" if x >= 18 else "taqiqlanadi"

print(f(yosh))


# 16-m
u = input("Web manzil kiriting: ")

f = lambda x: x.endswith(".uz")

print(f(u))


# 17-m
roy = [3, 126, 4.21, 701, 99.9, 1001, 100, 7]

natija = list(filter(lambda x: 100 <= x <= 999, roy))

print(natija)


