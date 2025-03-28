'''
Тут хранится несколько классов для работы с файлами

1. FileController - класс позволяющий работать с существующим файлом (получения инфы о файле, изминение содержимого, удаление и т.д.)
2. File - статический класс для общих функций таких, как прочесть содержимое, удалить, создать 
3. FileInfo - статический класс для сбора информации о файле
4. FolderController
'''

import os
import datetime

from typing import (
    List, 
    Any, 
    Dict, 
    Optional,
    Union,
    Tuple
)


def check_var(var: Any, types: Union[Any, Tuple[Any]], text: str = None) -> None: 
    if not isinstance(var, types):
        raise ValueError("Type of variable error." if not text else text)


class FileInfo:
    @staticmethod
    def get_size(filepath: str) -> int:
        '''Получение размера файла в байтах'''

        check_var(filepath, str, "Type of filepath error.")

        return os.path.getsize(filepath)
    

    @staticmethod
    def get_letters_count(lines: Union[str, List[str]]) -> int: 
        '''Получение количества символов строки или массива строк'''

        check_var(lines, (str, list), "Type of lines error.") 
        
        return len(lines) if isinstance(lines, str) else sum(len(line) for line in lines)


    @staticmethod
    def get_date_of_creating(filepath: str) -> str: 
        '''Получение даты создания файла'''

        check_var(filepath, str, "Type of filepath error.") 
        
        creation_time = int(os.path.getctime(filepath))
        creation_date = datetime.datetime.fromtimestamp(creation_time).strftime("%d/%m/%Y, %H:%M:%S")
        return creation_date
    

    @staticmethod
    def get_lines(filepath: str, encoding: bool = True) -> List[str]: 
        '''Получение списка строчек в файле'''
        
        check_var(filepath, str, "Type of filepath error.")        
        check_var(encoding, (bool, type(None)), "Type of encoding value error.")
        
        try:
            with open(filepath, "r", encoding='utf-8' if encoding else None) as file: 
                return file.readlines()
        except FileNotFoundError:
            raise Exception("File was not found.")
        except Exception as ex:
            raise Exception(f'Getting lines from file failed: {ex}')



class File: 
    @staticmethod
    def create(filepath: str, data: Union[str, List[str]] = None, encoding: bool = True) -> Dict[str, Union[str, int]]: 
        '''Создание нового файла'''
        
        check_var(data, (str, list), "Type of data error.")
        check_var(filepath, str, "Type of filepath error.")        
        check_var(encoding, (bool, type(None)), "Type of encoding value error.")

        try:
            if not os.path.exists(filepath):  # Если файла не существует
                with open(filepath, "w+", encoding='utf-8' if encoding else None) as file:
                    if data is not None:
                        if isinstance(data, str): 
                            file.write(data)
                        elif isinstance(data, list): 
                            file.writelines(data)
                        else:
                            raise ValueError("Type of data error")

                        return {
                            "lines": len(data) if isinstance(data, list) else 1,
                            "size (bytes)": FileInfo.get_size(filepath),
                            "letters": FileInfo.get_letters_count(data),
                            "created": FileInfo.get_date_of_creating(filepath)
                        }

                    return {
                        "lines": 0,
                        "size (bytes)": FileInfo.get_size(filepath),
                        "letters": 0,
                        "created": FileInfo.get_date_of_creating(filepath)
                    } 

            else:  # Если файл существует 
                raise FileExistsError("Such file already exists.")
        except FileNotFoundError:
            raise Exception("File was not found.")
        except Exception as ex:
            raise Exception(f"File creating failed: {ex}")
        
    
    @staticmethod
    def read(filepath: str, encoding: bool = True) ->  List[str]:
        '''Читает файл и возращает строку с его содержимым'''
        
        check_var(filepath, str, "Type of filepath error.")
        check_var(encoding, bool, "Type of encoding value error.")

        try:
            with open(filepath, "r+", encoding='utf-8' if encoding else None) as file:
                return file.readlines()
        except FileNotFoundError:
            raise Exception("File was not found.")
        except Exception as ex:
            raise Exception(f"File creating failed: {ex}")
        

    @staticmethod
    def delete(filepath: str) -> None:
        '''Удаление файла'''

        check_var(filepath, str, "Type of filepath error.")

        try:
            os.remove(filepath)
        except FileNotFoundError:
            print("File was not found.")
        except PermissionError:
            print("You have no rights for deleting this file.")
        except Exception as ex:
            print(f"File deleting failed: {ex}") 

    
    @staticmethod
    def get_info(filepath: str) -> Dict[str, Union[str, List[str], int]]:
        '''Получение информации о файле'''

        check_var(filepath, str, "Type of filepath error.")
        
        lines: List[str] = FileInfo.get_lines(filepath)

        return {
            "lines": len(lines),
            "size (bytes)": FileInfo.get_size(filepath),
            "letters": FileInfo.get_letters_count(lines),
            "created": FileInfo.get_date_of_creating(filepath)
        }


class Folder:
    @staticmethod
    def create(folderpath: str) -> Dict[str, Union[str, str]]:
        '''Создание папки по указанному пути'''

        check_var(folderpath, str, "Type of folderpath error.")

        try:
            os.makedirs(folderpath, exist_ok=True)
        except Exception as ex:
            raise Exception(f"Folder creating error: {ex}")
        else:
            return {
                # чето я уже заебался
            }


    @staticmethod
    def info(folderpath: str) -> Dict[str, Union[str, List[str], int]]:
        '''Возвращает кортеж с информацией про папку'''
        
        check_var(folderpath, str, "Type of folderpath error.")


    @staticmethod
    def delete(folderpath: str) -> None:
        '''Удаляет папку'''

        check_var(folderpath, str, "Type of folderpath error.")


    @staticmethod
    def get_files_count(folderpath: str) -> int:
        '''Получение количества файлов в директории'''
        
        check_var(folderpath, str, "Type of folderpath error.")

        return len(os.listdir(folderpath))


    @staticmethod
    def get_list_of_files(folderpath: str) -> Optional[List[str]]:
        '''Получение списка файлов из папки'''
        
        check_var(folderpath, str, "Type of folderpath error.")

        return os.listdir(folderpath)



if __name__ == '__main__':
    ...
