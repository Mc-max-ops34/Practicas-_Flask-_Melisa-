<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Calculadora de Rectángulo</title>
</head>
<body>
    <h2>Calculadora de Rectángulo</h2>
    
    <form method="POST" action="/">
        <label>Base: <input type="number" step="any" name="base" required></label><br><br>
        <label>Altura: <input type="number" step="any" name="altura" required></label><br><br>
        <button type="submit">Calcular</button>
    </form>

    {% if area is not none and perimetro is not none %}
        <h3>Resultados:</h3>
        <p>Área: {{ area }}</p>
        <p>Perímetro: {{ perimetro }}</p>
    {% endif %}
</body>
</html>