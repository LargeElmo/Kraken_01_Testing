import os
import sys
print()
print("Python interpreter in use:  ", sys.executable)
print()
current_working_directory = os.getcwd()
current_path = sys.path
os.getcwd() and __file__
print('__file__:    ', __file__)
print()
print('getcwd:      ', os.getcwd())
print()
print('__file__:    ', __file__)
print()
print('basename:    ', os.path.basename(__file__))
print()
print('dirname:     ', os.path.dirname(__file__))
print()
print('abspath:     ', os.path.abspath(__file__))
print()
print('abs dirname: ', os.path.dirname(os.path.abspath(__file__)))
