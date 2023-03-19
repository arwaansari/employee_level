from odoo import models, fields


class EmployeeLevel(models.Model):
    _name = "employee.level"
    _description = "Employee Level"
    _rec_name = 'level'
    _order = 'id desc'

    level = fields.Char(string='Level')
    salary = fields.Float(string='Salary')
