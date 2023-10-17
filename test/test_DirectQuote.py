from time import sleep
from pageObjects.DirectQuote import DirectQuote
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from testData.homePageData import HomePageData
from selenium.webdriver.support.select import Select
import pytest
import pyautogui


class TestDirectQuote(BaseClass):
    def inflow(self):
        return DirectQuote(self.driver)

    def test_home_title(self):
        act_title = self.driver.title
        log = self.getLogger()
        log.info("Test Home Page Title Verification")
        if act_title == "Custom Die Cutting Services | On-Demand Die Cut | Rapid Die Cut":
            log = self.getLogger()
            log.info("Test Home Page Title Verification")
            assert True
            log.info("Test Home Page Title PASS")

        else:
            assert False

    def test_get_quote(self):
        a = self.inflow()
        a.get_quote().click()
        sleep(2)
        act_title1 = self.driver.title
        if act_title1 == "Instant / Direct Quote | Rapid Die Cut":
            log = self.getLogger()
            log.info("Test Get Quote Button Verification")
            assert True
            log.info("Test Get Quote Button Pass")

        else:
            assert False

    def test_get_start(self):
        a = self.inflow()
        a.clickGetStart().click()

        sleep(2)
        act_title = self.driver.title
        if act_title == "Quote Login Page | Rapid Die-Cut":
            log = self.getLogger()
            log.info("Test Get Start Button Verification")
            assert True
            log.info("Test Get Start Button Pass")
        else:
            assert False
        sleep(2)

    def test_ProceedGuest(self):
        a = self.inflow()
        a.ProceedGuest().click()
        sleep(2)
        act_title = self.driver.title
        if act_title == "Create a Quote | Rapid Die Cut":
            log = self.getLogger()
            log.info("Test Proceed Guest Button Verification")
            assert True
            log.info("Test Proceed Guest Button PASS")
        else:
            assert False
            log.info("Test Proceed Guest Button Fail")

        sleep(2)

    def test_RequireValidation(self):
        log = self.getLogger()
        log.info("Test Proceed Guest Button Verification")
        a = self.inflow()
        a.RequireValidation().click()
        sleep(2)
        a = '//input[@style="border: 1px solid red !important"]'
        b = '//div[@style="border: 1px solid red;"]'
        style1 = f"{a}|{b}"
        style = self.driver.find_elements(By.XPATH, style1)
        print("Lenghtttttt", len(style))
        if len(style) == 10:
            print("Test Case Pass")
            assert True
        else:
            print("Test Cases Fail")
            assert False

    def test_formSubmission(self, getData):
        a = self.inflow()
        log = self.getLogger()
        sleep(1)
        log.info("Test Name and Last Name Verification")
        log.info("First Name " + getData["first_name"])
        a.getFirstName().send_keys(getData["first_name"])
        sleep(1)
        log.info("Last Name " + getData["last_name"])
        a.getLastName().send_keys(getData["last_name"])
        sleep(1)

    def test_email(self, getData):
        a = self.inflow()
        log = self.getLogger()
        log.info("Test Email Verification")
        log.info("Email:-" + getData["email"])
        a.getEmail().send_keys(getData["email"])
        a.getEmail().send_keys(Keys.TAB)
        sleep(1)
        # import pdb
        # pdb.set_trace()
        existText_style_string = a.existEmail().get_attribute("style")
        validText_style_string = a.vaildEmail().get_attribute("style")
        print("exist style", existText_style_string)
        print("valid style", validText_style_string)
        existText = a.existEmail().get_attribute("innerHTML").replace("  ", "").replace("\n", " ").strip()
        vaildText = a.vaildEmail().get_attribute("innerHTML").replace("  ", "").replace("\n", " ").strip()
        # print( a.existEmail().get_attribute("outerHTML"))
        sleep(1)
        if existText == "There is already an account with that email address!" and "display: none" not in existText_style_string:
            log.info("There is already an account with that email address!")
            assert False
        elif vaildText == "Please enter a valid email address." and "display: none" not in validText_style_string:
            print("Valid TEXTTTTTTTTTTTTTTttt", vaildText)
            print("Valid TEXTTTTTTTTTTTTTTttt", validText_style_string)
            log.info("Please enter a valid email address.")
            assert False
        else:
            assert True

    def test_phone_number(self, getData):
        a = self.inflow()
        log = self.getLogger()
        log.info("Phone Number" + getData["phone_no"])
        sleep(1)
        a.getPhoneNo().send_keys(getData["phone_no"])

    def test_material_details(self, getData):
        sleep(1)
        a = self.inflow()
        a.getPartNumber().send_keys(getData["part_number"])
        a.getLength().send_keys(getData["length"])
        a.getBreadth().send_keys(getData["breadth"])
        a.getThickness().send_keys(getData["thickness"])
        a.getQtyAmt().send_keys(getData["qty_amnt"])
        sleep(2)

    def test_count_material_type_drp_dwn(self):
        a = self.inflow()
        a.setMaterialType().click()
        ul_elements = a.getCountLi()
        li_elements = ul_elements.find_elements(By.TAG_NAME, "li")
        li_count = len(li_elements)
        print("Total number of <li> elements:", li_count)
        if li_count == 26:
            assert True
        else:
            assert False

    def test_material_type_drp_dwn(self, getData):
        sleep(1)
        a = self.inflow()
        # a.setMaterialType().click()
        sleep(1)
        drp_material_type = (a.setInpMaterialType())
        drp_material_type.send_keys(getData["material_type"])
        drp_material_type.send_keys(Keys.RETURN)
        sleep(1)

    def test_sub_category(self):
        a = self.inflow()
        a.setSubCategory().click()
        sleep(1)

    def test_Final_category(self):
        a = self.inflow()
        a.setFinalCategory().click()
        sleep(2)

    def test_Genrate_Price(self):
        sleep(1)
        a = self.inflow()
        sleep(1)
        a.RequireValidation().click()

    def test_Term_Check_Box(self):
        a = self.inflow()
        CheckBox = a.setTermCheckBox()
        sleep(1)
        a.driver.execute_script("arguments[0].click();", CheckBox)

    def test_Process_Check_Out(self):
        a = self.inflow()
        sleep(1)
        a.clickProceesCheckout().click()

    def test_ContactDetail(self, getData):
        a = self.inflow()
        sleep(1)
        a.setAddressLine1().send_keys(getData["address_Line1"])
        a.setAddressLine2().send_keys(getData["address_Line2"])
        a.setCompanyName().send_keys(getData["company_name"])
        a.setCity().send_keys(getData["city"])
        sleep(1)

    def test_Industry_Drp_Dwn_len(self):
        a = self.inflow()
        dropdown = Select(a.setIndustry())
        option_elements = dropdown.options
        total_options = len(option_elements)
        print("Total number of options:", total_options)
        if total_options == 23:
            assert True
        else:
            assert False

    def test_IndustryDropDown(self):
        a = self.inflow()
        # dropdown = Select(a.setIndustry())
        # dropdown.select_by_visible_text("Automotive")
        self.selectOptionByText(a.setIndustry(), "Automotive")

    def test_CountryDropDown(self):
        a = self.inflow()
        self.selectOptionByText(a.setCountry(), "Canada")

    def test_StateDropDown(self):
        a = self.inflow()
        self.selectOptionByText(a.setState(), "Alberta")

    def test_ZipCode(self, getData):
        a = self.inflow()
        a.getZipCode().send_keys(getData["zip_code"])

    def test_Password(self, getData):
        a = self.inflow()
        a.getPassword().send_keys(getData["password"])

    def test_Confirm_Password(self, getData):
        a = self.inflow()
        a.geConfirmPassword().send_keys(getData["confirm_password"])

    def test_Password_strenth(self):
        a = self.inflow()
        a.checkPasswordMeter()
        meter_value = a.checkPasswordMeter().get_attribute("value")
        meter_value = float(meter_value)
        print("meter_value==========", meter_value)
        if meter_value <= 0.5:
            print("Password Strength is Medium")
            assert False
        elif meter_value >= 0.8:
            print("Password is Strong")
            assert True

    def test_RegisterButton(self):
        a = self.inflow()
        a.clickRegister().click()

    def test_OkButton(self):
        a = self.inflow()
        a.clickOkBtn().click()

    def test_FileUpload(self):
        a = self.inflow()
        sleep(1)
        a.fileUpload().click()
        sleep(1)
        pyautogui.write('/home/gaurav.gaikwad/Downloads/dummy.pdf')
        pyautogui.press('enter')
        sleep(5)

    def test_FileUploadButton(self):
        a = self.inflow()
        sleep(5)
        a.uploadBtn().click()

    def test_PoUploadButton(self):
        a = self.inflow()
        sleep(2)
        RadioBtn = a.clickUploadPo()
        a.driver.execute_script("arguments[0].click();", RadioBtn)

    def test_PoUpload(self):
        a = self.inflow()
        sleep(1)
        file_po = a.SetFilePo()
        sleep(1)
        path = '/home/gaurav.gaikwad/Downloads/dummy.pdf'
        file_po[0].send_keys(path)

    def test_CarrierDropDown(self):
        a = self.inflow()
        sleep(1)
        dropdown = Select(a.setCarrierDrp())
        sleep(1)
        dropdown.select_by_value("2-UPS")

    def test_SpeedDropDown(self):
        a = self.inflow()
        sleep(2)
        self.selectOptionByText(a.setSpeedDrp(), "UPS Regular Ground")

    def test_Shipping(self, getData):
        a = self.inflow()
        sleep(2)
        a.getShipping().send_keys(getData["shipping_account_no_id"])

    def test_CheckBillingButton(self):
        a = self.inflow()
        sleep(1)
        a.clickCheckBillBtn().click()

    def test_Billing_Address(self, getData):
        sleep(2)
        a = self.inflow()
        a.getaddress1Ship().send_keys(getData["address_1_shipping"])
        a.getaddress2Ship().send_keys(getData["address_2_shipping"])
        a.getCityShipping().send_keys(getData["city_shipping"])
        a.getZipShipping().send_keys(getData["zip_shipping"])
        sleep(2)

    def test_CountryShipDropDown(self):
        a = self.inflow()
        sleep(1)
        self.selectOptionByText(a.setCountryShipDrp(), "Canada")

    def test_StateShipDropDown(self):
        a = self.inflow()
        sleep(1)
        self.selectOptionByText(a.setStateShipDrp(), "Alberta")

    def test_SubmitButton(self):
        a = self.inflow()
        sleep(2)
        a.clickSubmitBtn().click()

    @pytest.fixture(params=HomePageData.test_homePageData)
    def getData(self, request):
        return request.param
