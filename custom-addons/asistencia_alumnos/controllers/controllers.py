# -*- coding: utf-8 -*-
# from odoo import http


# class AsistenciaAlumnos(http.Controller):
#     @http.route('/asistencia_alumnos/asistencia_alumnos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asistencia_alumnos/asistencia_alumnos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('asistencia_alumnos.listing', {
#             'root': '/asistencia_alumnos/asistencia_alumnos',
#             'objects': http.request.env['asistencia_alumnos.asistencia_alumnos'].search([]),
#         })

#     @http.route('/asistencia_alumnos/asistencia_alumnos/objects/<model("asistencia_alumnos.asistencia_alumnos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asistencia_alumnos.object', {
#             'object': obj
#         })
