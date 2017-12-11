# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Greay Crystal odoo backend theme',
    'summary': 'If you a bored,try this theme',
    'category': 'Themes/Backend', 
    'author': 'sitepasmal.com',
    'website': "http://sitepasmal.com",
    'price': 200,
    'currency': 'EUR',
    'depends': ['base'],
    'version': '1.0',	

    'description': """Odoo Crystal Grey backend theme.
      ======================
    - Cruspy backend theme for odoo .
	- Enjoy it. See Odoo dirrently.
 
    """,
	
    'data': [
           'views/custom_view.xml'
    ],
    'css': ['static/src/css/styles.css'],
	
    "installable": True,
    "auto_install": False,
    "images":['static/description/banner.png'],
}
