import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://okayweather.pythonanywhere.com/dynamic"

# launch chromedriver
driver = webdriver.Chrome(shutil.which("chromedriver"))

# change the current URL to the dynamic page
driver.get(url)

# wait up to 10 seconds after the page loads,
# to make sure the button is clickable
button_css_selector = "button#getWeather"
WebDriverWait(driver, timeout=10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, button_css_selector))
)

# click the button
driver.find_element_by_css_selector(button_css_selector).click()

# wait up till 10 seconds after we've clicked the button,
# until the 'temperature' element has the text "Temperature" in it
temperature_css_selector = "p.temperature"
WebDriverWait(driver, timeout=10).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, temperature_css_selector), "Temperature"
    )
)

# find the elements we want
name_and_location = driver.find_element_by_css_selector("p.name")
temperature = driver.find_element_by_css_selector("p.temperature")

# print the text
print(name_and_location.text.strip())
print(temperature.text.strip())

# quit chromedriver
driver.quit()
