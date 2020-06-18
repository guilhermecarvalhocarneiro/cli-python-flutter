import os
import sys
import json
import time
import platform
import traceback
import subprocess
import shutil

from pathlib import Path

from snippets import Snippet

class Parser:
    
    def __init__(self, app_name):
        if app_name == None:
            sys.exit()

        self.app_name = app_name
        self.app_name_dir = ""
        self.sanitase()

        self.path_root = os.getcwd()

        self.app_dir = Path(f"{self.path_root}/{self.app_name_dir.lower()}")
        self.app_dir_views = Path(f"{self.app_dir}/views")

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

            self.content = Snippet.get_data_snippet()
            with open(self.data_file, 'w', encoding='utf-8') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None
            
            self.content = Snippet.get_controller_snippet()
            with open(self.controller_file, 'w', encoding='utf-8') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

            self.content = Snippet.get_model_snippet()
            with open(self.model_file, 'w', encoding='utf-8') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

            self.content = Snippet.get_service_snippet()
            with open(self.service_file, 'w', encoding='utf-8') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

            self.content = Snippet.get_index_views_snippet()
            with open(self.views_index_file, 'w', encoding='utf-8') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

            self.content = Snippet.get_list_views_snippet()
            with open(self.views_list_file, 'w', encoding='utf-8') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

            self.content = Snippet.get_create_views_snippet()
            with open(self.views_create_file, 'w', encoding='utf-8') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None
            
            self.content = Snippet.get_update_views_snippet()
            with open(self.views_update_file, 'w', encoding='utf-8') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

            self.content = Snippet.get_delete_views_snippet()
            with open(self.views_delete_file, 'w', encoding='utf-8') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None
            
            self.content = Snippet.get_detail_views_snippet()
            with open(self.views_detail_file, 'w', encoding='utf-8') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

            self.content = Snippet.get_widget_snippet()
            with open(self.widget_file, 'w', encoding='utf-8') as data_file:
                self.parse_content()
                data_file.write(self.content)
                self.content = None

        except Exception as error:
            # Excluindo o diretório criado de forma recursiva
            shutil.rmtree(Path(f"{self.app_dir}"))
            raise
