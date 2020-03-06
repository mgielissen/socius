from odoo import api, fields, models


class ResCompanyInherit(models.Model):
    _inherit = "res.company"

    social_skype = fields.Char('Skype Account')
    social_whatsapp = fields.Char('WhatsApp Account')