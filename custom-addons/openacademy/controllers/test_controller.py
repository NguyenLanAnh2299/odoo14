# from odoo import http
# from odoo.http import request
#
#
# class MyController(http.Controller):
#     @http.route('/some_url', auth='public')
#     def handler(self):
#         db_model = self.pool.get('base.external.dbsource')
#         res = db_model.execute(cr, uid, [<dbsource_id>], <sql_query>, <sql_params>)
#         for row in res['rows']:
#             print row
#         return "hello world!"
