from django import template

register = template.Library()


@register.simple_tag
def query_transform(request, **kwargs):
    """usages: {% query_transform request page=1 %}"""
    updated = request.GET.copy()

    for k, v in kwargs.iteritems():
        updated[k] = v
        #print(k, v)

    # trash any pjax params, we never want to render those
    try:
        del updated['_pjax']
    except KeyError:
        pass

    return updated.urlencode()
