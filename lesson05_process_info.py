import psutil  # 获取系统进程和资源使用信息


def bytes_to_mb(byte):
    # 将字节转换成 MB，并保留两位小数
    mb = byte / 1024 ** 2
    return round(mb, 2)

def get_current_process_info() -> dict:
    # 获取当前正在运行的 Python 程序的进程信息
    
    # Process() 没有传入 PID 时，表示当前这个 Python 程序
    process = psutil.Process()
    
    # memory_info() 返回当前进程的内存使用信息
    memory = process.memory_info()
    
    if memory is None:
        memory = None
    else:
        memory = bytes_to_mb(memory.rss)
    
    return  {
        # pid 是操作系统分配给当前进程的唯一编号
        'pid': process.pid,
        # name() 获取进程名称
        'name': process.name(),
        # status() 获取进程状态，例如 running、sleeping
        'status': process.status(),
        # username() 获取启动这个进程的系统用户
        'username': process.username(),
        # rss 表示当前进程实际占用的物理内存字节数
        'memory_mb': memory
    }
    
    
def get_process_list(limit=10) -> list:
    # 获取系统正在运行的进程的信息
    process_list = []
    
    # process_iter() 用于逐个遍历系统中正在运行的进程
    # attrs 指定需要提前读取的属性，减少重复调用
    # ad_value=None 表示某个属性无权读取时，用 None 代替
    # 这里给 processes 的是一个迭代器，
    # 迭代器里面的每一个才是 psutil.Process 对象
    processes = psutil.process_iter(
        # attrs 的作用是：
        # 遍历所有进程时，提前读取指定的属性，
        # 并把这些属性保存到每个进程对象的 info 字典中。
        attrs=['pid', 'name', 'status', 'username'],
        ad_value=None
    )
    
    for process in processes:
        # process.info 是字典，保存 attrs 中指定的进程属性
        # 因为 attrs 只指定了四项，所以每个对象的 info 里面只有存储4个项目
        info = process.info
        
        process_list.append({
            'pid': info['pid'],
            'name': info['name'],
            'status': info['status'],
            'username': info['username']
        })
        
        # 当列表中的进程数量达到 limit 时，停止遍历
        if len(process_list) >= limit:
            break
    
    return process_list

def main():
    all_pids = psutil.pids()
    print(f"系统进程数量：{len(all_pids)}")
        
    print("\n当前 Python 程序的进程信息：")
    print(get_current_process_info())
        
    print("\n系统中的前 10 个进程：")
    process_list = get_process_list(limit=10)
        
    for process in process_list:
        print(process)
        
if __name__ == "__main__":
    main()    
