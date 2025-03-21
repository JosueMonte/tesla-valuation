# Análisis Financiero de Tesla con Gobernanza de Datos
Este proyecto demuestra mi capacidad para analizar datos financieros de Tesla utilizando MySQL y Tableau Public, con un fuerte enfoque en gobernanza de datos.

## Objetivo
Analizar los estados financieros de Tesla (ingresos, balances, flujos de efectivo) asegurando la calidad y estructura de los datos mediante prácticas de gobernanza.

## Gobernanza de Datos Implementada
1. **Políticas de Calidad**: 
   - Eliminación de duplicados en transacciones financieras.
   - Validación de valores: ingresos y activos no negativos.
   - Estandarización de formatos (fechas en YYYY-MM-DD).
2. **Estructura**: 
   - Datos organizados en tablas relacionales (`Income_Statement`, `Balance_Sheet`, `Cash_Flow`).
   - Documentación de metadatos en `docs/metadata.md`.
3. **Procesos**: 
   - Pipeline automatizado en Python para limpieza y carga a MySQL.

## Tecnologías
- **MySQL**: Base de datos relacional para almacenar y consultar datos financieros.
- **Python**: Scripts de limpieza y validación (pandas).
- **Tableau Public**: Dashboard interactivo con métricas clave.

## Estructura del Repositorio
- `data/raw/`: Datos financieros originales.
- `data/clean/`: Datos procesados y validados.
- `scripts/clean_data.py`: Código para limpieza y gobernanza.
- `sql/tables.sql`: Definición de tablas y consultas.
- `dashboard/tesla_dashboard.twbx`: Archivo de Tableau (o enlace a Tableau Public).

## Resultados
- Dataset limpio y gobernado en MySQL.
- Dashboard en Tableau con tendencias de ingresos, márgenes y flujos de efectivo.
