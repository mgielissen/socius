{
    'name': 'News upload',
    'description': 'News Upload Module',
    'author': "Socius Innovative Global Brains",

    'depends': ['base','web'],
    'data': [
        'views/upload_view.xml',
        'security/ir.model.access.csv',
             ],

    'installable': True,
    'application': True,
    'auto_install': False,

}