import time
import datetime

# ----------------------------------------------
# reverse the number
number = int(input("Number : "))
reverse_number = 0
while number != 0:
    reverse_number = reverse_number * 10
    reverse_number = reverse_number + number % 10
    number = number // 10
print(reverse_number)

# ----------------------------------------------
# perfect number
pr_num = int(input("number : "))
i = 1
number_sum = 0
while i < pr_num:
    if pr_num % i == 0:
        number_sum += i
        print(number_sum)
    i += 1
if pr_num == number_sum:
    print("perfect number")
else:
    print("not")

# ----------------------------------------------
# Read to number
ones_digits = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
ten_digits = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
hundreds = ["", "yüz", "ikiyüz", "üçyüz", "dörtyüz", "beşyüz", "altıyüz", "yediyüz", "sekizyüz", "dokuzyüz"]
thousands = ["", "bin", "ikibin", "üçbin", "dörtbin", "beşbin", "altıbin", "yedibin", "sekizbin", "dokuzbin"]


def read_for_2(writen_number):
    one_dg = writen_number % 10
    ten_dg = writen_number // 10
    return ten_digits[ten_dg] + "" + ones_digits[one_dg]


def read_for_3(writen_number):
    one_dg = writen_number % 10
    ten_dg_one = writen_number // 10
    ten_dg = ten_dg_one % 10
    hundreds_dg = ten_dg_one // 10
    return hundreds[hundreds_dg] + "" + ten_digits[ten_dg] + "" + ones_digits[one_dg]


def read_for_4(writen_number):
    one_dg = writen_number % 10
    ten_dg_one = writen_number // 10
    ten_dg = ten_dg_one % 10
    hundreds_dg_one = ten_dg_one // 10
    hundreds_dg = hundreds_dg_one % 10
    thousands_dg = hundreds_dg_one // 10
    return thousands[thousands_dg] + "" + hundreds[hundreds_dg] + "" + ten_digits[ten_dg] + "" + ones_digits[one_dg]


x = int(input("Number  : "))
print(read_for_4(x))


# ----------------------------------------------
# factorial

def factorial(y):
    factorial_start = 1
    if y == 0 or y == 1:
        return factorial_start
    else:
        while y >= 1:
            factorial_start * y
            y -= 1
        print("factorial : ", factorial_start)


# ----------------------------------------------
# Write Speed

print("Start Typing After 3 Seconds... (Enter->X)")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("Start !")
time.sleep(1)
f_time = datetime.datetime.now()

write = input("Typing Area : ")
l_time = datetime.datetime.now()

speed = l_time - f_time
second = round(speed.total_seconds(), 2)
typing_speed = round(len(write) / second, 1)
print("Typing Speed : {}".format(second))
print(f"Word typing speed in {typing_speed} seconds ->  {second}")

# ----------------------------------------------
# Create Password
abc = "abcçdefgğhıijklmnoöprsştuüvyz "


def create_password():
    new_word = ""
    m_list = list()
    a = input("Password : ")
    a = a.lower()
    for w in range(0, len(a)):
        m_list += a[w]
    for r in range(0, len(m_list)):
        if m_list[r] == " ":
            m_list[r] = "0"
            new_one = m_list[r]
            new_word += new_one
        else:
            new = abc[abc.index(m_list[r]) + 1]
            new_word += new
    return new_word


def find_password(password):
    def_password = ""
    new_list = list()
    for lt in range(0, len(password)):
        new_list += password[lt]
        if new_list[lt] == "0":
            new_list[lt] = " "
            new = new_list[lt]
            def_password += new
        else:
            new = abc[abc.index(new_list[lt]) - 1]
            def_password += new
    return def_password


var = create_password()
print(var)
print(find_password(var))


# ----------------------------------------------
# Class


class SaveBook:
    book_sum = 0

    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        self.all_books()
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @title.deleter
    def title(self):
        del self.__title
        print("Deleted !")

    @classmethod
    def all_books(cls):
        cls.book_sum += 1


book = SaveBook("Book 1 ")
print(book.title)

book.title = "New Book Title"
print(book.title)

del book.title