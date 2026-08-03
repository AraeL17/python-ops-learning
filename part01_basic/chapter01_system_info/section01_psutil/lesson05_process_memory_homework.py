import psutil


def bytes_to_mb(byte):
    # 将字节转换成 MB，并保留两位小数
    mb = byte / 1024 ** 2
    return round(mb, 2)

def get_process_memory_list(limit=10) -> list:
    process_list = []
    
    processes = psutil.process_iter(
        attrs=['pid', 'name', 'memory_info'],
        ad_value=None
    )
    
    for process in processes:
        info = process.info
        
        memory_info = info['memory_info']
        
        if memory_info is None:
            # memory_mb = None 
            # 由于大部分进程管理员为 root 权限不足大部分为 None 
            # 所以设置为 None 就跳过循环
            continue
        
        memory_mb = bytes_to_mb(memory_info.rss)
        
        process_list.append({
            'pid': info['pid'],
            'name': info['name'],
            'memory_mb': memory_mb
        })
        
        if len(process_list) >= limit:
            break
        
    return process_list

def main():
    process_list = get_process_memory_list()
    
    for process in process_list:
        print(process)
        
if __name__ == "__main__":
    main()