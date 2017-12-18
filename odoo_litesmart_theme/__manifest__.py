# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Lite Smart Backend Theme',
    'summary': 'If want more space, use this theme',
    'category': 'Themes/Backend', 
    'author': 'sitepasmal.com',
    'website': "http://sitepasmal.com",
    'price': 250,
    'currency': 'EUR',
    'depends': ['base'],
    'version': '1.0',	

    'description': """Odoo lite and Smart Backend theme .
      ======================
    - Two buttons to hide and show left,right or both menus.
	- Clear lite design and  shaped menus . Small and rounded apps icons. Line search bar as in odoo entreprise.
	- Fully responsive. All in one, nothing else to install.
	- After you install the theme. Please restart odoo and update the application.
    """,
	
    'data': [
           'views/custom_view.xml'
    ],
    'css': ['static/src/css/styles.css'],
	
    "installable": True,
    "auto_install": False,
    'images':[
        'static/description/banner2.png',
       
	 ],
}
