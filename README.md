# Godot-REST_server

Demostración del uso de una API REST como servidor y Godot para cliente.

Este repositorio corresponde al servidor. Para el lado del cliente consulte el siguiente repositorio.

Puedes usar [pipvenv](https://pipenv.pypa.io/en/latest/) para facilitar su instalción.

## Caracteristicas

- Permite el inicio de sesion con esquema usuario / contraseña. Posterior intercambia una clave termporal dinamica para futuras consultas
- El clientes es capas de reconocer que su clave dinamica caduco y solicita una nueva.
- Se muestra graficamente la clave dinamica y su tiempo de vida.
