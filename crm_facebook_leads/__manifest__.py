# -*- coding: utf-8 -*-
{
    'name': "CRM Facebook Lead Ads",

    'summary': """
        Sync Facebook Leads with Odoo CRM""",

    'description': """
    """,

    'author': "IITA - Instituto de Innovación y Tecnología Aplicada, Jose Alejandro",
    'website': "https://iita.com.ar",
    'category': 'Lead Automation',
    'version': '13.0.1.0.0',
    'depends': ['crm'],
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',

    'data': [
        'security/ir.model.access.csv',
        'views/crm_view.xml',
    ]
}
