#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) odoo. All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import models, fields, api

class EmployeDocuments(models.AbstractModel):
    _name = 'report.hr_employee_certificates.certificate_report'

    def wage():
            
        amt = 0 
        data = self.env['hr.contract'].search([('employee_id.id','=',records.id)])
        for x in data:
            amt = x.wage

        return amt

    @api.model
    def get_report_values(self,docids, data=None):
        records = self.env['hr.employee'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'hr.employee',
            'docs': records,
            'data': data,
            'lang': "fr_FR",
            'get_wage': self.wage,
        }


