import json
import os
import getpass
import platform
import locale
import subprocess
try:
    import grp
except ImportError:
    grp = None

def get_user_info():
    user_info = {}
    try:
        # Username
        try:
            user_info["username"] = getpass.getuser()
        except (KeyError, OSError):
            try:
                user_info["username"] = os.getlogin()
            except OSError:
                pass
        # Home directory
        try:
            user_info["home_dir"] = os.path.expanduser("~")
        except (KeyError, OSError):
            if platform.system().lower() == "windows":
                try:
                    user_info["home_dir"] = os.environ.get("USERPROFILE", "")
                except (KeyError, OSError):
                    pass
        # Shell
        try:
            system = platform.system().lower()
            if system in ["linux", "darwin"]:
                user_info["shell"] = os.environ.get("SHELL", "")
            elif system == "windows":
                user_info["shell"] = os.environ.get("ComSpec", "cmd.exe")
                try:
                    result = subprocess.run(["powershell", "-Command", "Get-Command powershell -ErrorAction SilentlyContinue"], capture_output=True, text=True, timeout=5)
                    if result.returncode == 0 and result.stdout.strip():
                        user_info["shell"] = "powershell.exe"
                except (subprocess.SubprocessError, FileNotFoundError):
                    pass
        except Exception:
            pass
        # User ID
        try:
            if system in ["linux", "darwin"]:
                user_info["user_id"] = str(os.getuid())
            elif system == "windows":
                try:
                    result = subprocess.run(["whoami", "/user"], capture_output=True, text=True, timeout=5)
                    if result.returncode == 0:
                        for line in result.stdout.splitlines():
                            if "S-1-5" in line:
                                user_info["user_id"] = line.split()[-1].strip()
                                break
                except (subprocess.SubprocessError, FileNotFoundError):
                    pass
        except Exception:
            pass
        # Primary Group
        try:
            if system in ["linux", "darwin"] and grp:
                user_info["primary_group"] = grp.getgrgid(os.getgid()).gr_name
            elif system == "windows":
                try:
                    result = subprocess.run(["net", "user", user_info.get("username", ""), "/domain"], capture_output=True, text=True, timeout=5)
                    if result.returncode == 0:
                        for line in result.stdout.splitlines():
                            if "Primary Group" in line or "Group Memberships" in line:
                                parts = line.split()
                                if len(parts) > 2:
                                    user_info["primary_group"] = parts[-1].strip()
                                    break
                except (subprocess.SubprocessError, FileNotFoundError, KeyError):
                    user_info["primary_group"] = "Users"
        except Exception:
            pass
        # Locale
        try:
            loc = locale.getlocale()
            if loc and loc[0]:
                user_info["locale"] = loc[0].replace('_', '-')  # e.g., en_US → en-US
            elif system in ["linux", "darwin"]:
                user_info["locale"] = os.environ.get("LANG", "").split('.')[0].replace('_', '-') or ""
            elif system == "windows":
                try:
                    result = subprocess.run(["powershell", "-Command", "Get-Culture | Select-Object -ExpandProperty Name"], capture_output=True, text=True, timeout=5)
                    if result.returncode == 0:
                        user_info["locale"] = result.stdout.strip()
                except (subprocess.SubprocessError, FileNotFoundError):
                    pass
        except Exception:
            pass
    except Exception:
        pass
    # Remove empty values
    return {k: v for k, v in user_info.items() if v}

def main():
    profile = get_user_info()
    print(json.dumps(profile))

if __name__ == "__main__":
    main()
