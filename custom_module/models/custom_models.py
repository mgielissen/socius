from odoo import models, fields, api
import csv
import base64
import re


class CustomModel(models.Model):
    _name = 'backend.model'

    name = fields.Char(String="Content Heading")
    comment = fields.Char(String="Content")
    data_file = fields.Binary(string='Upload the image', required=True, help='Get you csv file ')


# class Newwizard(models.TransientModel):
#     _inherit = ['backend.model']
#     _name = 'accademic.create.attendee.wizard'
#     filename = fields.Char()
#
#     # @api.model
#     def import_file(self, **kw):
#         l = []
#         self.ensure_one()
#         s1 = self.data_file
#         content = base64.b64decode(s1)
#         # print(content)
#         a=self.filename
#         print(self.filename,"vvvvvvv")
#         data = self.env['backend.model'].search([])
#         for i in data:
#             print(i.name,i.comment)
#
#         l.append({'heading': i.name, 'content': i.comment, 'img': content})
#         print(l)
#         return l


























































# from odoo import models, fields, api
# import csv
# import base64
# import re
#
#
# class CustomModel(models.Model):
#     _name = 'custom.model'
#     _description = 'car request'
#     # _inherit = 'project.project'
#     #  _inherit = 'res.partner'
#     name = fields.Char('Name')
#
# class Newwizard(models.TransientModel):
#     _inherit = ['custom.model']
#     _name = 'accademic.create.attendee.wizard'
#     data_file = fields.Binary(string='Bank Statement File', required=True, help='Get you csv file ')
#     filename = fields.Char()
#
#     # @api.model
#     def import_file(self, **kw):
#         self.ensure_one()
#         s1 = self.data_file
#         content = base64.b64decode(s1)
#         print(content)
#         print(self.filename,"vvvvvvv")
#         # self.ensure_one()
#         # s1 = self.data_file.decode("UTF-8")
#         # b1 = s1.encode("UTF-8")
#         # d = base64.b64decode(b1)
#         # s2 = d.decode("UTF-8")
#         # print(s2)
#         # a = s2.split()
#         # # print(a)
#         # while ("" in a):
#         #     a.remove("")
#         # k = {}
#         note_ids = []
#         # for length in a:
#         #     b = length.split(',')
#         #     k['project'] = b[0]
#         #     k['task'] = b[1]
#         #     b = self.env['project.task'].create({
#         #         'project_id': self.env['project.project'].create({'name': k['project']}).id,
#         #         'name': k['task']
#         #     })
