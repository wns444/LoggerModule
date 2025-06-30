import logging
from datetime import datetime
import os


class LoggerClass:
    """Custom logger class with file and stream handlers."""
    def __init__(
            self,
            Name: str | None = None,
            PathLogFolder: str | None = None, 
            FormatLog: str | None = None
            ) -> None:
        """
        Initialize the logger.
        
        Args:
            Name: Name of the logger (default: "Untitled")
            PathLogFolder: Path to log folder (default: None - uses current directory/log)
            FormatLog: Log message format (default: includes timestamp, filename, function, levelname)
        """

        loger_time = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
        self.path = PathLogFolder if PathLogFolder else None
        self.name = Name if Name else "Untitled"
        self.filepath = None
        self.format = FormatLog if FormatLog else "[%(asctime)s] [%(filename)s] [%(funcName)s] [%(levelname)s] %(message)s"
        self.DateNow = loger_time
        
    def get_stream(self) -> logging.StreamHandler:
        """Create and configure stream handler."""

        ConsoleHandler = logging.StreamHandler()
        ConsoleHandler.setFormatter(logging.Formatter(fmt = self.format))
        return ConsoleHandler
    
    def get_file(self) -> logging.FileHandler:
        """Create and configure file handler with fallback to current directory."""

        if os.path.exists(self.path):
            if os.access(self.path, os.W_OK):
                print("Папка существует и доступна для записи")
            else:
                print("Папка существует, но недоступен для записи")
                print("Пробуем записать лог в директорию рядом с исполняемым файлом")
                self.path = self.get_folder()
        else:
            try:
                os.mkdir(self.path)
            except Exception as ex:
                print(f"Ошибка при создании папки. Тип ошибки - {type(ex).__name__}, сообщение ошибки - {ex}")
                print("Пробуем записать лог в директорию рядом с исполняемым файлом")
                self.path = self.get_folder()
                
        self.filepath = os.path.join(self.path, f"{self.name}_{self.DateNow}.log")
        FileHandler = logging.FileHandler(self.filepath, encoding='utf-8')
        FileHandler.setFormatter(logging.Formatter(fmt = self.format))
        return FileHandler
    
    def get_folder(self) -> str:
        """Get fallback log folder (current_directory/log)."""
        
        folder = str()
        curdir_folder = os.path.join(os.getcwd(), "log")
        if not os.path.exists(curdir_folder):
            try:
                os.mkdir(curdir_folder)
            except Exception as ex:
                print(f"Ошибка при создании папки рядом с исполняемым файлом. Тип ошибки - {type(ex).__name__}, сообщение ошибки - {ex}")
                folder = os.path.curdir
            else:
                folder = curdir_folder
        else:
            folder = curdir_folder
        
        return folder
    
    def get_logger(self) -> logging.Logger:
        """Get configured logger instance."""

        MainLogger = logging.getLogger(self.name)
        MainLogger.setLevel(logging.DEBUG)
        if not MainLogger.handlers:
            MainLogger.addHandler(self.get_stream())
            if self.path:
                MainLogger.addHandler(self.get_file())
        return MainLogger