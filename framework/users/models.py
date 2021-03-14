from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    group = models.ForeignKey(
        "Team", 
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )
    Badges = (
   ('B1', 'Bronze1'),
   ('B2', 'Bronze2'),
   ('B3', 'Bronze1'),
   ('S1', 'Silver1'),
   ('S2', 'Silver2'),
   ('S3', 'Silve3'),
   )
    Badge = models.CharField(choices=Badges, max_length=128, default='Bronze1')

    Progress = models.IntegerField()




    def __str__(self):
        return self.username

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    leader = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.name

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    description=  models.TextField()
    assigned = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.name
        
