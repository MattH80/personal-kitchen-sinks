"""Zipline Sim Autopilot Challenge
By: Sahil Kale (s3kale@uwaterloo.ca)"""
import sys
import struct

#wrapper for outputting the things to the sim. 
# @param 
def output(lateral_airspeed: float, drop_package_command: bool):
    COMMAND_STRUCT = struct.Struct(">fB3s")
    padding = b"abc"
    sys.stdout.buffer.write(COMMAND_STRUCT.pack(lateral_airspeed, drop_package_command, padding))
    sys.stdout.flush()

class telemetryInput:
    #__slots__ = [' '] #TODO: Figure out what __slots__ actually does? Theory: it's kinda like variable declaration. Remove this comment.
    # Structs used to pack/unpack the API messages
    # milliseconds [2 bytes]
    time: int
    # wind_x [4 bytes]
    wind_x: float
    # wind_y [4 bytes]
    wind_y: float
    # recovery_x error [2 bytes]
    recovery_x: int
    # recovery_y error [1 byte]
    recovery_y: int
    # 31 lidar samples [31 bytes]
    lidar_samples = []

    TELEMETRY_STRUCT = struct.Struct(">Hhffb31B")

    def __init__(self):
        cmd = sys.stdin.read(TELEMETRY_STRUCT.size)
        print(cmd)
        time, wind_x, wind_y , recovery_x, recovery_y, lidar_samples = TELEMETRY_STRUCT.unpack(cmd) #Load the elements into class vars
while True:
    TELEMETRY_STRUCT = struct.Struct(">Hhffb31B")
    cmd = sys.stdin.read(TELEMETRY_STRUCT.size)
    output(30, 0)
