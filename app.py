import os
from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# Función maestra para conectarse a Cloud SQL sin quemar contraseñas en el código
def obtener_conexion():
    return pymysql.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASS', ''),
        database=os.environ.get('DB_NAME', 'test_db')
    )

# Ruta original que ya probaste
@app.route('/', methods=['GET'])
def home():
    return jsonify({"mensaje": "¡Examen superado! API funcionando al 100."})

# Ruta nueva para probar la base de datos en el examen
@app.route('/db-test', methods=['GET'])
def test_db():
    try:
        # Intentamos abrir y cerrar la conexión para ver si los datos son correctos
        conexion = obtener_conexion()
        conexion.close()
        return jsonify({
            "estado": "Éxito", 
            "mensaje": "¡Conexión a Cloud SQL completamente operativa!"
        })
    except Exception as e:
        # Si falla, te dice exactamente por qué (ideal para debugear)
        return jsonify({
            "estado": "Error de conexión", 
            "detalle": str(e)
        }), 500

if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=puerto)