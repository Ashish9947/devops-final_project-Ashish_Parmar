Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.provider "virtualbox" do |vbox|
    vbox.memory = 8080
    vbox.cpus = 2
  end
  config.vm.network "private_network", type: "dhcp"
  config.vm.hostname = "minikube"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end
end
