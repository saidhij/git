# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import models, fields, api

class EmployeDocuments(models.Model):
    _name = 'report.employee_of_the_month_fancy.fancy_certificate_report'


    @api.model
    def get_report_values(self,docids, data=None):
        records = self.env['hr.employee'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'hr.employee',
            'docs': records,
            'data': data,
         
           
        }


