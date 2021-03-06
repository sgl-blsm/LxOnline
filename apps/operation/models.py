# encoding:utf-8
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models

from apps.users.models import UserProfile
from apps.courses.models import Course

# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    mobile = models.CharField(max_length=11, verbose_name=u'手机号码')
    course_name = models.CharField(max_length=50, verbose_name=u'课程名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseComment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    comment = models.CharField(max_length=200, verbose_name=u'评论')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.course


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    fav_id = models.IntegerField(default=0, verbose_name=u'数据id')
    fav_type = models.CharField(max_length=2, default='1', verbose_name=u'收藏类型',
                                choices=(('1', '课程'), ('2', '教师'), ('3', '机构')))
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u'接收用户')  # 0代表发给所有用户
    message = models.CharField(max_length=500, verbose_name=u'消息内容')
    is_read = models.BooleanField(default=False, verbose_name=u'是否读过')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'学习时间')

    class Meta:
        verbose_name = u'用户学习课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user
