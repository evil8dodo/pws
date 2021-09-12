
from engine.mathfunctions import *
from entities.entity import Entity

from typing import TypedDict
import random
from dataclasses import dataclass

import math
import time



# this is because dict.setdefault does not work. 
def dict_setdefault(dictionary: dict, key: str, value: list) -> list or None:
    """
    If dictionary key exists, return corresponding value
    If dictionary key does not exist apply value to new key 
    """
    r = dictionary.get(key,value)
    if key not in dictionary:
        dictionary[key] = value
    return r


class HashMap(object):
    """
    Hashmap is a a spatial index which can be used for a broad-phase
    collision detection strategy.
    """
    def __init__(self, cell_size: float) -> None:
        self.cell_size: float = cell_size
        self.grid: dict = {}


    def key(self, entity: Entity) -> tuple:
        cell_size: float = self.cell_size
        return (
            int((math.floor(entity.position.x/cell_size))*cell_size),
            int((math.floor(entity.position.y/cell_size))*cell_size),
            
        )
    
    def remove_from_key(self, key, entity: Entity) -> None:
        """
        Remove entity from hashmap
        """
        
        dict_setdefault( self.grid, key, []).remove(entity)
        

    def insert(self, entity: Entity) -> None:
        """
        Insert entity into the hashmap.
        """
        
        dict_setdefault( self.grid, self.key(entity), []).append(entity)
   
    def query(self, entity: Entity) -> list:
        """
        Return all objects in the cell specified by point.
        """
        
        return dict_setdefault( self.grid, self.key(entity), [])



