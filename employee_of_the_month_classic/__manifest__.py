# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Classic Employee of the Month certificate',
    'summary': 'Print from odoo your employee of the month certificate',
    'category': 'Reporting',
    'author': 'rhfree.com',
    'website': "http://rhfree.com",
    'price': 40,
    'currency': 'EUR',
    'depends': ['base'],
    'version': 'Classic1.0',	

    'description': """Employee of The Month.
      ======================
    - This application will help you print the certificate of the the employee of the month in a classic design
	- No time waiste, directly from employee menu. 
 
    """,
	
    'data': [
        'report/classic_certificate_template.xml',
        'report/classic_certificate_report.xml',
    ],
    'css': ['static/src/css/report.css'],
	
    "installable": True,
    # "auto_install": False
    "images":['static/description/Banner.png'],
}
