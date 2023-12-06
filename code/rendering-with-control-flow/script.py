from jinja2 import Environment, FileSystemLoader

names = [
    { 'name': 'John', 'age': 18},
    { 'name': 'Martha', 'age': 15},
    { 'name': 'Tim', 'age': 25},
]

environment = Environment(loader=FileSystemLoader('code/rendering-with-control-flow/templates'))
template = environment.get_template('message.txt')

for name in names:
    filename = 'code/rendering-with-control-flow/messages/' + name['name'] + '.txt'
    content = template.render(name)
    
    with open(filename, mode = 'w', encoding = 'utf-8') as messagefile:
        messagefile.write(content)
        print('Wrote', filename)