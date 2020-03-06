# -*- coding: utf-8 -*-

from odoo import fields, models


class WebsiteInherit(models.Model):
    _inherit = "website"

    def _default_social_skype(self):
        return self.env.ref('base.main_company').social_skype
    social_skype = fields.Char('Skype Account', default=_default_social_skype)

    def _default_social_whatsapp(self):
        return self.env.ref('base.main_company').social_whatsapp
    social_whatsapp = fields.Char('WhatsApp Account', default=_default_social_whatsapp)
