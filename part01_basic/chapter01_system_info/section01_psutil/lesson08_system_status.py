import time
from datetime import datetime

import psutil


def bytes_to_gb(byte):
    """将字节转换成 GB，并保留两位小数。"""
    gb = byte / 1024 ** 3
    return round(gb, 2)


def bytes_to_mb(byte):
    """将字节转换成 MB，并保留两位小数。"""
    mb = byte / 1024 ** 2
    return round(mb, 2)


def format_timestamp(timestamp):
    # 将时间戳转换为日期时间字符串。
    
    if timestamp is None:
        return None
    
    system_time = datetime.fromtimestamp(timestamp)
    
    # strftime() 将 datetime 对象转换为指定格式的字符串
    return system_time.strftime("%Y-%m-%d %H:%M:%S")


def get_boot_info() -> dict:
    # 获取系统启动时间和运行时长
    
    # boot_time() 返回系统启动时的 Unix 时间戳
    boot_timestamp = psutil.boot_time()
    
    # time.time() 返回当前时间的 Unix 时间戳
    current_timestamp = time.time()
    
    # 当前时间减去启动时间，得到系统已经运行的总秒数
    uptime_seconds = int(current_timestamp - boot_timestamp)
    
    # 一天有 86400 秒，// 表示整除, 获取一共运行了多少天
    uptime_days = uptime_seconds // 86400
    
    # % 表示取余数，得到除去完整天数后剩余的秒数
    remaining_seconds = uptime_seconds % 86400
    
    # 从剩余秒数中计算完整小时数
    uptime_hours = remaining_seconds // 3600
    
    # 除去完整小时后，再计算剩余分钟数
    uptime_minutes = (remaining_seconds % 3600) // 60
    
    return {
        'boot_time': format_timestamp(boot_timestamp),
        "uptime_days": uptime_days,
        "uptime_hours": uptime_hours,
        "uptime_minutes": uptime_minutes
    }


def get_logged_in_users() -> list:
    # 获取当前登录系统的用户
    user_list = []
    
    # user() 返回当前系统登录的用户列表
    users = psutil.users()
    
    for user in users:
        user_list.append({
            'name': user.name,
            
            'terminal': user.terminal,
            
            'host': user.host or '本机',
            
            'started': format_timestamp(user.started),
            
            'pid': user.pid
        })
    return user_list


def get_swap_info() -> dict:
    # 获取系统交换内存信息
    
    # swap_memory() 返回系统的 Swap 统计信息
    swap = psutil.swap_memory()
    
    return {
        # Swap 总容量
        'total_gb': bytes_to_gb(swap.total),
        
        # 已经使用的 Swap
        'used_gb': bytes_to_gb(swap.used),
        
        # 剩余的 Swap
        'free_gb': bytes_to_gb(swap.free),
        
        # Swap 使用率已经是百分比，不需要单位转换
        'percent': swap.percent,
        
        # sin 表示累计从磁盘换入内存的字节数
        'swap_in_mb': bytes_to_mb(swap.sin),
        
        # sout 表示累计从内存换出到磁盘的字节数
        'swap_out_mb': bytes_to_mb(swap.sout)
    }
    

def get_load_info() -> dict:
    # 获取系统最近 1、5、15 分钟的平均负载
    
    # getloadavg() 返回包含三个数字的元组
    load_1, load_5, load_15 = psutil.getloadavg()
    
    # 获取逻辑 CPU 核心数量
    logical_count = psutil.cpu_count(logical=True)
    
    if logical_count is None or logical_count == 0:
        normalized_1 = None
        normalized_5 = None
        normalized_15 = None
        
    else:
        # 负载除以逻辑核心数，方便比较任务量与核心数量
        # 归一化负载不是实际 CPU 使用率
        normalized_1 = round(load_1 / logical_count * 100, 2)
        normalized_5 = round(load_5 / logical_count * 100, 2)
        normalized_15 = round(load_15 / logical_count * 100, 2)
        
    return {
        'logical_cpu_count': logical_count,
        'load_1': round(load_1, 2),
        'load_5': round(load_5, 2),
        'load_15': round(load_15, 2),
        'normalized_1_percent': normalized_1,
        'normalized_5_percent': normalized_5,
        'normalized_15_percent': normalized_15,
    }
    

def main():
    print("系统启动信息：")
    print(get_boot_info())
    
    print("\n当前登录用户：")
    user_list = get_logged_in_users()
    
    if not user_list:
        print("没有获取到登录用户信息")
    else:
        for user in user_list:
            print(user)
    
    print("\nSwap 交换内存：")
    print(get_swap_info())
    
    print("\n系统平均负载：")
    print(get_load_info())
    
    
if __name__ == "__main__":
    main()