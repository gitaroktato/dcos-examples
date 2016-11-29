# DC/OS examples
* [Presentation](https://github.com/gitaroktato/dcos-examples/blob/master/presentation/Introduction_to_DCOS.odp?raw=true)
* [Demo video #1](https://github.com/gitaroktato/dcos-examples/blob/master/presentation/DCOS-hello-world.mp4?raw=true)
* [Demo video #2](https://github.com/gitaroktato/dcos-examples/blob/master/presentation/DCOS-end-to-end.mp4?raw=true)
# Usage
Use [DCOS Vagrant project](https://github.com/dcos/dcos-vagrant) to build your cluster.
## Versions used
I used Vagrant 1.8.4 and dcos-vagrant fb768f1dc0c.
## Configuration used in dcos-vagrant
```
m1:
  ip: 192.168.65.90
  cpus: 2
  memory: 1024
  type: master
a1:
  ip: 192.168.65.111
  cpus: 1
  memory: 640
  type: agent-private
a2:
  ip: 192.168.65.121
  cpus: 1
  memory: 512
  type: agent-private
a3:
  ip: 192.168.65.131
  cpus: 1
  memory: 512
  type: agent-private
a4:
  ip: 192.168.65.141
  cpus: 1
  memory: 512
  type: agent-private
p1:
  ip: 192.168.65.60
  cpus: 2
  memory: 512
  type: agent-public
  aliases:
  - spring.acme.org
  - oinker.acme.org
boot:
  ip: 192.168.65.50
  cpus: 2
  memory: 1024
  type: boot
```
To bring up the cluster with one machine, use this command
```
vagrant up m1 a1 boot
```
