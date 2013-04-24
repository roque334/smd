# -*- coding: utf-8 -*-
from sqlalchemy import *
db = create_engine('postgres://postgres:postgres@localhost:5432/db_fundacion')

db.echo = True
db.execute('DROP TABLE IF EXISTS donante, monetaria, mobiliaria, especie;')
metadata = MetaData(db)

donante = Table('donante', metadata,
                Column ('donante_id', String(12), primary_key = True),
                Column ('razon', String(50), nullable = False),
                Column ('tipo', String(8), nullable = False),
                Column ('direccion', String(60), nullable = False),
                Column ('telefono', String(12), nullable = False),
                CheckConstraint('tipo=\'Natural\' OR tipo=\'Juridico\'', name='dom_tipo'),
                CheckConstraint('(tipo=\'Natural\' AND (donante_id~\'^V-[0-9]{8}$\' OR donante_id~\'^E-[0-9]{8}\')) OR (tipo=\'Juridico\' AND (donante_id~\'^J-[0-9]{8}-[0-9]$\'))', name='dom_donante_id'),
                CheckConstraint('telefono~\'^0212-[0-9]{7}\' OR telefono~\'04(1|2)(2|4|6)-[0-9]{7}\'', name='dom_telefono')
                )

monetaria = Table('monetaria', metadata,
                Column ('monetaria_id',Integer(unsigned=True, zerofill=True), Sequence('monetaria_id_seq',start=1, increment=1,optional=True), primary_key = True),
                Column ('nro', String(15), nullable = True),
                Column ('tipo_op', CHAR, nullable = False),
                Column ('monto', Float, nullable = False),
                Column ('fecha', Date, nullable = False),
                Column ('donante_id', String(12), ForeignKey('donante.donante_id')),
                CheckConstraint('(tipo_op=\'E\' AND nro is null) OR ((tipo_op=\'C\' OR tipo_op=\'T\' OR tipo_op=\'D\') AND nro is not null)', name='dom_tipo_op'),
                CheckConstraint('monto>0.0', name='dom_monto'),
                CheckConstraint('(donante_id~\'^V-[0-9]{8}$\' OR donante_id~\'^E-[0-9]{8}\' OR donante_id~\'^J-[0-9]{8}-[0-9]$\')', name='dom_donante_id')
                )

mobiliaria = Table('mobiliaria', metadata,
                Column ('mobiliaria_id',Integer(unsigned=True, zerofill=True), Sequence('mobiliaria_id_seq', start=1, increment=1,optional=True), primary_key = True),
                Column ('concepto', String(30), nullable = False),
                Column ('cant', Float, nullable = False),
                Column ('fecha', Date, nullable = False),
                Column ('donante_id', String(12), ForeignKey('donante.donante_id')),
                CheckConstraint('cant>0.0', name='dom_cant'),
                CheckConstraint('(donante_id~\'^V-[0-9]{8}$\' OR donante_id~\'^E-[0-9]{8}\' OR donante_id~\'^J-[0-9]{8}-[0-9]$\')', name='dom_donante_id')

                )

especie = Table('especie', metadata,
                Column ('especie_id',Integer(unsigned=True, zerofill=True), Sequence('especie_id_seq',start=1,increment=1,optional=True), primary_key = True),
                Column ('concepto', String(30), nullable = False),
                Column ('cant', Float, nullable = False),
                Column ('fecha', Date, nullable = False),
                Column ('donante_id', String(12), ForeignKey('donante.donante_id')),
                CheckConstraint('cant>0.0', name='dom_cant'),
                CheckConstraint('(donante_id~\'^V-[0-9]{8}$\' OR donante_id~\'^E-[0-9]{8}\' OR donante_id~\'^J-[0-9]{8}-[0-9]$\')', name='dom_donante_id')

                )

metadata.create_all(db)

ins= donante.insert().values(donante_id='V-20028330', razon='Roque Contreras', tipo='Natural', direccion='Caracas, El Marques', telefono='0412-2802888')
db.execute(ins)

ins = mobiliaria.insert().values(concepto='Puerta', cant = 2, fecha='2012-02-20', donante_id='V-20028330')
ins.compile().params
db.execute(ins)

ins = especie.insert().values(concepto='Detergente', cant = 20, fecha='2013-04-15', donante_id='V-20028330')
ins.compile().params
db.execute(ins)

ins = monetaria.insert().values(nro='000123', monto = 100000, tipo_op= 'C', fecha='2013-04-15', donante_id='V-20028330')
ins.compile().params
db.execute(ins)
