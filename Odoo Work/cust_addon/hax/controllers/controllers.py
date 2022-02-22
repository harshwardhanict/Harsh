# -*- coding: utf-8 -*-
# from odoo import http


# class Hax(http.Controller):
#     @http.route('/hax/hax', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hax/hax/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hax.listing', {
#             'root': '/hax/hax',
#             'objects': http.request.env['hax.hax'].search([]),
#         })

#     @http.route('/hax/hax/objects/<model("hax.hax"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hax.object', {
#             'object': obj
#         })
