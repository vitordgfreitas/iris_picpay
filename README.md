# Nome do projeto

<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->


<img src="7156125-HSC00001-7.jpg" alt="exemplo imagem">

> Deploying a ML classifier of the Iris dataset using Flask, Docker and AWS EC2.



## 💻 Prerequisites:

* You need to have Docker installed.

## 🚀 Running

* The first step is to clone this reposity in your local machine
* The program is mapping to port 80. This is a privileged port and might not work in your pc, thus you might want to change it to a free port, such as 5000, in app.py.
* To run locally type `python app.py` in your terminal, open your browser and type http://127.0.0.1:80 (You need to substitute :80 for whatever port you put on app.py). This might not work in your computer, thus skip to the next step, which is dockerization.
* To run this on docker, type `docker build -t appiris .` then `docker run -p 80:80 appiris .` (you need to change the ports to your chosen ones on app.py and Dockerfile). Now navigate to http://127.0.0.1:80 and you will be able to input flower features and receive predictions.



