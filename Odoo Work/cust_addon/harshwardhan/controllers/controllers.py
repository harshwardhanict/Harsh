# -*- coding: utf-8 -*-
# from odoo import http


# class Harshwardhan(http.Controller):
#     @http.route('/harshwardhan/harshwardhan', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/harshwardhan/harshwardhan/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('harshwardhan.listing', {
#             'root': '/harshwardhan/harshwardhan',
#             'objects': http.request.env['harshwardhan.harshwardhan'].search([]),
#         })

#     @http.route('/harshwardhan/harshwardhan/objects/<model("harshwardhan.harshwardhan"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('harshwardhan.object', {
#             'object': obj
#         })
