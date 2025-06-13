import re

# Leer el contenido del archivo
with open('quijote.txt', 'r', encoding='utf-8') as file:
    quijote = file.read()

# Preparar archivo de salida
with open('busqueda-quijote.txt', 'w', encoding='utf-8') as output_file:
    # 1. Cabeceras de capítulo
    pattern1 = r'(CAP[ÍI]TULO [A-Z]+\.? .*)'
    matches1 = re.findall(pattern1, quijote, re.IGNORECASE)
    output_file.write(f"1. Cabeceras de capítulo ({len(matches1)} encontradas):\n")
    for match in matches1:
        output_file.write(f"   - {match}\n")
    
    # 2. Uso de "y" con palabras adyacentes
    pattern2 = r'(\b\w+\b) y (\b\w+\b)'
    matches2 = re.findall(pattern2, quijote)
    output_file.write(f"\n2. Palabras alrededor de 'y' ({len(matches2)} encontradas):\n")
    for i, (prev, next_word) in enumerate(matches2[:10], 1):  # Mostrar primeras 10
        output_file.write(f"   Ejemplo {i}: '{prev} y {next_word}'\n")
    
    # 3. Sílabas pra-pre-pri-pro-pru + letra d
    pattern3 = r'pr[aeiou]d\w*'
    matches3 = re.findall(pattern3, quijote, re.IGNORECASE)
    unique_matches3 = set(matches3)
    output_file.write(f"\n3. Sílabas 'pr[a,e,i,o,u]d' ({len(unique_matches3)} únicas):\n")
    for word in sorted(unique_matches3)[:10]:  # Mostrar primeras 10 únicas
        output_file.write(f"   - {word}\n")
    
    # 4. Palabras distintas que empiezan con cra-cre-cri-cro-cru
    pattern4 = r'\b[cc]r[aeiou]\w*'
    matches4 = re.findall(pattern4, quijote, re.IGNORECASE)
    unique_matches4 = set(word.lower() for word in matches4)
    output_file.write(f"\n4. Palabras con 'cr[a,e,i,o,u]' ({len(unique_matches4)} únicas):\n")
    for word in sorted(unique_matches4)[:10]:  # Mostrar primeras 10 únicas
        output_file.write(f"   - {word}\n")
    
    # 5. Palabras que terminan en cho-cha-che-chi-chu
    pattern5 = r'\b\w+ch[aeiou]\b'
    matches5 = re.findall(pattern5, quijote, re.IGNORECASE)
    unique_matches5 = set(word.lower() for word in matches5)
    output_file.write(f"\n5. Palabras terminadas en 'ch[a,e,i,o,u]' ({len(unique_matches5)} únicas):\n")
    for word in sorted(unique_matches5)[:10]:  # Mostrar primeras 10 únicas
        output_file.write(f"   - {word}\n")

print("Búsquedas de El Quijote guardadas en 'busqueda-quijote.txt'")