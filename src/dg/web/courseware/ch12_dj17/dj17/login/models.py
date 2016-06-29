# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Category1(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    path = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'category1'


class Category2(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    parent = models.ForeignKey(Category1, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'category2'


class Company(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    stage = models.CharField(max_length=255, blank=True)
    tag = models.CharField(max_length=255, blank=True)
    people_num = models.IntegerField(blank=True, null=True)
    home_url = models.CharField(max_length=255, blank=True)
    logo = models.CharField(max_length=255, blank=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Job(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    uid = models.ForeignKey('User', db_column='uid', blank=True, null=True)
    cid = models.ForeignKey(Company, db_column='cid', blank=True, null=True)
    category_path = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    scale = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    experience = models.CharField(max_length=255, blank=True)
    educational = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    tag = models.CharField(max_length=255, blank=True)
    desc = models.TextField(blank=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job'


class JobApply(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    uid = models.ForeignKey('User', db_column='uid', blank=True, null=True, related_name='uid')
    job = models.ForeignKey(Job, blank=True, null=True)
    resume = models.ForeignKey('Resume', blank=True, null=True)
    send_uid = models.ForeignKey('User', db_column='send_uid', blank=True, null=True, related_name='send_uid')
    is_read = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_apply'


class JobFeedback(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    uid = models.ForeignKey('User', db_column='uid', blank=True, null=True)
    content = models.TextField(blank=True)
    job = models.ForeignKey(Job, blank=True, null=True)
    is_read = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_feedback'


class Resume(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    uid = models.ForeignKey('User', db_column='uid', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    tag = models.CharField(max_length=255, blank=True)
    education = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    mobilephone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True)
    self_evaluate = models.CharField(max_length=255, blank=True)
    hope_work = models.CharField(max_length=255, blank=True)
    hope_type = models.CharField(max_length=255, blank=True)
    hope_city = models.CharField(max_length=255, blank=True)
    hope_salary = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    attach_file = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'resume'


class SenderValid(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True)
    cid = models.ForeignKey(Company, db_column='cid', blank=True, null=True)
    uid = models.ForeignKey('User', db_column='uid', blank=True, null=True)
    is_valid = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sender_valid'


class StudyExperience(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    resume = models.ForeignKey(Resume, blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    educational = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_experience'


class User(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(unique=True, max_length=255, blank=True)
    passwd = models.CharField(max_length=255, blank=True)
    mobilephone = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    is_avaliable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

    def __unicode__(self):
        return self.name


class WorkExperience(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    resume = models.ForeignKey(Resume, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    job = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_experience'
