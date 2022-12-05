This repository contains labs from the discipline 'Server Software Development Technologies'. Below are the instructions for running the web application on Windows and Linux platforms locally.

## 1. Preparation

To run the application correctly, you will need additional utilities: Python with the pip module, Git Bash, and Docker. Docker also requires a virtual machine to get up and running, therefore, it's better to additionally download and install any virtualization program (for example, VirtualBox or VMWare).

Before you install Git, it's a good idea to check to see if you already have it installed. To check whether you have git installed, simply open a terminal window and type `git --version`.

![image](https://user-images.githubusercontent.com/85063387/203256670-b10cdbb9-3959-4677-8370-8ae936e7f4b7.png)


If you don’t have it installed already, follow this [link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for more instructions.

Now let's move on to Python. To simplify, I add a [link](https://www.digitalocean.com/community/tutorials/install-python-windows-10) with an installation guide. The installer can be downloaded from the official [website](https://www.python.org/downloads/).

:exclamation: **Note!** Further, you may check the *Add python.exe to PATH* check box to include the interpreter in the execution path.

![image](https://user-images.githubusercontent.com/85063387/203262445-9afbdc98-58bd-4f48-b40f-458c1dd53552.png)

Also, in the *Customize installation* section, all the checkboxes must be checked:

![image](https://user-images.githubusercontent.com/85063387/203262505-1c42719a-0683-41db-a896-48f827b97ee6.png)

Optionally, you can change the installation path, add a shortcut to the desktop, and so on. After selecting the *Advanced options*, click **Install** to start installation.

:heavy_check_mark: If the previous steps were successful, now you should verify the Python installation:

- [X] Open the command prompt.
- [X] Type `python` and press enter.
- [X] The version of the python which you have installed will be displayed if the python is successfully installed on your windows.

![image](https://user-images.githubusercontent.com/85063387/203280521-555eabb9-a417-4af7-890d-cc1ff483d2e1.png)

Pip is a powerful package management system for Python software packages. Thus, make sure that you have it installed.

- [X] Open the command prompt.
- [X] Enter `pip --version` to check if pip was installed.
- [X] The following output appears if pip is installed successfully.

![image](https://user-images.githubusercontent.com/85063387/203281511-8d7e4c6d-e5b9-46ea-9968-1040f006bb7d.png)

So, the last step is to install Docker. You can download it from [here](https://docs.docker.com/get-docker/).

Docker can be quite difficult to install and use, especially for beginners. An easy and quick way to install it on [Windows 10](https://www.youtube.com/watch?v=PHYRSPCD69U&t=367s&ab_channel=%D0%9A%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80-%D1%8D%D1%82%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%82%D0%BE%21) and [Linux](https://www.youtube.com/watch?v=l6nSkqEwab0&ab_channel=Kodprog-%D0%BB%D0%B8%D0%BD%D1%83%D0%BA%D1%81%2C%D0%B2%D0%B5%D0%B1-%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0) can be found here.

As I said, Docker requires a virtual machine to work, which will be installed and automatically displayed in the virtualization program. I recommend using VirtualBox for these purposes ([link](https://www.virtualbox.org/wiki/Downloads) to the installer, installation [instructions](https://www.youtube.com/watch?v=sB_5fqiysi4&ab_channel=TechGumbo)).

There are different programs for developing in Python, but the most convenient one, in my opinion, is PyCharm. It can be downloaded from [here](https://www.jetbrains.com/pycharm/download/#section=windows).

You now have everything needed to run the application. Let's start!

## 2. Launch application using Python

:exclamation: **Note!** The instructions for installing and running the project locally apply to Windows only.

1. After installing, you need to clone this repository to your local machine. For this step you can use as command line, as Git Bash:

```
$ git clone https://github.com/Yakorrr/server_labs
```

![image](https://user-images.githubusercontent.com/85063387/203257692-b289ec23-57f9-4f28-8b03-2e982dec32eb.png)

2. Create a new PyCharm project, then change to the specified directory and create a virtual environment. Starting from this step, you must use the command line of your operating system:

```
cd <project folder>
python3 -m venv env
```

3. Activate the virtual environment using an *activate* script:

```
cd venv/Scripts
activate
```

At this point, the console output should look something like this:

![image](https://user-images.githubusercontent.com/85063387/203399285-3d05ad0d-a69c-480f-9459-84aed7d01d63.png)

4. Installing auxiliary modules - *Flask* and *names* using *pip*:

```
pip install flask
pip install names
```

5. Usually, all project dependencies are written to a special file called *requirements.txt*. This can be done with the following command:

```
pip freeze > requirements.txt
```

:exclamation: **Note!** The file must be in the root directory of the project.

The repository already has such a file, so this action is optional.

6. Now you need to copy the contents from the repository to the root directory of the project using the command:

```
xcopy <repository directory> <project directory> /e /h /q
```

The `xcopy` command has several additional parameters:

- /e – Copy subdirectories, including any empty ones.
- /h - Copy files with hidden and system file attributes.
- /q - Hides the information output.

The result should be the following:

![image](https://user-images.githubusercontent.com/85063387/203405934-089cf7f2-563d-460e-baaf-98f8cafd7ffd.png)

7. Now you can run the Flask application using terminal in PyCharm. Just copy the following commands and paste them into the terminal menu:

```
$env: FLASK_APP = 'files'
flask run
```

Or you can do another way:

```
flask run -host 0.0.0.0 -p <your port>
```

I used 5000-th port, but you can choose another one.

8. Well done! Now you can see this application running in your browser. You can enter the host address manually or follow the link from PyCharm:

![image](https://user-images.githubusercontent.com/85063387/203408975-76dadf47-ea30-4dc6-bf64-505b8399cb93.png)
![image](https://user-images.githubusercontent.com/85063387/203408984-20ae8b26-7a6f-48f8-bf28-220153c22324.png)


## 3. Launch application using Docker

At the very beginning, we installed Docker. Now let's try to run the application with it.

1. Move to the root directory of your project using Docker Terminal:

![image](https://user-images.githubusercontent.com/85063387/203415088-f735c3f1-8b34-4e8a-8de1-9b8bf2eecbe2.png)

:exclamation: **Note!** Keep these notes in mind when working with Docker Terminal:

  1. On the Windows command line, when specifying an absolute or relative path (for example, with the `cd` command), the backslash character `\` is used to separate directory names. Docker Terminal, on the other hand, uses the forward slash `/` symbol.
  2. If the directory name contains spaces, it must be enclosed in single `''` or double `""` brackets.


2. Run the following command:

```
docker build --build-arg PORT=5000 . -t application:latest
```

The `docker build` command [builds](https://docs.docker.com/engine/reference/commandline/build/#:~:text=The%20docker%20build%20command%20builds,a%20file%20in%20the%20context.) Docker images from a Dockerfile and a “context”. A build’s context is the set of files located in the specified `PATH` or `URL`.

The output should be like this:

![image](https://user-images.githubusercontent.com/85063387/203418108-4c0648c9-4381-496e-b3e7-aadd00e13887.png)

3. Now you need to build your Docker container using this command:

```
docker-compose build
```

Services are built once and then tagged, by default as `project_service`.

If the Compose file specifies an [image](https://github.com/compose-spec/compose-spec/blob/master/spec.md#image) name, the image is tagged with that name, substituting any variables beforehand. See [variable interpolation](https://github.com/compose-spec/compose-spec/blob/master/spec.md#interpolation).

So, if you change a service’s `Dockerfile` or the contents of its build directory, run `docker-compose build` to rebuild it.

The output should be like this:

![image](https://user-images.githubusercontent.com/85063387/203419234-6918b87a-7354-4d21-accd-100fdc0064ed.png)

4. Finally, you need to run your Docker container using the following command:

```
docker-compose up
```

The `docker-compose up` command aggregates the output of each container (like `docker-compose logs --follow` does). When the command exits, all containers are stopped. Running `docker-compose up --detach` starts the containers in the background and leaves them running.

If there are existing containers for a service, and the service’s configuration or image was changed after the container’s creation, `docker-compose up` picks up the changes by stopping and recreating the containers (preserving mounted volumes). To prevent Compose of picking up changes, use the `--no-recreate` flag.

The output should be like this:

![image](https://user-images.githubusercontent.com/85063387/203422953-2d6ffa4d-5599-41b6-a2d6-03f21c6aac99.png)

5. Well done! Now you can see this application running in Docker container. You can check the responses from the application in Docker Terminal.

## 4. Conclusion

To sum up, we were able to run the project locally using Python and Docker.

:exclamation: I have the third variant for the additional task.

I also add a [link](https://serverlabs.herokuapp.com/) to the project deployed on heroku.

Enjoy yourself! :wink:




