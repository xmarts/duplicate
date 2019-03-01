# -*- coding: utf-8 -*-
{
    'name': "duplicate_report",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Xmarts",
    'website': "https://www.xmarts.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://githb.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Reports',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable' : True,
    'application' : True
}