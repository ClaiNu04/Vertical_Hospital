# -*- coding: utf-8 -*-
{
    'name': "vertical_hospital",

    'description': """
        Este modulo sirve para la administracion de un Hospital
    """,

    'author': "Astra Tech",
    'website': "https://www.astratech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'reports/patient_card.xml',
        'reports/report.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/patient.xml',
        'views/patient_menu.xml',
        'views/treatment.xml',
        'views/templates.xml',  
        'views/settings.xml',   
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
