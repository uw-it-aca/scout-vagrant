# scout-vagrant
Vagrantfile and provisioning tasks for the scout project

To get started:

1. Install Vagrant: https://www.vagrantup.com/
2. Install VirtualBox: https://www.virtualbox.org/wiki/Downloads
3. Install ansible: sudo pip install ansible
4. Change directory into this repository
5. git submodule init
6. git submodule update
7. vagrant plugin install vagrant-host-shell
8. MY_VAR='scout' vagrant up

To reload configuration changes: MY_VAR='scout' vagrant reload --provision

To start fresh: MY_VAR='scout' vagrant destroy, then MY_VAR='scout' vagrant up
