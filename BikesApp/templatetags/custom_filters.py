from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, "Unknown")  # Return "Unknown" if key is not found
