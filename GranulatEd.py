from Interpolate import interpolate_wave_table as get_sample
import math as m
import numpy as np
import matplotlib.pyplot as plt


class SineTable:
    def __init__(self):
        self.size = 100000
        self.table = []
        delta = (2 * m.pi) / self.size
        current_angle = 0.0
        for i in range(self.size):
            self.table.append(m.sin(current_angle))
            current_angle += delta

    def get_sample(self, index):
        return get_sample(m.fmod(index, self.size - 1.0), self.size)


class CosTable:
    def __init__(self):
        self.size = 100000
        self.table = []
        delta = (2 * m.pi) / self.size
        current_angle = 0.0
        for i in range(self.size):
            self.table.append(m.cos(current_angle))
            current_angle += delta

    def get_sample(self, index):
        return get_sample(m.fmod(index, self.size - 1.0), self.table)


class NoiseTable:
    def __init__(self):
        self.size = 100000
        self.table = []
        delta = (2 * m.pi) / self.size
        current_angle = 0.0
        for i in range(self.size):
            self.table.append(np.random.normal(0.0, 0.4, 1)[0])
            current_angle += delta

    def get_sample(self, index):
        return get_sample(m.fmod(index, self.size - 1.0), self.table)

    def plot_table(self):
        plt.plot(self.table)
        plt.show()


class Phasor:
    def __init__(self, size):
        self.data = []
        self.size = size
        for i in range(self.size):
            self.data.append(i / (size - 1))


class Envelope:
    def __init__(self, size, amp, curve):
        if curve == "parabolic":
            self.amplitude = 0
            self.size = size
            rdur = 1.0 / size
            rdur2 = rdur * rdur
            slope = 4.0 * amp * (rdur - rdur2)
            curve = -8.0 * amp * rdur2
            self.data = []
            for i in range(size):
                self.amplitude = self.amplitude + slope
                self.data.append(self.amplitude)
                slope = slope + curve


class Grain:
    def __init__(self, envelope_type, start, duration, speed, data):
        self.__phasor_size = 100000
        self.envelope = Envelope(self.__phasor_size, 1.0, envelope_type)
        self.phasor = Phasor(self.__phasor_size)
        self.duration = duration
        self.current_index = 0.0
        self.__index_increment = self.__phasor_size / duration
        self.__finished = 0
        self.active = 0
        self.data = data
        self.speed = speed
        self.start = start
        self.amp = 1.0

    def activate_grain(self, envelope, start, duration, speed, amp):
        self.envelope = Envelope(self.__phasor_size, 1.0, envelope)
        self.__index_increment = self.__phasor_size / duration
        self.start = start
        self.duration = duration
        self.speed = speed
        self.amp = amp
        self.active = 1

    def get_next_sample(self):
        # Print Phasor Index to file
        # out = get_sample(self.current_index, self.phasor.data)

        # Print Envelope to File
        # out = get_sample(self.current_index, self.envelope.data)
        # Get The Envelope and Index From the File
        # Find the phasor position
        phasor_position = get_sample(self.current_index, self.phasor.data)

        # Find the index with respect to the file
        index = self.start + (phasor_position * self.duration) * self.speed
        out = get_sample(index, self.data)
        out *= get_sample(self.current_index, self.envelope.data)

        # Increment Index Based on Duration
        self.current_index += self.__index_increment
        if self.current_index >= self.__phasor_size:
            self.current_index = 0
            self.active = 0

        return out

    def is_active(self):
        return self.active


class RainGrain:
    def __init__(self, envelope_type, start, duration, speed, data):
        self.__phasor_size = 100000
        self.envelope = Envelope(self.__phasor_size, 1.0, envelope_type)
        self.phasor = Phasor(self.__phasor_size)
        self.duration = duration
        self.current_index = 0.0
        self.__index_increment = self.__phasor_size / duration
        self.__finished = 0
        self.active = 0
        self.data = data
        self.speed = speed
        self.start = start
        self.amp = 1.0
        self.noise = NoiseTable()
        self.osc = CosTable()

    def activate_grain(self, envelope, start, duration, speed, amp):
        self.envelope = Envelope(self.__phasor_size, 1.0, envelope)
        self.__index_increment = self.__phasor_size / duration
        self.start = start
        self.duration = duration
        self.speed = speed
        self.amp = amp
        self.active = 1

    def get_next_sample(self):
        # Print Phasor Index to file
        # out = get_sample(self.current_index, self.phasor.data)

        # Print Envelope to File
        #mod = self.osc.get_sample(self.current_index * ((self.osc.get_sample(self.current_index) * 0.25) - 0.5))
        out = get_sample(self.current_index, self.envelope.data)
        out *= self.amp
        # Get The Envelope and Index From the File
        # Find the phasor position
        # phasor_position = get_sample(self.current_index, self.phasor.data)
        #
        # # Find the index with respect to the file
        # index = self.start + (phasor_position * self.duration) * self.speed
        # out = get_sample(index, self.data)
        # out *= get_sample(self.current_index, self.envelope.data)
        #
        # Increment Index Based on Duration
        self.current_index += self.__index_increment
        if self.current_index >= self.__phasor_size:
            self.current_index = 0
            self.active = 0

        return out

    def is_active(self):
        return self.active


class OscGrain(Grain):
    def __init__(self, envelope_type, start, duration, speed, osc_type):
        Grain.__init__(self, envelope_type, start, duration, speed, None)
        if osc_type == "sin":
            self.osc = SineTable()
        elif osc_type == "cos":
            self.osc = CosTable()
        elif osc_type == "noise":
            self.osc == NoiseTable()


class Granulator:
    def __init__(self, data):
        self.data = data
