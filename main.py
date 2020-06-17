import os
import sys
import json
import time
import platform
import traceback
import subprocess

from pathlib import Path

class Parser:
    
    def __init__(self, app_name):
        if app_name == None:
            sys.exit()

        self.app_name = app_name
        self.app_name_dir = ""
        self.sanitase()

        self.path_cli = Path("C:/Users/guilh/Development/Python/cli")
        self.path_root = os.getcwd()

        self.app_dir = Path(f"{self.path_root}/{self.app_name_dir.lower()}")
        self.app_dir_views = Path(f"{self.app_dir}/views")
        
        self.data_snippet = Path(f"{self.path_cli}/snippets/data.txt")
        self.controller_snippet = Path(f"{self.path_cli}/snippets/controller.txt")
        self.service_snippet = Path(f"{self.path_cli}/snippets/service.txt")
        self.model_snippet = Path(f"{self.path_cli}/snippets/model.txt")
        self.views_index_snippet = Path(f"{self.path_cli}/snippets/views_index.txt")
        self.views_list_snippet = Path(f"{self.path_cli}/snippets/views_list.txt")
        self.views_detail_snippet = Path(f"{self.path_cli}/snippets/views_detail.txt")
        self.views_create_snippet = Path(f"{self.path_cli}/snippets/views_create.txt")
        self.views_update_snippet = Path(f"{self.path_cli}/snippets/views_update.txt")
        self.views_delete_snippet = Path(f"{self.path_cli}/snippets/views_delete.txt")
        self.widget_snippet = Path(f"{self.path_cli}/snippets/widget.txt")
        
        self.data_file = Path(f"{self.app_dir}/data.dart")
        self.model_file = Path(f"{self.app_dir}/model.dart")
        self.controller_file = Path(f"{self.app_dir}/controller.dart")
        self.service_file = Path(f"{self.app_dir}/service.dart")
        self.views_index_file = Path(f"{self.app_dir_views}/index.dart")
        self.views_list_file = Path(f"{self.app_dir_views}/list.dart")
        self.views_detail_file = Path(f"{self.app_dir_views}/detail.dart")
        self.views_create_file = Path(f"{self.app_dir_views}/create.dart")
        self.views_update_file = Path(f"{self.app_dir_views}/update.dart")
        self.views_delete_file = Path(f"{self.app_dir_views}/delete.dart")
        self.widget_file = Path(f"{self.app_dir_views}/widget.dart")
        self.content = None

    def to_camel_case(self, class_name=True):
        """Método para convert a váriavel de snake_case para camelCase

        Arguments:
            str {str} -- String convertida
        """
        try:
            components = self.app_name.split('_')
            if class_name:
                return components[0] + ''.join(x.title() for x in components[1:])
            if len(components) == 1:
                # Nome simples
                __string = components[0]
                return "{}{}".format(__string[:1].lower(), __string[1:])
        
        except Exception as error:
            self.__message(f"Ocorreu um erro no Camel Case: {error}")
            return None

    def sanitase(self):
        self.app_name_dir = self.app_name.replace(" ", "_")
        self.app_name = self.app_name.replace(" ", "").replace("_", "")

    def parse_content(self):
        self.content = self.content.replace("AppName", self.to_camel_case())
        self.content = self.content.replace("appName", self.to_camel_case(class_name=False))

    def parse(self):
        try:
            # Verificando se o diretório existe
            if os.path.isdir(self.app_dir):
                sys.exit()
            # Criando o diretório
            os.makedirs(self.app_dir)
            # Criando o subdiretório das views
            os.makedirs(self.app_dir_views)
            # Criando o arquivo data

            with open(self.data_snippet, 'r') as data_snippet:
                self.content = data_snippet.read()
            with open(self.data_file, 'w') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

            with open(self.controller_snippet, 'r') as data_snippet:
                self.content = data_snippet.read()
            with open(self.controller_file, 'w') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

            with open(self.model_snippet, 'r') as data_snippet:
                self.content = data_snippet.read()
            with open(self.model_file, 'w') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

            with open(self.service_snippet, 'r') as data_snippet:
                self.content = data_snippet.read()
            with open(self.service_file, 'w') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

            with open(self.views_index_snippet, 'r') as data_snippet:
                self.content = data_snippet.read()
            with open(self.views_index_file, 'w') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

            with open(self.views_list_snippet, 'r') as data_snippet:
                self.content = data_snippet.read()
            with open(self.views_list_file, 'w') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

            with open(self.views_create_snippet, 'r') as data_snippet:
                self.content = data_snippet.read()
            with open(self.views_create_file, 'w') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None
            
            with open(self.views_update_snippet, 'r') as data_snippet:
                self.content = data_snippet.read()
            with open(self.views_update_file, 'w') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

            with open(self.views_delete_snippet, 'r') as data_snippet:
                self.content = data_snippet.read()
            with open(self.views_delete_file, 'w') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None
            
            with open(self.views_detail_snippet, 'r') as data_snippet:
                self.content = data_snippet.read()
            with open(self.views_detail_file, 'w') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

            with open(self.widget_snippet, 'r') as data_snippet:
                self.content = data_snippet.read()
            with open(self.widget_file, 'w') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

        except Exception as error:
            print(error)


if __name__ == "__main__":
    app_name = "Exemplo Dois" #input("Informe o nome da app no formato Nome/Nome Composto: ")
    Parser(app_name).parse()
