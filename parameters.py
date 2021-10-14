import constants

def setPropertyType():
    print('\nPlease set types of properties you want to include the search')
    try:
        houses = input('\nHouses (detached, semi-detached, terraced, caravans)? (y/n): ').lower()
        if houses == 'y':
            houses = True
        else:
            houses = False
        flats = input('Flats / apartments (y/n): ').lower()
        if flats == 'y':
            flats = True
        else:
            flats = False
        bungalows = input('Bungalows? (y/n): ').lower()
        if bungalows == 'y':
            bungalows = True
        else:
            bungalows = False
        newhomes = input('New homes only? (y/n): ').lower()
        if newhomes == 'y':
            newhomes = True
        else:
            newhomes = False


        return houses, flats, bungalows, newhomes

    except:
        print('Something went wrong, try again')
        setPropertyType()

def setLocation():
    try:
        location = input('Location of the property in the UK \x1B[3m(e.g.: UK, Scotland, Greater Manchester, Liverpool):\x1B[0m ')
        location = location + ' '
        if not location.isascii():
            raise
    except:
        print('Invalid input, please try again')
        setLocation()
    return location

def setDistance():
    options = [0.0, 0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 7.5, 10.0, 15.0, 20.0, 30.0, 40.0]
    try:
        distance = input('Set the search area around the chosen location in miles (0 - 40): ')
        distance = float(distance)
        if distance < 0.0 or distance > 40.0:
            raise
        while distance not in options:
            distance = round(distance, 2)
            distance -= 0.05
        distance = str(distance)

    except:
        print('Invalid input, please try again')
        setDistance()
    return distance

def setMaxPrice():
    try:
        maxprice = input('Set the maximum price of the property (£10,000 - £15,000,000 or leave blank if any): ')
        if maxprice == '':
            pass
        elif maxprice != '':
            maxprice = maxprice.replace(',', '')
            maxprice = maxprice.replace('.','')
            maxprice = maxprice.replace('£', '')
            maxprice = int(maxprice)
            if maxprice < 10000 or maxprice > 15000000:
                raise
            else:
                maxprice = round(maxprice, -4)
            while maxprice not in constants.price_options:
                maxprice -= 10000
        print(maxprice)
    except:
        print('Invalid input, please try again')
        setMaxPrice()
    return maxprice

def setMinPrice():
    try:
        minprice = input('Set the minimum price of the property (£10,000 - £15,000,000 or leave blank if any): ')
        if minprice == '':
            pass
        elif minprice != '':
            minprice = minprice.replace(',', '')
            minprice = minprice.replace('.','')
            minprice = minprice.replace('£', '')
            minprice = int(minprice)
            if minprice < 10000 or minprice > 15000000:
                raise
            else:
                minprice = round(minprice, -4)
            while minprice not in constants.price_options:
                minprice -= 10000
        print(minprice)
    except:
        print('Invalid input, please try again')
        setMinPrice()
    return minprice

def setBedrooms():
    try:
        bedrooms = int(input('Set the number on minimum bedrooms 1 - 10 (0 for Studios): '))
        if bedrooms < 0 or bedrooms > 10:
            raise
    except:
        print('Invalid input, please try again')
        setBedrooms()
    return bedrooms