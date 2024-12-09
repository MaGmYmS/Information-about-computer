# System Metrics Exporter

## Описание проекта

Этот проект представляет собой экспортер метрик для Prometheus, написанный на Python. Экспортер собирает метрики об использовании ядер процессоров, общем объеме оперативной памяти и дискового пространства, а также об используемой памяти и дисковом пространстве.

## Установка и запуск

### Клонирование репозитория
Клонируйте репозиторий на ваш локальный компьютер:
   ```sh
   git clone https://github.com/MaGmYmS/Information-about-computer
   ```

### Перейдите в директорию проекта

1. Перейдите в директорию проекта:
   ```sh
   cd <имя вашей директории>
   ```
   
2. Создайте виртуальное окружение и активируйте его:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Unix/MacOS
    .\venv\Scripts\activate  # Для Windows
    ```
   
3. Установите необходимые зависимости:
    ```sh
    pip install -r requirements.txt
    ```

### Запуск экспортера
1. Установите переменные окружения EXPORTER_HOST и EXPORTER_PORT:
    ```sh
    set EXPORTER_HOST=0.0.0.0
    set EXPORTER_PORT=8000
    ```
   
2. Запустите экспортер:
    ```sh
    python exporter.py
    ```
   
## Проверка работы экспортера

Откройте браузер и перейдите по адресу:

```sh
http://<EXPORTER_HOST>:<EXPORTER_PORT>/metrics
```

Например:

```sh
http://localhost:8000/metrics
```
Вы должны увидеть метрики, которые собирает ваш экспортер.


## Настройка Prometheus

1. Создайте файл конфигурации c prometheus.yml в папке Prometheus:
    ```sh
    global:
      scrape_interval: 15s
    
    scrape_configs:
      - job_name: 'python_exporter'
        static_configs:
          - targets: ['<EXPORTER_HOST>:<EXPORTER_PORT>']
          # Пример
          #- targets: ["localhost:8000"] 
   ```

2. Запустите Prometheus с этой конфигурацией:
    ```sh
    cd prometheus
    prometheus.exe
    ```

## Выполнение запросов PromQL

1. Откройте интерфейс Prometheus по адресу:
    ```sh
    http://localhost:9090
    ```
2. Выполните следующие запросы PromQL для получения метрик:
   
   + Использование процессоров:
    ```sh
    cpu_usage
    ```
    
    + Общая память:
    ```sh
    total_memory
    ```
    
    Используемая память:
    ```sh
    used_memory
    ```
    
    + Общий объем дисков:
    ```sh
    total_disk
    ```
    
    + Используемый объем дисков:
    ```sh
    used_disk
    ```
