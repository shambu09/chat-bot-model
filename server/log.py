log_file = """
------------------Log File-------------------

load_model: loaded model
"""






























































#####################################
################CODE#################
#####################################
class Logger:
    __init = "\n------------------Log File-------------------\n"
    __func = ""

    def __writeFile(func):
        def inner(value=None):
            string, mode = func(str(value))
            with open(__file__, mode) as f:
                f.write(string)
        return inner

    def __readFile(func):
        def inner(*args):
            with open(__file__, "r") as f:
                string, i = func(f.read(), *args)
            return string, i
        return inner

    def wrap(func):
        def inner(*args):
            Logger.__func = f"{func.__name__}: "
            var = func(*args)
            Logger.__func = ""
            return var
        return inner

    @__readFile
    def __preprocess(string, log_string):
        log_string = f"{Logger.__func}{log_string}"
        i = -1*string[::-1].find('\n"""', 800)-5
        if log_string=="None":
            log_string = "\n"
        else:
            log_string = "\n" + log_string
        new_code = string[0:14] + string[14:i] + log_string + string[i: ]
        return new_code, i

    @__writeFile
    def log(string):
        new_code, _ = Logger.__preprocess(string)
        return new_code, "w"

    @__writeFile
    def clear(string):
        code, i = Logger.__preprocess(Logger.__init)
        new_code = code[0:14] + Logger.__init + code[i: ]
        return new_code, "w"
