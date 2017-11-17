# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api, _
from odoo.exceptions import ValidationError


	
class hr_contract(models.Model):
    _inherit = 'hr.contract'
	
	
    name = fields.Char('Contract Reference', required=False,readonly=True, copy=False, default='Autofill')

    @api.model
    def create(self, vals):
        if vals.get('number', 'Autofill') == 'Autofill':
            vals['name'] = self.env['ir.sequence'].next_by_code('contract.ref')
        return super(hr_contract, self).create(vals)
	
  

		
		

		
		
		
	