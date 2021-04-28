from odoo import http
from odoo.addons.base_external_dbsource.models.base_external_dbsource import BaseExternalDbsource
from odoo.http import request


class MyController(http.Controller):

    @http.route('/some_url', auth='public')
    def handler(self):
        vals = {}
        db_model = request.env.ref("base_external_dbsource_oracle.demo_oracle")

        conn = db_model.connection_open()

        query = 'select code, name from APPLICATION'

        cursor = db_model.execute(query,'')
        arrData = []
        for row in cursor.fetchall() or []:
            vals['code'] = row[0]
            vals['name'] = row[1]

        BaseExternalDbsource.connection_close(request.dbsource, conn)
        return "hello world!"

