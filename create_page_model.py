__author__ = 'tytkal'
class CreatePageModel:
    api_key = ''
    cc_first_name = ''
    cc_last_name = ''
    phone_number = ''
    billing_address = ''
    state = ''
    city = ''
    postal_code = ''
    country = ''
    email = ''
    amount = ''
    discount = ''
    reference_no = ''
    currency = ''
    title = ''
    ip_customer = ''
    ip_merchant = ''
    return_url = ''
    address_shipping = ''
    city_shipping = ''
    state_shipping = ''
    postal_code_shipping = ''
    country_shipping = ''
    quantity = ''
    unit_price = ''
    products_per_title = ''
    ChannelOfOperations = ''
    ProductCategory = ''
    ProductName = ''
    ShippingMethod = ''
    DeliveryType = ''
    CustomerId = ''
    msg_lang = ''

    def get_create_prams(self):
        create_params = {
            'api_key':self.api_key,
            'cc_first_name':self.cc_first_name,
            'cc_last_name':self.cc_last_name,
            'phone_number':self.phone_number,
            'billing_address':self.billing_address,
            'state':self.state,
            'city':self.city,
            'postal_code':self.postal_code,
            'country':self.country,
            'email':self.email,
            'amount':self.amount,
            'discount':self.discount,
            'reference_no':self.reference_no,
            'currency':self.currency,
            'title':self.title,
            'ip_customer':self.ip_customer,
            'ip_merchant':self.ip_merchant,
            'return_url':self.return_url,
            'address_shipping':self.address_shipping,
            'city_shipping':self.city_shipping,
            'state_shipping':self.state_shipping,
            'postal_code_shipping':self.postal_code_shipping,
            'country_shipping':self.country_shipping,
            'quantity':self.quantity,
            'unit_price':self.unit_price,
            'products_per_title':self.products_per_title,
            'ChannelOfOperations':self.ChannelOfOperations,
            'ProductCategory':self.ProductCategory,
            'ProductName':self.ProductName,
            'ShippingMethod':self.ShippingMethod,
            'DeliveryType':self.DeliveryType,
            'CustomerId':self.CustomerId,
            'msg_lang':self.msg_lang
        }
        return create_params