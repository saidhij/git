# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
##############################################################################

from datetime import datetime

from odoo import api, fields, models

to_string = fields.Date.to_string

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'
    
    payment_mode = fields.Selection([('Cheque', 'Cheque'), ('Virement', 'Virement'), ('Espece', 'Espece')], 'Mode de paiement')
    payment_date = fields.Date(default=fields.Date.today)
	


    @api.multi
    def compute_sheet(self):
        res = super(HrPayslip, self).compute_sheet()
        self.compute_ytd_amounts()
        return res

    @api.one
    def compute_ytd_amounts(self):
        if not self.line_ids:
            return

        query = (
            """SELECT pl_1.id, sum(
                case when p.credit_note then -pl_2.amount else pl_2.amount end)
            FROM hr_payslip_line pl_1, hr_payslip_line pl_2, hr_payslip p
            WHERE pl_1.id IN %(payslip_line_ids)s
            AND pl_1.salary_rule_id = pl_2.salary_rule_id
            AND pl_2.slip_id = p.id
            AND p.employee_id = %(employee_id)s
            AND p.company_id = %(company_id)s
            AND (p.state = 'draft' OR p.id = %(payslip_id)s)
            AND %(date_from)s <= p.date_payment
            AND p.date_payment <= %(date_to)s
            GROUP BY pl_1.id
            """)

        date_payment = fields.Date.from_string(self.date_payment)
        date_from = fields.Date.to_string(
            datetime(date_payment.year, 1, 1))

        cr = self.env.cr

        cr.execute(query, {
            'date_from': date_from,
            'date_to': self.date_payment,
            'payslip_line_ids': tuple(self.line_ids.ids),
            'employee_id': self.employee_id.id,
            'company_id': self.company_id.id,
            'payslip_id': self.id,
        })

        res = cr.fetchall()

        line_model = self.env['hr.payslip.line']

        for (line_id, amount_ytd) in res:
            line = line_model.browse(line_id)
            line.amount_ytd = amount_ytd

    @api.multi
    def ytd_amount(self, total):
        """
        Get the total amount since the beginning of the year
        of a given salary rule code.

        :param code: salary rule code
        :return: float
        """
        self.ensure_one()

        date_slip = fields.Date.from_string(self.date_payment)
        date_from = to_string(datetime(date_slip.year, 1, 1))

        query = (
            """SELECT sum(case when hp.credit_note = False then (pl.total) else (-pl.total) end)
            FROM hr_payslip_line as pl, hr_payslip as p
            WHERE pl.slip_id = p.id
            AND pl.total = p.total
            AND p.employee_id = %(employee_id)s
            AND p.company_id = %(company_id)s
            AND %(date_from)s <= p.date_payment
            AND p.date_payment <= %(date_to)s AND p.id = pl.slip_id AND pl.code = %s"""
            
        )


        cr = self.env.cr

        cr.execute(query, {
            'date_from': date_from,
            'date_to': self.date_payment,
            'company_id': self.company_id.id,
            'employee_id': self.employee_id.id,
            'total': total,
        })

        return cr.fetchone()[0] or 0
		
		
	