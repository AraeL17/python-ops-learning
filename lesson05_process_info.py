import psutil  # 获取系统进程和资源使用信息


def bytes_to_mb(byte):
    # 将字节转换成 MB，并保留两位小数
    mb = byte / 1024 ** 2
    return round(mb, 2)

