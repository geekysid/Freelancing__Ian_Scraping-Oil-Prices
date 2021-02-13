<p align="center">
    <img src="https://user-images.githubusercontent.com/59141234/93002341-ff261d00-f553-11ea-874d-19ab5cb1068f.png" height="70px" />
</p>
<h4 align="center">
    Oil Price Aggregator
</h4>
<p align="center">
    Scraper to fetch Oil prices from different websites and updates them to spreadsheet.
    <br />
    <a href="https://www.upwork.com/ab/f/contracts/262080201">
        Project Contract
    </a>
    &nbsp;&nbsp;·&nbsp;&nbsp;
    <a href="#">
        Client - Ian Markowitz
    </a>
    &nbsp;&nbsp;·&nbsp;&nbsp;
    <a href="#">
        Status - On Going
    </a>
</p>

<br />

<!-- Details of Content -->

## Table of contents

- [Prerequisite](#Prerequisite)
- [Unpacking](#Unpacking)
- [Installation Dependencies](#Installation-Dependencies)
- [Understanding Project File](#Understanding-Project-File)
- [Running The Script](#Running-The-Script)
- [Show Your Support](#Show-Your-Support)
- [Contact Me](#Contact-Me)

<br />

<!-- Prerequisite -->

## Prerequisite

    - Windows/MacOS
    - Python 3.6 or above
    - Chrome Webdriver

[Install Python on Windows 10](https://phoenixnap.com/kb/how-to-install-python-3-windows)

[Get Chrome WebDriver according to your Google Chrome Version](https://chromedriver.chromium.org/downloads)

<br />

<!-- Unpacking -->

## Unpacking

- Unzip the _OilPricesAggregator-Scrapper.zip_ in desired location. Let's assume that we unzip the file in location _Documents/OilPricesAggregator_
- After this the path of the Project lookes like _Documents/OilPricesAggregator_
- The project folder should look something like this:

![OilPriceScraper](https://user-images.githubusercontent.com/59141234/107860988-d8ed0c00-6e68-11eb-82a9-8b1358ad9b9f.png)

<!-- Instalation -->

## Installation Dependencies

- Start terminal and type below command in terminal to point to the project folder:

```
    ~$ cd Documents/OilPricesAggregator
```

- Now we need to download all the dependencies required to run the script. For this we will type below command in terminal:

```
    ~$ pip3 install -r requirements.txt
```

<!-- Understanding File -->

## Understanding Project File

#### Data Folder 🚫

All outpoutl files will be stored in this folder.

#### requirement.txt 🚫

This file contains all the dependencies that we need to install on our system. You can delete this file but its Ok to keep it there and forget that it exists.

#### script.py 🚫

This file is the main script that we need to run to get the desired output. **Please never touch this file**.

#### chomedriver.exe ⚠️

This is a chome webdriver. This is version 88.0.4324.146 and is supported by MacOs. In case you have different version of Chrome installed in your system or you have OS other than MacOs then, please replace it with the one that you will get [from here](https://chromedriver.chromium.org/downloads). Make sure you download the driver that supports your OS and have same version as that of chrome installed on your system.

#### config_selector.json ✍️

This file needs to be edited everytime you run the script and so it needs some explation...

- **pathToScript** => Path where script.exe is stored on your system.

- **pathToChromeDriver** => Path where _chromedriver.exe_ is stored.

- **google_sheet_cred** => Path to the json file having credentials for google sheets.

- **google_sheet_name** => Name of the sheet inside spreadsheet in which the data is to be saved.

- **website** => This is the list of websites from which data is to be fetched.

<!-- Google Sheet Setup -->

## Google Sheet Setup

Please watch [this video](https://www.youtube.com/watch?v=cnPlKLEGR7E&t=46s) and follow below timestamps:

- 0:10-0:30 => you create a new spreadsheet. This is the spreadsheet where the oil prices will be updated. Rename this spreadsheet as 'Oil_Prices'.

- 0:31-3:00 => setting up google drive credentials and enabling google sheet in your google account.

- At 2:30 => you have created a json file with credentials. download this file and rename this to _google_sheet_cred.json_ and place it inside GoogleSheet_Cred folder

- 3:30-3:53 => Giving permission to the google drive to access the spreadsheet.

- 3:53-\* => You can skip rest part.

<!-- Running the script -->

## Running The Script

So before running the script please make sure of two things:

- You have followed Google Sheet Stup properly.
- The pointer in terminal is pointing to the project forlder. If not then use below code:

```
    ~$ cd Documents/OilPricesAggregator
```

Now we need to enter below code to execute the script.

```
    ~$ python3 script.py
```

Now just grab yourself a pint of 🍺 and let the script do its task.

<!-- Asking for Supports -->

## Show Your Support

If you are happy with my work then please give me :star::star::star::star::star: rating and also leave really nice recommendation/feedback on upwork. This will help me a lot in getting more project. A small and happy bonus is always appreciated 🤩. Also kindly rememeber me if you have any such project or any scraping projects. <p />Thank You for giving me opportunity to work on this project.

<!-- Displaying message about me -->

## Contact Me

**Siddhant Shah** - Please feel free to connect to me in case there is any issue in the script or any changes are required. You can contact on below mentioned connects

> 🌐 [Website](https://gist.github.com/siddhantshah1986 "My Website") > &emsp;&emsp; 📮 [Mail Me](mailto:siddhant.shah.1986@gmail.com "siddhant.shah.1986@gmail.com") > &emsp;&emsp; 💹 [UpWork](https://www.upwork.com/fl/geekysid "Upwork") > &emsp;&emsp; 🌇 [Instagram](https://www.instagram.com/geekysid "Instagram") > &emsp;&emsp; 🟢 [WhatsApp](https://api.whatsapp.com/send?phone=+918584852091 "WhatsApp")
