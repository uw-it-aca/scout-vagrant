# scout-vagrant
Vagrantfile and provisioning tasks for the scout project

To get started:

1. Install Vagrant: https://www.vagrantup.com/
2. Install VirtualBox: https://www.virtualbox.org/wiki/Downloads
3. Install ansible: sudo pip install ansible
4. Change directory into this repository
5. vagrant plugin install vagrant-host-shell
6. vagrant up

To reload configuration changes: vagrant reload --provision

To start fresh: vagrant destroy, then vagrant up
