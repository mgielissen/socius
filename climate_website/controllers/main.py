from odoo import http
from odoo.http import request, route
from _datetime import datetime, timedelta
from odoo.addons.website.controllers.main import Website
import requests, json
from datetime import datetime, timedelta
from dateutil.tz import tzlocal
import logging
_logger = logging.getLogger(__name__)

class Website(Website):

    @http.route(auth='public')
    def index(self, data={}, **kwargs):
        super(Website, self).index(**kwargs)

        data=[]
        api_data = []
        error = []

        print(datetime.now(tzlocal()))

        defaults = {
            'start': datetime.now(),
            'finish': datetime.now() + timedelta(hours=1),
        }
        print(defaults)

        details = request.env['backend.model'].search([], order='date_from desc')
        for i in details:
            data.append(i)

        api_key = "71522e7cc5de039712346f640e2642fd"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        _logger.info("++++++++++++++++=")
        _logger.info(kwargs)
        x = {}
        if not kwargs:
            city_name = "india"
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()

        if "fw" in kwargs:
            city_name = "india"
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()

        if "id" in kwargs:
            if kwargs['id']:
                city_name = kwargs['id']  # Give city name
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name  # complete url address
                response = requests.get(complete_url)
                x = response.json()

            else:
                city_name = ''
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                x = response.json()

        if x["cod"] == "404" or x["cod"] == "400":
            error.append(x)

            return http.request.render('climate_website.climate_homepage_template', {'data': data, 'error': error})

        else:
            error.append(x)
            api_data.append(x['main'])

            return http.request.render('climate_website.climate_homepage_template', {'data': data, 'api': api_data, 'error': error})


