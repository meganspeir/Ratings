# -*- mode: ruby -*-
# vi: set ft=ruby :

# Name your project.
PROJECT_NAME = 'ratings'

Vagrant::Config.run do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "cloud64"

  # The url from where the 'config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.
  config.vm.box_url = "http://cloud-images.ubuntu.com/precise/current/precise-server-cloudimg-vagrant-amd64-disk1.box"

  # Boot with a GUI so you can see the screen. (Default is headless)
  # config.vm.boot_mode = :gui

  # Assign this VM to a host-only network IP, allowing you to access it
  # via the IP. Host-only networks can talk to the host machine as well as
  # any other machines on the same network, but cannot be accessed (through this
  # network interface) by any external networks.
  config.vm.network :hostonly, "192.168.20.20"

  # Assign this VM to a bridged network, allowing you to connect directly to a
  # network using the host's network device. This makes the VM appear as another
  # physical device on your network.
  # config.vm.network :bridged

  # Forward a port from the guest to the host, which allows for outside
  # computers to access the VM, whereas host only networking does not.
  config.vm.forward_port 80, 8080

  # This can be set to the host name you wish the guest machine to have.
  # Vagrant will automatically execute the configuration necessary to make
  # this happen.
  config.vm.host_name = PROJECT_NAME

  # Share an additional folder to the guest VM. The first argument is
  # an identifier, the second is the path on the guest to mount the
  # folder, and the third is the path on the host to the actual folder.
  # config.vm.share_folder "v-data", "/vagrant_data", "../data"
  config.vm.share_folder "v-data", "/Developer/Projects/#{PROJECT_NAME}", "."

  # Get viagra
  # The shell provisioner is the most basic provisioner, and allows you to
  # upload and execute a shell script as the root user in the VM.
  # This provisioner has one main configuration option: path. This should be a
  # path to the local shell script. This can be a relative path, and if so, it
  # will be expanded relative to the location of the Vagrantfile.
  config.vm.provision :shell, :path => "demand.sh"

end
