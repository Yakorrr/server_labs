This repository contains labs from the discipline 'Server Software Development Technologies'. Below are the instructions for running the web application on Windows and Linux platforms.

## 1. Preparation

To run the application correctly, you will need additional utilities: Python with the pip module, Git Bash, and Docker. Docker also needs a virtual machine to get up and running, therefore, it's better to additionally download and install any virtualization program (for example, VirtualBox or VMware).

Before you install Git, it's a good idea to check to see if you already have it installed. To check whether or not you have git installed, simply open a terminal window and type `git --version`.

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

You now have everything you need to run the application. Let's start!

## 2. Start

After installing, you need to clone this repository to your local machine:

`$ git clone https://github.com/Yakorrr/server_labs`

![image](https://user-images.githubusercontent.com/85063387/203257692-b289ec23-57f9-4f28-8b03-2e982dec32eb.png)

Change to the project folder:

`$ cd server_labs`
