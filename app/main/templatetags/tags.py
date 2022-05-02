from django import template
register = template.Library()


@register.simple_tag
def format_current_url_with_lang_code(request, language_code, curren_lang_code):
    return request.path.replace(curren_lang_code, language_code)
