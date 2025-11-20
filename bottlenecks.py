import pandas as pd
import psutil

def get_real_time_metrics():
    data = {
        'CPU (%)': [psutil.cpu_percent(interval=1)],
        'RAM (%)': [psutil.virtual_memory().percent],
        'Disk (%)': [psutil.disk_usage('/').percent]
    }
    return pd.DataFrame(data)

def detect_bottlenecks():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    issues = []

    if cpu > 85:
        issues.append("⚠️ High CPU usage detected!")
    elif cpu > 60:
        issues.append("Moderate CPU usage observed.")
    else:
        issues.append("✅ CPU usage is within normal range.")

    if ram > 85:
        issues.append("⚠️ High RAM usage detected!")
    elif ram > 60:
        issues.append("Moderate RAM usage observed.")
    else:
        issues.append("✅ RAM usage is within normal range.")

    if disk > 90:
        issues.append("⚠️ Disk space critically low!")
    elif disk > 70:
        issues.append("Moderate disk usage observed.")
    else:
        issues.append("✅ Disk usage is healthy.")

    return issues
