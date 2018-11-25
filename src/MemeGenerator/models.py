# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comment(models.Model):
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid')
    memeid = models.ForeignKey('Meme', models.DO_NOTHING, db_column='memeid')
    comment = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'Comment'


class Likereaction(models.Model):
    memeid = models.ForeignKey('Meme', models.DO_NOTHING, db_column='memeid')
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid')
    reactionid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'LikeReaction'


class Meme(models.Model):
    templateid = models.ForeignKey('Template', models.DO_NOTHING, db_column='templateid')
    textid = models.ForeignKey('Text', models.DO_NOTHING, db_column='textid')
    image = models.TextField()
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Meme'


class Memetag(models.Model):
    memeid = models.ForeignKey(Meme, models.DO_NOTHING, db_column='memeid')
    tagid = models.ForeignKey('Tag', models.DO_NOTHING, db_column='tagid')

    class Meta:
        managed = False
        db_table = 'MemeTag'


class Tag(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'Tag'


class Taguser(models.Model):
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid')
    tagid = models.ForeignKey(Tag, models.DO_NOTHING, db_column='tagid')

    class Meta:
        managed = False
        db_table = 'TagUser'


class Template(models.Model):
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'Template'


class Text(models.Model):
    top = models.CharField(max_length=128)
    bottom = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'Text'


class User(models.Model):
    login = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'User'


class Usertemplate(models.Model):
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userid')
    templateid = models.ForeignKey(Template, models.DO_NOTHING, db_column='templateid')

    class Meta:
        managed = False
        db_table = 'UserTemplate'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
