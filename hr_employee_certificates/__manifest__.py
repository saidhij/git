# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'CERTIFICATE OF EMPLOYMENT',
    'summary': 'Print from odoo the certificate of employement for your employees',
    'category': 'Human Resources',
    'author': 'sitepasmal.com',
    'website': "http://sitepasmal.com",
    'price': 40,
    'currency': 'EUR',
    'depends': ['base'],
    'version': '1.0',	

    'description': """Certificate of Employement.
      ======================
    - This application will help you print the certificate of employement for one or more employees
	- Print it directly from the employee menu. 
    """,
	
    'data': [
        'report/certificate_template.xml',
        'report/certificate_report.xml',
    ],
    'css': ['static/src/css/report.css'],
	
	
    "installable": True,
    "images":['static/description/Banner.png'],
	
}
