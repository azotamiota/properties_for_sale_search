import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
import re
import constants

class Onthemarket(webdriver.Chrome):
    def __init__(self, browser='C:\\webdrivers', teardown=False):
        self.browser = browser
        self.teardown = teardown
        #super().__init__()
        super(Onthemarket, self).__init__()
        self.implicitly_wait(30)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def front_page(self):
        #self.get('chrome://settings/')
        #self.execute_script('chrome.settingsPrivate.setDefaultZoom(0.75);')
        self.get('https://www.onthemarket.com/')
        self.maximize_window()
        cookies = self.find_element_by_css_selector('#cookie-notification > p > span.cookie-actions > button > span')
        cookies.click()

    def location(self, loc):
        self.loc = loc
        location = self.find_element_by_id("search-location-sale")
        location.send_keys(self.loc)
        time.sleep(1)
        first = self.find_element_by_xpath('//*[@id="homesearch-for-sale"]/div/div[1]/div/ul/li[1]')
        noresult = self.find_element_by_xpath('//*[@id="homesearch-for-sale"]/div/div[1]/div/ul/li/span')
        if noresult.text == 'No results found':
            print('No such location found. Please check your spelling, restart the program and try again')
            self.quit()
            exit()
        elif input('Location found: ' + first.text + '\nDo you want to proceed? (y/n): ').lower() == 'y':
            first.click()
            location.submit()
        else:
            self.quit()
            exit()

    def filters(self, houses, flats, bungalows, newhomes):
        filt = self.find_element_by_xpath('/ html / body / div[6] / div[4] / div[2] / div / div / div / form / div[1]')
        filt.click()
        if houses == True:
            houses = self.find_element_by_xpath('//*[@id="search-property-types"]/div/div[2]/label')
            houses.click()
        if flats == True:
            flats = self.find_element_by_xpath('//*[@id="search-property-types"]/div/div[3]/label')
            flats.click()
        if bungalows == True:
            bungalows = self.find_element_by_xpath('//*[@id="search-property-types"]/div/div[4]/label')
            bungalows.click()
        if newhomes == True:
            newhomes = Select(self.find_element_by_id('new-home-flag'))
            newhomes.select_by_value('T')
        retirementEx = self.find_element_by_xpath('/html/body/div[6]/div[4]/div[2]/div/div/div/form/div[4]/div[2]/div[3]/div[2]/div[1]/div[2]/div[2]/div[5]/div/select/option[2]')
        retirementEx.click()
        sharedEx = self.find_element_by_xpath('/html/body/div[6]/div[4]/div[2]/div/div/div/form/div[4]/div[2]/div[3]/div[2]/div[1]/div[2]/div[2]/div[6]/div/select/option[2]')
        sharedEx.click()
        apply = self.find_element_by_xpath('/html/body/div[6]/div[4]/div[2]/div/div/div/form/div[4]/div[2]/div[3]/div[2]/div[3]/button')
        apply.click()

    def min_price(self, number):
        price = self.find_element_by_id('price_min')
        price.click()
        priceBox = Select(self.find_element_by_id('price_min'))
        try:
            priceBox.select_by_value(f'{number}')
        except:
            pass

    def max_price(self, number):
        price = self.find_element_by_id('price_max')
        price.click()
        priceBox = Select(self.find_element_by_id('price_max'))
        priceBox.select_by_value(f'{number}')

    def bedrooms(self, number):
        bedrooms = Select(self.find_element_by_id('min-bedrooms'))
        bedrooms.select_by_value(f'{number}')
        #bedrooms = self.find_element_by_xpath(f'/html/body/div[6]/div[4]/div[2]/div/div/div/form/div[4]/div[2]/div[3]/div[1]/div/select/option[{number+2}]')
        #bedrooms.click()

    def distance(self, miles):
        drop = Select(self.find_element_by_id('radius'))
        try:
            drop.select_by_value(miles)
        except:
            drop.select_by_visible_text('+ 0 miles')


    #def listview(self):
    #    listview = self.find_element_by_class_name('icon-list-inactive-instance')
    #    listview.click()

    def sortLoHi(self):
        sortbutton = self.find_element_by_class_name('dropdownarrow')
        sortbutton.click()
        time.sleep(1)
        LotoHi = self.find_element_by_link_text('Lowest price')
        LotoHi.click()
        time.sleep(2)

    def properties(self):
        if self.find_element_by_xpath('//*[@id="results"]/div/div[2]/div[1]/div/span/span').text == 'No results':
            print('No properties found. Please restart the program with different search conditions.')
            self.quit()
            exit()
        for actualProperty in range(1, 25):
            try:
                propertDetails = self.find_element_by_xpath(
                    f'//*[@id="properties"]/li[{actualProperty}]/div[2]/p[2]/span[1]/a'
                )
                propertPhotos = self.find_element_by_xpath(
                f'//*[@id="properties"]/li[{actualProperty}]/div[1]/div[1]/a/div/div/picture/img'
                )
                details = propertDetails.text
                propertPhotos.click()
            except:
                print('First method to click failed')
                try:
                    page = self.find_element_by_tag_name('body')
                    for i in range(1, 8):
                        page.send_keys(Keys.PAGE_DOWN)
                        time.sleep(2)
                    propert = self.find_element_by_xpath(
                        f'//*[@id="properties"]/li[{actualProperty}]/div[1]/div[1]/a/div/div/picture/img'
                    )
                    propert.click()
                    print("Second method to click succeeded")
                except:
                    print('Problem occurred while loading the next property... \
                          \nPage number: ' + str(constants.pagenumber) + ', Property number: ' + str(actualProperty))
                    continue
            #time.sleep(2)
            taburl = self.current_url
            try:
                showMore = self.find_element_by_class_name('show-more')
                showMore.click()
            except:
                pass

            try:
                pageElem = self.find_element_by_class_name('main-col')
                pageText = pageElem.text
                leaseholdRegEx = re.search('Tenure: Leasehold+', pageText, re.IGNORECASE)
                freeholdRegEx = re.search('Tenure: Freehold+', pageText, re.IGNORECASE)
                sharedOS = re.search('Shared\s*Ownership+', pageText, re.IGNORECASE)
                pricebox = self.find_element_by_class_name('price-data')
                priceboxText = pricebox.text
                priceRegEx = re.findall('£\d*,*\d\d+,\d{3}', priceboxText)
                if len(priceRegEx) == 0:
                    price = 'Price was not found'
                else:
                    price = ('Price: ' + str(priceRegEx[0]))
                if leaseholdRegEx:
                    print(
                        'Leasehold property: ' + taburl + '\t' + price + '\tDetails: ' + details + '\nPage:' + str(constants.pagenumber) + ' Property no.: ' + str(actualProperty))
                elif freeholdRegEx:
                    print('Freehold property: ' + taburl + '\t' + price + '\tDetails: ' + details + '\nPage: ' + str(constants.pagenumber) + ' Property no.: ' + str(actualProperty))
                else:
                    print('Not detected if freehold or leasehold: ' + taburl + '\t' + price + '\tDetails: ' + details + '\nPage: ' + str(constants.pagenumber) + ' Property no.: ' + str(actualProperty))
                if sharedOS:
                    print('Shared Ownership mentioned...' + taburl + '\t' + price + '\tDetails: ' + details + '\nPage: ' + str(constants.pagenumber) + ' Property no.: ' + str(actualProperty))
            except:
                print('Failed gaining information' + '\nPage: ' + str(constants.pagenumber) + ' Property no.: ' + str(actualProperty))
                pass
            self.execute_script("window.history.go(-1)")

            try:
                # Possible pop-up window to close
                closeicon = self.find_element_by_id('modal-close')
                closeicon.click()
            except:
                pass

        try:
            nextButton = self.find_element_by_class_name('svg-icon.icon-small-arrow-right')
            nextButton.click()
            constants.pagenumber += 1
            self.properties()
        except:
            print('No more properties...')