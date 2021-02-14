import re
from random import randint
from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.simple_tag()
def random_num():
    return randint(1, 10)


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(content):
    code_list = re.findall(r'<pre class="(.*)"><code>', content, re.M)
    for code in code_list:
        content = re.sub(r'<pre class="(.*)"><code>',
                         '<pre class="(.*)"><div>'.format(code=code.lower()), content,
                         1)
    return content
