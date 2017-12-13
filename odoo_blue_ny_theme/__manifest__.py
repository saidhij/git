# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Majorelle blue theme NY2018',
    'summary': 'If you like blue,try this backend theme',
    'category': 'Themes/Backend', 
    'author': 'sitepasmal.com',
    'website': "http://sitepasmal.com",
    'price': 200,
    'currency': 'EUR',
    'depends': ['base'],
    'version': '1.0',	

    'description': """Odoo Majorelle blue backend theme theme with Happy New year.
      ======================
    - Nice looking blue theme for odoo .
	- Enjoy it. Your eyes will be happy .
	- After you install the theme. Please restart odoo and update the application.
    """,
	
    'data': [
           'views/custom_view.xml'
    ],
    'css': ['static/src/css/styles.css'],
	
    "installable": True,
    "auto_install": False,
    'images':[
        'static/description/banner.png',
        'static/description/cover.png',
	 ],
}
