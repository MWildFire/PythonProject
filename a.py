import re


import re

html_code = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

# Регулярное выражение для извлечения ссылки из атрибута src
pattern = re.compile(r'<iframe.*?src="https://www.youtube.com/embed/(.*?)".*?>')


# Находим все соответствия в HTML коде
matches = re.findall(pattern, html_code)


print(matches[0])
