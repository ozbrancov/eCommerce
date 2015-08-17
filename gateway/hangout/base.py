import datetime
import pytz

from django.db import models
from django.utils import timezone


# class CoreMixin(object):
#     def __repr__(self):
#         class_name = self.__class__.__name__.replace("_", " ")
#         if hasattr(self, "name"):
#             return "<%s[%s] ('%s')>" % (class_name, self.id, self.name)
#         else:
#             return "<%s[%s]>" % (class_name, self.id)


# class BaseMixin(OspreyCoreMixin):
#     id = models.IntegerField(primary_key=True, server_default='1', nullable=False)

#     created_date = models.DateTimeField(nullable=False)

#     last_modified_date = models.DateTimeField(nullable=False)

#     naive = datetime.datetime.utcnow()

#     aware = timezone.now()

#     def created_by_id(self):
#         return models.ForeignKey('user.id', default=naive, nullable=False)

#     def created_by(self):
#         return models.ForeignKey('user.username', default=None)


#     def last_modified_by_id(self):
#         return models.ForeignKey('user.id', default=None, nullable=False)
