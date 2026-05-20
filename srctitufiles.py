import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def extraer_titulares():
    print("🚀 [CI/CD] Iniciando Extractor de Titulares en la Nube...")

    url = "https://www.marca.com/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        print(f"📡 Conectando con {url}...")
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            print("✅ Conexión exitosa. Procesando el HTML...")

            soup = BeautifulSoup(response.text, 'html.parser')

            titulares = soup.select(
                'header h2, .ue-c-cover-content__headline, h2.ue-c-cover-content__headline-custom'
            )

            fecha = datetime.now().strftime('%d/%m/%Y %H:%M')

            print(f"\n📰 TITULARES DESTACADOS DE HOY ({fecha})")
            print("=" * 60)

            contador = 0

            # Crear archivo TXT
            with open("titulares.txt", "w", encoding="utf-8") as archivo:

                archivo.write(f"TITULARES DESTACADOS ({fecha})\n")
                archivo.write("=" * 60 + "\n\n")

                for t in titulares:
                    texto = t.get_text().strip()

                    if texto and len(texto) > 10:
                        contador += 1

                        linea = f"{contador}. {texto}"

                        # Mostrar en consola
                        print(f"🔥 {linea}")

                        # Guardar en TXT
                        archivo.write(linea + "\n")

                    if contador >= 15:
                        break

            if contador == 0:
                print("⚠️ No se pudieron extraer titulares.")

            else:
                print("\n✅ Archivo 'titulares.txt' generado correctamente.")

            print("=" * 60)

        else:
            print(f"❌ Error al acceder a la web. Código: {response.status_code}")

    except Exception as e:
        print(f"❌ Ocurrió un error durante el scraping: {e}")


if __name__ == "__main__":
    extraer_titulares()
