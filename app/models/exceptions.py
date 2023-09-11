from flask import jsonify

class CustomException(Exception):

    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response

#Ejercicio 1. Excepcion Personalizada 

class FilmNotFound(CustomException):
      def __init__(self, film_id):
        description = f"El film con id {film_id} no existe"
        super().__init__(status_code=404, name="Film no encontrado", description=description)
        
#Ejercicio 2

class InvalidDataError(CustomException):
    def __init__(self, description="Datos con formato invalido"):
        super().__init__(status_code=400, name="Formato invalido", description=description)
