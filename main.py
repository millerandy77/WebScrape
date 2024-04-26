# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import pandas as pd 
# driver = webdriver.Safari()
# agencies = []

# upletter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# lowletter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# for i in range(upletter):   
#     page = lowletter[i] + "#" + upletter[i]
#     print(page)
#     driver.get("https://www.usa.gov/agency-index" + page)
    
#     accordion = driver.find_elements(By.XPATH, "here")
#     title_table = driver.find_elements(By.XPATH, "here")
    
#     agency = []
#     agency.append(page)
#     zip_object = zip(accordion, title_table)
#     for agent_num, title_num in zip_object:
#         employee.append(agent_num.text)
#         employee.append(title_num.text)

#     employees.append(employee)

# df_data = pd.DataFrame(employees)
# df_data.to_excel('hhs_directoryTest.xlsx', index = False)

#     # print (len(employee))
#     # print ("\n")
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys

# Initialize the web driver (use appropriate driver for your browser)
driver = webdriver.Safari()

#info for contact forms
name = "Andrew Miller"
current_name = ""
email = "andy@slantball.com"
message = ", Thank you for your time. We are reaching out to introduce a new sport that could be a fun activity for your PE classes!"
# Create a list to store company data
employees = []

# Loop through the pages
for page in range(0,26):
    og_page = "https://www.fcps.edu/schools-centers?page=" + str(page)
    driver.get(og_page)
    titles = driver.find_elements(By.CSS_SELECTOR, '.view__row .node__title')

    # Extract the text from each title and print
    for title in titles:
        title_text = title.text.strip()
        link_element = title.find_element(By.TAG_NAME, 'a')
        link = link_element.get_attribute('href')
        driver.get(link)
        staff_directory_button = driver.find_element(By.XPATH,"//a[contains(@class, 'button') and contains(text(), 'Staff Directory')]")
        # Get the href attribute of the button
        staff_directory_link = staff_directory_button.get_attribute("href")
        driver.get(staff_directory_link)
        search_input = driver.find_element(By.ID,"edit-keywords")

        # Clear any existing text in the search input
        search_input.clear()

        # Type "Physical Education" into the search input
        search_input.send_keys("Physical Education")

        # Press Enter to perform the search
        search_input.send_keys(Keys.RETURN)

        # Wait for a moment to allow the page to load
        time.sleep(2)
        table_rows = driver.find_elements(By.CSS_SELECTOR,"tbody tr")
        i = 1
        # Iterate through each table row
        for row in table_rows:
            employee_section = row.find_element(By.TAG_NAME, "a")
            employee_link = employee_section.get_attribute("href")
            current_name = driver.find_element(By.XPATH,"//tbody/tr["+ str(i) + "]/td/a[2][@hreflang='en']")
            current_name = current_name.text
            driver2 = webdriver.Firefox()
            driver2.get(employee_link)
            time.sleep(2)
            name_input = driver2.find_element(By.ID,"edit-contact-name")
            name_input.send_keys(name)
            email_input = driver2.find_element(By.ID,"edit-contact-email")
            email_input.send_keys(email)
            message_input = driver2.find_element(By.ID,"edit-contact-message")
            custom_message = current_name + message
            message_input.send_keys(custom_message)
            i += 1
        print(title_text)
        
    # Extract information from each company data row
    # for employee in list:

    #     # Create a dictionary to store the company information
    #     employee_info = {
    #         'Name': teachname,
    #         'EAddress': address,
    #         'Phone': phone
    #     }

    #     # Append the dictionary to the list of companies
    #     employees.append(company_info)

# Close the web driver
driver.quit()

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(employees)

# Print or save the DataFrame as needed
print(df)
df_data = pd.DataFrame(employees, columns=["Name", "EAddress", "Phone"])
# Save the data to an Excel file
df_data.to_excel('teachers.xlsx', index=False)

# Quit the web driver
driver.quit()