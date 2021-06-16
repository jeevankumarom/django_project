from django.db import models

class task1(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)



class task2(models.Model):
    Mobile=models.IntegerField()
    Avtar=models.CharField(max_length=100)

"""class ocrregister(models.Model):
    
    clientname=models.CharField(max_length=100)
    contractorname=models.CharField(max_length=100)
    site_projectname=models.CharField(max_length=100)
    locationofwork=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    appropriategovt=models.CharField(max_length=100)
    zone-applicable=models.CharField(max_length=100)
    industry-applicable=models.CharField(max_length=100)
    po-startdate=models.CharField(max_length=100)
    po-enddate=models.CharField(max_length=100)
    licensestatus=models.CharField(max_length=100)
    liensenum=models.CharField(max_length=100)
    licensevalid=models.CharField(max_length=100)
    licensestrength=models.CharField(max_length=100)
    workmencompensation_policy=models.CharField(max_length=100)
    wcpvalid_till=models.CharField(max_length=100) 
    wcpstrength_covered=models.CharField(max_length=100)
    wcprisklocation_covered=models.CharField(max_length=100)
    mm-yy=models.CharField(max_length=100)
    salary-type=models.CharField(max_length=100)
    po/agreement/slagreement/workorder=models.CharField(max_length=100)
    labourLicenseUnderCLRA=models.CharField(max_length=100)
    musterroll=models.CharField(max_length=100)
    registerofwages=models.CharField(max_length=100)
    bankstatement=models.CharField(max_length=100)
    EPFchallan=models.CharField(max_length=100)
    EPFecr=models.CharField(max_length=100)
    EPFarrearchallan=models.CharField(max_length=100)
    EPFarrearecr=models.CharField(max_length=100)
    ESIdoubleverificationchallan=models.CharField(max_length=100)
    ESIcontributionhistory=models.CharField(max_length=100)
    ESIsupplementarychallan(arrear)=models.CharField(max_length=100)
    ESIarrearcontributionhistory=models.CharField(max_length=100)
    WCpolicy=models.CharField(max_length=100)"""
