import fitz  # PyMuPDF

archivo_entrada = "catalogo_tarot_dragon11.pdf"
archivo_blindado = "Catalogo_Tarot_Dragon11_Protegido.pdf"

# 1. Abrimos el PDF original y creamos uno nuevo vacío
doc_origen = fitz.open(archivo_entrada)
doc_nuevo = fitz.open()

# 2. Convertimos cada página en imagen de alta definición (300 DPI)
for pagina in doc_origen:
    pix = pagina.get_pixmap(dpi=300)
    nueva_pag = doc_nuevo.new_page(width=pagina.rect.width, height=pagina.rect.height)
    nueva_pag.insert_image(pagina.rect, pixmap=pix)

# 3. Aplicamos cifrado deshabilitando permisos de copia y extracción
permisos = fitz.PDF_PERM_PRINT  # Solo permite ver e imprimir, prohíbe copiar
doc_nuevo.save(
    archivo_blindado,
    encryption=fitz.PDF_ENCRYPT_AES_256,
    owner_pw="Dragon11MasterKey!",
    permissions=permisos,
)

print(f"✔ ¡Listo! Se creó '{archivo_blindado}' 100% blindado contra copia y pega.")