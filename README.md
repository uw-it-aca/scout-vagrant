# scout-vagrant
Vagrantfile and provisioning tasks for the scout project

**Dependencies:**

    1. Install Vagrant: https://www.vagrantup.com/
    2. Install VirtualBox: https://www.virtualbox.org/wiki/Downloads
    3. Install Ansible: $ sudo pip install ansible

**Installation:**

    $ git clone https://github.com/uw-it-aca/scout-vagrant.git
    $ cd scout-vagrant
    $ git submodule init
    $ git submodule update
    $ vagrant plugin install vagrant-host-shell
    $ vagrant up

If you want to skip installation of one of the components, you can use the following environment variables - SKIP_APP, SKIP_WEB, SKIP_SERVER, SKIP_LABSTATS, SKIP_ADMIN. For example if you just wanted scout and spotseeker_server, you could use:

    $ SKIP_WEB=True SKIP_LABSTATS=True SKIP_ADMIN=True vagrant up

**Troubleshooting**

To reload configuration changes:

    $ MY_VAR='scout' vagrant reload --provision

To start fresh:

    $ vagrant destroy
    $ rm -rf venv*
    $ vagrant up

**Setup Spotseeker Server:**

In a new terminal...    

    $ vagrant ssh

    vagrant@vagrant $ cd /vagrant/venv-server
    vagrant@vagrant $ source bin/activate
    (venv)vagrant@vagrant $ cd serverproject

Upload Craig's server.db to venv-server

    (venv)vagrant@vagrant $ python manage.py syncdb
    (venv)vagrant@vagrant $ python manage.py migrate

Create API consumer

    (venv)vagrant@vagrant $ python manage.py create_consumer

**Run Spotseeker Server:**    

    (venv)vagrant@vagrant $ python manage.py runserver 0:8000

**Run Spacescout Web Server:**

In a new terminal...    

    $ vagrant ssh
    vagrant@vagrant $ cd /vagrant/venv-web
    vagrant@vagrant $ source bin/activate
    (venv)vagrant@vagrant $ cd webproject
    (venv)vagrant@vagrant $ python manage.py runserver 0:8001

**Run Scout webserver:**

**Setup Scout webserver:**

Update settings.py

    SPOTSEEKER_HOST = "http://localhost:8000"
    SPOTSEEKER_OAUTH_KEY = ""
    SPOTSEEKER_OAUTH_SECRET = ""
    SPOTSEEKER_DAO_CLASS = "spotseeker_restclient.dao_implementation.spotseeker.Live"

Run Scout application

    $ vagrant ssh
    vagrant@vagrant $ cd /vagrant/venv
    vagrant@vagrant $ source bin/activate
    (venv)vagrant@vagrant $ cd scoutproject
    (venv)vagrant@vagrant $ python manage.py runserver 0:8001

**Selenium Testing with SauceLabs**

Install dependencies
    
    $ vagrant ssh
    vagrant@vagrant $ cd /vagrant/venv
    vagrant@vagrant $ source bin/activate
    (venv)vagrant@vagrant $ cd scoutproject
    (venv)vagrant@vagrant $ pip install -r requirements_saucelabs.txt
    
Update settings.py (get from Craig or Char)
    
    SAUCE_USERNAME = ""
    SAUCE_ACCESS_KEY = ""

Open a Sauce Connect Tunnel
    
    $ vagrant ssh
    vagrant@vagrant $ cd /vagrant/venv
    vagrant@vagrant $ source bin/activate
    (venv)vagrant@vagrant $ sc -u USERNAME -k ACCESS_KEY

Run your fucntional test (new terminal)
    
    $ vagrant ssh
    vagrant@vagrant $ cd /vagrant/venv
    vagrant@vagrant $ source bin/activate
    (venv)vagrant@vagrant $ cd scoutproject
    (venv)vagrant@vagrant $ python manage.py test scout.tests.PageFlowTest

View your test results
    
    https://saucelabs.com/u/uw-it-aca-scout

