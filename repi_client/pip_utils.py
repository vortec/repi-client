from pip.index import PackageFinder
from pip.req import InstallRequirement, RequirementSet
from pip.locations import build_prefix, src_prefix
from pip.util import get_installed_distributions
 

def install_package(package, version=None):
    requirement_set = RequirementSet(build_dir=build_prefix, src_dir=src_prefix, download_dir=None)

    if version:
        install = '{}=={}'.format(package, version)
    else:
        install = package
    requirement_set.add_requirement(InstallRequirement.from_line(install, None))
    finder = PackageFinder(find_links=[], index_urls=["http://pypi.python.org/simple/"])
    requirement_set.prepare_files(finder, force_root_egg_info=False, bundle=False)
    requirement_set.install([], [])


def get_package_information():
    ret = {}
    distributions = get_installed_distributions()
    for distribution in distributions:
        project_name = distribution.project_name
        version = distribution.version
        ret[project_name] = version
    return ret
