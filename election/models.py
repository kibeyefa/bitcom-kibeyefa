from django.db import models

# Create your models here.


class AgentName(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.IntegerField()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class AnnouncedLgaResults(models.Model):
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=10)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.lga_name} - {self.party_abbreviation} - {self.party_score}'


class AnnouncedPuResults(models.Model):
    polling_unit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50, null=True, blank=True)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)


class AnnouncedStateResults(models.Model):
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=11)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)


class AnouncedWardResults(models.Model):
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=11)
    party_score = models.IntegerField()
    entered_ny_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)


class LGA(models.Model):
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField()
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return self.lga_name


class Party(models.Model):
    partyid = models.CharField(max_length=4)
    partynmae = models.CharField(max_length=11)

    def __str__(self):
        return self.partyid


class PollingUnit(models.Model):
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField(blank=True, null=True)
    polling_unit_number = models.CharField(
        max_length=50, blank=True, null=True)
    polling_unit_name = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    long = models.CharField(max_length=255, blank=True, null=True)
    entered_by_user = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    user_ip_address = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.polling_unit_name


class State(models.Model):
    state_id = models.IntegerField(primary_key=True, unique=True)
    state_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.state_name


class Ward(models.Model):
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField()
    ward_description = models.TextField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)
