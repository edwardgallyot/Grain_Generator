import random
import sys

import soundfile as sf

import GranulatEd as gEd

import filters

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

    # Creating Asynchronous clouds

    # # Intitialising the maximum grains in an engine
    # grains = []
    #
    # for i in range(10):
    #     start = random.randint(0, random.randint(1, len(data)))
    #     grains.append(
    #         gEd.Grain("parabolic", start, 2000, 1.0, data, sample_rate))
    #
    # # print(grains)
    #
    # # print(len(grains))
    #
    # new_data = []
    #
    # for i in range(sample_rate * 2):
    #     new_data.append(0.0)
    #
    # for i in range(len(new_data)):
    #     randint = random.randint(1, 200)
    #     if randint == 1:
    #         for grain in grains:
    #             if not grain.is_active():
    #                 start = random.randint(0, random.randint(1, len(data)))
    #                 duration = random.randint(480, 4800)
    #                 speed = (random.random() * 0.01) + 0.5
    #                 amp = random.random()
    #                 grain.activate_grain("parabolic", start, duration, speed, amp)
    #                 break
    #
    #     for grain in grains:
    #         if grain.is_active():
    #             sample = grain.get_next_sample()
    #             new_data[i] += sample

    ###########################################################################################################
    #
    # # Creating Pitch Shifting and Time Stretching Effects
    #
    # grains = []
    #
    # for i in range(100):
    #     start = random.randint(0, random.randint(1, len(data)))
    #     grains.append(
    #         gEd.Grain("parabolic", start, 2000, 1.0, data))
    #
    # new_data = []
    #
    # stretch_factor = 10.0
    #
    # for i in range(int(len(data) * stretch_factor)):
    #     new_data.append(0.0)
    #
    # increment = 0
    #
    # grain_size = 4800
    #
    # number_of_grains = 4
    #
    # for i in range(number_of_grains):
    #     if grain_size % number_of_grains != 0:
    #         grain_size += 1
    #
    # for i in range(len(new_data)):
    #     for grain in grains:
    #         if increment == 0:
    #             if not grain.is_active():
    #                 start = i / stretch_factor
    #                 duration = grain_size
    #                 speed = 4.0
    #                 amp = 1
    #                 grain.activate_grain("parabolic", start, duration, speed, amp)
    #                 break
    #
    #     increment += 1
    #     if increment == grain_size / number_of_grains:
    #         increment = 0
    #
    #     for grain in grains:
    #         if grain.is_active():
    #             sample = grain.get_next_sample()
    #             new_data[i] += sample

    ###########################################################################################################

    # # Creating Basic Rain Fall Based on the Pressure Equation
    #
    # # Intitialising the maximum grains in an engine
    # grains = []
    #
    # for i in range(100):
    #     start = random.randint(0, random.randint(1, len(data)))
    #     grains.append(
    #         gEd.RainGrain("parabolic", start, 2000, 1.0, data))
    #
    # # print(grains)
    #
    # # print(len(grains))
    #
    # noise = gEd.NoiseTable()
    #
    # index = 0
    #
    # new_data = []
    #
    # for i in range(sample_rate * 5):
    #     new_data.append(0.0)
    #
    # # noise.plot_table()
    #
    # for i in range(len(new_data)):
    #     randint = noise.get_sample(index)
    #
    #     if randint > 1.4:
    #         for grain in grains:
    #             if not grain.is_active():
    #                 start = 0
    #                 duration = sample_rate / (randint * 60)
    #                 speed = 1.0
    #                 amp = 0.5 - randint
    #                 grain.activate_grain("parabolic", start, duration, speed, amp)
    #                 break
    #
    #     for grain in grains:
    #         if grain.is_active():
    #             sample = grain.get_next_sample()
    #             new_data[i] += sample * 0.05
    #     index += 1
    #
    # new_data = filters.butter_highpass_filter(new_data, 700, sample_rate, 1)
    # new_data = filters.butter_highpass_filter(new_data, 700, sample_rate, 1)
    #
    # lowpass_noise = []
    #
    # for i in range(len(new_data)):
    #     new_data[i] *= 10.0
    #     lowpass_noise.append(noise.get_sample(i) * 0.01)
    #
    # lowpass_noise = filters.butter_lowpass_filter(lowpass_noise, 2000, sample_rate, 1)
    #
    # new_data += lowpass_noise
    #
    # sf.write("out.wav", new_data, sample_rate)
