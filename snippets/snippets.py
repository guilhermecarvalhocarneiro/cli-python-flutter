import os
import sys
import json
import time
import platform
import traceback
import subprocess
import shutil

from pathlib import Path


class Snippet():

    @staticmethod
    def get_path():
        this_dir, this_filename = os.path.split(__file__)
        return this_dir

    @staticmethod
    def get_data_snippet():
        return open(os.path.join(Snippet.get_path(), "data.txt"), encoding='utf-8').read()

    @staticmethod
    def get_controller_snippet():
        return open(os.path.join(Snippet.get_path(), "controller.txt"), encoding='utf-8').read()

    @staticmethod
    def get_service_snippet():
        return open(os.path.join(Snippet.get_path(), "service.txt"), encoding='utf-8').read()

    @staticmethod
    def get_model_snippet():
        return open(os.path.join(Snippet.get_path(), "model.txt"), encoding='utf-8').read()

    @staticmethod
    def get_index_views_snippet():
        return open(os.path.join(Snippet.get_path(), "views_index.txt"), encoding='utf-8').read()

    @staticmethod
    def get_list_views_snippet():
        return open(os.path.join(Snippet.get_path(), "views_list.txt"), encoding='utf-8').read()

    @staticmethod
    def get_create_views_snippet():
        return open(os.path.join(Snippet.get_path(), "views_create.txt"), encoding='utf-8').read()

    @staticmethod
    def get_update_views_snippet():
        return open(os.path.join(Snippet.get_path(), "views_update.txt"), encoding='utf-8').read()

    @staticmethod
    def get_delete_views_snippet():
        return open(os.path.join(Snippet.get_path(), "views_delete.txt"), encoding='utf-8').read()

    @staticmethod
    def get_detail_views_snippet():
        return open(os.path.join(Snippet.get_path(), "views_detail.txt"), encoding='utf-8').read()

    @staticmethod
    def get_widget_snippet():
        return open(os.path.join(Snippet.get_path(), "widget.txt"), encoding='utf-8').read()

    @staticmethod
    def get_provider_snippet():
        return open(os.path.join(Snippet.get_path(), "provider.txt"), encoding='utf-8').read()

    @staticmethod
    def get_service_provider_snippet():
        return open(os.path.join(Snippet.get_path(), "service_provider.txt"), encoding='utf-8').read()

    @staticmethod
    def get_create_view_provider_snippet():
        return open(os.path.join(Snippet.get_path(), "views_create.provider.txt"), encoding='utf-8').read()

    @staticmethod
    def get_index_view_provider_snippet():
        return open(os.path.join(Snippet.get_path(), "views_index.provider.txt"), encoding='utf-8').read()

    @staticmethod
    def get_list_view_provider_snippet():
        return open(os.path.join(Snippet.get_path(), "views_list.provider.txt"), encoding='utf-8').read()

    @staticmethod
    def get_detail_view_provider_snippet():
        return open(os.path.join(Snippet.get_path(), "views_detail.provider.txt"), encoding='utf-8').read()

    @staticmethod
    def get_update_view_provider_snippet():
        return open(os.path.join(Snippet.get_path(), "views_update.provider.txt"), encoding='utf-8').read()

    @staticmethod
    def get_delete_view_provider_snippet():
        return open(os.path.join(Snippet.get_path(), "views_delete.provider.txt"), encoding='utf-8').read()

    @staticmethod
    def get_service_cubit_snippet():
        return open(os.path.join(Snippet.get_path(), "cubit", "service.txt"), encoding='utf-8').read()

    @staticmethod
    def get_cubit_snippet():
        return open(os.path.join(Snippet.get_path(), "cubit", "cubit.txt"), encoding='utf-8').read()

    @staticmethod
    def get_state_cubit_snippet():
        return open(os.path.join(Snippet.get_path(), "cubit", "state.txt"), encoding='utf-8').read()

    @staticmethod
    def get_create_view_cubit_snippet():
        return open(os.path.join(Snippet.get_path(), "cubit", "views_create.txt"), encoding='utf-8').read()

    @staticmethod
    def get_index_view_cubit_snippet():
        return open(os.path.join(Snippet.get_path(), "cubit", "views_index.txt"), encoding='utf-8').read()

    @staticmethod
    def get_list_view_cubit_snippet():
        return open(os.path.join(Snippet.get_path(), "cubit", "views_list.txt"), encoding='utf-8').read()

    @staticmethod
    def get_detail_view_cubit_snippet():
        return open(os.path.join(Snippet.get_path(), "cubit", "views_detail.txt"), encoding='utf-8').read()

    @staticmethod
    def get_update_view_cubit_snippet():
        return open(os.path.join(Snippet.get_path(), "cubit", "views_update.txt"), encoding='utf-8').read()

    @staticmethod
    def get_delete_view_cubit_snippet():
        return open(os.path.join(Snippet.get_path(), "cubit", "views_delete.txt"), encoding='utf-8').read()
