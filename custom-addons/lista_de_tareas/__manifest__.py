# -*- coding: utf-8 -*-
{
    'name': "Lista de Tareas",
    'summary': "Gestión simple de tareas",
    'description': """
        Módulo para crear, editar y administrar tareas con estados y etiquetas.
    """,
    'author': "Mi Empresa",
    'category': 'Productivity',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}