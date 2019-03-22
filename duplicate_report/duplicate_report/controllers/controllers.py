# -*- coding: utf-8 -*-
from odoo import http

# class Duplicate(http.Controller):
#     @http.route('/duplicate/duplicate/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/duplicate/duplicate/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('duplicate.listing', {
#             'root': '/duplicate/duplicate',
#             'objects': http.request.env['duplicate.duplicate'].search([]),
#         })

#     @http.route('/duplicate/duplicate/objects/<model("duplicate.duplicate"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('duplicate.object', {
#             'object': obj
#         })