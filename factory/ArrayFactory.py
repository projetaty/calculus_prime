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
    
        
    def objectGenerator(self, objectNameType : str) -> object:
        try:
            yield self.createArrayObject(objectNameType)
        except:
            raise BaseException

#from os import sys
#def main():
#    _name = "main"
#    
#    try:
#        objFactory = Factory()
#        emptyArray = objFactory.createArrayObject("Array")
#        print("%s" %(type(emptyArray.getEmptyArray())))
#        return
#    except:
#        raise BaseException
#    
#if __name__ == "__main__":
#    main()
#    sys.exit(0)