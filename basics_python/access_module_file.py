# import sample_module_file
import sample_module_file_new
# print(sample_module_file.s)

print("==============================")
print(sample_module_file_new.foo("test"))
print("==============================")

# from sample_module_file import *
from sample_module_file_new import s, foo

foo("test")

from module_dir.sample_module_file_folder import *
# from module_dir.sample_module_file_folder import PASS_CODE
#
print(PASS_CODE)
