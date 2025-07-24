import pandas as pd
from io import StringIO

# =============================
# DATOS SIMULADOS (Datos pequeños embebidos)
# =============================

# Datos de ventas
ventas_data = """Factura,Cliente,Fecha,Monto
F001,Juan,2025-06-01,150
F002,Ana,2025-06-02,11000
F002,Ana,2025-06-02,11000
F003,Pedro,2025-06-03,-15
F004,Lucas,2025-06-04,350"""

ventas = pd.read_csv(StringIO(ventas_data))

# Datos de pagos
pagos_data = """Factura,Banco,Fecha_Pago,Valor_Pagado
F001,Banco A,2025-06-02,150
F003,Banco B,2025-06-04,-15"""

pagos = pd.read_csv(StringIO(pagos_data))

# Datos de registros (horarios)
registros_data = """Usuario,Hora
Juan,07:45
Ana,08:30
Pedro,18:45
Lucas,12:15"""

registros = pd.read_csv(StringIO(registros_data))
registros['Hora'] = pd.to_datetime(registros['Hora'], format='%H:%M')

# Datos de nómina
nomina_data = """Empleado,Horas_Extras
Juan,10
Ana,13
Pedro,20
Lucas,5"""

nomina = pd.read_csv(StringIO(nomina_data))

# =============================
# PRUEBAS DE AUDITORÍA
# =============================

# 1. Facturas Duplicadas
facturas_duplicadas = ventas[ventas.duplicated(subset=['Factura', 'Fecha'], keep=False)]

# 2. Montos Inusuales
montos_inusuales = ventas[(ventas['Monto'] > 10000) | (ventas['Monto'] < 0)]

# 3. Conciliación de Pagos
cruce = ventas.merge(pagos, on='Factura', how='left', indicator=True)
no_pagadas = cruce[cruce['_merge'] == 'left_only']

# 4. Registros Fuera de Horario (08:00 - 18:00)
fuera_horario = registros[(registros['Hora'] < pd.to_datetime('08:00')) | (registros['Hora'] > pd.to_datetime('18:00'))]

# 5. Horas Extras Excesivas
horas_exceso = nomina[nomina['Horas_Extras'] > 12]

# =============================
# MOSTRAR RESULTADOS EN CONSOLA
# =============================

print("\n🔍 FACTURAS DUPLICADAS:")
print(facturas_duplicadas)

print("\n💰 MONTOS INUSUALES:")
print(montos_inusuales)

print("\n💳 FACTURAS NO PAGADAS:")
print(no_pagadas[['Factura', 'Cliente', 'Fecha', 'Monto']])

print("\n⏰ REGISTROS FUERA DE HORARIO:")
print(fuera_horario)

print("\n🕒 HORAS EXTRAS EXCESIVAS:")
print(horas_exceso)
