from django.db import models
from django.contrib.postgres.fields import ArrayField


class Subject(models.Model):
    name = models.CharField(max_length=255)
    chapters = ArrayField(models.CharField(max_length=255))
    total_duration = models.IntegerField("total duration in minutes")
    class_duration = models.IntegerField("average duration in minutes")

    def __str__(self):
        return "{}".format(self.name)


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    doj = models.DateField('date of joining')
    salary = models.FloatField("in hand salary LPA")
    twl = models.BooleanField("takes web lecture")
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return "{}".format(self.name)


class Student(models.Model):
    roll_number = models.IntegerField()
    name = models.CharField(max_length=255)
    doj = models.DateField('date of joining')
    standard = models.CharField(max_length=255)
    ranking = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)


class StudentContact(models.Model):
    name = models.CharField(max_length=255)
    relation = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=12)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return "{}({})".format(self.name,self.relation)


ClassRoomShapes = [("oval","oval"), ("rectangular","rectangular"), ("canopy","canopy"), ("elevated","elevated")]


class ClassRoom(models.Model):
    seating_capacity = models.IntegerField()
    web_support = models.BooleanField()
    shape = models.CharField(max_length=255,choices= ClassRoomShapes)

    def __str__(self):
        return "{} ({})".format(self.shape,self.id)


class Class(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return "{} {}".format(self.teacher,self.subject)


class ClassStudent(models.Model):
    subject_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

