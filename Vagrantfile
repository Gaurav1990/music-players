# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "music.box"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
  
    config.vm.network "forwarded_port", guest: 80, host: 4000
    config.vm.network "forwarded_port", guest: 4002, host: 4002
	config.vm.network "private_network", ip: "192.168.50.4"
	
  config.vm.synced_folder "../music-players", "/home/vagrant/music-players", :mount_options => ["fmode=644"]

  config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end
  
  config.vm.boot_timeout = 420
end
