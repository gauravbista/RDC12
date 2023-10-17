from selenium.webdriver.common.by import By
from time import sleep


class DirectQuote:
    # construtor
    def __init__(self, driver):
        self.driver = driver

    btn_get_quote = "//a[normalize-space()='Get a Quote']"
    btn_get_started_xpath = "//a[normalize-space()='get started']"
    btn_proceed_guest_xpath = '//*[@id="wrapwrap"]/main/div/div/div/div[2]/form/div/button'
    # Quote Detail Page
    txt_first_name_xpath = "//input[@name='firstName']"
    txt_last_name_xpath = "//input[@name='lastName']"
    txt_email_xpath = "//input[@id='guest-email']"
    txt_phone_no = "//input[@id='guest-phone-number']"
    btn_genrate_price_xpath = "//button[@id='generate_cost_btn']"
    exist_email_txt = "//span[@id='email-warning-already-exist']"
    email_vaild_txt = "//span[@id='email-warning']"
    phone_vaild_txt = "//span[@id='phone-warning']"
    txt_part_number_xpath = "//input[@id='part_number']"
    txt_length_xpath = "//input[@id='length']"
    txt_breadth_xpath = "//input[@id='breadth']"
    txt_thickness_xpath = "//input[@id='thickness']"
    txt_qty_amnt_xpath = "//input[@id='qty_amnt']"
    drp_material_xpath = "//div[@id='s2id_material_type']"
    inp_material_xpath = "(//input[@id='s2id_autogen1_search'])[1]"
    ul_drp_material_id = "//ul[@id='select2-results-1']"
    autogen1_search1 = "//*[text()='EPDM (Blend)']"
    autogen1_search2 = "//*[text()='RE-41E (4.0# - 8.0#) Black - 1.000\" thick']"
    check_box_term_xpath = "(//input[@id='terms'])[1]"
    btn_process_checkout_xpath = "//button[normalize-space()='Process Checkout']"
    txt_address_line1_id = "street_d_1"
    txt_address_line2_id = "street_d_2"
    txt_company_name_id = "company_name_d"
    txt_city_id = "city_d"
    drp_dwn_industry_id = "industry_d"
    drp_dwn_country_id = "country_d"
    drp_dwn_state_id = "state_d"
    get_zip_code_id = "zip_d"
    get_pswd_id = "password_d"
    get_conf_pswd_id = "confirm_pswd_d"
    pswd_meter_css = "meter.o_password_meter_web"
    btn_register_id = "create_user_direct_btn"
    btn_ok_id = "okButton"
    fil_upld_xpath = '//*[@id="my-awesome-dropzone"]/div/span'
    btn_upld_xpath = "//button[contains(@class,'upload_btn_w')]"
    radio_btn_id = "upload_po"
    file_po_name = "myFile"
    drp_dwn_carrier_id = "carrier_id"
    drp_dwn_speed_id = "speed_id"
    txt_shipping_account_no_id = "shipping_account_no"
    txt_name_shipping_id = "name_shipping"
    txt_address_1_shipping_id = "address_1_shipping"
    txt_address_2_shipping_id = "address_2_shipping"
    drp_dwn_country_shipping_id = "country_shipping"
    drp_dwn_state_shipping_add_id = "state_shipping_add"
    txt_city_shipping_id = "city_shipping"
    txt_zip_shipping_id = "zip_shipping"
    check_box_check_billing_id = "check_billing_same"
    btn_submit_button_id = "id_request_terms"

    def get_quote(self):
        return self.driver.find_element(By.XPATH, self.btn_get_quote)

    def clickGetStart(self):
        return self.driver.find_element(By.XPATH, self.btn_get_started_xpath)

    def ProceedGuest(self):
        return self.driver.find_element(By.XPATH, self.btn_proceed_guest_xpath)

    def RequireValidation(self):
        return self.driver.find_element(By.XPATH, self.btn_genrate_price_xpath)

    def getFirstName(self):
        return self.driver.find_element(By.XPATH, self.txt_first_name_xpath)

    def getLastName(self):
        return self.driver.find_element(By.XPATH, self.txt_last_name_xpath)

    def getEmail(self):
        return self.driver.find_element(By.XPATH, self.txt_email_xpath)

    def existEmail(self):
        return self.driver.find_element(By.XPATH, self.exist_email_txt)

    def vaildEmail(self):
        return self.driver.find_element(By.XPATH, self.email_vaild_txt)

    def getPhoneNo(self):
        return self.driver.find_element(By.XPATH, self.txt_phone_no)

    def vaildPhone(self):
        return self.driver.find_element(By.XPATH, self.phone_vaild_txt)

    def getPartNumber(self):
        return self.driver.find_element(By.XPATH, self.txt_part_number_xpath)

    def getLength(self):
        return self.driver.find_element(By.XPATH, self.txt_length_xpath)

    def getBreadth(self):
        return self.driver.find_element(By.XPATH, self.txt_breadth_xpath)

    def getThickness(self):
        return self.driver.find_element(By.XPATH, self.txt_thickness_xpath)

    def getQtyAmt(self):
        return self.driver.find_element(By.XPATH, self.txt_qty_amnt_xpath)

    def getCountLi(self):
        return self.driver.find_element(By.XPATH, self.ul_drp_material_id)

    def setMaterialType(self):
        return self.driver.find_element(By.XPATH, self.drp_material_xpath)

    def setInpMaterialType(self):
        return self.driver.find_element(By.XPATH, self.inp_material_xpath)

    def setSubCategory(self):
        return self.driver.find_element(By.XPATH, self.autogen1_search1)

    def setFinalCategory(self):
        return self.driver.find_element(By.XPATH, self.autogen1_search2)

    def setTermCheckBox(self):
        return self.driver.find_element(By.XPATH, self.check_box_term_xpath)

    def clickProceesCheckout(self):
        return self.driver.find_element(By.XPATH, self.btn_process_checkout_xpath)

    def setAddressLine1(self):
        return self.driver.find_element(By.ID, self.txt_address_line1_id)

    def setAddressLine2(self):
        return self.driver.find_element(By.ID, self.txt_address_line2_id)

    def setCompanyName(self):
        return self.driver.find_element(By.ID, self.txt_company_name_id)

    def setCity(self):
        return self.driver.find_element(By.ID, self.txt_city_id)

    def setIndustry(self):
        return self.driver.find_element(By.ID, self.drp_dwn_industry_id)

    def setCountry(self):
        return self.driver.find_element(By.ID, self.drp_dwn_country_id)

    def setState(self):
        return self.driver.find_element(By.ID, self.drp_dwn_state_id)

    def getZipCode(self):
        return self.driver.find_element(By.ID, self.get_zip_code_id)

    def getPassword(self):
        return self.driver.find_element(By.ID, self.get_pswd_id)

    def geConfirmPassword(self):
        return self.driver.find_element(By.ID, self.get_conf_pswd_id)

    def checkPasswordMeter(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.pswd_meter_css)

    def clickRegister(self):
        return self.driver.find_element(By.ID, self.btn_register_id)

    def clickOkBtn(self):
        return self.driver.find_element(By.ID, self.btn_ok_id)

    def fileUpload(self):
        return self.driver.find_element(By.XPATH, self.fil_upld_xpath)

    def uploadBtn(self):
        return self.driver.find_element(By.XPATH, self.btn_upld_xpath)

    def clickUploadPo(self):
        return self.driver.find_element(By.ID, self.radio_btn_id)

    def SetFilePo(self):
        return self.driver.find_elements(By.NAME, self.file_po_name)

    def setCarrierDrp(self):
        return self.driver.find_element(By.ID, self.drp_dwn_carrier_id)

    def setSpeedDrp(self):
        return self.driver.find_element(By.ID, self.drp_dwn_speed_id)

    def getShipping(self):
        return self.driver.find_element(By.ID, self.txt_shipping_account_no_id)

    def getShippingName(self):
        return self.driver.find_element(By.ID, self.txt_name_shipping_id)

    def getaddress1Ship(self):
        return self.driver.find_element(By.ID, self.txt_address_1_shipping_id)

    def getaddress2Ship(self):
        return self.driver.find_element(By.ID, self.txt_address_2_shipping_id)

    def setCountryShipDrp(self):
        return self.driver.find_element(By.ID, self.drp_dwn_country_shipping_id)

    def setStateShipDrp(self):
        return self.driver.find_element(By.ID, self.drp_dwn_state_shipping_add_id)

    def getCityShipping(self):
        return self.driver.find_element(By.ID, self.txt_city_shipping_id)

    def getZipShipping(self):
        return self.driver.find_element(By.ID, self.txt_zip_shipping_id)

    def clickCheckBillBtn(self):
        return self.driver.find_element(By.ID, self.check_box_check_billing_id)

    def clickSubmitBtn(self):
        return self.driver.find_element(By.ID, self.btn_submit_button_id)
