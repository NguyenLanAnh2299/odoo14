from odoo import api, models, fields
import requests

class CustomCategories(models.TransientModel):
    _name = "test_module.categories"
    _description = "Description custom categories"
    id = fields.Integer()
    code = fields.Char("code")
    name = fields.Char("name")

    @api.model
    def search_read(self, domain=None, fields=None, offset=0,
            limit=None, order=None):
        r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
        data = r.json()
        vals = {}
        list = data['data']
        for row in list or []:
            row['id'] = row["nationId"]
        # res = super(CustomCategories, self).search_read(domain, fields, offset, limit, order)
        return list

    def unlink(self):
        # "your code"
        return True

    @api.model
    def create(self, vals):
        rec = super(CustomCategories, self).create(vals)
        return rec

    @api.model
    def read(self):
        # rec = super(CustomCategories, self).search(vals)
        return "1"

    @api.model
    def write(self, vals):
        rec = super(CustomCategories, self).write(vals)
        return rec

    def get_odbc_data(self):
        r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
        data = r.json()
        vals = {}
        self.env['test_module.categories'].search([]).unlink()
        for row in data['data'] or []:
            vals['code'] = row["code"]
            vals['name'] = row["name"]
            self.create(vals)

        # db_model.connection_close(conn)
        action_vals =  {'name': 'Transient Model from external datasource',
                        'type': 'ir.actions.act_window',
                        'view_mode': 'tree',
                        'res_model': 'test_module.categories',
                        }
        return action_vals