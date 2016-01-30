# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  #config.vm.box = "puphpet/centos65-x64"
  config.vm.box = "ubuntu/trusty64"

  config.vm.network :private_network, ip: "192.168.33.10"

  config.vm.provision :fabric do |fabric|
    fabric.fabfile_path = './fabfile.py'
    fabric.tasks = ['main']
  end
end
