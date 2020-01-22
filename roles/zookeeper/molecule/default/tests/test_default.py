import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_sshd_inactive(host):
    assert host.service("zookeeper").is_running


def test_zookeeper_port(host):
    assert host.socket("tcp://0.0.0.0:2181").is_listening
