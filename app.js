require("dotenv").config();
const express = require("express");
const bodyParser = require("body-parser");
const { connectDB } = require("./config/db.config");
const almacenesRoutes = require("./routes/almacenes.routes");

const app = express();
const PORT = process.env.PORT || 3001;

app.use(bodyParser.json());

// Rutas
app.use("/api", almacenesRoutes);

// Iniciar servidor y conectar a la base de datos
app.listen(PORT, async () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
    await connectDB();
});
