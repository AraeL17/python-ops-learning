import psutil

def bytes_to_gb(byte):
    gb = byte / 1024 ** 3
    return round(gb,2) 
def get_cpu_info():
    physical_count = psutil.cpu_count(logical=False) # 物理核心
    logical_count = psutil.cpu_count(logical=True) # 逻辑核心
    percent = psutil.cpu_percent(interval=1) # 采集一秒内的 CPU 使用率
    
    return {'physical_count': physical_count, 'logical_count': logical_count, 'percent': percent}


def get_memory_info():
    memory = psutil.virtual_memory()    
    total_gb = bytes_to_gb(memory.total)    # 内存总大小
    available_gb = bytes_to_gb(memory.available)    # 内存剩余大小
    percent = memory.percent    # 内存使用率
    return {'total_gb': total_gb, 'available_gb': available_gb, 'percent': percent}



if __name__ == "__main__":
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    print(f"CPU 信息：{cpu_info}")
    print(f"内存信息：{memory_info}")
    
    
    111111
    22222