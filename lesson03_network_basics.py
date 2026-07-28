import socket
import psutil

def main():
    # 获取所有网络接口及其地址信息
    # 返回为字典，键为接口名称，值为该接口的地址列表
    interfaces = psutil.net_if_addrs()
    
    # 获取网络接口数量
    print(f"网络接口数量：{len(interfaces)}")
    
    # 逐个获取各个网卡的名字和地址列表（里面包含了ipv4，ipv6 和 mac地址，所以每一个类型是列表）
    for interface_name, addressw_list in interfaces.items():
        print(f"\n网络接口：{interface_name}")
        
        for address in addressw_list:
            # AF_INET 表示当前地址为 IPv4
            if address.family == socket.AF_INET:
                family_name = "IPv4"
                
            # AF_INET6 表示当前地址为 IPv6
            elif address.family == socket.AF_INET6:
                family_name = "IPv6"
                
            # AF_LINK 表示当前为链路层地址，通常是 MAC 地址
            elif address.family == socket.AF_LINK:
                family_name = "IPv6"

            else:
                family_name = "其他"
                
            print(f"    地址类型：{family_name}")
            print(f"    地址：{address.address}")
            
            # netmask 表示子网掩码
            if address.netmask:
                print(f"    子网掩码：{address.netmask}")
                
            # broadcast 表示广播地址
            # IPv6 或部分虚拟接口可能没有广播地址
            if address.broadcast:
                print(f"    广播地址为：{address.broadcast}")
    
if __name__ == "__main__":
    main()