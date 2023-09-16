# Experimentos de arquitectura - Proyecto final 1
## Equipo: ROCALEDA

### Integrantes
1. Camilo Sánchez
2. Daniela Castellanos
3. Cristian Toro
4. Roberto Parra


## Cómo ejecutar

1. Clonar el repositorio
2. Ejecutar `docker-compose build` en la raíz del proyecto
3. Ejecutar `docker-compose up` en la raíz del proyecto
  

## Cómo usar
1. El componente API Gateway se encontrará en el puerto 8000 de la máquina host
2. El componente Candidates se encontrará en el puerto 8001 de la máquina host
3. La base de datos se encontrará en el puerto 5432 de la máquina host

#### Ejecutando peticiones
1. Las peticiones deben realizarse al host `http://localhost:8000`
2. El único endpoint disponible sobre el microservicio de candidatos es `GET /candidate`
3. Este endpoint puede recibir ningún query param o el query param `soft_skills`, que puede aparecer varias veces en la request representando una lista de `soft_skills`
4. A continuación se muestra un ejemplo de respuesta de petición y su respectiva respuesta
   1. Request: `GET http://localhost:8000/candidate?soft_skills=1&soft_skills=2`
   2. Respuesta: 

    ```
      [
        {
            "document_number": "1018482325",
            "name": "Roberto",
            "cv_path": "url",
            "document_type": "Pasaporte",
            "id": 1
        },
        {
            "document_number": "1017222125",
            "name": "Daniela",
            "cv_path": "url",
            "document_type": "CC",
            "id": 2
        }
    ]
    ```
