# Trabajo Práctico N° 9 - Programación 4 - 6° Año PROA

import pandas as pd
import matplotlib.pyplot as plt

# ========== 1️⃣ Proyecto: Ubipark ==========

data_ubipark = {
    'Estacionamiento': ['Est1', 'Est2', 'Est3', 'Est4', 'Est5'],
    'Dia1': [80, 70, 85, 60, 95],
    'Dia2': [75, 80, 88, 70, 90],
    'Dia3': [85, 75, 80, 65, 80],
    'Dia4': [90, 85, 88, 60, 85],
    'Dia5': [80, 78, 75, 65, 88],
    'Dia6': [95, 90, 85, 70, 80],
    'Dia7': [88, 80, 80, 75, 92]
}

df_ubipark = pd.DataFrame(data_ubipark)
df_ubipark.set_index('Estacionamiento', inplace=True)

print("=== Ubipark ===")
promedio_dia = df_ubipark.mean(axis=0)
print("Promedio de ocupación por día:\n", promedio_dia)
print(f"Día con mayor ocupación: {promedio_dia.idxmax()}")
print(f"Día con menor ocupación: {promedio_dia.idxmin()}")

df_ubipark.T.plot(kind='bar', figsize=(10,6))
plt.title('Ocupación de Estacionamientos por Día')
plt.xlabel('Día')
plt.ylabel('Ocupación (%)')
plt.show()


# ========== 2️⃣ Proyecto: Planeta Modo Off ==========

data_modo_off = {
    'usuario': ['Ana', 'Luis', 'Carla', 'Julián', 'Esteban'],
    'minutos_diarios': [120, 45, 60, 150, 90],
    'desafios_completados': [4, 2, 3, 5, 4],
    'edad': [25, 30, 22, 28, 35]
}

df_modo_off = pd.DataFrame(data_modo_off)

print("\n=== Planeta Modo Off ===")
print("Media de minutos desconectados:", df_modo_off['minutos_diarios'].mean())
print("Desviación estándar:", df_modo_off['minutos_diarios'].std())

plt.scatter(df_modo_off['edad'], df_modo_off['minutos_diarios'])
plt.title('Edad vs Minutos Desconectados')
plt.xlabel('Edad')
plt.ylabel('Minutos Desconectados')
plt.show()

plt.hist(df_modo_off['desafios_completados'], bins=5)
plt.title('Histograma de Desafíos Completados')
plt.xlabel('Desafíos')
plt.ylabel('Frecuencia')
plt.show()


# ========== 3️⃣ Proyecto: Civic Report ==========

data_civic_report = {
    'tipo_problema': ['Alumbrado', 'Bache', 'Alumbrado', 'Bache', 'Basura'],
    'barrio': ['Centro', 'Norte', 'Sur', 'Centro', 'Este'],
    'tiempo_resolucion': [2, 5, 3, 4, 6]
}

df_civic_report = pd.DataFrame(data_civic_report)

print("\n=== Civic Report ===")
print("Promedio por tipo de problema:\n", df_civic_report.groupby('tipo_problema')['tiempo_resolucion'].mean())
print("Mediana por tipo de problema:\n", df_civic_report.groupby('tipo_problema')['tiempo_resolucion'].median())

df_civic_report['tipo_problema'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Tipos de Problemas Reportados')
plt.ylabel('')
plt.show()


# ========== 4️⃣ Proyecto: SafeZone ==========

data_safezone = {
    'alertas_enviadas': [50, 60, 45, 70, 65],
    'hora_alerta': [9, 14, 18, 3, 20],
    'tiempo_respuesta': [15, 20, 10, 25, 18]
}

df_safezone = pd.DataFrame(data_safezone)

print("\n=== SafeZone ===")
print("Moda de hora de alerta:", df_safezone['hora_alerta'].mode()[0])
print("Mediana de hora de alerta:", df_safezone['hora_alerta'].median())

plt.scatter(df_safezone['alertas_enviadas'], df_safezone['tiempo_respuesta'])
plt.title('Alertas vs Tiempo de Respuesta')
plt.xlabel('Alertas Enviadas')
plt.ylabel('Tiempo de Respuesta (min)')
plt.show()

plt.hist(df_safezone['hora_alerta'], bins=8)
plt.title('Frecuencia de Alertas por Hora')
plt.xlabel('Hora del Día')
plt.ylabel('Frecuencia')
plt.show()


# ========== 5️⃣ Proyecto: Colilla Amigable ==========

data_colilla = {
    'lugar': ['Plaza1', 'Plaza2', 'Plaza3', 'Plaza4', 'Plaza5'],
    'usuarios': [300, 250, 200, 150, 350],
    'colillas_recogidas': [1200, 1000, 800, 600, 1400]
}

df_colilla = pd.DataFrame(data_colilla)

print("\n=== Colilla Amigable ===")
print("Promedio de colillas recogidas:", df_colilla['colillas_recogidas'].mean())
print("Correlación entre usuarios y colillas:", df_colilla['usuarios'].corr(df_colilla['colillas_recogidas']))

df_colilla.set_index('lugar')['colillas_recogidas'].plot(kind='bar')
plt.title('Colillas Recogidas por Lugar')
plt.xlabel('Lugar')
plt.ylabel('Colillas Recogidas')
plt.show()
