import os
import datetime
import re

from django.db import models

import base


# Create your models here.
class Hangout(models.Model):
	id = models.IntegerField(primary_key=True, null=False)
	title = models.CharField(max_length=120, null=False, blank=False)
	status = models.TextField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
	alternate_price = models.TextField()
	slug = models.SlugField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	update = models.DateTimeField(auto_now_add=False, auto_now=True)
	requested_hangout = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
	active = models.BooleanField(default=False)


	def __unicode__(self):
		return self.title






# class User(models.Model, BaseMixin):
#     __tablename__ = "user"


#     username = models.CharField(max_length=120, unique=True))
#     name = models.CharField(max_length=120, nullable=False)
#     salt = models.CharField(max_length=128, nullable=False)
#     password_hash = models.CharField(max_length=80, nullable=True)  # Needs to be over 77+ to fit hashed passwords
#     email = models.CharField(max_length=255, nullable=False)
#     phone = models.CharField(max_length=14, nullable=False)
#     is_admin = models.BooleanField(default=False, nullable=False)

#     # keep track of logins
#     last_login = models.DateTime(datetime.datetime.utcnow(), nullable=False)
#     login_count = models.IntegerField(default=0, nullable=False)

#     # True to be able to login
#     is_active = models.BooleanField(default=True, nullable=False)

#     password = models.CharField(max_length=80, nullable=True)       # Needs to be over 77+ to fit hashed passwords


#     def __init__(self, username, name, password, email, phone, is_admin, **kwargs):
#         super(User, self).__init__(**kwargs)
#         self.phone = phone
#         self.username = username
#         self.name = name
#         self.salt = hash.get_random_string()
#         self.password_hash = common.hash_pass(password, sys_user=None, salt=self.salt)
#         self.password = self.password_hash 
#         self.email = email
#         self.phone = phone
#         self.is_admin = is_admin
#         self.last_login = datetime.datetime(2014, 10, 24, 17, 33, 38, 411915)  
#         self.is_active = True

#     def set_password(self, raw_password):
#         session = sa.orm.Session.object_session(self)
#         self.salt = hash.get_random_string()
#         self.password_hash = common.hash_pass(raw_password, sys_user=None, salt=self.salt)
#         self.password = self.password_hash
#         common.managed_commit(session)
