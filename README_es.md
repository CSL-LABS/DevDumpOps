# DevDumpOps
🛠️ En construcción 🛠️

Herramienta Open Source para el Dump de información de plataformas DevOps, enfocado al abuso de Tokens, APIS y cuentas de servicio expuestas que nos permitan la consulta a estas herramientas de desarrollo; desde una perspectiva de seguridad es muy útil y conveniente poder reconstruir el código fuente, extraer archivos de configuración, datos de despliegue y la mayor información posible de estas plataforma, para posteriores procesos de intrusión. 

### Instalación 🔧
```
git clone https://github.com/CSL-LABS/DevDumpOps.git
cd DevDumpOps
```

### Uso
```
python DevDumpOps.py --help
```

### Target's
- **Sonarqube**
- otros ~~en construccion~~

## Actions
### Enumeration 📋
Realiza una enumeración de la configuración del servidor SonarQube, así como de los permisos, organizaciones, proyectos y componentes de código visisible con o sin credenciales. 
### Dump
Se descarga y almacena la totalidad de los componentes de código visibles: 
- all
    - Todo el código
- member 
    - El código enlazado a las credenciales (util para SonarCloud.io)
### Hack ~~en construccion~~
Permite la realización de ataques especificos sobre el target seleccionado: 
- Fuerza Bruta
- Creación de Tokens (backdoor)
- Creación de usuarios
- Entre otros. 

## Ejemplos de uso
- Enumeración sin utilizar credenciales: 
```
python DevDumpOps.py --sonarqube [target]
```

- Descarga de código de los proyectos publicos: 
```
python DevDumpOps.py --sonarqube --dump all [target]
```
![SonarCloud-token](images/02_sonarLocal_download_files.PNG)

- Enumeración utilizando credenciales:
```
python DevDumpOps.py --sonarqube -u admin -p admin [target]
```
![SonarCloud-token](images/02_sonarLocal_user.PNG)

- Descarga de código de los proyectos privados:
```
python DevDumpOps.py --sonarqube -u admin -p admin --dump member [target]
```

- Descarga de codigo en proyectos SonarCloud: 
```
python DevDumpOps.py --sonarqube -t [token] --dump member sonarcloud.io
```
![SonarCloud-token](images/01_sonarcloud_token.PNG)
## Resultados

Los resultados son almacenados por defecto en la carpeta /results/ o en la que se defina bajo la opcion --output, y se encuentra la siguiente informacion: 
- Configuracion SMTP, GITHUB, GITLAB Y SVN
- Usuarios identificados
- Proyectos visibles
- Codigo descargado
- Componentes de código
- WebHooks extraidos
- Tokens de Usuario

## Referencias
- https://csl.com.co/sonarqube-auditando-al-auditor-parte-i/
- https://csl.com.co/sonarqube-auditando-al-auditor-parte-ii/ 