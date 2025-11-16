# -*- coding: utf-8 -*-
from odoo import models, fields

# Creación de la clase ListaTareas como módulo
class ListaTareas(models.Model):

    # Nombre del módulo
    _name = 'lista.tareas'
    # Nombre que aparece en el módulo
    _description = 'Lista de Tareas'

    # Nombre de la tarea:
    #   - Palabra Título
    #   - required=True: es obligatorio 
    nombre = fields.Char("Título", required=True)

    # Descripción de la tarea:
    #   - Palabra Descripción
    descripcion = fields.Text("Descripción")

    # Nombre de la tarea:
    #   - Palabra título
    #   - default=False: significa que de forma predeterminada aparece de otra manera
    completada = fields.Boolean("Completada", default=False)

    # Array con los diferentes estados de la tarea
    #   - Palabra Estado
    #   - default='pendiente': de forma predeterminada aparece como 'pendiente'
    #   - required=True: es obligatorio 
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ], string='Estado', default='pendiente', required=True)


    # Acción iniciar tarea: Hace que inicie la tarea y esta se encuentre en progreso
    def action_iniciar(self):
        # estado de la tarea = 'en_progreso'
        self.write({'estado': 'en_progreso'})

    # Acción completar tarea: Al ejecutarse indica que la tarea está completada
    def action_completar(self):
        # estado de la tarea = 'completada' |   indica que está completada
        self.write({'estado': 'completada', 'completada': True})

    # Acción cancelar tarea: Hace que la tarea se elimine/cancele
    def action_cancelar(self):
        # estado de la tarea = 'cancelada'
        self.write({'estado': 'cancelada'})

    # Acción reabrir tarea: Retoma una tarea y le devuelve el estado de pendiente y le quita el 'completada'
    def action_reabrir(self):
        self.write({'estado': 'pendiente', 'completada': False})
