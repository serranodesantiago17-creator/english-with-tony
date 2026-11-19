# English with Tony — Guía para publicar el sitio gratis y contar visitas

El sitio completo está en **un solo archivo: `index.html`**. No necesita base de datos, servidor propio ni una computadora encendida: cualquier servicio de "hosting estático" lo sirve las 24 horas.

## ¿Se puede alojar en Google Drive?

No. Google Drive dejó de servir páginas web el 31 de agosto de 2016. Hoy, si abres el `index.html` desde Drive, solo verás el código o una vista previa, no el sitio funcionando.

## ¿Y en WordPress?

- **WordPress.com gratis:** no permite JavaScript. El sitio se vería, pero los ejercicios no se podrían corregir (que es lo más importante). Su contador de visitas sí es gratuito.
- **Planes de pago de WordPress.com** o un WordPress propio con hosting: sí funcionaría, pero ya tiene costo.

## Opción recomendada: GitHub Pages + GoatCounter (gratis)

### 1. Crear el contador de visitas (5 minutos)
1. Entra a https://www.goatcounter.com y elige **Sign up**.
2. En *Code* escribe un nombre corto, por ejemplo `englishwithtony`. Tu panel de estadísticas quedará en `https://englishwithtony.goatcounter.com`.
3. Abre `index.html` con un editor de texto (Bloc de notas, TextEdit en modo texto plano o VS Code), busca esta línea:
   ```
   const GOATCOUNTER_CODE = "";
   ```
   y escribe tu código entre las comillas:
   ```
   const GOATCOUNTER_CODE = "englishwithtony";
   ```
4. Guarda el archivo.

El contador registra cada visita y también qué tema abre cada persona (aparecen como `/#tema-3`, `/#simulacro`, etc.). GoatCounter es gratuito para sitios sin fines comerciales y no usa cookies, así que no necesitas aviso de cookies.

### 2. Publicar el sitio (10 minutos, todo desde el navegador)
1. Crea una cuenta gratuita en https://github.com.
2. Pulsa **New repository**. Nombre: `english-with-tony`. Márcalo como **Public** y pulsa **Create repository**.
3. Pulsa **uploading an existing file**, arrastra `index.html` y pulsa **Commit changes**.
4. Ve a **Settings → Pages**. En *Branch* elige `main` y la carpeta `/ (root)`, y pulsa **Save**.
5. En uno o dos minutos el sitio estará en:
   `https://TU-USUARIO.github.io/english-with-tony/`

Para actualizarlo, vuelve a subir el `index.html` modificado al mismo repositorio.

## Otras opciones gratuitas

- **Netlify Drop** (https://app.netlify.com/drop): arrastras la carpeta con `index.html` y obtienes un enlace al instante. Crea una cuenta gratuita para que el sitio se conserve. Usa GoatCounter para las visitas (las estadísticas propias de Netlify son de pago).
- **Google Sites** (lo más parecido a "tenerlo en Drive"): crea un sitio en https://sites.google.com, luego **Insertar → Insertar → Insertar código** y pega todo el contenido de `index.html`. Google Sites puede conectarse a Google Analytics en *Configuración → Análisis*. Ten en cuenta que el código insertado se muestra dentro de un recuadro; si el editor no acepta el código completo, publica primero en GitHub Pages e inserta la dirección del sitio con **Insertar → Por URL**.

## Dominio propio (opcional)
Si más adelante compras un dominio (por ejemplo `englishwithtony.com`), GitHub Pages permite conectarlo gratis en **Settings → Pages → Custom domain**.

## Imágenes
Las fotografías se cargan desde Wikimedia Commons con licencias libres. Los autores y licencias están en la sección **Créditos** del sitio. No hace falta descargarlas ni subirlas. Si alguna vez una foto no carga, el sitio muestra automáticamente un panel ilustrado con el nombre del lugar.

## Editar el contenido
Los textos y ejercicios están dentro de `index.html`, en la sección que empieza con `window.TEMAS = [`. Cada pregunta tiene:
- `q`: la pregunta (`___` marca el espacio en blanco; en Written Expression, las partes subrayadas van entre `[[ ]]`),
- `o`: las cuatro opciones,
- `a`: el número de la respuesta correcta (0 = primera opción, 1 = segunda…),
- `f`: la explicación de cada opción, en el mismo orden.

Las opciones se barajan automáticamente al mostrarse, así que la correcta puede ir siempre en la primera posición.

La carpeta `fuente/` contiene el mismo contenido en archivos separados por si prefieres editar ahí (`temas1.js` a `temas4.js` y `ampliacion.js`): después ejecuta `python3 build.py` para generar un nuevo `index.html`.
