{
    'name': 'News upload!',
    'description': 'Description about you',
    'depends': ['base'],
    'data': [
        'views/custom_view.xml',
             # 'wizard/new_wizard.xml',
             # 'security/security.xml',
             'security/ir.model.access.csv',
             ],

    'installable': True,
    'application': True,
    'auto_install': False,

}