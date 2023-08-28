import streamlit as st

# Funciones de conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

st.title("Conversor Universal")

categorias = [
    "Temperatura",
    "Longitud",
    "Peso/Masa",
    "Volumen",
    "Tiempo",
    "Velocidad",
    "Área",
    "Energía",
    "Presión",
    "Tamaño de Datos"
]

selected_category = st.selectbox("Selecciona una categoría:", categorias)

if selected_category == "Temperatura":
    opciones_temperatura = [
        "Celsius a Fahrenheit",
        "Fahrenheit a Celsius",
        "Celsius a Kelvin",
        "Kelvin a Celsius"
    ]
    selected_conversion = st.selectbox("Selecciona un tipo de conversión:", opciones_temperatura)

    if selected_conversion == "Celsius a Fahrenheit":
        celsius = st.number_input("Ingresa la temperatura en Celsius:", value=0.0)
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.write(f"{celsius} Celsius equivale a {fahrenheit} Fahrenheit")

    elif selected_conversion == "Fahrenheit a Celsius":
        fahrenheit = st.number_input("Ingresa la temperatura en Fahrenheit:", value=32.0)
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.write(f"{fahrenheit} Fahrenheit equivale a {celsius} Celsius")

    elif selected_conversion == "Celsius a Kelvin":
        celsius = st.number_input("Ingresa la temperatura en Celsius:", value=0.0)
        kelvin = celsius_to_kelvin(celsius)
        st.write(f"{celsius} Celsius equivale a {kelvin} Kelvin")

    elif selected_conversion == "Kelvin a Celsius":
        kelvin = st.number_input("Ingresa la temperatura en Kelvin:", value=273.15)
        celsius = kelvin_to_celsius(kelvin)
        st.write(f"{kelvin} Kelvin equivale a {celsius} Celsius")

elif selected_category == "Longitud":
    opciones_longitud = [
        "Pies a Metros",
        "Metros a Pies",
        "Pulgadas a Centímetros",
        "Centímetros a Pulgadas"
    ]
    selected_conversion = st.selectbox("Selecciona un tipo de conversión:", opciones_longitud)

    if selected_conversion == "Pies a Metros":
        pies = st.number_input("Ingresa la longitud en Pies:", value=0.0)
        metros = pies * 0.3048
        st.write(f"{pies} Pies equivale a {metros} Metros")

    elif selected_conversion == "Metros a Pies":
        metros = st.number_input("Ingresa la longitud en Metros:", value=0.0)
        pies = metros / 0.3048
        st.write(f"{metros} Metros equivale a {pies} Pies")

    elif selected_conversion == "Pulgadas a Centímetros":
        pulgadas = st.number_input("Ingresa la longitud en Pulgadas:", value=0.0)
        centimetros = pulgadas * 2.54
        st.write(f"{pulgadas} Pulgadas equivale a {centimetros} Centímetros")

    elif selected_conversion == "Centímetros a Pulgadas":
        centimetros = st.number_input("Ingresa la longitud en Centímetros:", value=0.0)
        pulgadas = centimetros / 2.54
        st.write(f"{centimetros} Centímetros equivale a {pulgadas} Pulgadas")

elif selected_category == "Peso/Masa":
    opciones_peso_masa = [
        "Libras a Kilogramos",
        "Kilogramos a Libras",
        "Onzas a Gramos",
        "Gramos a Onzas"
    ]
    selected_conversion = st.selectbox("Selecciona un tipo de conversión:", opciones_peso_masa)

    if selected_conversion == "Libras a Kilogramos":
        libras = st.number_input("Ingresa el peso en Libras:", value=0.0)
        kilogramos = libras * 0.453592
        st.write(f"{libras} Libras equivale a {kilogramos} Kilogramos")

    elif selected_conversion == "Kilogramos a Libras":
        kilogramos = st.number_input("Ingresa el peso en Kilogramos:", value=0.0)
        libras = kilogramos / 0.453592
        st.write(f"{kilogramos} Kilogramos equivale a {libras} Libras")

    elif selected_conversion == "Onzas a Gramos":
        onzas = st.number_input("Ingresa el peso en Onzas:", value=0.0)
        gramos = onzas * 28.3495
        st.write(f"{onzas} Onzas equivale a {gramos} Gramos")

    elif selected_conversion == "Gramos a Onzas":
        gramos = st.number_input("Ingresa el peso en Gramos:", value=0.0)
        onzas = gramos / 28.3495
        st.write(f"{gramos} Gramos equivale a {onzas} Onzas")

elif selected_category == "Volumen":
    opciones_volumen = [
        "Galones a Litros",
        "Litros a Galones",
        "Pulgadas cúbicas a Centímetros cúbicos",
        "Centímetros cúbicos a Pulgadas cúbicas"
    ]
    selected_conversion = st.selectbox("Selecciona un tipo de conversión:", opciones_volumen)

    if selected_conversion == "Galones a Litros":
        galones = st.number_input("Ingresa el volumen en Galones:", value=0.0)
        litros = galones * 3.78541
        st.write(f"{galones} Galones equivale a {litros} Litros")

    elif selected_conversion == "Litros a Galones":
        litros = st.number_input("Ingresa el volumen en Litros:", value=0.0)
        galones = litros / 3.78541
        st.write(f"{litros} Litros equivale a {galones} Galones")

    elif selected_conversion == "Pulgadas cúbicas a Centímetros cúbicos":
        pulgadas_cubicas = st.number_input("Ingresa el volumen en Pulgadas cúbicas:", value=0.0)
        cm_cubicos = pulgadas_cubicas * 16.3871
        st.write(f"{pulgadas_cubicas} Pulgadas cúbicas equivale a {cm_cubicos} Centímetros cúbicos")

    elif selected_conversion == "Centímetros cúbicos a Pulgadas cúbicas":
        cm_cubicos = st.number_input("Ingresa el volumen en Centímetros cúbicos:", value=0.0)
        pulgadas_cubicas = cm_cubicos / 16.3871
        st.write(f"{cm_cubicos} Centímetros cúbicos equivale a {pulgadas_cubicas} Pulgadas cúbicas")

elif selected_category == "Tiempo":
    opciones_tiempo = [
        "Horas a Minutos",
        "Minutos a Segundos",
        "Días a Horas",
        "Semanas a Días"
    ]
    selected_conversion = st.selectbox("Selecciona un tipo de conversión:", opciones_tiempo)

    if selected_conversion == "Horas a Minutos":
        horas = st.number_input("Ingresa la cantidad de Horas:", value=0.0)
        minutos = horas * 60
        st.write(f"{horas} Horas equivale a {minutos} Minutos")

    elif selected_conversion == "Minutos a Segundos":
        minutos = st.number_input("Ingresa la cantidad de Minutos:", value=0.0)
        segundos = minutos * 60
        st.write(f"{minutos} Minutos equivale a {segundos} Segundos")

elif selected_category == "Velocidad":
    opciones_velocidad = [
        "Millas por hora a Kilómetros por hora",
        "Kilómetros por hora a Metros por segundo",
        "Nudos a Millas por hora",
        "Metros por segundo a Pies por segundo"
    ]
    selected_conversion = st.selectbox("Selecciona un tipo de conversión:", opciones_velocidad)

    if selected_conversion == "Millas por hora a Kilómetros por hora":
        mph = st.number_input("Ingresa la velocidad en Millas por hora:", value=0.0)
        kph = mph * 1.60934
        st.write(f"{mph} Millas por hora equivale a {kph} Kilómetros por hora")

    elif selected_conversion == "Kilómetros por hora a Metros por segundo":
        kph = st.number_input("Ingresa la velocidad en Kilómetros por hora:", value=0.0)
        mps = kph * 0.277778
        st.write(f"{kph} Kilómetros por hora equivale a {mps} Metros por segundo")

elif selected_category == "Área":
    opciones_area = [
        "Metros cuadrados a Pies cuadrados",
        "Pies cuadrados a Metros cuadrados",
        "Kilómetros cuadrados a Millas cuadradas",
        "Millas cuadradas a Kilómetros cuadrados"
    ]
    selected_conversion = st.selectbox("Selecciona un tipo de conversión:", opciones_area)

    if selected_conversion == "Metros cuadrados a Pies cuadrados":
        metros_cuadrados = st.number_input("Ingresa el área en Metros cuadrados:", value=0.0)
        pies_cuadrados = metros_cuadrados * 10.7639
        st.write(f"{metros_cuadrados} Metros cuadrados equivale a {pies_cuadrados} Pies cuadrados")

    elif selected_conversion == "Pies cuadrados a Metros cuadrados":
        pies_cuadrados = st.number_input("Ingresa el área en Pies cuadrados:", value=0.0)
        metros_cuadrados = pies_cuadrados / 10.7639
        st.write(f"{pies_cuadrados} Pies cuadrados equivale a {metros_cuadrados} Metros cuadrados")

elif selected_category == "Energía":
    opciones_energia = [
        "Julios a Calorías",
        "Calorías a Kilojulios",
        "Kilovatios-hora a Megajulios",
        "Megajulios a Kilovatios-hora"
    ]
    selected_conversion = st.selectbox("Selecciona un tipo de conversión:", opciones_energia)

    if selected_conversion == "Julios a Calorías":
        julios = st.number_input("Ingresa la cantidad de Julios:", value=0.0)
        calorias = julios * 0.239006
        st.write(f"{julios} Julios equivale a {calorias} Calorías")

    elif selected_conversion == "Calorías a Kilojulios":
        calorias = st.number_input("Ingresa la cantidad de Calorías:", value=0.0)
        kilojulios = calorias / 0.239006
        st.write(f"{calorias} Calorías equivale a {kilojulios} Kilojulios")

elif selected_category == "Presión":
    opciones_presion = [
        "Pascales a Atmósferas",
        "Atmósferas a Pascales",
        "Barras a Libras por pulgada cuadrada",
        "Libras por pulgada cuadrada a Bares"
    ]
    selected_conversion = st.selectbox("Selecciona un tipo de conversión:", opciones_presion)

    if selected_conversion == "Pascales a Atmósferas":
        pascales = st.number_input("Ingresa la presión en Pascales:", value=0.0)
        atmosferas = pascales * 0.00000986923
        st.write(f"{pascales} Pascales equivale a {atmosferas} Atmósferas")

    elif selected_conversion == "Atmósferas a Pascales":
        atmosferas = st.number_input("Ingresa la presión en Atmósferas:", value=0.0)
        pascales = atmosferas / 0.00000986923
        st.write(f"{atmosferas} Atmósferas equivale a {pascales} Pascales")

elif selected_category == "Tamaño de Datos":
    opciones_tamano_datos = [
        "Megabytes a Gigabytes",
        "Gigabytes a Terabytes",
        "Kilobytes a Megabytes",
        "Terabytes a Petabytes"
    ]
    selected_conversion = st.selectbox("Selecciona un tipo de conversión:", opciones_tamano_datos)

    if selected_conversion == "Megabytes a Gigabytes":
        megabytes = st.number_input("Ingresa la cantidad en Megabytes:", value=0.0)
        gigabytes = megabytes / 1024
        st.write(f"{megabytes} Megabytes equivale a {gigabytes} Gigabytes")

    elif selected_conversion == "Gigabytes a Terabytes":
        gigabytes = st.number_input("Ingresa la cantidad en Gigabytes:", value=0.0)
        terabytes = gigabytes / 1024
        st.write(f"{gigabytes} Gigabytes equivale a {terabytes} Terabytes")
