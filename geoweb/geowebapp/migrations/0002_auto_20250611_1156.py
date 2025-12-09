from django.db import migrations

import csv
from pathlib import Path


cv_files_path = {"CV_SamplingFeatureType": "static/data/odm2cv/samplingfeaturetype.csv",
                  "CV_SamplingFeatureGeoType": "static/data/odm2cv/samplingfeaturegeotype.csv",
                  "CV_ElevationDatum": "static/data/odm2cv/elevationdatum.csv",
                  "CV_VariableType": "static/data/odm2cv/variabletype.csv",
                  "CV_UnitsType": "static/data/odm2cv/unitstype.csv",
                  "CV_VariableName": "static/data/odm2cv/variablename.csv",
                  "CV_RelationshipType": "static/data/odm2cv/relationshiptype.csv",
                  "CV_Medium": "static/data/odm2cv/medium.csv",
                  "CV_OrganizationType": "static/data/odm2cv/organizationtype.csv",
                  "CV_Speciation": "static/data/odm2cv/speciation.csv",
                  "CV_Status": "static/data/odm2cv/status.csv",
                  "CV_TaxonomicClassifierType": "static/data/odm2cv/taxonomicclassifiertype.csv",
                  "CV_ActionType": "static/data/odm2cv/actiontype.csv",
                  "CV_AggregationStatistic": "static/data/odm2cv/aggregationstatistic.csv",
                  "CV_QualityCode": "static/data/odm2cv/qualitycode.csv",
                  "CV_CensorCode": "static/data/odm2cv/censorcode.csv",
                  "CV_ResultType": "static/data/odm2cv/resulttype.csv",
                  "CV_MethodType": "static/data/odm2cv/methodtype.csv",
                  "CV_SiteType": "static/data/odm2cv/sitetype.csv",
                  "CV_DataQualityType": "static/data/odm2cv/dataqualitytype.csv",
                }


def load_cvs(apps, schema_editor):
    for model_name, file_path in cv_files_path.items():
        model = apps.get_model('geowebapp', model_name)
        full_file_path = Path(__file__).resolve().parent.parent / file_path
        with open(full_file_path, newline='\n', encoding="utf8") as csvfile:
            cvs = csv.reader(csvfile, delimiter=',')
            next(cvs)
            for cv in cvs:
                term, name, definition, category, sourcevocabularyuri, _, _ = cv
                model(term=term, name=name,
                      definition=definition, category=category,
                      sourcevocabularyuri=sourcevocabularyuri
                    ).save()


class Migration(migrations.Migration):

    dependencies = [
        ("geowebapp", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(load_cvs)
    ]

