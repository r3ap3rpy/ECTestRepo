from abc import ABCMeta, abstractmethod
from time import sleep

class Platform(metaclass = ABCMeta):
    @abstractmethod
    def stop_systems(self):
        raise NotImplementedError("Please implement the stop_systems method!")

    @abstractmethod
    def start_systems(self):
        raise NotImplementedError("Please implement the start_systems method!")
    
    @abstractmethod
    def health_check_systems(self):
        raise NotImplementedError("Please implement the health_check_systems method!")

class WebServers(Platform):
    __nodes = ['web_node_a','web_node_b','web_node_c']
    def stop_systems(self):
        for system in self.__nodes:
            print(f"Stopping system: {system}")
            sleep(0.5)

    def start_systems(self):
        for system in self.__nodes:
            print(f"Starting system: {system}")
            sleep(0.5)

    def health_check_systems(self):
        for system in self.__nodes:
            print(f"Checking system: {system}")
            sleep(0.5)
        
class FireWalls(Platform):
    __nodes = ['fw_node_a','fw_node_b','fw_node_c']
    def stop_systems(self):
        for system in self.__nodes:
            print(f"Stopping system: {system}")
            sleep(0.5)
            
    def start_systems(self):
        for system in self.__nodes:
            print(f"Starting system: {system}")
            sleep(0.5)

    def health_check_systems(self):
        for system in self.__nodes:
            print(f"Checking system: {system}")
            sleep(0.5)

class PatchingFactory(object):
    def stop_all(self, platform_object):
        print(f"Stopping platform: {platform_object}")
        return eval(platform_object)().stop_systems()
    
    def start_all(self, platform_object):
        print(f"Starting platform: {platform_object}")
        return eval(platform_object)().start_systems()

    def hc_all(self, platform_object):
        print(f"Performing health check on plaform: {platform_object}")
        return eval(platform_object)().health_check_systems()

    def patching_magic(self, platform_object):
        self.hc_all(platform_object)
        self.stop_all(platform_object)
        self.start_all(platform_object)
        self.hc_all(platform_object)

PF = PatchingFactory()
PFORMS = [ 'WebServers','FireWalls' ]
for platform in PFORMS:
    PF.hc_all(platform)
    PF.stop_all(platform)
    PF.start_all(platform)
    PF.hc_all(platform)