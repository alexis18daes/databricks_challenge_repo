# coding: utf-8

# ||********************************************************************************************************
# || PROYECTO   		: POCP -CHALLENGE GLOBLANT 
# || NOMBRE     		: challenge.py
# || TABLA DESTINO	: challenge.reporte_final
# || TABLAS FUENTES	: departments.csv
# ||                  hired_employees.csv
# ||                  jobs.csv
# || OBJETIVO   		: ETL - big data migrati
# || TIPO       		: pyspark
# || REPROCESABLE	  : NA
# || SCHEDULER		  : NA
# || JOB  		      : NA
# || VERSION   DESARROLLADOR           FECHA        DESCRIPCION
# || 1.1       ALEXIS DAVILA        21/03/23     Creacion del proceso
# *************************************************************************************************************

###
 # @section Import
 ##
import datetime
import calendar
import os
import sys
import json
from datetime import datetime
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, current_timestamp, unix_timestamp
from pyspark.sql import functions as F
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np
