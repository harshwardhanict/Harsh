# -*- coding: utf-8 -*-
# from odoo import http


# class Harsh(http.Controller):
#     @http.route('/harsh/harsh', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/harsh/harsh/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('harsh.listing', {
#             'root': '/harsh/harsh',
#             'objects': http.request.env['harsh.harsh'].search([]),
#         })

#     @http.route('/harsh/harsh/objects/<model("harsh.harsh"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('harsh.object', {
#             'object': obj
#         })
