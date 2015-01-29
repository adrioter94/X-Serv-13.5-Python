#!/usr/bin/python
fich = open("/etc/passwd", "r");
usuarios = fich.readlines();

dicc = {};
for usuario in usuarios:
    conf = usuario.split(':');
    username = conf[0];
    shell = conf[-1];
    dicc[username] = shell
    
print 'root: ' + dicc['root'];

try:
    print dicc['imaginario'];

except :
    print('La clave "imaginario" no existe\n');

print "Numero de usuarios: " + str(len(usuarios));
fich.close();
