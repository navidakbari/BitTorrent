# Adding name spaces
sudo ip netns add h1
sudo ip netns add h2
sudo ip netns add h3
# Adding Switches
sudo ovs-vsctl add-br s1
sudo ovs-vsctl add-br s2
# Adding links 
sudo ip link add h1-vth type veth peer name s1-vth1
sudo ip link add h2-vth type veth peer name s1-vth2
sudo ip link add s1-switch-vth type veth peer name s2-switch-vth
sudo ip link add h3-vth type veth peer name s2-vth1
# Connecting switchs to each other
sudo ovs-vsctl add-port s1 s1-switch-vth
sudo ovs-vsctl add-port s2 s2-switch-vth
# Link h1 to s1
sudo ovs-vsctl add-port s1 s1-vth1
sudo ip link set h1-vth netns h1
# Link h2 to s1
sudo ovs-vsctl add-port s1 s1-vth2
sudo ip link set h2-vth netns h2
# Link h3 to s2
sudo ovs-vsctl add-port s2 s2-vth1
sudo ip link set h3-vth netns h3
# Set Ip to hosts
sudo ip netns exec h1 ifconfig h1-vth 10.0.0.1 up
sudo ip netns exec h2 ifconfig h2-vth 10.0.0.2 up
sudo ip netns exec h3 ifconfig h3-vth 10.0.0.3 up
# Activate switch interfaces
sudo ifconfig s1-switch-vth up
sudo ifconfig s2-switch-vth up
sudo ifconfig s1-vth1 up
sudo ifconfig s1-vth2 up
sudo ifconfig s2-vth1 up
# Get ping h3 in h1
sudo ip netns exec h1 ping 10.0.0.3

