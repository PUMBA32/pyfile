import os, datetime

from typing import (
    List, 
    Any, 
    Optional,
    Union,
    Tuple
)


def check_var(var: Any, types: Union[type, Tuple[type, ...]], text: str = None) -> None: 
    if not isinstance(var, types):
        raise ValueError("Type of variable error." if not text else text)


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
                    for line in data:
                        file.write(line+'\n')

            if not fullpath:
                return filepath
            
        except FileNotFoundError:
            raise FileNotFoundError("Filepath is incorrect.")
        except Exception as ex:
            raise Exception(f"File creating failed: {ex}")
        
    
    @staticmethod
    def delete(fullpath: str) -> None:
        '''Deletes the file by path.'''

        check_var(fullpath, str)

        try:
            os.remove(fullpath)
        except PermissionError:
            raise PermissionError("You have no such right for deleting this.")
        except FileNotFoundError:
            raise FileNotFoundError("Filepath is incorrect.")
        except Exception as ex:
            raise Exception(f"File deleting failed: {ex}")

    
    @staticmethod
    def read(fullpath: str, encoding: bool = True) -> List[str]:
        '''Reads the file by filepath and returns the list of strokes from this file.'''

        check_var(fullpath, str)
        check_var(encoding, bool)

        try: 
            with open(fullpath, 'r', encoding='utf-8' if encoding else None) as file:
                return file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError("Filepath is incorrect.")
        except Exception as ex:
            raise Exception(f"File deleting failed: {ex}") 
        
    
    @staticmethod
    def add(filepath: str, data: List[str], encoding: bool = True) -> None:
        '''Adds data into file.'''

        check_var(filepath, str)
        check_var(data, list)
        check_var(encoding, bool)

        try:
            with open(filepath, 'a', encoding='utf-8' if encoding else None) as file:
                for line in data:
                    file.write(line+'\n')
        except FileNotFoundError:
            raise FileNotFoundError("Filepath is incorrect.")
        except PermissionError:
            raise PermissionError("Can't change content of this file.")
        except Exception as ex:
            raise Exception(f"Adding data into failed: {ex}")


    @staticmethod
    def clear(filepath: str) -> None:
        check_var(filepath, str)

        try:
            with open(filepath, 'w') as _: pass
        except FileNotFoundError:
            raise FileNotFoundError("Filepath is incorrect.")
        except PermissionError:
            raise PermissionError("Can't change content of this file.")
        except Exception as ex:
            raise Exception(f"Clearing file data was failed: {ex}")


    @staticmethod
    def get_date(filepath: str) -> str: 
        '''Returns date of creating in string type.'''

        check_var(filepath, str)

        try:
            creation_time = os.path.getctime(filepath)
            return datetime.datetime.fromtimestamp(creation_time).strftime("%d/%m/%Y, %H:%M:%S")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found by {filepath} path.")
        except Exception as ex:
            raise Exception(f"Getting date of creating was failed: {ex}")


    @staticmethod
    def get_lines_count(filepath: str) -> int:
        '''Returns count of lines in the file.'''

        return len(FileManager.read(filepath))
    

    @staticmethod
    def get_size(filepath: str) -> int:
        '''Return size of file in the bytes.'''

        check_var(filepath, str)

        try:
            return os.path.getsize(filepath)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found by {filepath} path.")
        except Exception as ex:
            raise Exception(f"Getting file size was failed: {ex}") 


if __name__ == '__main__':
    # from time import sleep
    # fl = FileManager

    # path = fl.create('data.txt', data=['niggers', 'niggers'])
    
    # fl.add(path, ['niggers3'])

    # print(fl.get_lines_count(path))

    # fl.clear(path)

    # print(fl.get_lines_count(path))

    # print(fl.get_size(path))
    # print(fl.get_date(path))

    # fl.add(path, ['niggers'])
    
    pass