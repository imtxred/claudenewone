with open('/root/.claude/uploads/f65f0cab-92ee-59ef-9c6b-94a4c2e4666c/616ef878-ARhml.txt', 'r', encoding='utf-8') as f:
    c = f.read()

r = [
    # Publisher
    ('SaludInfo Argentina', 'SaludInfo Panamá'),

    # Title adjective
    ('el joven médico argentino', 'el joven médico panameño'),
    ('médico argentino', 'médico panameño'),

    # Doctor name — full forms first, then surname-only
    ('dr. Carlos Mendoza', 'dr. Eduardo Vargas'),
    ('Dr. Carlos Mendoza', 'Dr. Eduardo Vargas'),
    ('Carlos Mendoza', 'Eduardo Vargas'),
    ('dr. Mendoza', 'dr. Vargas'),
    ('Dr. Mendoza', 'Dr. Vargas'),

    # Places — most specific first
    ('llegamos a Luján, en la provincia de Buenos Aires',
     'llegamos a La Chorrera, en la provincia de Panamá Oeste'),
    ('asilo de Luján, Buenos Aires', 'asilo de La Chorrera'),
    ('clínica privada de Buenos Aires', 'clínica privada de Ciudad de Panamá'),
    ('asilo de Córdoba', 'asilo de David'),
    ('asilo de Rosario', 'asilo de Colón'),
    ('asilo de Mendoza', 'asilo de Santiago de Veraguas'),
    ('asilo de Mar del Plata', 'asilo de Las Tablas'),
    ('asilo de Tucumán', 'asilo de Chitré'),
    ('de la Patagonia a Jujuy, del sur al norte del país',
     'de Chiriquí a Bocas del Toro, del Pacífico al Atlántico'),

    # Country refs — specific before generic
    ('ciudadano argentino', 'ciudadano panameño'),
    ('de toda Argentina', 'de todo Panamá'),
    ('toda Argentina', 'todo Panamá'),
    ('en Argentina', 'en Panamá'),
    ('para Argentina', 'para Panamá'),
    ('Buenos Aires', 'Ciudad de Panamá'),
    ('Argentina', 'Panamá'),

    # Salary / currency
    ('1.500.000 pesos\n        argentinos mensuales', '2,500 dólares mensuales'),
    ('69800 ARS', '69.90 USD'),
    ('34900 ARS', '34.90 USD'),
    ('value="AR"', 'value="PA"'),

    # Commenters — last name first format
    ('García María', 'González María'),
    ('López Eva', 'Batista Eva'),
    ('Martínez Ana', 'Araúz Ana'),
    ('González Esteban', 'Chen Esteban'),
    ('Hernández Pedro', 'Herrera Pedro'),
    ('Ramírez Andrea', 'Sanjur Andrea'),
    ('Torres Judith', 'Barría Judith'),
    ('Flores Luis', 'Cedeño Luis'),
    ('Morales Catalina', 'Quintero Catalina'),
    ('Castillo Elizabeth', 'Domínguez Elizabeth'),
    ('Reyes José', 'Muñoz José'),
    ('Cruz Teodoro', 'Ábrego Teodoro'),
    ('Jiménez Ilda', 'Pimentel Ilda'),
    ('Sánchez Susana', 'Tejada Susana'),
    ('Vargas Gabriel', 'Valderrama Gabriel'),
]

for old, new in r:
    c = c.replace(old, new)

with open('/home/user/claudenewone/landing-example/landing-PA.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Done")
