#Name: Zac Waite
#Date: April 4 2021
#Program Name: dot.py
#Purpose: Class file to access dictionaris with dot syntax in python

#https://dev.to/0xbf/use-dot-syntax-to-access-dictionary-key-python-tips-10ec
#Used this source on April 3 to make a dot syntax for position

class Dot(dict):
    '''Used to access dictionaires with dot syntax'''
    def __getattr__(self, key): 
        '''Gets attribute'''
        try:return self[key]
        except KeyError as k:raise AttributeError(k)
    def __setattr__(self, key, value):
        '''Sets attribute'''
        self[key] = value
    def __delattr__(self, key):
        '''Deletes attribute'''
        try: del self[key]
        except KeyError as k: raise AttributeError(k)
    def __repr__(self):
        '''Prints attribute information'''
        return '<DictX ' + dict.__repr__(self) + '>'