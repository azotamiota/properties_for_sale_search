from onthemarket_automation import Onthemarket
import parameters

print('\nThis program will detect if properties for sale in the UK \nadvertised at \
www.onthemarket.com are leasehold, freehold or unknown.\n')

with Onthemarket() as bot:
    bot.front_page()
    location = parameters.setLocation()
    bot.location(location)
    houses, flats, bungalows, newhomes = parameters.setPropertyType()
    distance = parameters.setDistance()
    minprice = parameters.setMinPrice()
    maxprice = parameters.setMaxPrice()
    bedrooms = parameters.setBedrooms()
    bot.filters(houses, flats, bungalows, newhomes)
    bot.distance(distance)
    bot.min_price(minprice)
    bot.max_price(maxprice)
    bot.bedrooms(bedrooms)
    #bot.listview()
    bot.sortLoHi()
    bot.properties()

