# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hide Top and Left Menu',
    'summary': 'If want more space in your screen, buy this app',
    'category': 'Tools', 
    'author': 'sitepasmal.com',
    'website': "http://sitepasmal.com",
    'price': 70,
    'currency': 'EUR',
    'depends': ['base'],
    'version': '1.0',	

    'description': """Odoo top and left menu control  .
      ======================
    - Two buttons to hide and show left,right or both menus.
	- You get more space on your laptop or pad, or even smartphone.
    """,
	
    'data': [
           'views/custom_view.xml'
    ],
	
    "installable": True,
    "auto_install": False,
    'images':[
        'static/description/banner.png',
       
	 ],
}
