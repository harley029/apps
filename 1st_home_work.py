name = 'Alex'
age = 25

rate = 1.68
value_day = 20
value_night = 30
payment = rate * value_day + (rate / 2 * value_night)

first_name = 'Alex'
last_name = 'Harley'
full_name = first_name + ' ' + last_name

length=2.75
width=1.75
area=length*width
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
print (show)

length = "2.75"
width = "1.75"
area = float(length) * float(width)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
print (show)

name = input("Your name? ")
email = input("Your e-mail& ")
age = int(input("Your age& "))
height = float(input("Your height& "))
is_active = bool(input())

my_list = [2024, 3.12]
some_data = ['Python']
my_list.extend(some_data)
my_list.insert(1, 'Python')
my_list.reverse()
print (my_list)

cat = {}
info = {"status": "vaccinated", "breed": True}
cat = {"nick":"Simon", "age": 7, "characteristics": ["ввічливий", "кусаёться"]}
age = cat.get("age")
cat.update(info)