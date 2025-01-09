const express = require("express");
const router = express.Router();
const { pool } = require("../config/db.config");

// Ruta para crear un almacén
router.post("/almacenes", async (req, res) => {
    const { nombre, direccion, capacidad } = req.body;
    try {
        const result = await pool
            .request()
            .input("nombre", nombre)
            .input("direccion", direccion)
            .input("capacidad", capacidad)
            .query(
                "INSERT INTO Almacenes (nombre, direccion, capacidad) VALUES (@nombre, @direccion, @capacidad)"
            );
        res.status(201).json({ message: "Almacén creado exitosamente", result });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

module.exports = router;
