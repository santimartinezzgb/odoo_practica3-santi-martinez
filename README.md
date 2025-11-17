# Práctica 3: Primeros módulos en Odoo

## Descripción

Práctica sobre creación, instalación y personalización de módulos en Odoo 16 usando Docker Compose.

## Repositorio

https://github.com/santimartinezzgb/odoo_practica3-santi-martinez

## Módulos creados

### 1. Hola Mundo
Módulo básico de prueba para verificar la detección de módulos personalizados.

### 2. Módulos con Scaffold
Cinco módulos orientados a la educación:
- agenda_profesor
- clases
- asistencia_alumnos
- calendario
- registro_notas

### 3. Lista de tareas
Módulo funcional completo para gestionar tareas con:
- Estados: pendiente, en progreso, completada, cancelada
- Sistema de colores
- Métodos de acción para cambiar estados

## Requisitos

- Odoo 16
- Docker y Docker Compose
- Python 3.x

## Instalación
```bash
git clone https://github.com/santimartinezzgb/odoo_practica3-santi-martinez
docker-compose up -d
```

## Actualizar módulos

1. Modificar archivos necesarios
2. Reiniciar contenedores
3. En Odoo: módulo → 3 puntos → Actualizar


## Autor

Santi Martínez
