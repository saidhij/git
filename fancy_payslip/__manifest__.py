# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'FANCY PAYSLIP',
    'summary': 'Print from odoo the certificate of employement for your employees',
    'category': 'Reporting',
    'author': 'sitepasmal.com',
    'website': "http://sitepasmal.com",
    'price': 60,
    'currency': 'EUR',
    'depends': ['base','hr_payroll',],
    'version': '1.0',	

    'description': """Certificate of Employement.
      ======================
    - This application will help you print the certificate of employement for one or more employees
	- Print it directly from the employee menu. 
    """,
	
    'data': [
        'report/payslip_report.xml',	
        'report/payslip_template.xml',		
        'views/hr_payslip_view.xml',
        'views/hr_employee_view.xml',		
		
    ],
    'css': ['static/src/css/report.css'],
	
	
    "installable": True,
    "images":['static/description/Banner.png'],
	
}
