# Price-tracker


This Python script does the following:

1. **Imports necessary libraries**: It imports the required libraries for web scraping, HTTP requests, data manipulation, file handling, date and time operations, delaying, and sending emails.

2. **Gets HTML from a website**: It sends an HTTP request to a specified URL, retrieves the HTML content of the webpage, and parses it using BeautifulSoup.

3. **Extracts data**: It extracts the product name and price from the HTML content.

4. **Creates a CSV file**: It creates a CSV file named 'airpods_price.csv' in the current working directory and writes the extracted data into it.

5. **Defines functions**: It defines two functions: `check_price()` to periodically fetch the product price and update the CSV file, and `send_mail()` to send an email notification if the price drops below a certain threshold.

6. **Loops through functions**: It continuously calls the `check_price()` function every 86400 seconds (1 day) and sends an email notification if the price drops below 10000.
