from django import template
#This is customise filter
register=template.Library()

@register.filter(name='cut')
#Creatinmg filter
def cut(value,arg):
    """
    This cuts out all value of arg from the String
    """
    return value.replace(arg,'')

#Registering the filter
#register.filter('cut',cut)
