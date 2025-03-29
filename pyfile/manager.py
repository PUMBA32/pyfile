import os, datetime 

from typing import (
    List, 
    Any, 
    Dict, 
    Optional,
    Union,
    Tuple
)


def check_var(var: Any, types: Union[type, Tuple[type, ...]], text: str = None) -> None: 
    if not isinstance(var, types):
        raise ValueError("Type of variable error." if not text else text)


class FolderInfo: ...
class FileInfo: ...

class FileManager: 
    __BASE_PATH: str = os.path.dirname(__file__)


    @classmethod
    def create(cls, 
               name: str, 
               data: List[str] | None = None, 
               fullpath: str | None = None, 
               encoding: bool = True
            ) -> Optional[str]:
        
        '''Creating file with some data if are there.<p>Returns filepath if fullpath was not None.</p>'''
        
        # Проверка параметров функции на валидность типов данных
        check_var(name, str)
        check_var(fullpath, (str, type(None)))
        check_var(data, (list, type(None)))
        check_var(encoding, bool)

        # Функционал
        filepath: str = os.path.join(cls.__BASE_PATH, name)

        try:
            with open(filepath if not fullpath else fullpath, 'w', encoding='utf-8' if encoding else None) as file:
                if data:
                    file.writelines(data)

            if not fullpath:
                return filepath
        except FileNotFoundError:
            raise FileNotFoundError("Filepath is incorrect.")
        except Exception as ex:
            raise Exception(f"File creating failed: {ex}")
        
    
    @staticmethod
    def delete(fullpath: str) -> None:
        check_var(fullpath, str)

        try:
            os.remove(fullpath)
        except PermissionError:
            raise PermissionError("You have no such right for deleting this.")
        except FileNotFoundError:
            raise FileNotFoundError("Filepath is incorrect.")
        except Exception as ex:
            raise Exception(f"File deleting failed: {ex}")
        
    
    @classmethod





class FolderManager: ...


if __name__ == '__main__':
    from time import sleep

    # path: str = FileManager.create("data.txt", data=['some data\n', 'another data'])    
    # FileManager.delete(path)
