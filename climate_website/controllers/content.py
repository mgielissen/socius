from datetime import datetime, date, timedelta
from odoo import http,api,fields,models
import datetime
from odoo.http import request
# from odoo.addons.portal.controllers.portal import Websitedetail

class Websitedetail(http.Controller):
    @http.route(['/page/content'], type='http', auth="public", website=True, csrf=False)
    def content(self,**kw):
        data = []
        details = request.env['backend.model'].browse(int(kw['id']))
        for i in details:
            data.append(i)
        return request.render('climate_website.content',  {'data':data})