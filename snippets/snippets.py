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
        return "test"

    @staticmethod
    def get_data_snippet():
        return """
/// Local Data do model AppName

/// [Travar o arquivo]
/// Caso deseje "travar" o arquivo para não ser parseado novamente
/// pelo manage do Django adicione um # antes da palavra abaixo
/// FileLocked

import 'package:path/path.dart';
import 'package:sembast/sembast_io.dart' as smbt_io;
import 'package:sembast/sembast.dart' as smbt;
import 'package:path_provider/path_provider.dart';

import 'model.dart';
import '../../../utils/config.dart';

class AppNameData {

  // Istanciando a classe AppNameModel
  AppNameModel _appNameModel = AppNameModel();

  static final AppNameData _instance = AppNameData.internal();

  factory AppNameData() => _instance;

  AppNameData.internal();

  // Iniciando o objeto DataBase
  smbt.Database _db;

  final String _storeName = "appNameStoreDB";

  // Método para inicialiar o banco de dados criando a tabela.
  // TODO: Alterar o nome do DbName na linha 41 para o nome do banco do projeto
  Future<smbt.Database> initDb() async {
    try {
      // get the application documents directory
      var dir = await getApplicationDocumentsDirectory();
      // make sure it exists
      await dir.create(recursive: true);
      // build the database path
      var dbPath = join(dir.path, 'DbName.db');
      // open the database
      return await smbt_io.databaseFactoryIo.openDatabase(dbPath);
    } catch (error, exception) {
      DebugPrint.error(
          "Erro no método initDB -> error: $error, message: $exception");
    }
    return null;
  }

  /// Método para recuperar todos os dados de AppName
  ///
  /// returns:
  ///   Instância do AppNameModel
  Future<List<AppNameModel>> fetchAll() async {
    try {
      _db = await initDb();
      var _store = smbt.intMapStoreFactory.store(_storeName);
      var _data = await _store.find(_db);
      return _data.map((snapshot){
        final _result = AppNameModel.fromMap(snapshot.value);
      }).toList();
    } catch (e) {
      return null;
    } finally {
      _db.close();
    }
  }

  /// Método para recuperar o primeiro registro de AppName
  ///
  /// returns:
  ///   Instância do AppNameModel
  Future<AppNameModel> get(int id) async {
    try {
      _db = await initDb();
      var _store = smbt.intMapStoreFactory.store(_storeName);
      var _data = await _store.findFirst(_db);
      return AppNameModel.fromMap(_data.value);
    } catch (e) {
      return null;
    } finally {
      _db.close();
    }
  }

  /// Método para salvar localmente um(a) AppName
  ///
  /// returns:
  ///    bool -> true salvo com sucesso, false ocorreu um erro
  Future<bool> save(AppNameModel appName) async {
    try {
      _db = await initDb();
      var _store = smbt.intMapStoreFactory.store(_storeName);
      // Salvando o dado do novo appName
      await _store.add(_db, appName.toMap());
      return true;
    } catch (error, exception) {
      return false;
    } finally {
      _db.close();
    }
  }

  /// Método para deletar todos os registros do(a) AppName
  ///
  /// returns:
  ///    bool -> true salvo com sucesso, false ocorreu um erro
  Future<bool> deleteAll() async {
    try {
      _db = await initDb();
      var _store = smbt.intMapStoreFactory.store(_storeName);
      // Apagando todos os registros anteriores
      await _store.delete(_db);
      return true;
    } catch (error, exception) {
      return false;
    } finally {
      _db.close();
    }
  }

  /// Método para deletar um registro do(a) AppName
  ///
  /// returns:
  ///    bool -> true salvo com sucesso, false ocorreu um erro
  Future<bool> delete(int id) async {
    try {
      _db = await initDb();
      var _store = smbt.intMapStoreFactory.store(_storeName);
      // Apagando todos os registros anteriores
      await _store.delete(_db);
      return true;
    } catch (error, exception) {
      return false;
    } finally {
      _db.close();
    }
  }

  /// Método para deletar um registro do(a) AppName
  ///
  /// returns:
  ///    bool -> true salvo com sucesso, false ocorreu um erro
  Future<bool> update(AppNameModel AppName) async {
    try {
      _db = await initDb();
      var _store = smbt.intMapStoreFactory.store(_storeName);
      // TODO: Implementar o Update
      return true;
    } catch (error, exception) {
      return false;
    } finally {
      _db.close();
    }
  }
}
        """

    @staticmethod
    def get_controller_snippet():
        return """
/// Controller do model AppName
/// 
///    O CÓDIGO DO ARQUIVO controller.g.dart NUNCA DEVE SER ALTERADO MANUALMENTE.
///    Quando for alterado algo no arquivo controller.dart deve ser executado o comando:
///      flutter pub run build_runner build
///
/// Após a execução do comando acima o arquivo controller.g.dart terá sido atualizado 
/// com as novas features.
///
/// Os Métodos padrões gerados são:
///   Métodos da API
///     fecthAll() -> Recupera a lista de AppName.
///     reload() -> Recarrega a lista de AppName.
///     detail() -> Recupera os detalhes de um AppName.
///     post() -> Salva um novo AppName.
///     put() -> Atualiza os dados de um AppName.
///     delete() -> Deleta um AppName.
///
///   Métodos do Data
///     fetchLocal() -> Recupera a lista de AppName
///     reloadLocal() -> Recarrega a lista de AppName
///     detailLocal() -> Recupera os detalhes de um AppName
///     saveLocal() -> Salva um novo AppName
///     updateLocal() -> Atualiza um novo AppName
///     deleteLocal() -> Deleta um novo AppName
///     deleteAllLocal() -> Deleta um novo AppName

///
/// As regras de negócio devem ser implementadas nesse arquivo evitando ao máximo
/// de serem implementadas nos arquivos das views/pages.
///
/// Todos os métodos de acesso à API devem ser implementados no Service.

/// [Travar o arquivo]
/// Caso deseje "travar" o arquivo para não ser parseado novamente
/// pelo manage do Django adicione um # antes da palavra abaixo
/// FileLocked

import 'data.dart';
import 'model.dart';
import 'service.dart';
import '../../../utils/config.dart';
import '../../../utils/process.controller.dart';

import 'package:mobx/mobx.dart';
import 'package:get_it/get_it.dart';

part 'controller.g.dart';

class AppNameController = _AppNameControllerBase with _$AppNameController;

/// Declarando a classe abstrata do AppName com o Mixin de Store
abstract class _AppNameControllerBase with Store {

  // Instanciando o controller de processamento
  ProcessController _processController = GetIt.I.get<ProcessController>();

  // Instanciando o AppNameData responsável pelo acesso ao SQLite.
  AppNameData _appNameData = AppNameData();

  // Instanciando o AppNameService responsável pelo acesso à API.
  AppNameService _appNameService = AppNameService();

  // Declarando os elementos observáveis padrões do AppNameController.
  @observable
  ObservableList<AppNameModel> appNameList;
  
  @observable
  AppNameModel appNameModel;

  /// Declarando os elementos observáveis do Db do AppNameController.
  @observable
  ObservableList<AppNameModel> appNameLocalList;

  @observable
  AppNameModel appNameLocalModel;

  /// Declarando os actions padrões do AppNameController.
  
  /// Action responsável pelo retorno da lista de elementos da API.
  @action
  fetchAll() async{
    try{
     _processController.processing = true;
      // Recuperando a lista de AppName da API.
      appNameList = ObservableList<AppNameModel>.of(await _appNameService.fetchAll());
    } catch (error, exception) {
      _error(error.toString(), exception.toString());
    }finally{
      _processController.processing = false;
    }
  }

  /// Action responsável por recarregar os dados da API.
  @action
  reload() async{
    try{
      _processController.processing = true;
      // Limpando os dados contidos na lista de AppName
      appNameList.clear();
      // Invocando o método que carrega os dados da API.
      this.fetchAll();
    } catch (error, exception) {
      _error(error.toString(), exception.toString());
    }finally{
      _processController.processing = false;
    }
  }

  /// Action responsável por detalhar um AppName
  @action
  detail() async{
    try{
      _processController.processing = true;
      // Recuperando o detalhe de um determinado AppName da API. 
      appNameModel = await _appNameService.detail(appNameModel);
    } catch (error, exception) {
      _error(error.toString(), exception.toString());
    }finally{
      _processController.processing = false;
    }
  }

  /// Action responsável por salvar os dados de uma instância do AppName na API.
  @action
  post() async{
    try{
      _processController.processing = true;
      // Recuperando o detalhe de um determinado AppName da API. 
      appNameModel = await _appNameService.post(appNameModel);
    } catch (error, exception) {
      _error(error.toString(), exception.toString());
    }finally{
      _processController.processing = false;
    }
  }

  /// Action responsável por atualizar os dados de uma instância do AppName na API.
  @action
  put() async{
    try{
      _processController.processing = true;
      // Recuperando o detalhe de um determinado AppName da API. 
      appNameModel = await _appNameService.put(appNameModel);
    } catch (error, exception) {
      _error(error.toString(), exception.toString());
    }finally{
      _processController.processing = false;
    }
  }

  /// Action responsável por excluir os dados de uma instância do AppName na API.
  @action
  delete() async{
    try{
      _processController.processing = true;
      // Recuperando o detalhe de um determinado AppName da API. 
      bool _result = await _appNameService.delete(appNameModel);
      if(_result){
        _success("ok");
      }
    } catch (error, exception) {
      _error(error.toString(), exception.toString());
    }finally{
      _processController.processing = false;
    }
  }

  /// Action para recuperar todos os registros do Db
  @action
  fetchAllLocal() async{
    try{
      _processController.processing = true;
      appNameLocalList = ObservableList<AppNameModel>.of(await _appNameData.fetchAll());
    } catch (error, exception) {
      _error(error.toString(), exception.toString());
    }
  }
  
  /// Action para atualizar a lista de AppName do Db
  @action
  reloadLocal() async{
    try{
      appNameLocalList.clear();
      this.fetchAllLocal();
    } catch (error, exception) {
      _error(error.toString(), exception.toString());
    }
  }

  /// Action para detalhar um AppName do Db
  @action
  detailLocal(int id) async{
    try{
      appNameLocalModel = await _appNameData.get(id);
    } catch (error, exception) {
      _error(error.toString(), exception.toString());
    }finally{
      _processController.processing = false;
    }
  }

  /// Action para detalhar um AppName do Db
  @action
  saveLocal(AppNameModel model) async{
    try{
      bool _result = await _appNameData.save(model);
      if(_result){
        appNameLocalModel = model;
      }
    } catch (error, exception) {
      _error(error.toString(), exception.toString());
    }
  }

  /// Action para atualizar um AppName do Db
  @action
  updateLocal(AppNameModel model) async{
    try{
      bool _result = await _appNameData.update(model);
      if(_result){
        appNameLocalModel = model;
      }
    } catch (error, exception) {
      _error(error.toString(), exception.toString());
    }
  }

  /// Action para deletar um AppName do Db
  @action
  deleteLocal(int id) async{
    try{
      return await _appNameData.delete(id);
    } catch (error, exception) {
      _error(error.toString(), exception.toString());
    }
  }

  /// Action para deletar todos os AppNames do Db
  @action
  deleteAllLocal() async{
    try{
      return await _appNameData.deleteAll();
    } catch (error, exception) {
      _error(error.toString(), exception.toString());
    }
  }

  /// Métodos para tratar o retorno do processamento
  void _success(String message) async {
    try {
      _processController.withSuccess(message: message);
    } catch (e) {
      DebugPrint.imprimir("Ocorreu um erro no método error: $e");
    }
  }

  void _error(String error, String exception) async {
    try {
      _processController.withError(
        error: error,
        exception: exception,
      );
    } catch (e) {
      DebugPrint.imprimir("Ocorreu um erro no método error: $e");
    }
  }

}        
        """

    @staticmethod
    def get_service_snippet():
        return """
/// Service do model AppName

/// Os Métodos padrões gerados são:
///     fecthAll() -> Recupera a lista de Agendamento da API.
///     detail()   -> Recupera os detalhes de Agendamento da API.
///     post()     -> Salva os dados de uma instância do Agendamento na API.
///     put()      -> Atualiza os dados de uma instância do Agendamento na API.
///     delete()   -> Deleta os dados de uma instância do Agendamento na API.

/// Os métodos de acesso à API devem ser implementados no nessa classe.

/// [Travar o arquivo]
/// Caso deseje "travar" o arquivo para não ser parseado novamente
/// pelo manage do Django adicione um # antes da palavra abaixo
/// FileLocked

import 'package:dio/dio.dart';
import 'package:get_it/get_it.dart';

import 'model.dart';
import '../../../utils/config.dart';
import '../../../utils/custom_dio.dart';
import '../../../utils/process.controller.dart';

class AppNameService {
  static String _uri = "";

  // Criando uma instância privada do AppNameModel
  AppNameModel _appName = AppNameModel();

  // Criando uma instância privada de List<AppNameModel>
  List<AppNameModel> _appNameList = List<AppNameModel>();

  // Instanciando o Controller Process
  ProcessController _processController = GetIt.I<ProcessController>();

  // Construtor
  AppNameService({AppNameModel appName, List<AppNameModel> appNameList}) {
    if (appName != null) _appName = appName;
  }

  // Método para retornar o AppName principal
  Future<List<AppNameModel>> fetchAll() async {    
    try {
      String _url;
      _appNameList?.clear();
      CustomDio _dio = CustomDio(_url);
      _dio.makeHeadersAuthentication();
      var dataResponse = await _dio.getHttp();
      if (dataResponse != null) {
        _appNameList?.clear();
        _success("ok");
        String _next = dataResponse["next"] ?? "";
        String _previous = dataResponse["previous"] ?? "";
        for (var data in dataResponse["results"]) {
          AppNameModel appNameModel = AppNameModel.fromJson(data);
          appNameModel.nextUrl = _next;
          appNameModel.previousUrl = _previous;
          _appNameList.add(appNameModel);
        }
      }
    } catch (error, exception) {
      _error(error, exception.toString());
    }
    return _appNameList;
  }

  // Método para retornar o AppName principal
  Future<List<AppNameModel>> getMore(String uri) async {
    List<AppNameModel> _appNameList = List<AppNameModel>();
    String _url;
    try {
      CustomDio _dio = CustomDio(_url);
      _dio.makeHeadersAuthentication();
      var dataResponse = await _dio.getHttp();
      if (dataResponse != null) {
        String _next = dataResponse["next"] ?? "";
        String _previous = dataResponse["previous"] ?? "";
        for (var data in dataResponse["results"]) {
          AppNameModel appNameModel = AppNameModel.fromJson(data);
          appNameModel.nextUrl = _next;
          appNameModel.previousUrl = _previous;
          _appNameList.add(appNameModel);
        }
        _success("ok");
      }
    } catch (error, exception) {
      _error(error, exception.toString());
    }
    return _appNameList;
  }

  /// Método para detalhar um AppName da API
  Future<AppNameModel> detail(AppNameModel appName) async {
    String _url = "";

    try {
      CustomDio _dio = CustomDio(_url);
      var data = await _dio.getHttp();
      if (data != null) {
        _appName = AppNameModel.fromJson(data);
      }
    } catch (error, exception) {
        _error(error.toString(), exception.toString());
    }
    return _appName;
  }  

  // Método para criar um novo appName na API
  Future<AppNameModel> post(AppNameModel appName) async {
    try {
      String _uri = "${Config.uri}appName";
      CustomDio _dio = CustomDio(_uri);
      _dio.makeHeadersAuthentication();
      var data = appName.toJson();
      var dataResponse = await _dio.postHttp(data);
      if (dataResponse != null) {
        appName = AppNameModel.fromJson(dataResponse);
        _success("ok");
      }
    } catch (error, exception) {
      _error(error, exception.toString());
    }
    return appName;
  }

  Future<AppNameModel> put(AppNameModel appName) async {
    try {
      String _uri = "${Config.uri}appName/${appName.id}";
      CustomDio _dio = CustomDio(_uri);
      _dio.makeHeadersAuthentication();
      // Criando o elemento JSON conforme documentação para atualizar
      // apenas os campos permitidos.
      FormData data = FormData.fromMap({});
      var dataResponse = await _dio.patchHttp(data);
      if (dataResponse != null) {
        _success("ok");
        return AppNameModel.fromJson(dataResponse);
      }
    } catch (error, exception) {
      _error(error, exception.toString());
    }
    return null;
  }

  Future<bool> delete(AppNameModel appName) async {
    try {
      String _uri = "${Config.uri}appName/${appName.id}";
      CustomDio _dio = CustomDio(_uri);
      _dio.makeHeadersAuthentication();
      var data = appName.toJson();
      var dataResponse = await _dio.deleteHttp(data, appName.id.toString());
      if (dataResponse != null) {
        _success("ok");
        return true;
      }
      return false;
    } catch (error, exception) {
      _error(error, exception.toString());
      return false;
    }
  }
 
 /// Métodos para tratar o retorno do processamento
 void _success(String message) async {
   try {
     _processController.withSuccess(message: message);
   } catch (error) {
     DebugPrint.imprimir("Ocorreu um erro no service de AppName: $error");
   }
 }
 
 void _error(String error, String exception) async {
   try {
     _processController.withError(
       error: error,
       exception: exception,
     );
   } catch (error) {
     DebugPrint.imprimir("Ocorreu um erro no service de AppName: $error");
   }
 }
}        
        """

    @staticmethod
    def get_model_snippet():
        return """
/// Model da app AppName

/// [Travar o arquivo]
/// Caso deseje "travar" o arquivo para não ser parseado novamente
/// pelo manage do Django adicione um # antes da palavra abaixo
/// FileLocked

import 'dart:convert';

class AppNameModel{  
  int id;
  String nextUrl;
  String previousUrl;
  
  AppNameModel({
    this.id,
    this.nextUrl, 
    this.previousUrl,
  });

  factory AppNameModel.fromJson(String str) => AppNameModel.fromMap(json.decode(str));

  String toJson() => json.encode(toMap());

  factory AppNameModel.fromMap(Map<String, dynamic> json) => AppNameModel(
      nextUrl: json["nextUrl"] == null ? null : json["nextUrl"],
      previousUrl: json["previousUrl"] == null ? null : json["previousUrl"],
  );

  Map<String, dynamic> toMap() => {
      "nextUrl": nextUrl == null ? null : nextUrl,
      "previousUrl": previousUrl == null ? null : previousUrl,
  };
}
        """

    @staticmethod
    def get_index_views_snippet():
        return """ 
/// Views Index da AppName

/// [Travar o arquivo]
/// Caso deseje "travar" o arquivo para não ser parseado novamente
/// pelo manage do Django adicione um # antes da palavra abaixo
/// FileLocked

import 'package:get_it/get_it.dart';
import 'package:flutter/material.dart';
import 'package:mobx/mobx.dart';

import 'widget.dart';
import '../model.dart';
import '../controller.dart';
import '../../../../user_interface/font.dart';
import '../../../../user_interface/widget.dart';
import '../../../../utils/process.controller.dart';

class IndexAppNamePage extends StatefulWidget {
  @override
  _IndexAppNamePageState createState() => _IndexAppNamePageState();
}

class _IndexAppNamePageState extends State<IndexAppNamePage> {
  
  // Instanciando o controller do Scaffold
  final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();

  // Instanciando o controller de processamento
  ProcessController _processController = GetIt.I.get<ProcessController>();

  // Instanciando um controller para Animações
  AnimationController _animationController;

  // Instanciando uma lista de Disposes das Reactions
  List<ReactionDisposer> _disposers = [];

  // Istanciando o controller do AppName
  AppNameController _appNameController = GetIt.I.get<AppNameController>();

  // Declarando o model do AppName
  AppNameModel _model = AppNameModel();

  @override
  void initState() {
    // Criando a reaction para mostrar a Snackbar
    // conforme o retorno do _processController.sucess
    _disposers.add(
      autorun((_) {
        if (_processController.success == true) {
          _showMessage(_processController.message);
          _hideKeyboard(context);
        } else if (_processController.success == false) {
          _showMessage(_processController.error,
              error: true);
        }
      }),
    );    
    _model = _appNameController.appNameModel;
    super.initState();
  }

  @override
  void dispose() {
    _disposers.forEach((dispose) => dispose());
    _animationController.dispose();
    _model = null;
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: _scaffoldKey,
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        backgroundColor: Colors.transparent
      ),
      body: _buildBody(),
    );
  }

  Widget _buildBody() {
    return Stack(
      children: <Widget> [
        HeadWidget(),
        _buildPage()
      ]
    );
  }

  Widget _buildPage() {
    return Container();
  }

  /// Método para mostrar/ocultar a barra de mensagem para o usuário
  ///    Parameters:
  ///      message -> String contendo a mensagem a ser mostrada.
  ///      error -> bool para determinar se a mensagem é de erro ou não.
  _showMessage(String message, {bool error = false}) {
    setState(() {
      _scaffoldKey.currentState.showSnackBar(
        error == false
            ? customSuccessSnackbar(message)
            : customErrorSnackbar(message),
      );
    });
  }

  /// Método para ocultar o teclado após o usuário clicar no botão de Salvar
  ///    Parameters:
  ///        context -> BuildContext
  _hideKeyboard(BuildContext context) {
    FocusScope.of(context).requestFocus(FocusNode());
  }
}
"""

    @staticmethod
    def get_list_views_snippet():
        return """
/// Views List da AppName

/// [Travar o arquivo]
/// Caso deseje "travar" o arquivo para não ser parseado novamente
/// pelo manage do Django adicione um # antes da palavra abaixo
/// FileLocked

import 'package:get_it/get_it.dart';
import 'package:flutter/material.dart';
import 'package:mobx/mobx.dart';

import 'widget.dart';
import '../model.dart';
import '../controller.dart';
import '../../../../user_interface/font.dart';
import '../../../../user_interface/widget.dart';
import '../../../../utils/process.controller.dart';

class ListAppNamePage extends StatefulWidget {
  @override
  _ListAppNamePageState createState() => _ListAppNamePageState();
}

class _ListAppNamePageState extends State<ListAppNamePage> {
  
  // Instanciando o controller do Scaffold
  final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();

  // Instanciando o ScrollController
  final ScrollController _scrollController = ScrollController();

  // Instanciando o controller de processamento
  ProcessController _processController = GetIt.I.get<ProcessController>();

  // Instanciando um controller para Animações
  AnimationController _animationController = AnimationController(vsync: null);

  // Instanciando uma lista de Disposes das Reactions
  List<ReactionDisposer> _disposers = [];

  // Istanciando o controller do AppName
  AppNameController _appNameController = GetIt.I.get<AppNameController>();

  // Declarando o model do AppName
  AppNameModel _model = AppNameModel();

  @override
  void initState() {
    // Criando a reaction para mostrar a Snackbar
    // conforme o retorno do _processController.sucess
    _disposers.add(
      autorun((_) {
        if (_processController.success == true) {
          _showMessage(_processController.message);
          _hideKeyboard(context);
        } else if (_processController.success == false) {
          _showMessage(_processController.error,
              error: true);
        }
      }),
    );    
    _model = _appNameController.appNameModel;
    super.initState();
  }

  @override
  void dispose() {
    _disposers.forEach((dispose) => dispose());
    _scrollController.dispose();
    _animationController.dispose();
    _model = null;
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: _scaffoldKey,
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        backgroundColor: Colors.transparent
      ),
      body: _buildBody(),
    );
  }

  Widget _buildBody() {
    return Stack(
      children: <Widget> [
        HeadWidget(),
        _buildPage()
      ]
    );
  }

  Widget _buildPage() {
    return Container();
  }

  /// Método para mostrar/ocultar a barra de mensagem para o usuário
  ///    Parameters:
  ///      message -> String contendo a mensagem a ser mostrada.
  ///      error -> bool para determinar se a mensagem é de erro ou não.
  _showMessage(String message, {bool error = false}) {
    setState(() {
      _scaffoldKey.currentState.showSnackBar(
        error == false
            ? customSuccessSnackbar(message)
            : customErrorSnackbar(message),
      );
    });
  }

  /// Método para ocultar o teclado após o usuário clicar no botão de Salvar
  ///    Parameters:
  ///        context -> BuildContext
  _hideKeyboard(BuildContext context) {
    FocusScope.of(context).requestFocus(FocusNode());
  }
}

        """

    @staticmethod
    def get_create_views_snippet():
        return """ 
/// Views Create da AppName

/// [Travar o arquivo]
/// Caso deseje "travar" o arquivo para não ser parseado novamente
/// pelo manage do Django adicione um # antes da palavra abaixo
/// FileLocked

import 'package:get_it/get_it.dart';
import 'package:flutter/material.dart';
import 'package:mobx/mobx.dart';

import 'widget.dart';
import '../model.dart';
import '../controller.dart';
import '../../../../user_interface/font.dart';
import '../../../../user_interface/widget.dart';
import '../../../../utils/process.controller.dart';

class CreateAppNamePage extends StatefulWidget {
  @override
  _CreateAppNamePageState createState() => _CreateAppNamePageState();
}

class _CreateAppNamePageState extends State<CreateAppNamePage> {
  
  // Instanciando o controller do Scaffold
  final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();

  // Instanciando o controller de processamento
  ProcessController _processController = GetIt.I.get<ProcessController>();

  // Instanciando um controller para Animações
  AnimationController _animationController;

  // Instanciando uma lista de Disposes das Reactions
  List<ReactionDisposer> _disposers = [];

  // Istanciando o controller do AppName
  AppNameController _appNameController = GetIt.I.get<AppNameController>();

  // Declarando o model do AppName
  AppNameModel _model = AppNameModel();

  @override
  void initState() {
    // Criando a reaction para mostrar a Snackbar
    // conforme o retorno do _processController.sucess
    _disposers.add(
      autorun((_) {
        if (_processController.success == true) {
          _showMessage(_processController.message);
          _hideKeyboard(context);
        } else if (_processController.success == false) {
          _showMessage(_processController.error,
              error: true);
        }
      }),
    );    
    _model = _appNameController.appNameModel;
    super.initState();
  }

  @override
  void dispose() {
    _disposers.forEach((dispose) => dispose());
    _animationController.dispose();
    _model = null;
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: _scaffoldKey,
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        backgroundColor: Colors.transparent
      ),
      body: _buildBody(),
    );
  }

  Widget _buildBody() {
    return Stack(
      children: <Widget> [
        HeadWidget(),
        _buildPage()
      ]
    );
  }

  Widget _buildPage() {
    return Container();
  }

  /// Método para mostrar/ocultar a barra de mensagem para o usuário
  ///    Parameters:
  ///      message -> String contendo a mensagem a ser mostrada.
  ///      error -> bool para determinar se a mensagem é de erro ou não.
  _showMessage(String message, {bool error = false}) {
    setState(() {
      _scaffoldKey.currentState.showSnackBar(
        error == false
            ? customSuccessSnackbar(message)
            : customErrorSnackbar(message),
      );
    });
  }

  /// Método para ocultar o teclado após o usuário clicar no botão de Salvar
  ///    Parameters:
  ///        context -> BuildContext
  _hideKeyboard(BuildContext context) {
    FocusScope.of(context).requestFocus(FocusNode());
  }
}
        """

    @staticmethod
    def get_update_views_snippet():
        return """
/// Views Update da AppName

/// [Travar o arquivo]
/// Caso deseje "travar" o arquivo para não ser parseado novamente
/// pelo manage do Django adicione um # antes da palavra abaixo
/// FileLocked

import 'package:get_it/get_it.dart';
import 'package:flutter/material.dart';
import 'package:mobx/mobx.dart';

import 'widget.dart';
import '../model.dart';
import '../controller.dart';
import '../../../../user_interface/font.dart';
import '../../../../user_interface/widget.dart';
import '../../../../utils/process.controller.dart';

class UpdateAppNamePage extends StatefulWidget {
  @override
  _UpdateAppNamePageState createState() => _UpdateAppNamePageState();
}

class _UpdateAppNamePageState extends State<UpdateAppNamePage> {

  // Instanciando o controller do Scaffold
  final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();

  // Instanciando o controller de processamento
  ProcessController _processController = GetIt.I.get<ProcessController>();

  // Instanciando um controller para Animações
  AnimationController _animationController;

  // Instanciando uma lista de Disposes das Reactions
  List<ReactionDisposer> _disposers = [];

  // Istanciando o controller do AppName
  AppNameController _appNameController = GetIt.I.get<AppNameController>();

  // Declarando o model do AppName
  AppNameModel _model = AppNameModel();

  @override
  void initState() {
    // Criando a reaction para mostrar a Snackbar
    // conforme o retorno do _processController.sucess
    _disposers.add(
      autorun((_) {
        if (_processController.success == true) {
          _showMessage(_processController.message);
          _hideKeyboard(context);
        } else if (_processController.success == false) {
          _showMessage(_processController.error,
              error: true);
        }
      }),
    );    
    _model = _appNameController.appNameModel;
    super.initState();
  }

  @override
  void dispose() {
    _disposers.forEach((dispose) => dispose());
    _animationController.dispose();
    _model = null;
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: _scaffoldKey,
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        backgroundColor: Colors.transparent
      ),
      body: _buildBody(),
    );
  }

  Widget _buildBody() {
    return Stack(
      children: <Widget> [
        HeadWidget(),
        _buildPage()
      ]
    );
  }

  Widget _buildPage() {
    return Container();
  }

  /// Método para mostrar/ocultar a barra de mensagem para o usuário
  ///    Parameters:
  ///      message -> String contendo a mensagem a ser mostrada.
  ///      error -> bool para determinar se a mensagem é de erro ou não.
  _showMessage(String message, {bool error = false}) {
    setState(() {
      _scaffoldKey.currentState.showSnackBar(
        error == false
            ? customSuccessSnackbar(message)
            : customErrorSnackbar(message),
      );
    });
  }

  /// Método para ocultar o teclado após o usuário clicar no botão de Salvar
  ///    Parameters:
  ///        context -> BuildContext
  _hideKeyboard(BuildContext context) {
    FocusScope.of(context).requestFocus(FocusNode());
  }
}
         """

    @staticmethod
    def get_delete_views_snippet():
        return """
/// Views Delete da AppName

/// [Travar o arquivo]
/// Caso deseje "travar" o arquivo para não ser parseado novamente
/// pelo manage do Django adicione um # antes da palavra abaixo
/// FileLocked

import 'package:get_it/get_it.dart';
import 'package:flutter/material.dart';
import 'package:mobx/mobx.dart';

import 'widget.dart';
import '../model.dart';
import '../controller.dart';
import '../../../../user_interface/font.dart';
import '../../../../user_interface/widget.dart';
import '../../../../utils/process.controller.dart';

class DeleteAppNamePage extends StatefulWidget {
  @override
  _DeleteAppNamePageState createState() => _DeleteAppNamePageState();
}

class _DeleteAppNamePageState extends State<DeleteAppNamePage> {
  
  // Instanciando o controller do Scaffold
  final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();

  // Instanciando o controller de processamento
  ProcessController _processController = GetIt.I.get<ProcessController>();

  // Instanciando um controller para Animações
  AnimationController _animationController;

  // Instanciando uma lista de Disposes das Reactions
  List<ReactionDisposer> _disposers = [];

  // Istanciando o controller do AppName
  AppNameController _appNameController = GetIt.I.get<AppNameController>();

  // Declarando o model do AppName
  AppNameModel _model = AppNameModel();

  @override
  void initState() {
    // Criando a reaction para mostrar a Snackbar
    // conforme o retorno do _processController.sucess
    _disposers.add(
      autorun((_) {
        if (_processController.success == true) {
          _showMessage(_processController.message);
          _hideKeyboard(context);
        } else if (_processController.success == false) {
          _showMessage(_processController.error,
              error: true);
        }
      }),
    );    
    _model = _appNameController.appNameModel;
    super.initState();
  }

  @override
  void dispose() {
    _disposers.forEach((dispose) => dispose());
    _animationController.dispose();
    _model = null;
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: _scaffoldKey,
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        backgroundColor: Colors.transparent
      ),
      body: _buildBody(),
    );
  }

  Widget _buildBody() {
    return Stack(
      children: <Widget> [
        HeadWidget(),
        _buildPage()
      ]
    );
  }

  Widget _buildPage() {
    return Container();
  }

  /// Método para mostrar/ocultar a barra de mensagem para o usuário
  ///    Parameters:
  ///      message -> String contendo a mensagem a ser mostrada.
  ///      error -> bool para determinar se a mensagem é de erro ou não.
  _showMessage(String message, {bool error = false}) {
    setState(() {
      _scaffoldKey.currentState.showSnackBar(
        error == false
            ? customSuccessSnackbar(message)
            : customErrorSnackbar(message),
      );
    });
  }

  /// Método para ocultar o teclado após o usuário clicar no botão de Salvar
  ///    Parameters:
  ///        context -> BuildContext
  _hideKeyboard(BuildContext context) {
    FocusScope.of(context).requestFocus(FocusNode());
  }  
}

         """

    @staticmethod
    def get_detail_views_snippet():
        return """ 
/// Views Detail da AppName

/// [Travar o arquivo]
/// Caso deseje "travar" o arquivo para não ser parseado novamente
/// pelo manage do Django adicione um # antes da palavra abaixo
/// FileLocked

import 'package:get_it/get_it.dart';
import 'package:flutter/material.dart';
import 'package:mobx/mobx.dart';

import 'widget.dart';
import '../model.dart';
import '../controller.dart';
import '../../../../user_interface/font.dart';
import '../../../../user_interface/widget.dart';
import '../../../../utils/process.controller.dart';

class DetailAppNamePage extends StatefulWidget {
  @override
  _DetailAppNamePageState createState() => _DetailAppNamePageState();
}

class _DetailAppNamePageState extends State<DetailAppNamePage> {
  
  // Instanciando o controller do Scaffold
  final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();

  // Instanciando o controller de processamento
  ProcessController _processController = GetIt.I.get<ProcessController>();

  // Instanciando um controller para Animações
  AnimationController _animationController;

  // Instanciando uma lista de Disposes das Reactions
  List<ReactionDisposer> _disposers = [];

  // Istanciando o controller do AppName
  AppNameController _appNameController = GetIt.I.get<AppNameController>();

  // Declarando o model do AppName
  AppNameModel _model = AppNameModel();

  @override
  void initState() {
    // Criando a reaction para mostrar a Snackbar
    // conforme o retorno do _processController.sucess
    _disposers.add(
      autorun((_) {
        if (_processController.success == true) {
          _showMessage(_processController.message);
          _hideKeyboard(context);
        } else if (_processController.success == false) {
          _showMessage(_processController.error,
              error: true);
        }
      }),
    );    
    _model = _appNameController.appNameModel;
    super.initState();
  }

  @override
  void dispose() {
    _disposers.forEach((dispose) => dispose());
    _animationController.dispose();
    _model = null;
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: _scaffoldKey,
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        backgroundColor: Colors.transparent
      ),
      body: _buildBody(),
    );
  }

  Widget _buildBody() {
    return Stack(
      children: <Widget> [
        HeadWidget(),
        _buildPage()
      ]
    );
  }

  Widget _buildPage() {
    return Container();
  }

  /// Método para mostrar/ocultar a barra de mensagem para o usuário
  ///    Parameters:
  ///      message -> String contendo a mensagem a ser mostrada.
  ///      error -> bool para determinar se a mensagem é de erro ou não.
  _showMessage(String message, {bool error = false}) {
    setState(() {
      _scaffoldKey.currentState.showSnackBar(
        error == false
            ? customSuccessSnackbar(message)
            : customErrorSnackbar(message),
      );
    });
  }

  /// Método para ocultar o teclado após o usuário clicar no botão de Salvar
  ///    Parameters:
  ///        context -> BuildContext
  _hideKeyboard(BuildContext context) {
    FocusScope.of(context).requestFocus(FocusNode());
  }
}

         """

    @staticmethod
    def get_widget_snippet():
        return """
/// Arquivo contendo os Widgets componentizados da app AppName

/// [Travar o arquivo]
/// Caso deseje "travar" o arquivo para não ser parseado novamente
/// pelo manage do Django adicione um # antes da palavra abaixo
/// FileLocked
        """
