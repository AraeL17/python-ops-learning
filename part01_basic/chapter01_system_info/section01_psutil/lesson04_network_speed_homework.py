import time

import psutil


def bytes_to_mb(byte):
    mb = byte / 1024 ** 2
    return round(mb, 2)

def get_network_speed(interface_name="en0", interval=1):
    interface_io = psutil.net_io_counters(pernic=True)
    first_io = interface_io[interface_name]
    
    time.sleep(interval)
    
    interface_io = psutil.net_io_counters(pernic=True)
    second_io = interface_io[interface_name]
    
    sent = bytes_to_mb((second_io.bytes_sent - first_io.bytes_sent) / interval)
    recv = bytes_to_mb((second_io.bytes_recv - first_io.bytes_recv) / interval)

    return {
        "interface": interface_name,
        "upload_mb_s": sent,
        "download_mb_s": recv
    }

if __name__ == "__main__":
    get_speed = get_network_speed()
    
    print(
        f"网络接口：{get_speed['interface']}",
        f"上传速度：{get_speed['upload_mb_s']} MB/s",
        f"下载速度：{get_speed['download_mb_s']} MB/s",
        sep="\n"
    )
    