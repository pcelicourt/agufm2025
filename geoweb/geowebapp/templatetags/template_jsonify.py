import json

from django import template

register = template.Library()

from ..models import SamplingFeatures


@register.simple_tag
def sensors_count():
      return SamplingFeatures.objects.filter(samplingfeaturecode__istartswith='CAF').count()

@register.filter(name='jsonify')
def jsonify(data):
    if isinstance(data, dict):
        return data
    else:
        return json.loads(data)

