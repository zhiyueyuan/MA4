""" Python interface to the C++ Person class """
"""
Student: Zhiyue Yuan
Mail: yuriyeahyeah@163.com
Reviewed by: Mina
Date: 2023-10-18
"""
import ctypes
lib = ctypes.cdll.LoadLibrary('./libperson.so')

class Person(object):
	def __init__(self, age):
		lib.Person_new.argtypes = [ctypes.c_int]
		lib.Person_new.restype = ctypes.c_void_p
		lib.Person_getAge.argtypes = [ctypes.c_void_p]
		lib.Person_getAge.restype = ctypes.c_int
		lib.Person_setAge.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Person_getDecades.argtypes = [ctypes.c_void_p]
		lib.Person_getDecades.restype = ctypes.c_double # change return type from int to double
		# Added for executing fibonacci-calculations
		lib.Person_fib.argtypes = [ctypes.c_void_p]
		lib.Person_fib.restype = ctypes.c_longlong
		lib.Person_delete.argtypes = [ctypes.c_void_p]
		self.obj = lib.Person_new(age)

	def getAge(self):
		return lib.Person_getAge(self.obj)

	def setAge(self, age):
		lib.Person_setAge(self.obj, age)

	def getDecades(self):
		return lib.Person_getDecades(self.obj)
	
	# Added for executing fibonacci-calculations
	def fib(self):
		return lib.Person_fib(self.obj)
        
	def __del__(self):
		return lib.Person_delete(self.obj)
