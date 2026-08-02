import psutil


def bytes_to_mb(byte):
    # 将字节转换成 MB，并保留两位小数
    mb = byte / 1024 ** 2
    return round(mb, 2)


def get_top_memory_processes(limit=10) -> list:
    process_list = []
    
    processes_list = psutil.process_iter(
        attrs=['pid', 'name', 'memory_info'],
        ad_value=None
    )
    
    for process in processes_list:
        
        if process.info['memory_info'] is None:
            continue
        memory_mb = bytes_to_mb(process.info['memory_info'].rss)
        
        process_list.append({
            'pid': process.info['pid'],
            'name': process.info['name'],
            'memory_mb': memory_mb
        })
        
    process_list.sort(
        key=lambda item: item['memory_mb'],
        reverse=True
    )
        
    return process_list[:limit]

if __name__ == "__main__":
    processes = get_top_memory_processes()
    
    print("占用内存最大的前十个进程：")
    for process in processes:
        print(process)