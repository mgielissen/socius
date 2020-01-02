# -*- coding: utf-8 -*-
{
    'name': "breitschtraeff_resources",

    'summary': """
        all resources used accross modules by the breitschtraeff site
        """,

    'description': """
        all resources used accross modules by the breitschtraeff site
    """,

    'author': "redO2oo",
    'website': "http://www.redO2oo.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Theme/Creative',
    'version': '13.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['backend_theme_v13','website'],

    # always loaded
    'data': [
        'views/assets.xml',
        'views/invoice_action_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
}