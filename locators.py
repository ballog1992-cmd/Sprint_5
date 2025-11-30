from selenium.webdriver.common.by import By


class Locators:
    # Для регистрации
    # Поле имя в форме регестрации
    REG_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле email в форме регестрации
    REG_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле пароль в форме регестрации
    REG_PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Кнопка 'Зарегестрироваться' в форме регестрации
    REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Ошибка при неверном пароле
    ERROR_PASSWORD = (By.CSS_SELECTOR, ".input__error.text_type_main-default")

    # Для входа зарегистрированным пользователем
    # Кнопка 'Войти в аккаунт' на главной странице
    BUTTON_TRANSFER_LOGIN_PAGE = (By.XPATH,
        "//button[contains(text(), 'Войти в аккаунт')]")
    # Кнопка 'Оформить заказ' на главной странице,после успешной авторизации
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    # Ссылка 'Личный Кабинет'
    ACCOUNT_LINK = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and @href='/account']")
    # Поле имя в форме входа
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле пароль в форме входа
    PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Кнопка 'Войти' в форме входа
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    # Ссылка 'Зарегестрироваться' в форме входа
    REG_BUTTON_TRANSFER_LOGIN_PAGE = (By.XPATH, "//a[text()='Войти']")
    # Ссылка 'Войти' в форме входа
    PASSWORD_BUTTON_TRANFER_LOGIN_PAGE = (By.XPATH, "//a[text()='Войти']")

    # Для личного кабинета

    # Кнопка 'Выйти' в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

    # Переход в конструктор

    CLICK_THE_LOGO_OF_CONSTRUCTOR = (By.XPATH,"//div[contains(@class, 'AppHeader_header__logo__2D0X2')]/a[@href='/']")
    CONSTRUCTOR_BUTTON = (By.XPATH,"//a[@class='AppHeader_header__link__3D_hX' and @href='/']")
    # Вкладки ингридиентов
    # Раздел "Булки"
    TAB_BUNS = (By.XPATH, './/span[text()="Булки"]')
    # Раздел "Соусы"
    TAB_SAUSES = (By.XPATH, './/span[text()="Соусы"]')
    # Раздел "Начинки"
    TAB_STUFFING = (By.XPATH, './/span[text()="Начинки"]')
