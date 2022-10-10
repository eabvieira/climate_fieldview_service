from app.errors.error_codes import get_all_error_codes
import asyncio

class ErroSeguradoraParser(Exception):
    def __init__(self, message, code=500):
        super().__init__(message)

        self.error_code = 0
        self.errors = message
        self.code = code

        codigos_erros_dict = get_all_error_codes()

        if type(message) == str:
            mensagem = message.strip()

            for key in codigos_erros_dict:
                original_message = key['original_message']
                if original_message in mensagem:
                    error = key['error_code']

                    self.errors = {'codigo': error}
        elif type(message) == list:
            for key in codigos_erros_dict:
                for msg in message:
                    original_message = key['original_message']
                    if original_message in str(msg):
                        error = key['error_code']
                        self.errors = {'codigo': error}
                        break
