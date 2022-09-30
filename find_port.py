from scrapli.driver.core import JunosDriver
import re
import sys
import getpass

DEVICE = {
    "host": sys.argv[1],
    "auth_username": "python",
    "auth_password": getpass.getpass(),
    "auth_strict_key": False
}

def find_port(patch_port: str) -> str:
    """Get interface descriptions and regex match for interfaces"""
    with JunosDriver(**DEVICE) as conn:
        response = conn.send_command("show interface descriptions | match " + patch_port)
        port = re.match("..-\d\/\d\/\d",response.result)
        print(f"Patch panel {patch_port} is connected to switch port {port[0]}.")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            find_port(sys.argv[2])
        except AttributeError:
            print("Can't find an interface with this description.")
        except TypeError:
            print("Can't find an interface with this description.")
        except:
            print("An error occurred")
    else:
        print("This script takes exactly 2 arguments.\nEx: \'python3 find_port.py 192.168.1.1 A-1\'")
