import werkzeug

from odoo import http
from odoo.http import request


class WebsiteButtondetails(http.Controller):

    @http.route('/page/appoint', type='http', auth='public', website=True)
    def appointment(self, redirect=None, ):
        print("hii")

        return request.render('website_module.not_avail', {})

