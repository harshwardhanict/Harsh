# -*- coding: utf-8 -*-
# from odoo import http


# class Harry(http.Controller):
#     @http.route('/harry/harry', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/harry/harry/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('harry.listing', {
#             'root': '/harry/harry',
#             'objects': http.request.env['harry.harry'].search([]),
#         })

#     @http.route('/harry/harry/objects/<model("harry.harry"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('harry.object', {
#             'object': obj
#         })
