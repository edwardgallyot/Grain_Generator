from Interpolate import interpolate_wave_table as get_sample


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
    def __init__(self, envelope_type, start, duration, speed, data, sample_rate):
        self.sample_rate = sample_rate
        self.__phasor_size = 44100
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

    def activate_grain(self):
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


class Granulator:
    def __init__(self, data):
        self.data = data
