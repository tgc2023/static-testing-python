# Testing estático

 El objetivo de este repositorio es poder entender la base de cómo las herramientas de análisis estático están implementadas. 
 
 Se crearon archivos con el objetivo de crear reglas de revisión de código fuente automática y personalizada. Reglas básicas implementadas:
 
 <img width="844" alt="image" src="https://user-images.githubusercontent.com/111657504/233803920-eb463c87-8069-4d72-91f0-3af565ad2ae9.png">
 
 Además de transformaciones automáticas de código fuente, útiles para auto reparar defectos. Transformaciones básicas implementadas:
 
 <img width="760" alt="image" src="https://user-images.githubusercontent.com/111657504/233803946-8eb8f25d-054e-4f1f-acb7-419c23c83dce.png">

 
 
 # Ejecución
  - Para levantar warnings asociadas a los archivos de código en la carpeta input-code: 
    - python analyze.py
  - Para realizar transformaciones asociadas a los archivos de código en la carpeta input-code:
    - python transform.py
    - el comando anterior creará los nuevos archivos transformados dentro de la carpeta transformed-code
 
 
