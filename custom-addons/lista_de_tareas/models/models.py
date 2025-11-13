from odoo import models, fields, api

class ListaDeTareas(models.Model):
    _name = 'lista.tareas'
    _description = 'Lista de Tareas'
    _order = 'estado, create_date desc'

    nombre = fields.Char(string="Título", required=True)
    descripcion = fields.Text(string="Descripción")
    valor = fields.Integer(string="Valor")
    valor2 = fields.Float(string="Valor en %", compute="_calcular_valor", store=True)
    completada = fields.Boolean(string="Completada", default=False)
    
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ], string='Estado', default='pendiente', required=True)
    
    etiqueta_ids = fields.Many2many(
        'lista.tareas.etiqueta',
        string='Etiquetas'
    )
    
    color = fields.Integer(string='Color', compute='_compute_color', store=True)
    
    @api.depends('valor')
    def _calcular_valor(self):
        for record in self:
            record.valor2 = record.valor / 100 if record.valor else 0
    
    @api.depends('estado')
    def _compute_color(self):
        color_map = {
            'pendiente': 4,
            'en_progreso': 3,
            'completada': 10,
            'cancelada': 1,
        }
        for record in self:
            record.color = color_map.get(record.estado, 0)
    
    def action_iniciar(self):
        self.write({'estado': 'en_progreso'})
    
    def action_completar(self):
        self.write({'estado': 'completada', 'completada': True})
    
    def action_cancelar(self):
        self.write({'estado': 'cancelada'})
    
    def action_reabrir(self):
        self.write({'estado': 'pendiente', 'completada': False})


class ListaTareasEtiqueta(models.Model):
    _name = 'lista.tareas.etiqueta'
    _description = 'Etiqueta de Tarea'
    
    name = fields.Char(string='Etiqueta', required=True)
    color = fields.Integer(string='Color')