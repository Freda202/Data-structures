# list of available cars and their prices
typeOfCars={'Nissan':25000,'Jaguar':34000,'Range Rover':95000,'Lamborghini':100000,'Ford':23000,'BMW':50000,\
'Chevolet':15000,'Toyota':20000,'Kia':18000,'Picanto':15000,'Volvo':15600,'Hyundai':35000,'Mazda':45000,\
'Subaru':20000,'Acura':15000,'Lexus':23000,'Chrysler':25000,'Ferrari':150000,'Infiniti':35000,'Jeep':45000,\
'Audi':30000,'Corolla':26130,'SUV':36000,'G-Wagon':50000,'Porsche':35000}
# get user input for car name
carName = input('Enter your preferred car_name')
# check if car name is in the list of available cars
if carName in typeOfCars:
   print('Yes its available')
   #if car name is present, get the price
   car_price=typeOfCars[carName]
   print(f'The price of{carName}is Ghana cedis{car_price}')
else:
    print(f'The price of {carName} is not available.')
    
#github link:https://github.com/Freda202
#index number 6948521