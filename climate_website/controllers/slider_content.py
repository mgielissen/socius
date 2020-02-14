from datetime import datetime, date, timedelta
from odoo import http,api,fields,models
import datetime
from odoo.http import request
# from odoo.addons.portal.controllers.portal import Websitedetail

class Websitedetail(http.Controller):
    @http.route(['/page/details'], type='http', auth="public", website=True, csrf=False)
    def content(self):
        return request.render('climate_website.slider_content_view',  {})

class Beardetail(http.Controller):
    @http.route(['/page/bear'], type='http', auth="public", website=True, csrf=False)
    def bear_content(self):
        return request.render('climate_website.bear_content', {})

class Sliderdetail(http.Controller):
    @http.route(['/page/slides'], type='http', auth="public", website=True, csrf=False)
    def slider_content(self):
        return request.render('climate_website.slider_content', {})