# -*- coding: utf-8 -*-
# from odoo import http


# class Alcance(http.Controller):
#     @http.route('/alcance/alcance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alcance/alcance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('alcance.listing', {
#             'root': '/alcance/alcance',
#             'objects': http.request.env['alcance.alcance'].search([]),
#         })

#     @http.route('/alcance/alcance/objects/<model("alcance.alcance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alcance.object', {
#             'object': obj
#         })
