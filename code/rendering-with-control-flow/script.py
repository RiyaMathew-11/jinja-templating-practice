from jinja2 import Environment, FileSystemLoader


names = [
    { 'name': 'John', 'age': 18},
    { 'name': 'Martha', 'age': 15},
    { 'name': 'Tim', 'age': 25},
]
environment = Environment(loader=FileSystemLoader('code/rendering-with-control-flow/templates'))

#Rendering Text Messages with if statements

template = environment.get_template('message.txt')

for name in names:
    filename = 'code/rendering-with-control-flow/messages/' + name['name'] + '.txt'
    content = template.render(name)
    
    with open(filename, mode = 'w', encoding = 'utf-8') as messagefile:
        messagefile.write(content)
        print('Wrote', filename)
        
        
#Rendering HTML with loops

render_file = "code/rendering-with-control-flow/messages/age_data_render.html"
render_template = environment.get_template('age_data.html')

context = { "names": names }

with open(render_file, mode = 'w', encoding = 'utf-8') as render_file:
    render_file.write(render_template.render(context))
    print('Wrote render file for', render_template)

