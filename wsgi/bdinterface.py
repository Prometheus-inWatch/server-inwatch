# -*- coding: utf-8 -*-

import MySQLdb
from bd import *


class BDInterface:
    conexion = None

    def connect(self):
        self.conexion = MySQLdb.connect(BDHOST,BDUSER,BDPASS,BDNAME)


    def disconnect(self):
        self.conexion.close()


    def insertarConsejo(self,text):
        cursor = self.conexion.cursor()
        query = "INSERT INTO tips (texto) VALUES (\'"+text+"\')"
        try:
            cursor.execute(query)
            self.conexion.commit()
        except:
            self.conexion.rollback()
        print query
