import platform
import psutil

def get_system_info():
    print("Printing System Information.... ")
    print("--------------------------------")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release Date: {platform.release()}")
    print(f"Machine: {platform.machine()}")
    print(f"CPU usage: {psutil.cpu_percent()}")
    print(f"Memory usage: {psutil.virtual_memory().percent}")
    print(f"Disk usage: {psutil.disk_usage('/').percent}")


if __name__ == "__main__":
    get_system_info()
