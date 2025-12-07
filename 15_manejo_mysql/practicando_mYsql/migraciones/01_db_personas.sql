DROP DATABASE IF EXISTS personas_db;

-- 2. Crea la nueva base de datos
CREATE DATABASE personas_db;

-- 3. Selecciona la base de datos para su uso
USE personas_db;

-- 4. Crea la tabla 'personas'
CREATE TABLE personas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    edad INT
);

