import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime, timedelta

# Gerar dados simulados
def generate_traffic_data(start_date, num_records):
    """Gera dados simulados de tráfego."""
    data = []
    current_time = start_date
    for _ in range(num_records):
        vehicle_count = random.randint(0, 100)  # Simula o número de veículos
        data.append([current_time, vehicle_count])
        current_time += timedelta(minutes=5)  # Incrementa o tempo em 5 minutos
    return pd.DataFrame(data, columns=['Timestamp', 'VehicleCount'])

# Processar dados
def process_traffic_data(df):
    """Processa dados de tráfego para análise."""
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)
    df_resampled = df.resample('1H').sum()  # Resample para dados horários
    return df_resampled

# Visualizar dados
def plot_traffic_data(df):
    """Gera um gráfico dos dados de tráfego."""
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['VehicleCount'], marker='o', linestyle='-', color='b')
    plt.title('Número de Veículos por Hora')
    plt.xlabel('Hora')
    plt.ylabel('Número de Veículos')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Parâmetros
start_date = datetime(2024, 8, 16, 0, 0)
num_records = 288  # Aproximadamente um dia de dados com intervalos de 5 minutos

# Gerar e processar dados
traffic_data = generate_traffic_data(start_date, num_records)
processed_data = process_traffic_data(traffic_data)

# Visualizar resultados
plot_traffic_data(processed_data)