# -*- coding: utf-8 -*-
# from odoo import http


# class AgendaProfesor(http.Controller):
#     @http.route('/agenda_profesor/agenda_profesor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agenda_profesor/agenda_profesor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('agenda_profesor.listing', {
#             'root': '/agenda_profesor/agenda_profesor',
#             'objects': http.request.env['agenda_profesor.agenda_profesor'].search([]),
#         })

#     @http.route('/agenda_profesor/agenda_profesor/objects/<model("agenda_profesor.agenda_profesor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agenda_profesor.object', {
#             'object': obj
#         })
