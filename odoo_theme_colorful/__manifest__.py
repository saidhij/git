# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'A colorful odoo backend theme',
    'summary': 'If you like colors,buy this theme',
    'category': 'Themes/Backend', 
    'author': 'sitepasmal.com',
    'website': "http://sitepasmal.com",
    'price': 200,
    'currency': 'EUR',
    'depends': ['base'],
    'version': '1.0',	

    'description': """Colorful Odoo theme.
      ======================
    - Fancy Colorful theme for odoo .
	- Enjoy it. Odoo as never seen before.
 
    """,
	
    'data': [
           'views/custom_view.xml'
    ],
    'css': ['static/src/css/styles.css'],
	
    "installable": True,
    "auto_install": False,
    "images":['static/description/Banner.png'],
}
