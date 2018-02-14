import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sysctl(host):
    '''
    Only some settings actually take effect in Docker, just check for the ones
    that actually work
    '''
    assert host.sysctl("vm.swappiness") == 0
    assert host.sysctl("vm.dirty_ratio") == 80
    assert host.sysctl("vm.dirty_background_ratio") == 5
    assert host.sysctl("vm.dirty_expire_centisecs") == 12000
