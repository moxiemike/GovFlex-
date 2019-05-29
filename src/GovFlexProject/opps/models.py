from django.db import models

# Create your models here.
class Opportunity(models.Model):
  title        = models.CharField(max_length=512)
  solicNum     = models.CharField(max_length=128, blank=True, null=True)
  agency       = models.CharField(max_length=128, blank=True, null=True)
  office       = models.CharField(max_length=128, blank=True, null=True)
  location     = models.CharField(max_length=128)
  jobType      = models.CharField(max_length=64)
  origJobType  = models.CharField(max_length=64)
  lastPost     = models.DateField()
  origPost     = models.DateField()
  respDeadline = models.CharField(max_length=64, blank=True, null=True)
  archPolicy   = models.CharField(max_length=64, blank=True, null=True)
  archDate     = models.DateField(blank=True, null=True)
  setAsideType = models.CharField(max_length=64, blank=True, null=True)
  classCode    = models.CharField(max_length=8)
  NAICScode    = models.IntegerField(blank=True, null=True)
  officeAddr   = models.CharField(max_length=256, blank=True, null=True)
  contactInfo  = models.TextField(blank=True, null=True)
  placeOfPerf  = models.TextField(blank=True, null=True)
  addInfoLink  = models.CharField(max_length=256, blank=True, null=True)
  description  = models.TextField()
  active       = models.CharField(max_length=8)
  link         = models.SlugField(max_length=128)
  
  def __str__(self):
    return 'Opportunity %s: %s' % (self.title, self.solicNum)
  
  #def save(self, *args, **kwargs):
    
        