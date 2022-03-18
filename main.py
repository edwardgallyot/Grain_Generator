import numpy as np

import GranulatEd as gEd
import soundfile as sf
import sys
import random
import matplotlib.pyplot as plt
from Interpolate import interpolate_wave_table as get_sample_cubic

if __name__ == '__main__':
    ###########################################################################################################
    if len(sys.argv) == 1:
        print("Usage: main.py file")
        sys.exit()
    else:
        file_string = sys.argv[1]

    # Load in the file
    data, sample_rate = sf.read(file_string)

    print(data[0])
    print(file_string + " Loaded")

    # Data format is data[frame][channel]

    ###########################################################################################################

    # Creating a Loop
    # new_data = [0.0] * sample_rate * 2

    # print(len(new_data))
    #
    # for i in range(2):
    #     for j in range(len(data)):
    #         offset = i * len(data)
    #         new_data[offset + j] = data[j]

    # new_data = []

    ###########################################################################################################

    # Creating a Phasor Object - Andy Farnell

    phasor1 = gEd.Phasor(44100)

    # plt.plot(phasor1.data)
    # plt.show()

    # Creating an Envelope Object - Ross Bencina

    envelope = gEd.Envelope(44100, 1.0, "parabolic")

    # We can show the envelope object here

    # plt.plot(envelope.data)
    # plt.show()

    speedInHz = 2

    rate = phasor1.size / speedInHz

    # new_data = []

    # for i in range(25):
    #     for j in range(int(rate)):
    #         # Find where the phasor is sitting in relation to itself
    #         sample_table_index = (float(j / rate)) * phasor1.size
    #         envelope_table_index = (float(j / rate)) * phasor1.size
    #
    #         # Find the index of the data at the phasor
    #         sample_index = get_sample_cubic(sample_table_index, phasor1.data) * (len(data) / 8)
    #         envelope_index = get_sample_cubic(envelope_table_index, phasor1.data) * len(envelope.data)
    #
    #         # Find the sample at in the chunk that we wanted
    #         sample = get_sample_cubic(sample_index, data)
    #         sample *= get_sample_cubic(envelope_index, envelope.data)
    #
    #         # Append the sample to the data
    #         new_data.append(sample)

    ###########################################################################################################

    # Defining a single Grain
    # grain = gEd.Grain("parabolic", 4000, 2.0, data, sample_rate)

    # new_data = [0.0] * sample_rate * 2

    # grain.activate_grain()

    # sample = 0.0

    # Testing Phasors

    # tmp_sample = 0.0

    # for i in range(len(new_data)):
    #     if i = 20000:
    #         grain.activate_grain()
    #
    #     if grain.is_active():
    #         sample = grain.get_next_sample()
    #         for z in range(2):
    #             tmp_sample = copy.copy(sample)
    #             new_data[i] = tmp_sample
    #     else:
    #         for z in range(2):
    #             new_data[i] = 0.0

    ###########################################################################################################

    # Intitialising the maximum grains in an engine
    grains = []

    for i in range(300):
        start = random.randint(0, random.randint(1, len(data)))
        grains.append(
            gEd.Grain("parabolic", start, 2000, 1.0, data, sample_rate))

    # print(grains)

    # print(len(grains))

    new_data = []

    for i in range(sample_rate * 10):
        new_data.append(0.0)

    active_grains = 0

    for i in range(len(new_data)):
        randint = random.randint(1, 600)
        if randint == 1:
            for grain in grains:
                if not grain.is_active():
                    grain.activate_grain()
                    active_grains += 1
                    break

        for grain in grains:
            if grain.is_active():
                sample = grain.get_next_sample()
                new_data[i] += sample

sf.write("out.wav", new_data, sample_rate)
