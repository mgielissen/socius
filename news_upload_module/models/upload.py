from odoo import api, fields, models, _
import csv
import base64
import re
import datetime


class CustomModel(models.Model):
    _name = 'backend.model'

    name = fields.Char(String="Content Heading",required=True)
    comment = fields.Char(String="Content",required=True)
    date_from = fields.Date(string='Uploading Date', required=True)
    data_file = fields.Binary(string='Upload the image', required=True, help='Get you csv file ')








