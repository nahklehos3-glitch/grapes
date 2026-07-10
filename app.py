from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
import platform

options = webdriver.ChromeOptions()

options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

options.binary_location = "/usr/bin/chromium"


print("Python:", platform.python_version())
print("OS:", platform.platform())

print("Checking Chrome...")
os.system("google-chrome --version")

print("Checking Chromium...")
os.system("chromium --version")

print("Checking Chromium Browser...")
os.system("chromium-browser --version")

print("Creating driver...")
service = Service(executable_path="/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)
print("Driver created!")








print(driver.current_url)
print(driver.title)


# Demo login page
driver.get("https://discord.com/login")
time.sleep(10)

print("EMAIL exists:", bool(os.getenv("APP_EMAIL")))
print("PASSWORD exists:", bool(os.getenv("APP_PASSWORD")))

email = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input[aria-label="Email or Phone Number"]')
    )
)

password = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input[name="password"]')
    )
)

email.clear()
email.send_keys(os.getenv("APP_EMAIL"))

password.clear()
password.send_keys(os.getenv("APP_PASSWORD"))
password.send_keys(Keys.ENTER)

print("Login submitted")

time.sleep(15)

print("URL after login:", driver.current_url)
print("Title after login:", driver.title)

driver.save_screenshot("debug.png")

with open("page.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Screenshot saved:", os.path.exists("debug.png"))
print("Page source length:", len(driver.page_source))
print(driver.page_source[:5000])



try:
    while True:
        
        time.sleep(10)
        driver.get("https://discord.com/channels/1487975983016316992/1487975983830007840")
        time.sleep(10)
        #textbox = driver.find_element(By.CSS_SELECTOR, '[role="textbox"]')
        textbox = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[role="textbox"]'))
)
        textbox.click()
        textbox.send_keys("/pick")
        time.sleep(1)
        textbox.send_keys(Keys.ENTER)
        time.sleep(2)
        textbox.send_keys(Keys.ENTER)
       

        # Wait 5 minutes
        time.sleep(300)

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
