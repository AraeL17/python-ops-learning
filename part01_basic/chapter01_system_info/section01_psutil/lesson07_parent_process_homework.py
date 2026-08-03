import psutil


def get_parent_process_detail(pid) -> dict:
    if not psutil.pid_exists(pid):
        return {
            'error': '该 PID 的进程不存在'
        }
    
    try:
        process = psutil.Process(pid)
    
        parent = process.parent()

        if parent is None:
            return {'error': '父进程为 None'}
        
        info_process = process.as_dict(
            # attrs 格式为列表形式
            attrs=[
                'pid',
                'name',
            ]
        )
        
        info_parent = parent.as_dict(
            # attrs 格式为列表形式
            attrs=[
                'pid',
                'name',
                'status',
                'exe',
                'cmdline'
            ]
        )
    except psutil.NoSuchProcess:
        return {
            'error': '该 PID 进程已经运行结束'
        }
    except psutil.AccessDenied:
        return {
            'error': '该 PID 进程没有权限读取'
        }
    
    return {
        "child_pid": info_process['pid'],
        "child_name": info_process['name'],
        "parent_pid": info_parent['pid'],
        "parent_name": info_parent['name'],
        "parent_status": info_parent['status'],
        "parent_exe": info_parent['exe'],
        "parent_cmdline": info_parent['cmdline']
    }
    
    
def main():
    process = psutil.Process()
    
    process_pid = process.pid
    
    process_detail = get_parent_process_detail(process_pid)
    
    if 'error' in process_detail:
        print(process_detail['error'])
        return
    
    print(process_detail)


if __name__ == "__main__":
    main()