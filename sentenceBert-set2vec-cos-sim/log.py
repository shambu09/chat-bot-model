log_file = """
------------------Log File-------------------


cosine matrix : [0.22727524 0.3581024  0.23890063 0.25685427 0.27844733 0.22884378
 0.16079564 0.22170201]
label : 1 - 0.358102411031723

cosine matrix : [0.34126547 0.23848823 0.30871403 0.2899548  0.24924217 0.14149205
 0.25470322 0.29490003]
label : 0 - 0.341265469789505

cosine matrix : [0.28256875 0.25203484 0.26016435 0.3520647  0.2785889  0.13308007
 0.2391718  0.30677226]
label : 3 - 0.35206469893455505

cosine matrix : [0.2429555  0.16094644 0.2217111  0.23409766 0.22705668 0.09438558
 0.35776684 0.2686213 ]
label : 6 - 0.3577668368816376

cosine matrix : [0.2325571  0.1747624  0.20630161 0.23151916 0.24124804 0.10395606
 0.3103559  0.26121327]
label : 6 - 0.31035590171813965

cosine matrix : [0.24195658 0.22595479 0.24385522 0.28291538 0.24164063 0.14418367
 0.20367765 0.26484585]
label : 3 - 0.2829153835773468
"""






























































#####################################
################CODE#################
#####################################
class Logger:
    __init = "\n------------------Log File-------------------\n"

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

    @__readFile
    def __preprocess(string, log_string):
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
