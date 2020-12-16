#!/usr/bin/python3.7
#coding: utf-8
##########################################################################################################
#    
#    NOTA: ESTE PROGRAMA SERA PARTE INTEGRANTE DO SISTEMA C.A.I.O PARA I.A NO MODULO RUSSELL RPA; 
#    @AUTHOR: SANDRO REGIS CARDOSO
##########################################################################################################
import sys

class MetaSingleton(type):
    _name = "meta.singleton"
    _description = "Meta class Singleton for Array object"
    
    _instances = {}
    
    def __call__(self, *args, **kwargs):
        try:
            if self not in self._instances and len(self._instances) == 0:
                self._instances[self] = super(MetaSingleton, self).__call__(*args, **kwargs)
                return self._instances[self]
            else:
                self._instances[self] = super(MetaSingleton, self).__init__(*args, **kwargs)
                return self._instances[self]
        except:
            raise BaseException
    

class ArraySingleton(metaclass=MetaSingleton):
    _name = "array.singleton"
    _description = "Singleton for Array object"
    
    _list = list
    
    @classmethod
    def _List_To_Class(self, _list):
        try:
            return getattr(sys.modules[__name__], _list)
        except:
            raise BaseException

