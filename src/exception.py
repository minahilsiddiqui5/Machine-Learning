import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() 

    #exc_tb = this will probably give you all the info like on which file the exception has occurred
    file_name = exc_tb.tb_frame.f_code.co_file_name
    error_message = "Error occured in python script name [{0}] Line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super._init_(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message