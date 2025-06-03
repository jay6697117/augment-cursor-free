import os
import sys
from pathlib import Path


def get_home_dir() -> str:
    """
    Get the user's home directory across different platforms.

    Returns:
        str: Path to the user's home directory
    """
    return str(Path.home())


def get_app_data_dir() -> str:
    """
    Get the application data directory across different platforms.

    Returns:
        str: Path to the application data directory

    Platform specific paths:
        - Windows: %APPDATA% (typically C:\\Users\\<username>\\AppData\\Roaming)
        - macOS: ~/Library/Application Support
        - Linux: ~/.local/share
    """
    if sys.platform == "win32":
        # Windows
        return os.getenv("APPDATA", "")
    elif sys.platform == "darwin":
        # macOS
        return os.path.join(str(Path.home()), "Library/Application Support")
    else:
        # Linux and other Unix-like systems
        return os.path.join(str(Path.home()), ".local/share")


def get_storage_path() -> str:
    """
    Get the storage.json path across different platforms.

    Returns:
        str: Path to the storage.json file

    Platform specific paths:
        - Windows: %APPDATA%/Cursor/User/globalStorage/storage.json
        - macOS: ~/Library/Application Support/Cursor/User/globalStorage/storage.json
        - Linux: ~/.config/Cursor/User/globalStorage/storage.json
    """
    if sys.platform == "win32":
        # Windows
        base_path = os.getenv("APPDATA", "")
        return os.path.join(base_path, "Cursor", "User", "globalStorage", "storage.json")
    elif sys.platform == "darwin":
        # macOS
        return os.path.join(str(Path.home()), "Library", "Application Support", "Cursor", "User", "globalStorage", "storage.json")
    else:
        # Linux and other Unix-like systems
        return os.path.join(str(Path.home()), ".config", "Cursor", "User", "globalStorage", "storage.json")


def get_db_path() -> str:
    """
    Get the state database path across different platforms.

    Returns:
        str: Path to the state database file

    Platform specific paths:
        - Windows: %APPDATA%/Cursor/User/globalStorage/state.vscdb
        - macOS: ~/Library/Application Support/Cursor/User/globalStorage/state.vscdb
        - Linux: ~/.config/Cursor/User/globalStorage/state.vscdb
    """
    if sys.platform == "win32":
        # Windows
        base_path = os.getenv("APPDATA", "")
        return os.path.join(base_path, "Cursor", "User", "globalStorage", "state.vscdb")
    elif sys.platform == "darwin":
        # macOS
        return os.path.join(str(Path.home()), "Library", "Application Support", "Cursor", "User", "globalStorage", "state.vscdb")
    else:
        # Linux and other Unix-like systems
        return os.path.join(str(Path.home()), ".config", "Cursor", "User", "globalStorage", "state.vscdb")


def get_machine_id_path() -> str:
    """
    Get the machine ID file path across different platforms.

    Returns:
        str: Path to the machine ID file

    Platform specific paths:
        - Windows: %APPDATA%/Cursor/User/machineid
        - macOS: ~/Library/Application Support/Cursor/machineid
        - Linux: ~/.config/Cursor/User/machineid
    """
    if sys.platform == "win32":
        # Windows
        base_path = os.getenv("APPDATA", "")
        return os.path.join(base_path, "Cursor", "User", "machineid")
    elif sys.platform == "darwin":
        # macOS
        return os.path.join(str(Path.home()), "Library", "Application Support", "Cursor", "machineid")
    else:
        # Linux and other Unix-like systems
        return os.path.join(str(Path.home()), ".config", "Cursor", "machineid")


def get_workspace_storage_path() -> str:
    """
    Get the workspaceStorage path across different platforms.

    Returns:
        str: Path to the workspaceStorage directory

    Platform specific paths:
        - Windows: %APPDATA%/Cursor/User/workspaceStorage
        - macOS: ~/Library/Application Support/Cursor/User/workspaceStorage
        - Linux: ~/.config/Cursor/User/workspaceStorage
    """
    if sys.platform == "win32":
        # Windows
        base_path = os.getenv("APPDATA", "")
        return os.path.join(base_path, "Cursor", "User", "workspaceStorage")
    elif sys.platform == "darwin":
        # macOS
        return os.path.join(str(Path.home()), "Library", "Application Support", "Cursor", "User", "workspaceStorage")
    else:
        # Linux and other Unix-like systems
        return os.path.join(str(Path.home()), ".config", "Cursor", "User", "workspaceStorage")
