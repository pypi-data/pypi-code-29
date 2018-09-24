from typing import Dict, Callable, List, Union
from inspect import getfullargspec
from collections import namedtuple
import sys

def error_dict( 
    code:Union[str,int], 
    message:str, 
    request_id:Union[str,int,None] = None, 
    data:Union[str,List,Dict,None]=None
    )->Dict:
    """Вернуть словарь составленный по правилам объекта error из json_rpc"""
    json_result:Dict = {"jsonrpc": "2.0", "error": {"code": code, "message": message} }
    if request_id:
        json_result["id"] = request_id
    if data:
        json_result["error"]["data"] = data
    return json_result


MinMaxArgs = namedtuple('MinMaxArgs','min max')
"""Тип, представляющий именовынный кортеж с полями min и max"""


def min_max_arg_count( f:Callable ) -> MinMaxArgs:
    """Вернуть минимальное и максимальное количество аргументов, применимых к функции"""
    spec = getfullargspec(f)
    args = len(spec.args)
    defaults = len(spec.defaults) if spec.defaults else 0
    # Минимальное необходимое количество аргументов = количество позициональных - кол-во дефолтных значений.
    min_args = args - defaults
    # Максимальное кличество аргументов ограничивается только если нет *args и **args:
    max_args = 255
    if not spec.varargs and not spec.varkw:
        max_args = args
    # Возвращаем кортеж с именованными полями:
    return MinMaxArgs(min_args,max_args)


def is_applicable( func:Callable, params:Union[List,Dict,None] ) -> bool:
    """Вернуть true/false в зависимости от того, применимы ли параметры params к функци func"""
    params_count = len(params) if params else 0
    min_max = min_max_arg_count(func)
    return min_max.min <= params_count <= min_max.max


async def json_rpc_v2_router( 
    request, 
    request_json_extractor:Callable,
    methods_map:Dict[str,Callable]
     ) -> Dict:
    """Вызвать обработчик метода method из json из request и вернуть словарь с результатом.
    
    request - объект POST-запроса, передаваемый фреймворком в обработчик. 
    request_json_extractor - функция, принимающая на вход объект request и возвращающая словарь из json из его тела.
    methods_map - словарь { method:function }
        ,где:
            method - имя метода, 
            fucntion - функция которую нужно вызвать для этого метода. """
    result:Dict
    try:
        json:Dict = await request_json_extractor(request) 
    except Exception:
        return error_dict( code=-32700, message="Parse error", request_id=None )

    req_id = json.get('id', None)
    
    if 'method' not in json:
        return error_dict( code=-32600, message="Invalid Request", request_id=req_id )
    req_method = json['method']
    
    if req_method not in methods_map:
        return error_dict( code=-32601, message="Method not found", request_id=req_id )
    
    handler:Callable = methods_map[req_method]

    req_params = json.get('params',None)
    
    if not is_applicable( handler, req_params ):
        min_max = min_max_arg_count( handler )
        data = {'required_params_count': { 'min':min_max.min, 'max':min_max.max }}
        return error_dict( code=-32602, message="Invalid params", request_id=req_id, data=data )

    try:
        if isinstance(req_params,List):
            result = await handler( *req_params )
        elif isinstance(req_params,Dict):
            result = await handler( **req_params )
        elif not req_params:
            result = await handler()
        else:
            result = error_dict( 
                code=-32603, 
                message="Internal error", 
                request_id=req_id,
                data="Unknow how to handle method {} with params {}".format(req_method,req_params)
                )

    except Exception:
        result = error_dict( 
            code=-32603, 
            message="Internal error", 
            request_id=req_id,
            data=str( sys.exc_info() )
            )
    
    return result