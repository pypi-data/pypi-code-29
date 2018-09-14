
import enum

class PacketFunc(enum.IntEnum):
    func_sync  = 1
    func_ack   = 2
    func_nack  = 3
    func_string = 5
    func_array  = 6
    func_struct = 7
