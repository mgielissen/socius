from odoo import http
import base64
from odoo.http import  request, route
from _datetime import datetime, timedelta
from odoo.addons.website.controllers.main import Website


class Website(Website):

    @http.route(auth='public')
    def index(self, data={}, **kwargs):
        super(Website, self).index(**kwargs)
        data=[]

        details = request.env['backend.model'].search([])
        for i in details:
            data.append(i)
        return http.request.render('climate_website.climate_homepage_template', {'data':data})
