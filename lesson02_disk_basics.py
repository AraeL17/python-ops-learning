import psutil

def bytes_to_gb(byte):
    """将字节转换成 GB。"""
    gb = byte / 1024 ** 3
    return round(gb, 2)

def main():
    partitions = psutil.disk_partitions()
    
    print(f"磁盘分区数量:{len(partitions)}")
    
    if partitions:
        first_partitions = partitions[0]
        
        print(f"\n第一个磁盘分区的信息:")
        
        print(f"设备名称:{first_partitions.device}")
        
        print(f"挂载点:{first_partitions.mountpoint}")
        
        print(f"文件系统:{first_partitions.fstype}")
        
        print(f"挂载选项:{first_partitions.opts}")
        
    # 获取根目录“/”所在磁盘的容量信息
    root_usage = psutil.disk_usage("/")
    
    print("\n根目录所在磁盘的使用情况:")
    
    print(f"总容量:{bytes_to_gb(root_usage.total)}")
    
    print(f"已使用:{bytes_to_gb(root_usage.used)}")
    
    print(f"剩余容量:{bytes_to_gb(root_usage.free)}")
    
    print(f"使用率:{root_usage.percent}")
    
    print("\n所有磁盘分区：")

    for partition in partitions:
        print(
            f"设备:{partition.device},"
            f"挂载点:{partition.mountpoint},"
            f"文件系统:{partition.fstype}"
        )
        
if __name__ == "__main__":
    main()