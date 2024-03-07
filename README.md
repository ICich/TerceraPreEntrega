# AppMantenimiento  

PreEntrega3 Coderhouse

El proyecto consta de una aplicacion para llevar el registro de mantenimientos a vehiculos, realizados en un taller mecanico.

## Requerimientos
* Python: Este puede ser descargado desde [python.org](https://www.python.org/downloads/)
* Django: Este puede ser instalado con el comando `pip install django`

## Orden
1. Primero hacer las migraciones si es necesario: `python manage.py makemigrations`
2. Seguido el migrate: `python manage.py migrate`
3. Finalmente para correr el servidor: `python manage.py runserver`

## URLS
Los urls funcionales son:

**/nuevo_mecanico/: URL para agregar un nuevo mecánico.  
**/nuevo_vehiculo/: URL para agregar un nuevo vehículo.  
**/nuevo_mantenimiento/: URL para agregar un nuevo mantenimiento.  
**/buscar_mecanico/: URL para buscar un mecánico.  
**/resultado/: URL para mostrar los resultados de la búsqueda de mecánicos.
