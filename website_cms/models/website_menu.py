# -*- coding: utf-8 -*-

# pylint: disable=E0401
# pylint: disable=R0903

from odoo import models,fields



class WebsiteMenu(models.Model):
    """Override website menu model."""

    _inherit = "website.menu"

    cms_page_id = fields.Many2one(
        string='CMS Page',
        comodel_name='cms.page'
    )
