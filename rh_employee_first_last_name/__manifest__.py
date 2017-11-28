# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Employee First last Name and code',
    'category': 'Employees',
    'author': 'sitepasmal.com',
    'website': 'http://sitepasmal.com',
    'version': '1.0',
	'price': 18,
    'currency': 'EUR',
    'depends': ['hr_payroll','base'],
    
	
    'description': """ First name ,Last name and Code of the employee. All in one
	
======================

    - First and Last name of the employee in separate fields reported automatically into the  field 'name' of Odoo
	- Adds also a  sequential code for the employee. No need to type it. Besides who wants to remember  all codes in order to avoid a duplicate
  
    """,
    'data': [
        'data/hr_employee_sequence.xml',  
        'views/hr_employee_first_last_views.xml',

    ],
	
    "installable": True,
    "images":['static/description/banner.png'],	
}

