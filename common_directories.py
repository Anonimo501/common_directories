import requests
from bs4 import BeautifulSoup

def buscar_directorios():
    software = input("Introduce el nombre del software: ")
    query = f"{software} common web directories"
    response = requests.get(f"https://www.google.com/search?q={query}")
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("div", class_="r")

    print(f"Resultados de la búsqueda para '{query}':")
    for result in results:
        link = result.find("a")
        print(link.text)

    if software.lower() == "wordpress":
        common_directories = [
            "/wp-admin/",
            "/wp-content/",
            "/wp-includes/",
            "/wp-json/",
            "/xmlrpc.php",
            "/wp-plugins/",
            "/wp-themes/",
            "/wp-themes/"
        ]

        print("\nDirectorios comunes de WordPress:")
        for directory in common_directories:
            print(directory)

    elif software.lower() == "joomla":
        common_directories = [
            "/administrator/",
            "/components/",
            "/images/",
            "/includes/",
            "/language/",
            "/media/",
            "/modules/",
            "/plugins/",
            "/templates/",
            "/cache/",
            "/layouts/",
            "/libraries/",
            "/tmp/",
            "/cli/",
            "/htaccess.txt/"
        ]

        print("\nDirectorios comunes de Joomla:")
        for directory in common_directories:
            print(directory)
    
    elif software.lower() == "apache":
        common_directories = [
            "/cgi-bin/",
            "/conf/",
            "/htdocs/",
            "/logs/",
            "/manual/",
            "/icons/"
        ]

        print("\nDirectorios comunes de Apache:")
        for directory in common_directories:
            print(directory)

    elif software.lower() == "nginx":
        common_directories = [
            "/conf/",
            "/html/",
            "/logs/",
            "/temp/",
            "/www/",
            "/ssl/",
            "/client_body_temp/"
        ]

        print("\nDirectorios comunes de Nginx:")
        for directory in common_directories:
            print(directory)

    elif software.lower() == "php":
        common_directories = [
            "/ext/",
            "/include/",
            "/lib/",
            "/manual/",
            "/tmp/",
            "/pear/"
        ]

        print("\nDirectorios comunes de PHP:")
        for directory in common_directories:
            print(directory)

    elif software.lower() == "ruby":
        common_directories = [
            "/app/",
            "/bin/",
            "/config/",
            "/db/",
            "/lib/",
            "/public/",
            "/test/",
            "/vendor/"
        ]

        print("\nDirectorios comunes de ruby on rails:")
        for directory in common_directories:
            print(directory)

    elif software.lower() == "django":
        common_directories = [
            "/manage.py/",
            "/media/",
            "/static/",
            "/templates/",
            "/app_name/",
            "/app_name/migrations/",
            "/app_name/templatetags/"
        ]

        print("\nDirectorios comunes de ruby on rails:")
        for directory in common_directories:
            print(directory)
    else:
        print("\nSoftware desconocido. No se encontraron resultados.")

if __name__ == "__main__":
    buscar_directorios()
