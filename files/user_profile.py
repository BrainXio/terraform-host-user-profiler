import json
import os
import getpass

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
            if os.name == "nt":
                try:
                    user_info["home_dir"] = os.environ.get("USERPROFILE", "")
                except (KeyError, OSError):
                    pass
    except Exception:
        pass
    return user_info

def main():
    profile = get_user_info()
    print(json.dumps(profile))

if __name__ == "__main__":
    main()
