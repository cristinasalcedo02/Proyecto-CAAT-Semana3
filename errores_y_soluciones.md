# 🛠 Errores y Soluciones Encontradas – Semana 3

Este documento detalla los errores encontrados durante el desarrollo de la herramienta CAAT en Python y las soluciones aplicadas para cada uno.

---

## ❌ Error 1: Conversión de Hora en el archivo de registros

**Problema:**  
Al intentar convertir los valores de la columna `Hora` a formato `datetime`, Python generaba un error de formato.

**Mensaje:**  
ValueError: time data '8:30' does not match format '%H:%M'

**Causa:**  
Los valores deben estar escritos con formato estricto, por ejemplo `08:30` y no `8:30`.

**Solución aplicada:**  
Se usó `pd.to_datetime(..., format='%H:%M')` para forzar el formato correcto y se validaron los datos con ceros a la izquierda.

---

## ❌ Error 2: No detectaba duplicados correctamente

**Problema:**  
Al aplicar `.duplicated()` en la columna `Factura` únicamente, algunas duplicaciones no se identificaban correctamente.

**Solución aplicada:**  
Se ajustó el parámetro `subset` para que detecte duplicados por combinación de `Factura` y `Fecha`:
```python
ventas.duplicated(subset=['Factura', 'Fecha'], keep=False)
```

---

## ❌ Error 3: No mostraba resultados claros

**Problema:**  
Inicialmente, el código solo ejecutaba los filtros pero no mostraba nada en pantalla.

**Solución aplicada:**  
Se agregaron `print()` estructurados para que cada resultado se visualice claramente en consola.

---

## ✅ Resultado

El código ahora ejecuta las 5 pruebas correctamente, muestra resultados por consola, y no depende de archivos externos.
