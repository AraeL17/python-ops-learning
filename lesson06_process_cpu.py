import time

import psutil

def get_top_cpu_processes(limit=10, interval=1) -> list:
    """获取 CPU 使用率最高的进程。"""
    process_objects = []
    
    # 依然和第五个作业一样，使用 psutil.process_iter() 获取每个进程的数据
    # 再使用 attrs 属性来设置获取进程的信息
    # 设置 ad_value=None ,为无权限读取为便为 None
    processes = psutil.process_iter(
        attrs=['pid', 'name'],
        ad_value=None
    )
    
    for process in processes:
        try:
            # 第一次调用 cpu_percent(interval=None) 是初始化采样，
            # interval=None：为时间为 None ， 所以运行这个只是初始一下数据
            # 第一次得到的 0.0 没有实际意义，因此不保存结果，
            # 但是把这个元素添加到列表中，用来第二次采样
            process.cpu_percent(interval=None)
            
            # 将初始化好的进程，添加到列表中，这样可以使第二次采样接着使用同一对象
            process_objects.append(process)
            
        # 进程肯呢个已经结束，或者当前用户没有读取权限，就跳过这个进程
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
        
    time.sleep(interval)
    
    process_list = []
        
    # 进行第二次遍历：第二次获取间隔 interval 秒过后内对 CPU 使用频率
    for process in process_objects:
        try:
            cpu_percent = process.cpu_percent(interval=None)
            
            process_list.append({
                'pid': process.pid,
                
                'name': process.info['name'] or '未知进程',
                
                'cpu_percent': round(cpu_percent, 2)
            })
        
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
        
        
    # 使用 sort() 对原列表进行排列，
    # key 指定按照什么排序，
    # reverse=True 表示从大到小进行排序
    process_list.sort(
        key=lambda item: item['cpu_percent'],
        reverse=True
    )
    
    return process_list[:limit]

def main():
    print("CPU 使用率最高的 10 个进程：")
    
    process_list = get_top_cpu_processes(
        limit=10,
        interval=1
    )
    
    for process in process_list:
        print(
            f"PID：{process['pid']}, "
            f"进程名称：{process['name']}, "
            f"CPU 使用率：{process['cpu_percent']}%"
        )
        
if __name__ == "__main__":
    main()