from jinja2 import Environment, FileSystemLoader

names = [
    { 'recepient_name': 'John', 'sender_name': 'Jane'},
    { 'recepient_name': 'Martha', 'sender_name': 'Mary'},
]

environment = Environment(loader=FileSystemLoader('templates/'))
template = environment.get_template('message.txt')

for name in names:
    filename = 'messages/' + name['recepient_name'] + '.txt'
    content = template.render(name)
    
    with open(filename, mode = 'w', encoding = 'utf-8') as messagefile:
        messagefile.write(content)
        print('Wrote', filename)