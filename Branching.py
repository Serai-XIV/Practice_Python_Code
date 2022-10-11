Menu = ("Davy's auto shop services\n" #outputs a menu
               "Oil change -- $35\n"
               "Tire rotation -- $19\n"
               'Car wash -- $7\n'
               'Car wax -- $12\n')

print(Menu)

Service1 = input('Select first service:\n')
Service2 = input('Select second service:\n')
Service_money = int()
Service_money_2 = int()

Services = {'Cost of oil change': 35, 
'Cost of tire rotation': 19, 
'Cost of car wash': 7,
'Cost of wax': 12}

if Service1 == 'Oil change':
    Service_money = Services['Cost of oil change']
elif Service1 == 'Tire rotation':
    Service_money = Services['Cost of tire rotation']
elif Service1 == 'Car wash':
    Service_money = Services['Cost of car wash']
elif Service1 == 'Car wax':
    Service_money = Services['Cost of wax']
elif Service1 == '-':
    Service_money = 0
    Service1= 'No service'
else:
    print(f'You entered: {Service1}')
    print('Error: Requested service is not recognized')

if Service2 == 'Oil change':
    Service_money_2 = Services['Cost of oil change']
elif Service2 == 'Tire rotation':
    Service_money_2 = Services['Cost of tire rotation']
elif Service2 == 'Car wash':
    Service_money_2 = Services['Cost of car wash']
elif Service2 == 'Car wax':
    Service_money_2 = Services['Cost of wax']
elif Service2 == '-':
    Service_money_2 = 0
    Service2= "No service"

print()
print("Davy's auto shop invoice\n")
if Service1 == 'No service':
    print(f'Service 1: {Service1}')
else:
    print(f'Service 1: {Service1}, ${Service_money}')
if Service2 == 'No service':
    print(f'Service 2: {Service2}\n')
else:
    print(f'Service 2: {Service2}, ${Service_money_2}\n')
print(f'Total: ${Service_money + Service_money_2}')