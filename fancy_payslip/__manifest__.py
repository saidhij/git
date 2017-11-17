# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'ELEGANT PAYSLIP',
    'summary': 'Print Elegant Payslips for your employees',
    'category': 'Human Resources',
    'author': 'sitepasmal.com',
    'website': "http://sitepasmal.com",
    'price': 60,
    'currency': 'EUR',
    'depends': ['base','hr_payroll', 'report'],
    'version': '1.0',	

    'description': """Elegant Payslip.
      ======================
    - This application will help you print elegant payslips for your employees
	- You can keep pour old one. 
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
