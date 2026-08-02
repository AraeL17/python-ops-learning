from datetime import datetime


import psutil


def format_timestamp(timestamp):
    # 将时间戳转换为日期时间字符串。
    
    # 如果时间信息无法读取，就直接返回 None
    if timestamp is None:
        return None
    
    # fromtimestamp() 将时间戳转换为 datetime 对象
    process_time = datetime.fromtimestamp(timestamp)
    
    # strftime() 按照指定格式生成日期时间字符串
    return process_time.strftime("%Y-%m-%d %H:%M:%S")


def get_process_detail(pid) -> dict:
    # 根据 pid 获取指定进程的相信信息
    
    if not psutil.pid_exists(pid):
        return {
            'error': f"pid {pid} 不存在"
        }
        
    try:
        # Process(pid) 根据指定 pid 创建进程对象
        process = psutil.Process(pid)
        
        # as_dict() 一次获取进程的多个属性，并返回字典
        # attrs 指定需要获取哪些属性
        # ad_value=None 表示无权限读取的属性使用 None
        info = process.as_dict(
            attrs=[
                'pid',
                'ppid',
                'name',
                'status',
                'username',
                'exe',
                'cmdline',
                'cwd',
                'create_time',
                'num_threads'
            ],
            ad_value=None
        )
        
        return {
            # 当前进程的 PID
            "pid": info["pid"],

            # ppid 是父进程的 PID
            "ppid": info["ppid"],

            # 进程名称
            "name": info["name"],

            # 进程当前状态
            "status": info["status"],

            # 启动进程的系统用户
            "username": info["username"],

            # 可执行程序的绝对路径
            "exe": info["exe"],

            # 启动进程时使用的命令及参数，通常是列表
            "cmdline": info["cmdline"],

            # 进程当前的工作目录
            "cwd": info["cwd"],

            # 将进程启动时间转换为日期时间字符串
            "create_time": format_timestamp(info["create_time"]),

            # 进程当前包含的线程数量
            "num_threads": info["num_threads"]
        }
        
    except psutil.NoSuchProcess:
        return {
            'error': f'PID {pid} 已经结束'
        }
        
    except psutil.AccessDenied:
        return {
            'error': f'没有权限查询 PID {pid}'
        }
        
def main():
    current_process = psutil.Process()
    
    target_pid = current_process.pid
    
    print(f"正在查询 PID：{target_pid}")
    
    process_detail = get_process_detail(target_pid)
    
    if "error" in process_detail:
        print(process_detail["error"])
        return
    
    print(f"PID：{process_detail['pid']}")
    print(f"父进程 PID：{process_detail['ppid']}")
    print(f"进程名称：{process_detail['name']}")
    print(f"进程状态：{process_detail['status']}")
    print(f"所属用户：{process_detail['username']}")
    print(f"程序路径：{process_detail['exe']}")
    print(f"命令行参数：{process_detail['cmdline']}")
    print(f"工作目录：{process_detail['cwd']}")
    print(f"启动时间：{process_detail['create_time']}")
    print(f"线程数量：{process_detail['num_threads']}")
    
if __name__ == "__main__":
    main()