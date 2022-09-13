from odoo import models, fields, api


class hr_report(models.Model):
    _inherit = 'hr.employee'

    test_name = fields.Char()
