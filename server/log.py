log_file = """
------------------Log File-------------------

load_model: loaded model
Question added to dataBase - Hi
Answer added: Hello, I am ComBot
Question added to dataBase - What do you do?
Answer added: I can help you upgrade your server and can host a website....
Question added to dataBase - where do you live?
Answer added: In the cloud ofc
Question added to dataBase - where do you stay?
Answer added: In the cloud ofc
find_similiar: "hi"
find_similiar: "Where do you live ComBot?"
find_similiar: "How can I help you?"
find_similiar: "can you show me a world map"
find_similiar: "how are you?"
find_similiar: "are you fine?"
Question added to dataBase - How are you?
Answer added: fine
find_similiar: "how are you?"
find_similiar: "are you fine?"
find_similiar: "how can I help you ComBot?"
find_similiar: "can I help you ComBot"
find_similiar: "Hi"
find_similiar: "where do you stay?"
find_similiar: "what do you do?"
find_similiar: "can I help you?"
find_similiar: "hi"
find_similiar: "where do you live?"
find_similiar: "what do you do?"
find_similiar: "can I help you"
find_similiar: "hi"
find_similiar: "where do you stay?"
find_similiar: "what do you do?"
find_similiar: "can I help you ComBot"
Question added to dataBase - how can I help you ComBot
Answer added: I am here to help you not the the other way around
find_similiar: "can I help you ComBot"
find_similiar: "show me a world map"
Question added to dataBase - Can you show me a world map 
Answer added: Check here www.worldmap.com
find_similiar: "show me a world map"
load_model: loaded model
"""






























































##############################################
##################CODE########################
####https://github.com/shambu09/self-logger###
##############################################
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
