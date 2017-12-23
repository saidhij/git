# coding: utf-8


from odoo import fields, models,api, _
from odoo.exceptions import ValidationError


class Hr_employee(models.Model):
    _inherit = 'hr.employee'

    
	
    imageemp = fields.Binary(string="Photo" ,related='image_small')	
    contractn = fields.Binary(string="Photo" ,related='image_small')	
    cname = fields.Char(string="Contract N°", related='contract_id.name')
    cstate = fields.Selection(string="Contract State", related='contract_id.state')
    start = fields.Date(string="Contract Start", related='contract_id.date_start')
    end = fields.Date(string="Contract end", related='contract_id.date_end')

  	
	
