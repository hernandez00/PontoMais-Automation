"""
######### Login Credentials: #########
E-mail: leonardo.hernandez@fmxsolucoes.com.br
Password: HernandeZ!#%5
"""

"""
Login field: 
//android.view.ViewGroup[@content-desc="Campo de login"]/android.widget.EditText

Password field:
//android.view.ViewGroup[@content-desc="Campo de senha"]/android.widget.EditText

Login button:
//android.view.ViewGroup[@content-desc="Botão de envio"]
"""

from appium.webdriver.common.mobileby   import MobileBy
class LoginLocators(object):
    FIELD_LOGIN = (
        MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Campo de login']/android.widget.EditText")
    FIELD_PASSWORD = (
        MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Campo de senha']/android.widget.EditText")
    BUTTON_LOGIN = (
        MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Botão de envio']")