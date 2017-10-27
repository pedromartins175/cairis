---
layout: default
title: Getting started
---

{% include toc.html %}

# Live Demo

A live demo of CAIRIS is available to use on [http://demo.cairis.org](http://demo.cairis.org).  The username and password you need are *test* and *test*.  The live demo is rebuilt every night based on the latest updates to CAIRIS.

The live demo comes with two example models: [NeuroGrid](http://cairis.org/NeuroGrid) and [ACME Water](http://cairis.org/ACME_Water).  To open these, select the System / Open Database menu, and choose the model to open.

# Installing CAIRIS

## CAIRIS container on Docker Hub

If you have Docker installed on your laptop or an available machine, the easiest way of getting up and running with the web application is to download the CAIRIS container from [Docker hub](https://hub.docker.com/r/shamalfaily/cairis/).  This is built from the latest changes in github, and uses [mod_wsgi-express](https://pypi.python.org/pypi/mod_wsgi) to deliver the CAIRIS web services.

* Download and run the container, and its linked mysql container:  
{% highlight bash %}
$ sudo docker run --name cairis-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:5.5
$ sudo docker run --name CAIRIS --link cairis-mysql:mysql -d -P -p 80:8000 --net=bridge shamalfaily/cairis
{% endhighlight %}


* From the web browser of your choice, connect to the CAIRIS URL, e.g. http://localhost
When asked for credentials, provide test/test

* If you want to interact with a pre-existing CAIRIS model, you can find some examples on the CAIRIS github, repository, e.g. [NeuroGrid](https://github.com/failys/cairis/blob/master/examples/exemplars/NeuroGrid/NeuroGrid.xml). You can import this from the System/Import menu, selecting type 'Model', and the model file to import. Allow a minute or two for this import to complete.

![fig:initStartup]({{ site.baseurl }}/images/CAIRIS_docker.jpg)

* Please feel free to use this container to evaluate CAIRIS, but do not use it for operational use. It uses all manner of default/easy-to-brute force credentials!

## Source installation and configuration

CAIRIS web services can be installed on any platform that its open-source dependencies are available for.  The most tested platforms are [Ubuntu](http://www.ubuntu.com) or [Debian](https://www.debian.org) Linux.

* Install the required applications and dependencies:

{% highlight bash %}
$ sudo apt-get install python-dev build-essential mysql-server mysql-client graphviz docbook dblatex python-pip python-numpy git libmysqlclient-dev --no-install-recommends texlive-latex-extra docbook-utils inkscape libxml2-dev libxslt1-dev poppler-utils python-setuptools
{% endhighlight %}

* Clone the latest version of the CAIRIS github repository, and use pip to install the dependencies in the root directory, i.e.

{% highlight bash %}
$ git clone https://github.com/failys/cairis
$ cd cairis
$ sudo pip install -r requirements.txt
{% endhighlight %}

* Run the CAIRIS quick setup initialisation script (which can be found in cairis/).  When you run this script, you should get the below form.

{% highlight bash %}
$ ./quick_setup.py
{% endhighlight %}

![fig:quick_setup_db]({{ site.baseurl }}/images/quick_setup_db.jpg)

You can accept many of these defaults, except for the database root password.  When you select `Ok`, the script will create a new CAIRIS database, and accompanying CAIRIS configuration file; this file will ensure that CAIRIS knows what database it needs to refer to when you start up the tool and setup the necessary environment variables. The form below will then be displayed.

![fig:quick_setup_user]({{ site.baseurl }}/images/quick_setup_user.jpg)

You will need to supply a username and password here. When you select `Ok`, the script will add a user to the CAIRIS database.

* Reload your .bashrc file i.e.

{% highlight bash %}
source .bashrc
{% endhighlight bash%}

* Starting cairisd

If you want to run the Flask development server, run `./cairisd.py runserver` (the script can be found in cairis/cairis/bin).   

* Starting mod_wsgi-express

If you want to run CAIRIS in a production environment then it may be sensible to run CAIRIS via mod_wsgi-express.  To do this, you will need to use pip to install the requisite dependencies, i.e.

{% highlight bash %}
$ sudo pip install -r wsgi_requirements.txt
{% endhighlight %}

To start mod_wsgi-express, you should run `mod_wsgi-express start-server cairis.wsgi`; cairis.wsgi can also be found in cairis/cairis/bin.

* Use the application

You can now point your browser to http://SERVERNAME:PORT_NUMBER, depending on where `cairisd` is installed, and what port cairisd or mod_wsgi-express is listening to, e.g. http://myserver.org:7071.