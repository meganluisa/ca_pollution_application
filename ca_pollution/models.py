# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models

class DmrFacility(models.Model):
    permit_num = models.CharField(primary_key=True, max_length=255)
    frs_id = models.CharField(max_length=12, blank=True, null=True)
    f_name = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    st = models.CharField(max_length=2, blank=True, null=True)
    sic_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'dmr_facility'


class DmrRelease(models.Model):
    gid = models.AutoField(primary_key=True)
    year = models.DateField(blank=True, null=True)
    permit_num = models.ForeignKey(DmrFacility, models.DO_NOTHING, db_column='permit_num', blank=True, null=True)
    frs_id = models.CharField(max_length=254, blank=True, null=True)
    huc_code = models.CharField(max_length=254, blank=True, null=True)
    watershed = models.CharField(max_length=254, blank=True, null=True)
    f_lat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    f_long = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pollutant = models.CharField(max_length=254, blank=True, null=True)
    sub_reg_id = models.CharField(max_length=254, blank=True, null=True)
    cas_id = models.CharField(max_length=254, blank=True, null=True)
    avg_day_fl = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    twpe = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_lbs = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dfr_link = models.CharField(max_length=254, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'dmr_release'


class TriFacility(models.Model):
    f_id = models.CharField(primary_key=True, max_length=255)
    frs_id = models.CharField(max_length=12, blank=True, null=True)
    f_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    st = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    federal = models.BooleanField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'tri_facility'


class TriRelease(models.Model):
    gid = models.AutoField(primary_key=True)
    year = models.DateField(blank=True, null=True)
    f = models.ForeignKey(TriFacility, models.DO_NOTHING, blank=True, null=True)
    frs_id = models.CharField(max_length=254, blank=True, null=True)
    f_lat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    f_long = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    industry_c = models.CharField(max_length=254, blank=True, null=True)
    industry = models.CharField(max_length=254, blank=True, null=True)
    sic = models.CharField(max_length=254, blank=True, null=True)
    naics = models.CharField(max_length=254, blank=True, null=True)
    pollutant = models.CharField(max_length=254, blank=True, null=True)
    cas_id = models.CharField(max_length=254, blank=True, null=True)
    srs_id = models.CharField(max_length=254, blank=True, null=True)
    release = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unit = models.CharField(max_length=254, blank=True, null=True)
    clean_air = models.BooleanField(blank=True, null=True)
    metal = models.BooleanField(blank=True, null=True)
    carcinogen = models.BooleanField(blank=True, null=True)
    medium = models.CharField(max_length=254, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'tri_release'
