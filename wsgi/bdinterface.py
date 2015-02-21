# -*- coding: utf-8 -*-

import MySQLdb
from bd import *
import random

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


    def getConsejo(self):
        cursor = self.conexion.cursor()
        query = "SELECT * FROM tips"
        cursor.execute(query)
        consejos = cursor.fetchall()
        numero = random.randint(0, len(consejos)-1)
        return consejos[numero]



    def insertarUsuario(self, email,cigarsPerDay,cigarsPerPacket,pricePerPacket,stopSmokingDate,totalUnsmokedCigars,
    totalMoneySaved,totalTimeSaved,totalDaysClean):
        cursor = self.conexion.cursor()

        query = "INSERT INTO user (email,cigarsPerDay,cigarsPerPacket,pricePerPacket,stopSmokingDate,\
        totalUnsmokedCigars, totalMoneySaved, totalTimeSaved, totalDaysClean)\
        VALUES ( \'"+email+"\', \'"+str(cigarsPerDay)+"\', \'"+str(cigarsPerPacket)+"\', \
        \'"+str(pricePerPacket)+"\', \'"+str(stopSmokingDate)+"\', \'"+str(totalUnsmokedCigars)+"\', \
        \'"+str(totalMoneySaved)+"\', \'"+str(totalTimeSaved)+"\', \'"+str(totalDaysClean)+"\')"

        try:
            cursor.execute(query)
            self.conexion.commit()
        except:
            self.conexion.rollback()



    def getUsuario(self,email):
        cursor = self.conexion.cursor()
        query = "SELECT * FROM user WHERE email like \'"+email+"\'"
        cursor.execute(query)
        usuario = cursor.fetchall()
        return usuario[0]


    
