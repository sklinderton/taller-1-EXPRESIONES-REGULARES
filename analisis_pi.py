import re

# Leer el contenido del archivo
with open('Pi125MDP.txt', 'r') as file:
    pi_decimal = file.read().strip()

# Preparar archivo de salida
with open('busqueda-pi.txt', 'w') as output_file:
    # 1. Todas las ocurrencias de "1415"
    pattern1 = r'1415'
    count1 = len(re.findall(pattern1, pi_decimal))
    output_file.write(f"1. Patrón: '{pattern1}' -> Ocurrencias: {count1}\n")
    
    # 2. "1415" seguida de un dígito impar
    pattern2 = r'1415[13579]'
    count2 = len(re.findall(pattern2, pi_decimal))
    output_file.write(f"2. Patrón: '{pattern2}' -> Ocurrencias: {count2}\n")
    
    # 3. 3 dígitos pares seguidos
    pattern3 = r'[02468]{3}'
    count3 = len(re.findall(pattern3, pi_decimal))
    output_file.write(f"3. Patrón: '{pattern3}' -> Ocurrencias: {count3}\n")
    
    # 4. 3 dígitos pares seguidos de un 9
    pattern4 = r'[02468]{3}9'
    count4 = len(re.findall(pattern4, pi_decimal))
    output_file.write(f"4. Patrón: '{pattern4}' -> Ocurrencias: {count4}\n")
    
    # 5. 3 dígitos pares seguidos de un dígito impar
    pattern5 = r'[02468]{3}[13579]'
    count5 = len(re.findall(pattern5, pi_decimal))
    output_file.write(f"5. Patrón: '{pattern5}' -> Ocurrencias: {count5}\n")
    
    # 6. 3 dígitos pares seguidos de 0 o 9
    pattern6 = r'[02468]{3}[09]'
    count6 = len(re.findall(pattern6, pi_decimal))
    output_file.write(f"6. Patrón: '{pattern6}' -> Ocurrencias: {count6}\n")
    
    # 7. 2 dígitos pares seguidos de 0, 1 o 3 dígitos impares
    pattern7 = r'[02468]{2}(?:[13579]|[13579]{3})?'
    count7 = len(re.findall(pattern7, pi_decimal))
    output_file.write(f"7. Patrón: '{pattern7}' -> Ocurrencias: {count7}\n")
    
    # 8. 2 dígitos impares seguidos de 0
    pattern8 = r'[13579]{2}0'
    count8 = len(re.findall(pattern8, pi_decimal))
    output_file.write(f"8. Patrón: '{pattern8}' -> Ocurrencias: {count8}\n")
    
    # 9. 1 dígito impar seguido de al menos 2 dígitos pares
    pattern9 = r'[13579][02468]{2,}'
    count9 = len(re.findall(pattern9, pi_decimal))
    output_file.write(f"9. Patrón: '{pattern9}' -> Ocurrencias: {count9}\n")
    
    # 10. 111, 113, 115, 117 o 119
    pattern10 = r'11[13579]'
    count10 = len(re.findall(pattern10, pi_decimal))
    output_file.write(f"10. Patrón: '{pattern10}' -> Ocurrencias: {count10}\n")
    
    # 11. 111, 113, 115, 117 o 119 seguidos de dígito par
    pattern11 = r'11[13579][02468]'
    count11 = len(re.findall(pattern11, pi_decimal))
    output_file.write(f"11. Patrón: '{pattern11}' -> Ocurrencias: {count11}\n")

print("Búsquedas de Pi guardadas en 'busqueda-pi.txt'")