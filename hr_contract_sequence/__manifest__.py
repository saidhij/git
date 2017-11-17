# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Auto Contract Sequence',
    'summary': 'Autofilled employees contract reference. No need to type it',
    'category': 'Human Resources',
    'author': 'rhfree.com',
    'website': "http://rhfree.com",
    'price': 40,
    'currency': 'EUR',
    'depends': ['hr_payroll','hr_contract'],
    'version': '1.0',	

    'description': """Autofilled Contract Reference.
      ======================
    - This application will assign automatically a reference number to a new employee's contract
	- No need to remember or to worry about duplicates. 
 
    """,
	
    'data': [
        'data/hr_contract_sequence.xml',
    ],

	
    "installable": True,
    # "auto_install": False
    "images":['static/description/Banner.png'],
}
