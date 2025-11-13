# -*- coding: utf-8 -*-
# from odoo import http


# class ListaDeTareas(http.Controller):
#     @http.route('/lista_de_tareas/lista_de_tareas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lista_de_tareas/lista_de_tareas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lista_de_tareas.listing', {
#             'root': '/lista_de_tareas/lista_de_tareas',
#             'objects': http.request.env['lista_de_tareas.lista_de_tareas'].search([]),
#         })

#     @http.route('/lista_de_tareas/lista_de_tareas/objects/<model("lista_de_tareas.lista_de_tareas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lista_de_tareas.object', {
#             'object': obj
#         })
