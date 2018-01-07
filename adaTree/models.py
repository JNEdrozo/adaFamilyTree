from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Cohort Information
C1 = 'C1'
C2 = 'C2'
C3 = 'C3'
C4 = 'C4'
C5 = 'C5'
C6_BRACKETS = 'C6 Brackets'
C6_PARENS = 'C6 Parens'
C7_QUEUES = 'C7 Queues'
C7_STACKS = 'C7 Stacks'
C8_CARETS = 'C8 Carets'
C8_PIPES = 'C8 Pipes'

COHORT_CLASSES = (
    (C1, '(Oct 2014)'),
    (C2, '(Aug 2015)'),
    (C3, '(April 2016)'),
    (C4, '(Sept 2016)'),
    (C5, '(Feb 2017)'),
    (C6_BRACKETS, '(July 2017)'),
    (C6_PARENS, '(July 2017)'),
    (C7_QUEUES, '(Jan 2018)'),
    (C7_STACKS,'(Jan 2018)'),
    (C8_CARETS, '(July 2018)'),
    (C8_PIPES, '(July 2018)'),
)

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ada_relation = models.CharField(
      max_length=20,
      blank=False,
    )

    cohort_served = MultiSelectField(
        choices=COHORT_CLASSES,
        max_choices=3,
        max_length=3,
        blank=False,
    )

    pronouns = models.CharField(
      max_length=20,
      blank=False,
    )



    github_username = models.CharField(
      max_length=30,
      blank=False
    )

    bio = models.TextField(
      max_length=500,
      blank=True
    )
