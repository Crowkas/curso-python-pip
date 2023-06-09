import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return[1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hyperblog 2.0 es un blog del futuro</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <div id="container">
        <div id="cabecera">
            <img id="logo" src="../Exercises/imagenes/dragon.png"/>
            Hyperblog 
            <span id="tagline">
                Tu blog de confianza
            </span>
        </div>
        <div id="post">
            <h1>Este es el título atractivo e interesante del post</h1>
            <p>Y este es el p&aacute;rrafo de inicio donde vamos 
            a explicar las cosas incre&iacute;bles que se pueden hacer
            con branches.</p>
            <p><img src="https://i.imgur.com/prQbDgJ.png" width="100%"/></p>
            <p>Los blogs son la mejor forma de compartir informaci&oacute;n
            y tus ideas. Mucho mas que ir a conferencias o salir
            en Youtube. Excepto si eres un rockstar. Pero 
            estad&iacute;sticamente no lo eres... por ahora.</p>
            <p>Suscribete y dale like</p>
	    <p>Nicolas Mesa</p>
        </div>
	<div id="footer">
		Hecho con amor en mi Home 💜
	</div>	
    </div>    
</body>
</html>'''

def run():
    store.get_categories()

if __name__ == '__main__':
    run()