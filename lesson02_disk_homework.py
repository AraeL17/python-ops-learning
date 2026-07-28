import psutil

def bytes_to_gb(byte):
    gb = byte / 1024 ** 3
    return round(gb,2)  

# 返回根目录所在磁盘的信息，并返回字典
def get_root_disk_info() -> dict:
    # 获取根目录的磁盘信息（就是获取根所在的硬盘的信息）
    root_usage = psutil.disk_usage("/")
    total_gb = bytes_to_gb(root_usage.total)
    used_gb = bytes_to_gb(root_usage.used)
    free_gb = bytes_to_gb(root_usage.free)
    percent = root_usage.percent
    
    return {'total_gb': total_gb, 'used_gb': used_gb , 'free_gb': free_gb, 'percent': percent}

# 获取所有磁盘分区的基本信息，最终返回一个列表。
def get_partition_info() -> list:
    partition_list = []
    
    # 获取系统分区信息
    partitions = psutil.disk_partitions()
    for partition in partitions:
        device = partition.device
        mountpoint = partition.mountpoint
        fstype = partition.fstype
        partition_list.append({'device': device,'mountpoint': mountpoint,'fstype': fstype})
    
    return partition_list

def main():
    print(f"磁盘信息：{get_root_disk_info()}")
    
    print("\n分区信息：")
    partition_list = get_partition_info()
    print(f"分区数量：{len(partition_list)}")
    for item in partition_list:
        print(item)
        
if __name__ == "__main__":
    main()