{
    'name': "Website Help Desk / Support Ticket - Timesheets",
    'version': "13.0.0.0",
    'author': "",
    'category': "Tools",
    'summary':'Track time spend on tickets and send an invoice',
    'license':'LGPL-3',
    'data': [
        'views/website_support_ticket_views.xml',
        'views/website_support_ticket_timesheet_views.xml',
        'views/website_support_ticket_templates.xml',
        'data/website.support.ticket.state.csv',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'depends': ['website_support','project','account'],
    'images':[
        'static/description/1.jpg',
    ],
    'installable': True,
}