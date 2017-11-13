# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Fancy Employee of the Month certificate',
    'summary': 'Print from odoo your employee of the month certificate',
    'category': 'Reporting',
    'author': 'rhfree.com',
    'website': "http://rhfree.com",
    'price': 50,
    'currency': 'EUR',
    'depends': ['base'],
    'version': 'Fancy1.0',	

    'description': """Fancy Employee of The Month Certificate.
      ======================
    - This application will help you print the certificate of the the employee of the month in a classic design
	- No time waiste, directly from employee menu. 
 
    """,
	
    'data': [
        'report/certificate_template_fancy.xml',
        'report/certificate_report_fancy.xml',
    ],
    'css': ['static/src/css/report.css'],
	
    "installable": True,
    # "auto_install": False
    "images":['static/description/Banner.png'],	
}
