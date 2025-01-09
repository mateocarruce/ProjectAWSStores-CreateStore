const sql = require("mssql");

const dbConfig = {
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    server: process.env.DB_SERVER,
    database: process.env.DB_NAME,
    options: {
        encrypt: true, // Si usas Azure o conexiones SSL
        trustServerCertificate: true, // Para desarrollo local
    },
};

const pool = new sql.ConnectionPool(dbConfig);
const connectDB = async () => {
    try {
        await pool.connect();
        console.log("Conexión a la base de datos exitosa");
    } catch (err) {
        console.error("Error al conectar con la base de datos", err);
    }
};

module.exports = { pool, connectDB };
