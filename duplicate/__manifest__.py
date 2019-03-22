# -*- coding: utf-8 -*-
{
    'name': "duplicate_report",

    'summary': """This module duplicates a budget / order report""",

    'description': """
        This module duplicates a budget / order report
    """,

    'author': "Xmarts",
    'website': "https://www.xmarts.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://githb.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
    'sale_management',
    'sale',
    'point_of_sale',

    
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/report_recibo_ticket.xml',
        'reports/reports_menu.xml',
        'views/views.xml',
        'views/templates.xml',
       
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
     'qweb': [
         'static/src/xml/pos.xml'
     ],
}