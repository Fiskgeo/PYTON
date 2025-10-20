from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)
driver.implicitly_wait(20)

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')


WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Done"))




find = driver.find_element(By.CSS_SELECTOR, "#award")
f = find.get_attribute("src")
print(f)
driver.quit()