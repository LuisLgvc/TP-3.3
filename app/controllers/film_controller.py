from ..models.film_model import Film

from flask import request

from decimal import Decimal

class FilmController:
    """Film controller class"""

    @classmethod
    def get(cls, film_id):
        """Get a film by id"""
        film = Film(film_id=film_id)
        result = Film.get(film)
        if result is not None:
            return result.serialize(), 200
        
    @classmethod
    def get_all(cls):
        """Get all films"""
        film_objects = Film.get_all()
        films = []
        for film in film_objects:
            films.append(film.serialize())
        return films, 200
    
    @classmethod
    def create(cls):
        """Create a new film"""
        data = request.json
        # TODO: Validate date
        film = Film(**data)
        if Film.validate(film):
            Film.create(film)
            return {'message': 'Film created successfully'}, 201

    @classmethod
    def update(cls, film_id):
        """Update a film"""
        data = request.json
        # TODO: Validate data
        
        data['film_id'] = film_id

        film = Film(**data)

        # TODO: Validate film exists
        # Verifico la existencia del film
        if Film.exists(film_id): # Ejercicio 3
            # Verifico que el film cumpla con el formato requerido
            if Film.validate(film): # Ejercicio 4
                Film.update(film)
        return {'message': 'Film updated successfully'}, 200
    
    @classmethod
    def delete(cls, film_id):
        """Delete a film"""
        film = Film(film_id=film_id)

        # TODO: Validate film exists
        # Verifico la existencia del film
        if Film.exists(film_id):
            Film.delete(film)
        return {'message': 'Film deleted successfully'}, 204