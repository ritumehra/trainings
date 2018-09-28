
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg)

test_var_args('xoriant','python','training','code','test')


def testify(arg1, arg2, arg3):

    print("======== Testify Start ========")
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
    print("======== Testify End ========")

def testify_new(*arg):
    for iter in arg:
        print("arg:", iter)

# with *args
args = ("hey", 14, "joey")
testify(*args)
testify_new(*args)


def argument_function(**kwmyarg):
    print("Argument and Keyword argument function")

    for key, value in kwmyarg.items():
        print("{},{}".format(key, value))

kw_my_arg = {'a': 12, 'b': 13}

argument_function(**kw_my_arg)