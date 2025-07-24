# CAAT - Herramienta de Auditoría Asistida por Computadora

## 📌 Descripción
Este proyecto desarrolla una herramienta CAAT en Python, capaz de realizar 5 pruebas de auditoría básicas sobre datos simulados, sin necesidad de cargar archivos externos.

## 🧪 Pruebas implementadas
1. **Facturas Duplicadas**  
2. **Montos Inusuales (> $10.000 o negativos)**  
3. **Conciliación de Pagos (facturas sin pago)**  
4. **Registros Fuera de Horario (antes de 08:00 o después de 18:00)**  
5. **Horas Extras Excesivas (> 12 horas/semana)**

## 🛠 Cómo ejecutar
1. Instala pandas:  
```bash
pip install pandas
```

2. Ejecuta el archivo `codigo_caat.py`  
```bash
python codigo_caat.py
```

3. Los resultados se mostrarán por consola.

## ⚠️ Errores encontrados y soluciones

- ❌ Error al convertir texto a hora (`Hora`)  
  ✅ Solución: Se usó `pd.to_datetime(registros['Hora'], format='%H:%M')`

- ❌ Duplicados no detectados solo con ID  
  ✅ Solución: Se usó `duplicated` con `subset=['Factura', 'Fecha']` para mayor precisión.

## ✅ Avance correspondiente a:
**Semana 3 – Proyecto Final CAAT – 2do Parcial**
