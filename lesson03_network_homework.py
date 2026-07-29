import socket

import psutil

def get_network_info():
    network_list = []
    
    interfaces = psutil.net_if_addrs()
    for interface_name, address_list in interfaces.items():
        interface = interface_name
        for item in address_list:
            if item.family == socket.AF_INET:
                family = "IPv4"
                
            elif item.family == socket.AF_INET6:
                family = "IPv6"
                
            elif item.family == psutil.AF_LINK:
                family = "MAC"
            
            else:
                family = "其他"
            
            address = item.address
            netmask = item.netmask
            
            if item.broadcast:
                broadcast = item.broadcast
            else:
                broadcast = None
                
            network_list.append({
                'interface': interface,
                'family': family,
                'address': address,
                'netmask': netmask,
                'broadcast': broadcast
            })
    return network_list

if __name__ == "__main__":
    network_info = get_network_info()
    print(f"地址总数为:{len(network_info)}")
    for item in network_info:
        print(item)

