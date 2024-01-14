# a = b = False
# if not a and not b:
#     print ("Result is TRUE")

# age = input("How old are you? ")
# try:
#     age = int(age)
#     if age >= 18:
#         print("You are adult.")
#     else:
#         print("You are infant")
# except ValueError:
#     print(f"{age} is not a number")

# def is_even(num: int) -> bool:
#     return num % 2 == 0

# check_even = is_even(age)
# print(check_even)  # Виведе: True

# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник  
#             codes[ch] = ord(ch)  
#     return codes
# result = string_to_codes("Hello world!")
# print(result)

# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result

# print(factorial(6))

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for char in message:
#     if char == search:
#         result =result +1
# print (result)

# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool // quantity
#     print (chunk)
# except ZeroDivisionError:
#     print('Divide by zero completed!')

# def invite_to_event(username):
#     return f"Dear {username}, we have the honour to invite you to our event"

# print(invite_to_event("Alex"))

# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#         price = price * (1 - discount)
#     apply_discount()   
#     return price
# new = discount_price(10, 0.5)
# print (new)

# def get_fullname(first_name, last_name, middle_name=""):
#     if middle_name:
#         return f"{first_name} {middle_name} {last_name}"
#     else:
#         return f"{first_name} {last_name}"
# print (get_fullname("FN", "SN"))

# def format_string(string, length):
#     if len(string) < length:
#         spaces = " " * (length - len(string))
#         return spaces + string
#     else:
#         return string
# print (format_string("abaa", 15))

# def first(size, *args):
#     numb = 0
#     for i in args:
#         numb +=1
#     return size + numb

    
# def second(size, **kwargs):
#     numb = 0
#     for i in kwargs:
#         numb +=1
#     return size + numb
# print (first(2, "asd", 2))
# print (second(1, name="Alice", age=25))

# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)

# def number_of_groups(n, k):
#     return factorial (n) // (factorial(n-k)*factorial(k))

# print (number_of_groups(50, 7))
