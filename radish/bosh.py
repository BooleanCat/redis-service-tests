import json
import subprocess


class Bosh:
    def __init__(self, config):
        self.config = config

    def get_vm_ips(self):
        vms = self.get_vms()
        ips_index = self.get_column_index(vms['Header'], 'IPs')
        return [row[ips_index] for row in vms['Rows']]

    def get_vms(self):
        vms = json.loads(subprocess.check_output(self._get_bosh_command('vms')))
        return vms['Tables'][0]

    def get_column_index(self, header, name):
        index = header.index(name)
        if index == -1:
            raise IndexError('failed to get header index: `%s`' % name)
        return index

    def _get_bosh_command(self, op):
        return [
            self.config['path'],
            '--ca-cert=%s' % self.config['ca-cert'],
            '--client=%s' % self.config['username'],
            '--client-secret=%s' % self.config['password'],
            '-e', self.config['url'],
            '-d', self.config['deployment'],
            '--json',
            op,
        ]
