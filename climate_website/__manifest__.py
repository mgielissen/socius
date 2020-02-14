{
    'name': "Climate Website Module",

    'description': "Climate Website Module",

    'version': '0.1',
    'author': "Socius Innovative Global Brains",

    # any module necessary for this one to work correctly
    'depends': ['base','website','web'],

    # always loaded
    'data': [
         'views/home.xml',
         'views/assets.xml',
         'views/content.xml',
         'views/slider_content_view.xml',
         'views/bear_content_view.xml',
         'views/top_menu.xml',
         'views/slides_view.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': False,
    'auto_install': False,
}