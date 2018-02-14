# aws_ec2_perf

Master: [![Build Status](https://travis-ci.org/sansible/aws_ec2_perf.svg?branch=master)](https://travis-ci.org/sansible/aws_ec2_perf)
Develop: [![Build Status](https://travis-ci.org/sansible/aws_ec2_perf.svg?branch=develop)](https://travis-ci.org/sansible/aws_ec2_perf)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

Applies performance enhancements intended to Ubuntu Trust and Xenial based EC2 instances.

Enhancements are taken from Netflix's findings:

* [https://youtu.be/89fYOo1V2pA](https://youtu.be/89fYOo1V2pA)
* [https://www.slideshare.net/brendangregg/how-netflix-tunes-ec2-instances-for-performance](https://www.slideshare.net/brendangregg/how-netflix-tunes-ec2-instances-for-performance)

All enhancements are turned off by defaults, several flags are provided to turn the settings on:

| Variable| Default| Description|
|---|---|---|
|sansible_aws_ec2_perf_clocksource_enabled|yes|Enable Clocksource fix for Trusty over Xen|
|sansible_aws_ec2_perf_filesystem_enabled|no|Enable Filesystem based enhancements|
|sansible_aws_ec2_perf_huge_pages_enabled|no|Enable Huge Page disablement|
|sansible_aws_ec2_perf_network_enabled|no|Enable Network based enhancements|
|sansible_aws_ec2_perf_numa_enabled|no|Enable NUMA balancing disablement|
|sansible_aws_ec2_perf_virtual_mem_enabled|no|Enable Virtual Memory swappiness disablement|




## Installation and Dependencies

To install run `ansible-galaxy install sansible.aws_ec2_perf` or add this to your
`roles.yml`.

```YAML
- name: sansible.aws_ec2_perf
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses a single tage: **build**

* `build` - Installs performance enhancements, useful for baking into images




## Examples

Simply include role in your playbook

```YAML
- name: Install and configure aws_ec2_perf
  hosts: "somehost"

  roles:
    - role: sansible.aws_ec2_perf
      sansible_aws_ec2_perf_clocksource_enabled: yes
      sansible_aws_ec2_perf_filesystem_enabled: yes
      sansible_aws_ec2_perf_huge_pages_enabled: yes
```
