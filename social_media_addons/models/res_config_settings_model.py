# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResConfigSettingsInherit(models.TransientModel):
    _inherit = 'res.config.settings'
    social_skype = fields.Char(related='website_id.social_skype', readonly=False)
    social_whatsapp = fields.Char(related='website_id.social_whatsapp', readonly=False)
    whatsapp_number = fields.Char(readonly=False)
    skype_id = fields.Char(readonly=False)

    def get_values(self):
        res = super(ResConfigSettingsInherit, self).get_values()
        res.update(
            social_skype=self.env["ir.config_parameter"].sudo().get_param('social_media_addons.social_skype'),
            social_whatsapp=self.env["ir.config_parameter"].sudo().get_param('social_media_addons.social_whatsapp'),
            whatsapp_number=self.env["ir.config_parameter"].sudo().get_param('social_media_addons.whatsapp_number'),
            skype_id=self.env["ir.config_parameter"].sudo().get_param('social_media_addons.skype_id')
        )
        return res

    def set_values(self):
        super(ResConfigSettingsInherit, self).set_values()
        param = self.env['ir.config_parameter'].sudo()
        field1 = self.social_skype and self.social_skype or False
        field2 = self.social_whatsapp and self.social_whatsapp or False
        field3 = self.whatsapp_number and self.whatsapp_number or False
        field4 = self.skype_id and self.skype_id or False
        param.set_param('social_media_addons.social_skype', field1)
        param.set_param('social_media_addons.social_whatsapp', field2)
        param.set_param('social_media_addons.whatsapp_number', field3)
        param.set_param('social_media_addons.skype_id', field4)

    @api.onchange('whatsapp_number')
    def _social_whatsapp(self):
        w_no = self.whatsapp_number
        if not w_no:
            self.social_whatsapp = ''
        else:
            self.social_whatsapp = str("https://api.whatsapp.com/send?phone=" + w_no + "+&text=hello")

    @api.onchange('skype_id')
    def _social_skype(self):
        s_id = self.skype_id
        if not s_id:
            self.social_skype = ''
        else:
            self.social_skype = str("skype:" + s_id + "?chat")

    @api.depends('website_id', 'social_twitter', 'social_facebook', 'social_github', 'social_linkedin',
                 'social_youtube', 'social_instagram', 'social_skype', 'social_whatsapp')
    def has_social_network(self):
        self.has_social_network = self.social_twitter or self.social_facebook or self.social_github \
                                  or self.social_linkedin or self.social_youtube or self.social_instagram or self.social_skype or self.social_whatsapp

    def inverse_has_social_network(self):
        if not self.has_social_network:
            self.social_twitter = ''
            self.social_facebook = ''
            self.social_github = ''
            self.social_linkedin = ''
            self.social_youtube = ''
            self.social_instagram = ''
            self.social_skype = ''
            self.social_whatsapp = ''

    has_social_network = fields.Boolean("Configure Social Network", compute=has_social_network,
                                        inverse=inverse_has_social_network)
