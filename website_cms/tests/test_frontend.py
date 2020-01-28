# -*- coding: utf-8 -*-
# Copyright 2016 OCA/oscar@vauxoo.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import HttpCase


class UICase(HttpCase):

    def test_ui_website_cms(self):
        """Test frontend tour."""
        self.phantom_js(
            "/",
            "odoo.__DEBUG__.services['web_tour.tour'].run('test_create_page',\
            'test')",
            "odoo.__DEBUG__.services['web_tour.tour'].tours.test_create_page",
            login="admin")
