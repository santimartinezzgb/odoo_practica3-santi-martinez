{
    # Nombre del módulo
    'name': "Lista de Tareas",

    # resumen
    'summary': "Gestión simple de tareas",

    # Explicación un poco más larga
    'description': """
        Este módulo sirve para poder crear tareas y cambiarlas de estado.
        También se pueden editar y poner etiquetas si hace falta.
    """,

    # Quién lo hizo
    'author': "Mi Empresa",

    # Categoría donde aparece
    'category': 'Productivity',

    # Versión del módulo
    'version': '0.1',

    # Módulos que hacen falta
    'depends': ['base'],

    # Archivos que carga el módulo
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],

    # Para que se pueda instalar
    'installable': True,

    # Para que salga como aplicación en el menú de Odoo
    'application': True,

    # Licencia
    'license': 'LGPL-3',
}
