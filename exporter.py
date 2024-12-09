from prometheus_client import start_http_server, Gauge
import psutil
import time
import os

# Создаем метрики с метками
cpu_usage = Gauge('cpu_usage', 'Usage of CPU cores', ['core'])
total_memory = Gauge('total_memory', 'Total RAM in the OS in GB')
used_memory = Gauge('used_memory', 'Used RAM in the OS in GB')
total_disk = Gauge('total_disk', 'Total disk space in GB')
used_disk = Gauge('used_disk', 'Used disk space in GB')


def collect_metrics():
    # Сбор метрик CPU
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    for i, percentage in enumerate(cpu_percent):
        cpu_usage.labels(core=str(i)).set(percentage)

    # Сбор метрик памяти
    mem = psutil.virtual_memory()
    total_memory.set(round(mem.total / (1024 ** 3), 3))  # Переводим в гигабайты
    used_memory.set(round(mem.used / (1024 ** 3), 3))  # Переводим в гигабайты

    # Сбор метрик диска
    disk = psutil.disk_usage('/')
    total_disk.set(round(disk.total / (1024 ** 3), 3))  # Переводим в гигабайты
    used_disk.set(round(disk.used / (1024 ** 3), 3))  # Переводим в гигабайты


if __name__ == '__main__':
    # Определяем переменные окружения
    exporter_host = os.getenv('EXPORTER_HOST', '0.0.0.0')
    exporter_port = int(os.getenv('EXPORTER_PORT', 8000))

    # Создаем ссылку на метрики
    metrics_url = f"http://localhost:{exporter_port}/metrics"
    print(f"Metrics available at: {metrics_url}")

    # Запускаем HTTP-сервер для Prometheus
    start_http_server(exporter_port, addr=exporter_host)

    # Бесконечный цикл для сбора метрик
    while True:
        collect_metrics()
        time.sleep(1)
