## Operadores AND y OR -- En el caso del AND, evalua que las dos condiciones se cumplan
#                      -- En el caso de OR, evalua que al menos una condiciones se cumpla

usuario_logueado = True
usuario_admin =True

if usuario_logueado and usuario_admin:
    print("Usuario Adminsitrador")
elif usuario_logueado:
    print("Acceso de Usuario")    
else:
    print("Debe Iniciar Sesion")    
    
    


