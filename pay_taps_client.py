# -*- coding: utf-8 -*-
from create_page_model import CreatePageModel

__author__ = 'tytkal'
from rest_client import RestClient
class PayTapsClient:
    username = ''
    password = ''
    res_client = None
    api_key = ''
    auth_url = 'authentication'
    create_pay_page = 'create_pay_page'
    valide_api_key = 'api_key_valid'
    verify_payment = 'verify_payment'
    expire_key = 'logout'
    def __init__(self):
        self.res_client = RestClient('https://www.paytabs.com/api/')
    def auth(self):
        params = {'merchant_id':self.username,'merchant_password':self.password}
        self.res_client.resourse = 'authentication'
        responce = self.res_client.post(params=params)
        api_key = responce.json()['api_key']
        if api_key == None:
            print 'password is wrong'
        else:
            self.api_key = api_key
            #print self.api_key
        return  self.api_key
    def validate_api_key(self):
        print ''

    def vrify_payment(self):
        print ''

    def expire_api_key(self):
        print ''

    def create_pay_page(self):
        cr_pa_mo = CreatePageModel()
        cr_pa_mo.api_key = self.auth()
        cr_pa_mo.title = 'testing'
        #cr_pa_mo.address_shipping = 'nakil'
        cr_pa_mo.amount = 1200
        #cr_pa_mo.billing_address = 'nakil'
        cr_pa_mo.cc_first_name = 'khalid'
        cr_pa_mo.cc_last_name = 'al hussayen'
        #cr_pa_mo.ChannelOfOperations = 'Somthing'
        #cr_pa_mo.city = 'Riyadh'
        #cr_pa_mo.city_shipping = 'Riyadh'
        cr_pa_mo.country = 'المملكة العربية السعودية'
        cr_pa_mo.country_shipping = 'المملكة العربية السعودية'
        cr_pa_mo.currency = 'SAR'
        cr_pa_mo.CustomerId = '14523654789'
        cr_pa_mo.DeliveryType = 'None'
        cr_pa_mo.discount = ''
        cr_pa_mo.email = 'tytkal@gmail.com'
        #cr_pa_mo.ip_customer = '192.168.95.89'
        cr_pa_mo.msg_lang = 'Arabic'
        #cr_pa_mo.ip_merchant = '192.168.95.89'
        cr_pa_mo.phone_number = '0506411119'
        cr_pa_mo.postal_code = '8684'
        cr_pa_mo.postal_code_shipping = '8684'
        cr_pa_mo.ProductCategory = 'Hg'
        cr_pa_mo.ProductName = 'pppo'
        cr_pa_mo.products_per_title = 'plo'
        cr_pa_mo.quantity = '1'
        cr_pa_mo.reference_no = '122225'
        cr_pa_mo.return_url = 'https://google.com'
        cr_pa_mo.ShippingMethod = 'car'
        cr_pa_mo.state = 'المملكة العربية السعودية'
        cr_pa_mo.state_shipping = 'المملكة العربية السعودية'
        cr_pa_mo.unit_price = '10'
        params = cr_pa_mo.get_create_prams()
        print params
        self.res_client.resourse = 'create_pay_page'
        responce = self.res_client.post(params=params)
        print responce.json()
        print responce.json()['payment_url']