# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ListaTareas(models.Model):
    _name = 'lista.tareas'
    _description = 'Lista de Tareas'

    nombre = fields.Char("Título", required=True)
    descripcion = fields.Text("Descripción")
    completada = fields.Boolean("Completada", default=False)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ], string='Estado', default='pendiente', required=True)

    def action_iniciar(self):
        self.write({'estado': 'en_progreso'})

    def action_completar(self):
        self.write({'estado': 'completada', 'completada': True})

    def action_cancelar(self):
        self.write({'estado': 'cancelada'})

    def action_reabrir(self):
        self.write({'estado': 'pendiente', 'completada': False})
