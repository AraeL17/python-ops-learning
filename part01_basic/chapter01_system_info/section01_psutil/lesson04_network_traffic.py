import psutil


def bytes_to_mb(byte):
    # 将字节换成 MB，并保留两位小数
    mb = byte / 1024 ** 2
    return round(mb, 2)

def main():
    # 在使用中函数没设置 pernic=True 时，为返回所有网络接口的总流量
    total_io = psutil.net_io_counters()
    
    print("系统总网络流量：")
    
    # bytes_sent 统计累计发送的字节数
    print(f"发送流量：{bytes_to_mb(total_io.bytes_sent)} MB")
    
    # bytes_recv 统计累计接收的字节数
    print(f"接收流量：{bytes_to_mb(total_io.bytes_recv)} MB")
    
    # packets_sent 统计累计发送的数据包数量
    print(f"发送数据包：{total_io.packets_sent} 个")
    
    # packets_sent 统计累计接收的数据包数量
    print(f"接收数据包：{total_io.packets_recv} 个")
    
    # errin 统计接收数据包出现的错误数量
    print(f"接收错误：{total_io.errin}")
    
    # errin 统计发送数据包出现的错误数量
    print(f"接收错误：{total_io.errout}")
    
    # pernic=True 表示分别获取每个网络接口的流量
    # 返回值是字典：键是接口名称，值是接口流量信息
    interface_io = psutil.net_io_counters(pernic=True)
    
    print("\n各个网络接口的流量：")
    
    for interface_name, counters in interface_io.items():
        print(f"\n网络接口：{interface_name}")
        
        # 当前接口累计发送的流量
        print(f"    发送流量：{bytes_to_mb(counters.bytes_sent)} MB")

        # 当前接口累计接收的流量
        print(f"    接收流量：{bytes_to_mb(counters.bytes_recv)} MB")

        # 当前接口累计发送的数据包数量
        print(f"    发送数据包：{counters.packets_sent} 个")

        # 当前接口累计接收的数据包数量
        print(f"    发送数据包：{counters.packets_recv} 个")

        # 当前接口接收和发送时的错误数量
        print(f"    接收错误：{counters.errin}")
        print(f"    接收错误：{counters.errout}")
        
if __name__ == "__main__":
    main()