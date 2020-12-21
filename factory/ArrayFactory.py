#!/usr/bin/python3.7
#coding: utf-8

class Factory(object):
    _name = "factory"
    types = []
    
    def createArrayObject(self, nameType):
        try:
            class ArrayFactory(Factory):
                _name = "array.factory"
                
                def getEmptyArray(self):
                    emptyArray = []
                    return emptyArray
            
            if nameType == "Array":
                return ArrayFactory()
            
            assert 0, "Bad factory creation: %s" % type
        except:
            raise BaseException
  
