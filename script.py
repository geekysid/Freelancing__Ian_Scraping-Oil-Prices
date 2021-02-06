#!/usr/local/bin/python3


# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                       #
#   Name: Siddhant Shah                                 #
#   Date: 30/01/2021                                    #
#   Desc: SCRAPER FOR OIL PRICE FROM MULTIPLE SOURCE    #
#   Email: siddhant.shah.1986@gmail.com                 #
#                                                       #
# # # # # # # # # # # # # # # # # # # # # # # # # #     #


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from colorama import init
from termcolor import cprint
import time, json, os, sys


# global variables
DATA = {}
CONFIG_DATA = {}
WAIT_TIME = 10
BROWSER = None


# just fro decoration
def intro_deco():
    print("\n\n")
    print("  ", '#'*50)
    print("  ", "#                                                #")
    print("  ", "#   SCRAPER FOR OIL PRICE FROM MULTIPLE SOURCE   #")
    print("  ", "#                By: SIDDHANT SHAH               #")
    print("  ", "#                  Dt: 30-01-2021                #")
    print("  ", "#          siddhant.shah.1986@gmail.com          #")
    print("  ", "#        **Just for Educational Purpose**        #")
    print("  ", "#                                                #")
    print("  ", '#'*50)
    print()


# getting information from config file
def initializer():
    global CONFIG_DATA
    global DATA

    if os.path.exists(f'{os.getcwd()}/config_selector.json'):
        with open (f'{os.getcwd()}/config_selector.json', 'r') as r:
            CONFIG_DATA = json.load(r)

    if os.path.exists(f'{os.getcwd()}/Data/output.json'):
        with open (f'{os.getcwd()}/Data/output.json', 'r') as r:
            DATA = json.load(r)
            # print(json.dumps(DATA, indent=4))
            # input()


# Setting up webdriver
def get_browser(headless=False):

    pathToChromeDriver = CONFIG_DATA['pathToChromeDriver']

    chrome_options = Options()

    # giving a higher resolution to headless browser so that click operation works
    if headless:
        chrome_options.headless = headless
    else:
        chrome_options.add_argument('--window-size=1920,1080')
        # chrome_options.add_argument("--start-maximized")

    browser = webdriver.Chrome(executable_path = pathToChromeDriver, options=chrome_options)

    return browser


# save Data to JSON
def save_json():
    with open('Data/output.json', 'w') as file:
        json.dump(DATA, file)


# getting element from config
def get_element(selector, base=''):
    base = BROWSER if (base == '') else base
    selector_type = list(selector.keys())[0]

    try:
        if selector_type == 'class':
            return base.find_element_by_class_name(selector[selector_type])
        elif selector_type == 'id':
            return base.find_element_by_id(selector[selector_type])
        elif selector_type == 'attribute':
            selector_tag =selector[list(selector.keys())[1]]
            return base.find_element_by_xpath(f"//{selector_tag}[{selector[selector_type]}]")
        elif selector_type == 'tag_name':
            return base.find_element_by_tag_name(selector[selector_type])
        elif selector_type == 'xpath':
            return base.find_element_by_xpath(selector[selector_type])
    except Exception as err:
        cprint(f'    [x] Exeption: Can\'t locate selector. \n{str(err)}', 'red', attrs=['bold'])
        pass


# getting elements from config
def get_elements(selector, base=''):

    base = BROWSER if (base == '') else base
    selector_type = list(selector.keys())[0]

    if selector_type == 'class':
        return base.find_elements_by_class_name(selector[selector_type])
    if selector_type == 'id':
        return base.find_elements_by_id(selector[selector_type])
    if selector_type == 'tag_name':
        return base.find_elements_by_tag_name(selector[selector_type])


# waiting for certain element on page to load
def page_load_wait(selector):
    selector_type = list(selector.keys())[0]

    try:
        if selector_type == 'id':
            WebDriverWait(BROWSER, WAIT_TIME).until(EC.visibility_of_element_located((By.ID, selector[selector_type])))
        if selector_type == 'xpath':
            WebDriverWait(BROWSER, WAIT_TIME).until(EC.visibility_of_element_located((By.XPATH, selector[selector_type])))
        return True
    except Exception as err:
        cprint(f'    [x] Exception while waiting for page to load.', 'red', attrs=['bold'])
        cprint(f'    [x] Exception: {str(err)}', 'red', attrs=['bold'])
        return False


# adding data to the json
def add_data_to_json(website, zipcode, region, price):
    global DATA

    key =  region if website == 'cheapestoil' else zipcode

    if website in DATA.keys():
        if key in DATA[website].keys():
            DATA[website][key]["price"][datetime.today().strftime('%Y-%m-%d')] = price
        else:
             DATA[website][key] = {
            "zipcode": None if website == 'cheapestoil' else zipcode,
            "region": region,
            "price": {
                datetime.today().strftime('%Y-%m-%d'): price
            }
        }
    else:
        DATA[website] = {}
        DATA[website][key] = {
            "zipcode": None if website == 'cheapestoil' else zipcode ,
            "region": region,
            "price": {
                datetime.today().strftime('%Y-%m-%d'): price
            }
        }
    save_json()


# retrieve oil prices
def get_oil_price(selectors, website):
    if page_load_wait(selectors['result_page_load_wait']):
        time.sleep(3)

        # CASH-HEATING-OIL
        if website == 'cashheatingoil':
            result_divs = get_elements(selectors['result_container'])
            price = []

            for result_div in result_divs:
                result_table = get_element(selectors['result_tables'], base=result_div)

                rows = get_elements(selectors['result_rows'], base=result_table)
                for row in rows:
                    qnty = get_elements(selectors['result_columns'], base=row)[0].text.strip()
                    # print(f'{qnty} || {qnty == "150-199"}')
                    if qnty == "150-199":
                        rate = get_elements(selectors['result_columns'], base=row)[1].text.replace('$', '').strip()
                        price.append(float(rate))

            if len(price) > 0:
                min_price = min(price)
                cprint(f'          [>>] Price for 150-199 gallons: {min_price}\n', 'yellow', attrs=['bold'])
                return min_price
                # input()

        # CHEAPEST OIL
        elif website == 'cheapestoil':
            result_divs1 = get_elements(selectors['rows_odd'])
            result_divs2 = get_elements(selectors['rows_even'])
            result_divs = [*result_divs1, *result_divs2]
            price = []

            for result_div in result_divs:
                # supplier = get_element(selectors['supplier_a'], result_div).text
                rate = float(get_element(selectors['price_span']).text.split('($')[-1].split(' per gallon')[0].strip())
                price.append(float(rate))
            if len(price) > 0:
                min_price = min(price)
                cprint(f'          [>>] Price for 150 gallons: {min_price}\n', 'yellow', attrs=['bold'])
                return min_price

        # COD-OIL
        else:
            result_div = get_element(selectors['result_page_load_wait'])
            result_lists = get_elements(selectors['result_lists'], base=result_div)

            for div in result_lists:
                text_el = get_element(selectors['result_text'], base=div)
                if text_el.text.strip() == '150-199 gallons':
                    price_el = get_element(selectors['result_price'], base=div)
                    cprint(f'          [>>] Price for 150-199 gallons: {price_el.text}\n', 'yellow', attrs=['bold'])
                    return float(price_el.text.replace('$', '').strip())
                    break
    else:
        cprint('        [x] Unable to load the result page', 'red', attrs=['bold'])
        # break


# getting laptops that are on auction
def get_data_from_website(website):
    config = CONFIG_DATA['website'][website]

    # looping for different location`
    for location in config['search_params']:
        zipcode = location['zipcode']
        region = location['region']
        selectors = config['selectors']
        valid_page_flag = True

        if website == 'cheapestoil':
            cprint(f'      [>] Searching for Zipcode: {region}', 'cyan', attrs=['bold'])
            url = location['url']
            BROWSER.get(url)

            if page_load_wait(selectors['result_page_load_wait']):
                valid_page_flag = True
            else:
                valid_page_flag = False
                cprint('        [x] Unable to load the page', 'red', attrs=['bold'])
        else:
            cprint(f'      [>] Searching for Zipcode: {zipcode} ({region})', 'cyan', attrs=['bold'])
            # going to base url
            BROWSER.get(config['url'])

            if page_load_wait(selectors['fieldset']):
                fieldset = get_element(selectors['fieldset'])
                zipcode_element = get_element(selectors['zipcode_text'], base=fieldset)
                zipcode_element.send_keys(zipcode)
                time.sleep(1)
                submit_element = get_element(selectors['zipcode_button'], base=fieldset)
                submit_element.click()
                valid_page_flag = True

            else:
                valid_page_flag = False
                cprint('        [x] Unable to load the page', 'red', attrs=['bold'])
                break

        if valid_page_flag:
            # get oil price
            price = get_oil_price(selectors, website)

            # adding data to the json
            add_data_to_json(website, zipcode, region, price)


# getting required data from website
def get_required_data():
    for website in CONFIG_DATA['website'].keys():
        cprint(f'  [+] {website.upper()}', 'blue', attrs=['bold'])
        # if website == 'codoil' or website == 'cashheatingoil':
        #     continue
        get_data_from_website(website)


# executing script only if its not imported
if __name__ == '__main__':
    try:
        init()
        intro_deco()
        initializer()
        BROWSER = get_browser(headless=False)
        get_required_data()
        BROWSER.quit()
    except Exception as error:
        cprint(f'  [+] EXCEPTION: {str(error)}', 'red', attrs=['bold'])
        input()
        if BROWSER:
            BROWSER.quit()
