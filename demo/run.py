import os
import platform
from pathlib import Path


os.chdir(Path(__file__).parent.parent.joinpath("amis_admin_theme_editor"))

IS_WINDOWS = platform.system() == "Windows"  # Linux
host = "127.0.0.1"
port = 8090
debug = False


def run():
    """pdm Launching uvicorn fastAPI run script"""
    import uvicorn
    root_path: str = os.path.join(os.path.dirname(__file__))
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        debug=False,
        reload=False,
        app_dir=root_path
    )


def kill():
    """pdm Kill uvicorn fastAPI run script"""
    proc = kill_port(port)
    if proc:
        print(f"kill port {port} process {proc.name()}")
    else:
        print(f"port {port} process not found")


# kill Specify the port process
def kill_port(port):
    import psutil

    for proc in psutil.process_iter():
        if proc.name().find("python") == -1:
            continue
        for conns in proc.connections(kind="inet"):
            if conns.laddr.port == port:
                proc.kill()
                # logging 输出日志
                return proc
    return None


if __name__ == "__main__":
    run()
