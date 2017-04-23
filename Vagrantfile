Vagrant.configure(2) do |config|
  config.vm.box = "bento/ubuntu-16.04"

  config.vm.network "forwarded_port", guest: 8000, host: 8080

  config.vm.provision :shell, path: "bootstrap.sh"
end
