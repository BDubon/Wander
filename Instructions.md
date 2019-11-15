

#### [Home Page](./readme.md)

# Instructions

### Here at Wander, we like our users to have a clean user expierence. 
### Below are some steps for setting up your Wander application.

#### ***1. Download the entire project from GitHub.*** 

#### ***2. Use our embedded project interepretter so pycharm doesnt give you any sill import errors.*** 

#### ***4. Run File from MAIN.py***

#### ***3. You're good to go!***

##### ***Note: this program uses MS excel to display CSVs***



## Wander has various functions. Below is a list of the functions you will encounter. 



### 1. Submit a url:

  - Copy and paste a link to an amazon product page and press submit

  - Now a graph will apear showing you visually the current and average price.

  - you will also be able to see average, current, max, and min prices as well. If you have aleardy ran this url, you can see your historical data.

  - Most importantly after pasting a url, a csv file will be created and now can be added to by updating databases (Tools > Update Database...) 
  
#### Use these URLs to see the historical data of these products:
      - https://www.amazon.com/gp/product/B01LXLTMUW
      - https://www.amazon.com/gp/product/B01ND3Z3DZ
  

### 2. Update Databases

  - Under the tools section in the top left corner lives 'Update Databases...'

  - Here you can run all of your autocrawler which will run through the existing CSVs

  - After running update your csvs will contain the most current price

  - You can set this function up with windows task scheduler and start scheduling data collection
  
  - Program will become unresponsive for a short time, as it iterates through the product pages 

### 3. Buy it Now

  - This button opens the URL's respective amazon product webpage 

### 4. Show CSV

  - This button is located in the tool bar

  - When selected, Excel will open the URL's respective information in CSV format (All of the collected Data)  

### 5. Graph

  - This autopopulates after submiting the URL

  - Displays a Red line that represents the average price of the URL's historical data

  - Displays a Blue line that represents the price according to date

  - Provides buttons with various functionalities in the bottom left of the window

### 6. Quit

  - This button exits the application 
  
  
  
#### [Home Page](./readme.md)
