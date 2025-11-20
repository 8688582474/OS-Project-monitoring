import psutil

def suggest_optimizations():
    suggestions = []

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    if cpu > 85:
        suggestions.append("🔴 Close background applications to reduce CPU load.")
    elif cpu > 60:
        suggestions.append("🟠 Monitor CPU usage to avoid potential slowdowns.")
    else:
        suggestions.append("✅ CPU is operating efficiently.")

    if ram > 85:
        suggestions.append("🔴 Consider upgrading RAM or closing memory-heavy apps.")
    elif ram > 60:
        suggestions.append("🟠 Check for memory leaks or unused apps.")
    else:
        suggestions.append("✅ Memory usage is optimal.")

    if disk > 90:
        suggestions.append("🔴 Free up disk space by deleting unnecessary files.")
    elif disk > 70:
        suggestions.append("🟠 Clean up temporary files and large unused data.")
    else:
        suggestions.append("✅ Disk storage is well-managed.")

    return suggestions
