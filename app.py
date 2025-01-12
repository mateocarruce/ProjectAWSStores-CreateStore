import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_SERVER = os.getenv('DB_SERVER')
DB_NAME = os.getenv('DB_NAME')

# Verificar si las variables se cargaron correctamente
if not all([DB_USER, DB_PASSWORD, DB_SERVER, DB_NAME]):
    raise ValueError("Faltan variables de entorno en el archivo .env")

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de Almacén
class Almacen(db.Model):
    __tablename__ = 'Almacenes'  # Nombre de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    creado_en = db.Column(db.DateTime, default=text('GETDATE()'), nullable=False)

# Ruta para crear un almacén
@app.route('/almacenes', methods=['POST'])
def crear_almacen():
    try:
        datos = request.json
        nuevo_almacen = Almacen(
            nombre=datos['nombre'],
            direccion=datos['direccion'],
            capacidad=datos['capacidad']
        )
        db.session.add(nuevo_almacen)
        db.session.commit()
        return jsonify({'mensaje': 'Almacén creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para listar todos los almacenes
@app.route('/almacenes', methods=['GET'])
def listar_almacenes():
    try:
        almacenes = Almacen.query.all()
        resultado = [
            {'id': a.id, 'nombre': a.nombre, 'direccion': a.direccion, 'capacidad': a.capacidad}
            for a in almacenes
        ]
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para eliminar un almacén por ID
@app.route('/almacenes/<int:id>', methods=['DELETE'])
def eliminar_almacen(id):
    try:
        almacen = Almacen.query.get(id)
        if not almacen:
            return jsonify({'error': 'Almacén no encontrado'}), 404
        db.session.delete(almacen)
        db.session.commit()
        return jsonify({'mensaje': 'Almacén eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
