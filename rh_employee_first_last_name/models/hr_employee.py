# -*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import date
from dateutil.relativedelta import relativedelta


from odoo import fields, models,api, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import ValidationError


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

	
    first_name = fields.Char(string="First Name", required=False)
    last_name = fields.Char(string="Last Name", required=False)
    code2 = fields.Char('Code', required=False,readonly=False, copy=False, default='Autofilled')

    @api.onchange('first_name', 'last_name') # if these fields are changed, call method
    def check_change(self):     

        self.name = (self.first_name or '')+' '+(self.last_name or '')
		
    @api.model
    def create(self, val):
        if val.get('number', 'autofill') == 'autofill':
            val['code2'] = self.env['ir.sequence'].next_by_code('employee.code2')
        return super(HrEmployee, self).create(val)
		


	
	
	

		