from jinja2 import Template

#for

temp8 = '''
<ul>
{% for elem in elems -%}
<li>{{loop.index}} - {{ elem }}</li>
{% endfor -%}
</ul>
'''
print(Template(temp8).render(elems=["Amarillo", "Verde", "Rojo"]))

#if

temp9='''
{% if elems %}
<ul>
{% for elem in elems -%}
	{% if elem is divisibleby 2 -%}
		<li>{{elem}} es divisible por 2.</li>
	{% else -%}
		<li>{{elem}} no es divisible por 2.</li>
	{% endif -%}
{% endfor -%}
</ul>
{% endif %}
'''
print(Template(temp9).render(elems=[1,2,3,4,5,6]))