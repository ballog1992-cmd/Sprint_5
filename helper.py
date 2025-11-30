# from faker import Faker

# faker = Faker()


# def generate_registration_data():
#     name = faker.first_name()
#     email = faker.email()
#     password = faker.password(length=6)

#     return name, email, password

from selenium import webdriver

def get_chromedriver_version():
    driver = webdriver.Chrome()
    try:
        version = driver.capabilities['chrome']['chromedriverVersion']
        print(f"ChromeDriver version: {version}")
    finally:
        driver.quit()

get_chromedriver_version()