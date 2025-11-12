# -*- coding: utf-8 -*-
# from odoo import http


# class RegistroNotas(http.Controller):
#     @http.route('/registro_notas/registro_notas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/registro_notas/registro_notas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('registro_notas.listing', {
#             'root': '/registro_notas/registro_notas',
#             'objects': http.request.env['registro_notas.registro_notas'].search([]),
#         })

#     @http.route('/registro_notas/registro_notas/objects/<model("registro_notas.registro_notas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('registro_notas.object', {
#             'object': obj
#         })
