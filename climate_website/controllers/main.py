from odoo import http
import base64
from odoo.http import  request, route
from _datetime import datetime, timedelta
from odoo.addons.website.controllers.main import Website


class Website(Website):

    @http.route(auth='public')
    def index(self, data={}, **kwargs):
        super(Website, self).index(**kwargs)

# Home Page Product banner
        data=[]
        l=[]

        details = request.env['backend.model'].search([])
        for i in details:
            print(i.name,"bbbbb")
            print(i.id)

            x=i.id
            a=i.data_file
            # data = [{'heading': i.name, 'content': i.comment, 'img': i.data_file, 'id':i.id}]

            data.append(i)

            print(data,"aaaaa")


        return http.request.render('climate_website.climate_homepage_template', {'data':data})

# Random Products Display Home Page

        # product_data = request.env['product.template'].search([])
        # pro_img = []
        # for i in product_data:
        #     details = [{"id": i.id}, i.name, i.image_medium, i.list_price]
        #     pro_img.append(details)

# Product Brands

        # brands = []
        # brand_details = request.env['product.brand'].search([])
        # for i in brand_details:
        #     keep = QueryURL('/page/product_brands', brand_id=[])
        #     brand_details = [{"id": i.id}, i.name, i.logo]
        #     brands.append(brand_details)

# Product Offers

        # offer_price = request.env['product.template'].search([])
        # offer_details = []
        # for i in offer_price:
        #     if i.item_ids.pricelist_id.offer == True:
        #         values = [{"id": i.id}, i.name, i.list_price, i.item_ids.fixed_price, i.image_medium]
        #         offer_details.append(values)
        # doc = {'details': offer_details, 'banner': product_banner, 'brand': brands, 'random_pro': pro_img}
        # return http.request.render('ecommerce_website.homepage_template', doc)






