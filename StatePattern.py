from abc import abstractmethod, ABCMeta

class InternalState(metaclass = ABCMeta):
    @abstractmethod
    def changeState(self):
        pass

class TurnedOn(InternalState):
    def changeState(self):
        print("Turning on the station!")
        return "ON"

class TurnedOff(InternalState):
    def changeState(self):
        print("Turning off the station!")
        return "OFF"

class IncreaseVolume(InternalState):
    def changeState(self):
        print("Increasing volume!")
        return "+10"

class DecreaseVolume(InternalState):
    def changeState(self):
        print(f"Decreasing volume!")
        return "-10"

class RadioStation(InternalState):
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state
    def setState(self, value):
        self.state = value
    def changeState(self):
        self.state = self.state.changeState()


Radio = RadioStation()
print(f"The radio's internal state is {Radio.getState()}")

ON = TurnedOn()
OFF = TurnedOff()
Louder = IncreaseVolume()
Lower = DecreaseVolume()
Radio.setState(ON)
Radio.changeState()
print(f"The radios state is currently: {Radio.getState()}")

Radio.setState(Louder)
Radio.changeState()
print(f"The radios state is currently: {Radio.getState()}")