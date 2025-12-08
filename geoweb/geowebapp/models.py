# from django.db import models

# Create your models here.
from django.contrib.gis.db import models


class CV_UnitsType(models.Model):
    term = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "CV_UnitsType"


class CV_VariableName(models.Model):
    term = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "CV_VariableName"


class CV_VariableType(models.Model):
    term = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "CV_VariableType"


class CV_ElevationDatum(models.Model):
    term = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        db_table = "CV_ElevationDatum"
        managed = True


class CV_SamplingFeatureGeoType(models.Model):
    term = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        db_table = "CV_SamplingFeatureGeoType"
        managed = True


class CV_SamplingFeatureType(models.Model):
    term = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        db_table = "CV_SamplingFeatureType"
        managed = True


class CV_RelationshipType(models.Model):
    term = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CV_RelationshipType'


class CV_SiteType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CV_SiteType'


class SamplingFeatures(models.Model):
    samplingfeatureid = models.AutoField(primary_key=True)
    samplingfeatureuuid = models.UUIDField()
    samplingfeaturetypecv = models.ForeignKey(CV_SamplingFeatureType, models.DO_NOTHING,
                                              db_column='samplingfeaturetypecv')
    samplingfeaturecode = models.CharField(unique=True, max_length=255)
    samplingfeaturename = models.CharField(
        max_length=255, blank=True, null=True)
    samplingfeaturedescription = models.CharField(
        max_length=5000, blank=True, null=True)
    samplingfeaturegeotypecv = models.ForeignKey(CV_SamplingFeatureGeoType, models.DO_NOTHING,
                                                 db_column='samplingfeaturegeotypecv', blank=True, null=True)
    featuregeometry = models.GeometryField(srid=3857, blank=True, null=True)
    featuregeometrywkt = models.CharField(
        max_length=10000000, blank=True, null=True)
    elevation_m = models.FloatField(blank=True, null=True)
    elevationdatumcv = models.ForeignKey(CV_ElevationDatum, models.DO_NOTHING,
                                         db_column='elevationdatumcv', blank=True, null=True)

    class Meta:
        db_table = "SamplingFeatures"
        managed = True


class RelatedFeatures(models.Model):
    relationid = models.AutoField(primary_key=True)
    samplingfeatureid = models.ForeignKey(
        SamplingFeatures, models.DO_NOTHING, db_column='samplingfeatureid')
    relationshiptypecv = models.ForeignKey(
        CV_RelationshipType, models.DO_NOTHING, db_column='relationshiptypecv')
    relatedfeatureid = models.ForeignKey(SamplingFeatures, models.DO_NOTHING, db_column='relatedfeatureid',
                                         related_name='relatedsamplingfeatures')

    # spatialoffsetid = models.ForeignKey(SpatialOffsets, models.DO_NOTHING, db_column='spatialoffsetid', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'RelatedFeatures'


class CV_OrganizationType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CV_OrganizationType'


class Organizations(models.Model):
    organizationid = models.AutoField(primary_key=True)
    organizationtypecv = models.ForeignKey(
        CV_OrganizationType, models.DO_NOTHING, db_column='organizationtypecv')
    organizationcode = models.CharField(unique=True, max_length=50)
    organizationname = models.CharField(max_length=255)
    organizationdescription = models.CharField(
        max_length=5000, blank=True, null=True)
    organizationlink = models.CharField(max_length=255, blank=True, null=True)
    parentorganizationid = models.ForeignKey('self', models.DO_NOTHING, db_column='parentorganizationid', blank=True,
                                             null=True)

    class Meta:
        managed = True
        db_table = 'Organizations'


class People(models.Model):
    personid = models.AutoField(primary_key=True)
    personfirstname = models.CharField(max_length=255)
    personmiddlename = models.CharField(max_length=255, blank=True, null=True)
    personlastname = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'People'


class Affiliations(models.Model):
    affiliationid = models.AutoField(primary_key=True)
    personid = models.ForeignKey(
        People, models.DO_NOTHING, db_column='personid')
    organizationid = models.ForeignKey(Organizations, models.DO_NOTHING, db_column='organizationid', blank=True,
                                       null=True)
    isprimaryorganizationcontact = models.BooleanField(blank=True, null=True)
    affiliationstartdate = models.DateField()
    affiliationenddate = models.DateField(blank=True, null=True)
    primaryphone = models.CharField(max_length=50, blank=True, null=True)
    primaryemail = models.CharField(max_length=255)
    primaryaddress = models.CharField(max_length=255, blank=True, null=True)
    personlink = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Affiliations'


class CV_MethodType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CV_MethodType'


class CV_ActionType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CV_ActionType'


class Methods(models.Model):
    methodid = models.AutoField(primary_key=True)
    methodtypecv = models.ForeignKey(
        CV_MethodType, models.DO_NOTHING, db_column='methodtypecv')
    methodcode = models.CharField(unique=True, max_length=50)
    methodname = models.CharField(max_length=255)
    methoddescription = models.CharField(
        max_length=5000, blank=True, null=True)
    methodlink = models.CharField(max_length=255, blank=True, null=True)
    organizationid = models.ForeignKey(Organizations, models.DO_NOTHING, db_column='organizationid', blank=True,
                                       null=True)

    class Meta:
        managed = True
        db_table = 'Methods'


class Actions(models.Model):
    actionid = models.AutoField(primary_key=True)
    actiontypecv = models.ForeignKey(
        CV_ActionType, models.DO_NOTHING, db_column='actiontypecv')
    methodid = models.ForeignKey(
        Methods, models.DO_NOTHING, db_column='methodid')
    begindatetime = models.DateTimeField()
    begindatetimeutcoffset = models.IntegerField()
    enddatetime = models.DateTimeField(blank=True, null=True)
    enddatetimeutcoffset = models.IntegerField(blank=True, null=True)
    actiondescription = models.CharField(
        max_length=5000, blank=True, null=True)
    actionfilelink = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Actions'


class ActionBy(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    actionid = models.ForeignKey(
        Actions, models.DO_NOTHING, db_column='actionid')
    affiliationid = models.ForeignKey(
        Affiliations, models.DO_NOTHING, db_column='affiliationid')
    isactionlead = models.BooleanField()
    roledescription = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ActionBy'


class FeatureActions(models.Model):
    featureactionid = models.AutoField(primary_key=True)
    samplingfeatureid = models.ForeignKey(
        SamplingFeatures, models.DO_NOTHING, db_column='samplingfeatureid')
    actionid = models.ForeignKey(
        Actions, models.DO_NOTHING, db_column='actionid')

    class Meta:
        managed = True
        db_table = 'FeatureActions'


class CV_Speciation(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CV_Speciation'


class Variables(models.Model):
    variableid = models.AutoField(primary_key=True)
    variabletypecv = models.ForeignKey(
        CV_VariableType, models.DO_NOTHING, db_column='variabletypecv')
    variablecode = models.CharField(unique=True, max_length=50)
    variablenamecv = models.ForeignKey(
        CV_VariableName, models.DO_NOTHING, db_column='variablenamecv')
    variabledefinition = models.CharField(
        max_length=5000, blank=True, null=True)
    speciationcv = models.ForeignKey(
        CV_Speciation, models.DO_NOTHING, db_column='speciationcv', blank=True, null=True)
    nodatavalue = models.FloatField()

    class Meta:
        managed = True
        db_table = 'Variables'


class Units(models.Model):
    unitsid = models.AutoField(primary_key=True)
    unitstypecv = models.ForeignKey(
        CV_UnitsType, models.DO_NOTHING, db_column='unitstypecv')
    unitsabbreviation = models.CharField(max_length=50)
    unitsname = models.CharField(max_length=255)
    unitslink = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Units'


class CV_ResultType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CV_ResultType'


class CV_Medium(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CV_Medium'


class CV_Status(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CV_Status'


class ProcessingLevels(models.Model):
    processinglevelid = models.AutoField(primary_key=True)
    processinglevelcode = models.CharField(unique=True, max_length=50)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    explanation = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ProcessingLevels'


class CV_TaxonomicClassifierType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CV_TaxonomicClassifierType'


class TaxonomicClassifiers(models.Model):
    taxonomicclassifierid = models.AutoField(primary_key=True)
    taxonomicclassifiertypecv = models.ForeignKey(CV_TaxonomicClassifierType, models.DO_NOTHING,
                                                  db_column='taxonomicclassifiertypecv')
    taxonomicclassifiername = models.CharField(max_length=255)
    taxonomicclassifiercommonname = models.CharField(
        max_length=255, blank=True, null=True)
    taxonomicclassifierdescription = models.CharField(
        max_length=5000, blank=True, null=True)
    parenttaxonomicclassifierid = models.ForeignKey('self', models.DO_NOTHING, db_column='parenttaxonomicclassifierid',
                                                    blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TaxonomicClassifiers'


class SpatialReferences(models.Model):
    spatialreferenceid = models.AutoField(primary_key=True)
    srscode = models.CharField(max_length=50, blank=True, null=True)
    srsname = models.CharField(max_length=255)
    srsdescription = models.CharField(max_length=5000, blank=True, null=True)
    srslink = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'SpatialReferences'


class Results(models.Model):
    resultid = models.BigAutoField(primary_key=True)
    resultuuid = models.UUIDField()
    featureactionid = models.ForeignKey(
        FeatureActions, models.DO_NOTHING, db_column='featureactionid')
    resulttypecv = models.ForeignKey(
        CV_ResultType, models.DO_NOTHING, db_column='resulttypecv')
    variableid = models.ForeignKey(
        Variables, models.DO_NOTHING, db_column='variableid')
    unitsid = models.ForeignKey(Units, models.DO_NOTHING, db_column='unitsid')
    taxonomicclassifierid = models.ForeignKey(TaxonomicClassifiers, models.DO_NOTHING,
                                              db_column='taxonomicclassifierid', blank=True, null=True)
    processinglevelid = models.ForeignKey(
        ProcessingLevels, models.DO_NOTHING, db_column='processinglevelid')
    resultdatetime = models.DateTimeField(blank=True, null=True)
    resultdatetimeutcoffset = models.BigIntegerField(blank=True, null=True)
    validdatetime = models.DateTimeField(blank=True, null=True)
    validdatetimeutcoffset = models.BigIntegerField(blank=True, null=True)
    statuscv = models.ForeignKey(
        CV_Status, models.DO_NOTHING, db_column='statuscv', blank=True, null=True)
    sampledmediumcv = models.ForeignKey(
        CV_Medium, models.DO_NOTHING, db_column='sampledmediumcv')
    valuecount = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'Results'


class CV_CensorCode(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CV_CensorCode'


class CV_DataQualityType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CV_DataQualityType'


class CV_QualityCode(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CV_QualityCode'


class CV_AggregationStatistic(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=5000, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sourcevocabularyuri = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CV_AggregationStatistic'


class MeasurementResults(models.Model):
    resultid = models.OneToOneField(
        Results, models.DO_NOTHING, db_column='resultid', primary_key=True)
    xlocation = models.FloatField(blank=True, null=True)
    xlocationunitsid = models.ForeignKey(Units, models.DO_NOTHING, db_column='xlocationunitsid', blank=True,
                                         null=True, related_name='xlocationunits')
    ylocation = models.FloatField(blank=True, null=True)
    ylocationunitsid = models.ForeignKey(Units, models.DO_NOTHING, db_column='ylocationunitsid', blank=True,
                                         null=True, related_name='ylocationunits')
    zlocation = models.FloatField(blank=True, null=True)
    zlocationunitsid = models.ForeignKey(Units, models.DO_NOTHING, db_column='zlocationunitsid', blank=True,
                                         null=True, related_name='zlocationunits')
    spatialreferenceid = models.ForeignKey(SpatialReferences, models.DO_NOTHING, db_column='spatialreferenceid',
                                           blank=True, null=True)
    censorcodecv = models.ForeignKey(
        CV_CensorCode, models.DO_NOTHING, db_column='censorcodecv')
    qualitycodecv = models.ForeignKey(
        CV_QualityCode, models.DO_NOTHING, db_column='qualitycodecv')
    aggregationstatisticcv = models.ForeignKey(CV_AggregationStatistic, models.DO_NOTHING,
                                               db_column='aggregationstatisticcv')
    timeaggregationinterval = models.FloatField()
    timeaggregationintervalunitsid = models.ForeignKey(Units, models.DO_NOTHING,
                                                       db_column='timeaggregationintervalunitsid',
                                                       related_name='timeaggregationintervalunits')

    class Meta:
        managed = True
        db_table = 'MeasurementResults'


class MeasurementResultValues(models.Model):
    valueid = models.BigAutoField(primary_key=True)
    resultid = models.ForeignKey(
        MeasurementResults, models.DO_NOTHING, db_column='resultid')
    datavalue = models.FloatField()
    valuedatetime = models.DateTimeField()
    valuedatetimeutcoffset = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'MeasurementResultValues'
        unique_together = (
            ('resultid', 'datavalue', 'valuedatetime', 'valuedatetimeutcoffset'),)


class TimeSeriesResults(models.Model):
    resultid = models.OneToOneField(
        Results, models.DO_NOTHING, db_column='resultid', primary_key=True)
    xlocation = models.FloatField(blank=True, null=True)
    xlocationunitsid = models.ForeignKey(Units, models.DO_NOTHING, db_column='xlocationunitsid',
                                         related_name="tsr_xlocationunits", blank=True, null=True)
    ylocation = models.FloatField(blank=True, null=True)
    ylocationunitsid = models.ForeignKey(Units, models.DO_NOTHING, db_column='ylocationunitsid',
                                         related_name="tsr_ylocationunits", blank=True, null=True)
    zlocation = models.FloatField(blank=True, null=True)
    zlocationunitsid = models.ForeignKey(Units, models.DO_NOTHING, db_column='zlocationunitsid',
                                         related_name="tsr_zlocationunits", blank=True, null=True)
    spatialreferenceid = models.ForeignKey(SpatialReferences, models.DO_NOTHING, db_column='spatialreferenceid',
                                           blank=True, null=True)
    intendedtimespacing = models.FloatField(blank=True, null=True)
    intendedtimespacingunitsid = models.ForeignKey(Units, models.DO_NOTHING, db_column='intendedtimespacingunitsid',
                                                   related_name="tsr_intendedtimespacingunits", blank=True, null=True)
    aggregationstatisticcv = models.ForeignKey(CV_AggregationStatistic, models.DO_NOTHING,
                                               db_column='aggregationstatisticcv')

    class Meta:
        managed = True
        db_table = 'TimeSeriesResults'


class TimeSeriesResultValues(models.Model):
    valueid = models.BigAutoField(primary_key=True)
    resultid = models.ForeignKey(
        TimeSeriesResults, models.DO_NOTHING, db_column='resultid')
    datavalue = models.FloatField()
    valuedatetime = models.DateTimeField()
    valuedatetimeutcoffset = models.IntegerField()
    censorcodecv = models.ForeignKey(
        CV_CensorCode, models.DO_NOTHING, db_column='censorcodecv')
    qualitycodecv = models.ForeignKey(
        CV_QualityCode, models.DO_NOTHING, db_column='qualitycodecv')
    timeaggregationinterval = models.FloatField()
    timeaggregationintervalunitsid = models.ForeignKey(Units, models.DO_NOTHING,
                                                       db_column='timeaggregationintervalunitsid')

    class Meta:
        managed = True
        db_table = 'TimeSeriesResultValues'
        unique_together = (('resultid', 'datavalue', 'valuedatetime', 'valuedatetimeutcoffset', 'censorcodecv',
                            'qualitycodecv', 'timeaggregationinterval', 'timeaggregationintervalunitsid'),)


class Sites(models.Model):
    samplingfeatureid = models.OneToOneField(
        SamplingFeatures, models.DO_NOTHING, db_column='samplingfeatureid', primary_key=True)
    sitetypecv = models.ForeignKey(
        CV_SiteType, models.DO_NOTHING, db_column='sitetypecv')
    latitude = models.FloatField()
    longitude = models.FloatField()
    spatialreferenceid = models.ForeignKey(
        'Spatialreferences', models.DO_NOTHING, db_column='spatialreferenceid')

    class Meta:
        managed = True
        db_table = 'Sites'
