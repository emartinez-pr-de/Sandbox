from pathlib import Path

class FileMgmt:
    @staticmethod
    def delete_file(file_path: str) -> bool:
        try:
            Path(file_path).unlink(missing_ok=True)
            return True
        except FileNotFoundError:
            return False
