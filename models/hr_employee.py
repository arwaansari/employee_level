from odoo import models, fields


class EmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    employee_level_id = fields.Many2one('employee.level',
                                        string='Employee Level')
    salary = fields.Float(string='Salary', related='employee_level_id.salary')
    btn_visibility = fields.Boolean()
    level_inc = fields.Integer(default=0)

    def action_promote_btn(self):
        emp_level = self.env['employee.level'].search([], order='salary asc')
        print(emp_level)
        li = [rec.id for rec in emp_level]
        if self.env['employee.level'].search([]):
            self.employee_level_id = li[self.level_inc]
            self.level_inc += 1
        if self.employee_level_id.id == li[-1]:
            self.btn_visibility = True
