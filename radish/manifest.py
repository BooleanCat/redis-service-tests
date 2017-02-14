from functools import lru_cache

import yaml


class Manifest:
    def __init__(self, path):
        self.path = path

    def get_name(self):
        return self._manifest['name']

    def get_properties_for(self, group_name, job_name):
        jobs = self.get_instance_group(group_name)['jobs']
        is_job = lambda job: job['name'] == job_name

        return next(filter(is_job, jobs))['properties']

    def get_instance_group(self, name):
        groups = self._manifest['instance_groups']
        is_group = lambda group: group['name'] == name

        return next(filter(is_group, groups))

    @property
    @lru_cache(None)
    def _manifest(self):
        with open(self.path) as raw_manifest:
            return yaml.load(raw_manifest)
