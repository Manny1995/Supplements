from peewee import *
import sqlite3
from sqlite3 import Error
import datetime as dt


# SOURCES
# https://medium.com/@prabhath_kiran/introduction-to-peewee-and-relations-1c72af26e1b9


db = SqliteDatabase('supplements.db', check_same_thread=False)

def open_connection():
	db.connect()

def close_connection():
	if not db.is_closed():
		db.close()


class SupplementCategory(Model):
	name = CharField()

	class Meta:
		database = db

# Gym, sleep, academic, side project
class WorkType(Model):
	name = CharField()

	class Meta:
		database = db


class User(Model):
	username = CharField(unique=True)
	first_name = CharField()
	last_name = CharField()
	email = CharField()
	password = CharField()
	auth_token = CharField()

	class Meta:
		database = db


class Supplement(Model):
	name = CharField()
	description = CharField()

	# FOREIGN KEYS
	category_id = ForeignKeyField(SupplementCategory, related_name='supplements') 			# Categorical, I'm thinking like stimulant or something

	class Meta:
		database = db


class Entry(Model):
	start = DateField(default = dt.datetime.now)
	description = CharField()
	dosage = DoubleField(constraints=[Check('dosage > 0')])													# we do this in milligrams
	alertness = IntegerField(constraints=[Check('alertness <= 10 and alertness >= 1')]) 					# 1 to 10 How awake, cognitive ability
	productivity = IntegerField(constraints=[Check('productivity <= 10 and productivity >= 1')]) 			# 1 to 10 was I able to get work done?
	effectiveness = IntegerField(constraints=[Check('effectiveness <= 10 and effectiveness >= 1')]) 		# 1 to 10, effectiveness of the product on desired effect
	activation_time = IntegerField(constraints=[Check('activation_time <= 10 and activation_time >= 1')]) 	# Amount of time it took to take into effect

	# FOREIGN KEYS
	work_id = ForeignKeyField(WorkType, related_name='worktypes')					# Categorical, gym, sleep, exerciese, sleep, Academic, Side Project
	supplement_id = ForeignKeyField(Supplement, related_name='supplements')			# The supplement foreign key that this entry belongs to
	user_id = ForeignKeyField(User, related_name='users', on_delete='CASCADE')		# The user foriegn key that this entry belongs to


	class Meta:
		database = db



db.create_tables([SupplementCategory, WorkType, User, Supplement, Entry], safe=True)
