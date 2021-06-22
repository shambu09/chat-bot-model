log_file = """
------------------Log File-------------------

load_model: loaded model
load_model: loaded model
Question added to dataBase - what kinda work do you do
Answer added: I Chat
load_model: loaded model
load_model: loaded model
Question added to dataBase - what kinda work do you do
Answer added: I Chat
current QS: ['What is your name', 'hello', 'tell me your name?', 'what do you do?', 'locations', 'thank you so much', 'where do you live', 'what is your location', 'where do you live', 'what kinda work do you do', 'what kinda work do you do']
 Answers: ['chatbot', 'hi', 'chatbot', 'I chat', 'India', 'welcome', 'India', 'India', 'India', 'I Chat', 'I Chat']
Question added to dataBase - how can i help you
Answer added: I am here to help you not the other way round
current QS: ['What is your name', 'hello', 'tell me your name?', 'what do you do?', 'locations', 'thank you so much', 'where do you live', 'what is your location', 'where do you live', 'what kinda work do you do', 'what kinda work do you do', 'how can i help you']
 Answers: ['chatbot', 'hi', 'chatbot', 'I chat', 'India', 'welcome', 'India', 'India', 'India', 'I Chat', 'I Chat', 'I am here to help you not the other way round']
Question added to dataBase - how can i help you
Answer added: I am here to help you not the other way round
current QS: ['What is your name', 'hello', 'tell me your name?', 'what do you do?', 'locations', 'thank you so much', 'where do you live', 'what is your location', 'where do you live', 'what kinda work do you do', 'what kinda work do you do', 'how can i help you', 'how can i help you']
 Answers: ['chatbot', 'hi', 'chatbot', 'I chat', 'India', 'welcome', 'India', 'India', 'India', 'I Chat', 'I Chat', 'I am here to help you not the other way round', 'I am here to help you not the other way round']
load_model: loaded model
load_model: loaded model
Question added to dataBase - how are you doing bot
Answer added: I am fine
current QS: ['What is your name', 'hello', 'tell me your name?', 'what do you do?', 'locations', 'thank you so much', 'where do you live', 'what is your location', 'where do you live', 'what kinda work do you do', 'what kinda work do you do', 'how can i help you', 'how can i help you', 'how are you doing bot']
 Answers: ['chatbot', 'hi', 'chatbot', 'I chat', 'India', 'welcome', 'India', 'India', 'India', 'I Chat', 'I Chat', 'I am here to help you not the other way round', 'I am here to help you not the other way round', 'I am fine']
Question added to dataBase - lets toast bot
Answer added: I am virtual you idiot
current QS: ['What is your name', 'hello', 'tell me your name?', 'what do you do?', 'locations', 'thank you so much', 'where do you live', 'what is your location', 'where do you live', 'what kinda work do you do', 'what kinda work do you do', 'how can i help you', 'how can i help you', 'how are you doing bot', 'lets toast bot']
 Answers: ['chatbot', 'hi', 'chatbot', 'I chat', 'India', 'welcome', 'India', 'India', 'India', 'I Chat', 'I Chat', 'I am here to help you not the other way round', 'I am here to help you not the other way round', 'I am fine', 'I am virtual you idiot']
load_model: loaded model
find_similiar: "give me a toast"
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
