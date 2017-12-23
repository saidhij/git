# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Efficient Emplooyees List',
    'summary': 'Adds employee picture and more info about contracts in the tree view',
    'category': 'Human Resources', 
    'author': 'sitepasmal.com',
    'website': "http://sitepasmal.com",
    'price': 40,
    'currency': 'EUR',
    'depends': ['base','hr','hr_payroll','hr_contract',],
    'version': '1.0',	

    'description': """Elaborated employees tree view.
      ======================
    - Added a small picture of the employee .
	- Added contract reference
	- Added state of the contract .
	- Added start and end date of the contrat
    """,
	
    'data': [
           'views/employee_view.xml'
    ],


    "installable": True,
    "auto_install": False,
    'images':[
        'static/description/banner.jpg',
        
	 ],
}
